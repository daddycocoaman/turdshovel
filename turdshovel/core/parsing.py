from functools import lru_cache
from typing import Dict

import System
from Microsoft.Diagnostics.Runtime import ClrElementType
from rich import inspect, print


def _remove_backing_field_string(name):
    return name[1 : name.index(">")] if "k__backingfield" in name.lower() else name


def _convert_basic_fields(obj, element_type):
    if element_type == ClrElementType.String:
        return obj.AsString()
    elif element_type == ClrElementType.Boolean:
        return bool(obj)

    elif element_type in [
        ClrElementType.Int8,
        ClrElementType.Int16,
        ClrElementType.Int32,
        ClrElementType.Int64,
        ClrElementType.UInt8,
        ClrElementType.UInt16,
        ClrElementType.UInt32,
        ClrElementType.UInt64,
    ]:
        return int(obj)
    elif element_type in [ClrElementType.Float, ClrElementType.Double]:
        return float(obj)
    elif element_type == ClrElementType.Pointer:
        return hex(obj.ToInt64())
    else:
        return repr(obj)


def _check_basic_fields(obj, field, element_type=None):
    """ "Check fields for basic values"""

    # Check to see if element_type was passed or if we can get from field object
    if not element_type:
        element_type = field.get_ElementType()

    field_data = None
    if element_type == ClrElementType.String:
        field_data = obj.ReadStringField(field.Name)

    elif element_type == ClrElementType.Boolean:
        field_data = obj.ReadField[bool](field.Name)

    elif element_type == ClrElementType.Int8:
        field_data = obj.ReadField[System.Int8](field.Name)
    elif element_type == ClrElementType.Int16:
        field_data = obj.ReadField[System.Int16](field.Name)
    elif element_type == ClrElementType.Int32:
        field_data = obj.ReadField[System.Int32](field.Name)
    elif element_type == ClrElementType.Int64:
        field_data = obj.ReadField[System.Int64](field.Name)
    elif element_type == ClrElementType.UInt8:
        field_data = obj.ReadField[System.Byte](field.Name)
    elif element_type == ClrElementType.UInt16:
        field_data = obj.ReadField[System.UInt16](field.Name)
    elif element_type == ClrElementType.UInt32:
        field_data = obj.ReadField[System.UInt32](field.Name)
    elif element_type == ClrElementType.UInt64:
        field_data = obj.ReadField[System.UInt64](field.Name)
    elif element_type == ClrElementType.Float:
        field_data = obj.ReadField[System.Single](field.Name)
    elif element_type == ClrElementType.Double:
        field_data = obj.ReadField[System.Double](field.Name)

    elif element_type == ClrElementType.Pointer:
        ptr = obj.ReadField[System.IntPtr](field.Name)
        field_data = hex(ptr.ToInt64())

    return field_data


def _iter_field(runtime, obj, field, visited_objects, is_dict=False):
    """Recursively iterates through fields"""
    #                 Array = 20
    #               Boolean = 2
    #                  Char = 3
    #                 Class = 18
    #                Double = 13
    #                 Float = 12
    #       FunctionPointer = 27
    #  GenericInstantiation = 21
    #                 Int16 = 6
    #                 Int32 = 8
    #                 Int64 = 10
    #                  Int8 = 4
    #                  MVar = 30
    #             NativeInt = 24
    #            NativeUInt = 25
    #                Object = 28
    #               Pointer = 15
    #                String = 14
    #                Struct = 17
    #               SZArray = 29
    #                UInt16 = 7
    #                UInt32 = 9
    #                UInt64 = 11
    #                 UInt8 = 5
    #               Unknown = 0
    #                   Var = 19
    #                  Void = 1

    # Also Arrays are a little harder because we should figure out the type first.
    # Also, Check to see if we've been here before. If so, return

    # TODO: Figure out the best way to prevent recursion
    if (obj.Address, field) in visited_objects:
        return field
    visited_objects.add(tuple((obj.Address, field)))
    if is_dict:
        field_data = []

        # we have to loop this way because ClrArray object is not iterable in Python
        for idx in range(field.Length):

            entry = field.GetStructValue(idx)

            key_data = {}
            value_data = {}

            try:
                key_obj = entry.ReadValueTypeField("key")
            except:
                key_obj = entry.ReadObjectField("key")

            if key_type := key_obj.get_Type():
                for sub_field in key_type.Fields:
                    sub_field_name = _remove_backing_field_string(sub_field.Name)
                    key_data[sub_field_name] = _iter_field(
                        runtime, key_obj, sub_field, visited_objects
                    )
            else:
                key_data = key_obj

            try:
                value_obj = entry.ReadValueTypeField("value")
            except:
                value_obj = entry.ReadObjectField("value")

            if type_ := value_obj.get_Type():
                for sub_field in type_.Fields:
                    sub_field_name = _remove_backing_field_string(sub_field.Name)
                    value_data[sub_field_name] = _iter_field(
                        runtime, value_obj, sub_field, visited_objects
                    )

            field_data.append(
                {
                    "key": key_data,
                    "value": value_data,
                }
            )
    else:
        # Normal parsing
        element_type = field.get_ElementType()
        field_data = _check_basic_fields(obj, field)

        # If it's not basic, be complex
        if not field_data:

            if element_type in [ClrElementType.Class, ClrElementType.Object]:
                field_data = {}
                sub_obj = runtime.Heap.GetObject(
                    obj.ReadObjectField(field.Name).Address
                )

                if sub_obj.IsNull:
                    field_data = None
                elif sub_obj.IsValid and not sub_obj.IsFree:
                    if sub_obj.Type:

                        # If a Dictionary, we don't want ALL the fields. Let the _iter_field handle this.
                        if sub_obj.Type.Name.startswith(
                            "System.Collections.Generic.Dictionary"
                        ):
                            try:
                                entries = sub_obj.ReadObjectField("entries")
                            except:
                                try:
                                    entries = sub_obj.ReadObjectField("_entries")
                                except:
                                    # Weird case where sometimes it's referred to as _dictionary and _entries is a level below
                                    # inspect(sub_obj)
                                    # entries = sub_obj.ReadObjectField(
                                    #     "_dictionary"
                                    # ).ReadObjectField("_entries")
                                    entries = None
                                    field_data = {}

                            if entries:
                                if entries.IsNull:
                                    field_data = {}
                                else:
                                    field_data = _iter_field(
                                        runtime,
                                        sub_obj,
                                        entries.AsArray(),
                                        visited_objects,
                                        is_dict=True,
                                    )
                        else:
                            for sub_field in sub_obj.Type.Fields:
                                sub_field_name = _remove_backing_field_string(
                                    sub_field.Name
                                )
                                field_data[sub_field_name] = _iter_field(
                                    runtime, sub_obj, sub_field, visited_objects
                                )

                    # If we get here, try to parse as a basic type. If not, then we need additional logic for element type
                    else:
                        field_data = _convert_basic_fields(sub_obj, element_type)
                        if not field_data:
                            inspect(ClrElementType)
                            inspect(sub_obj, all=True)

            elif element_type == ClrElementType.SZArray:
                field_data = []
                sub_obj = obj.ReadObjectField(field.Name)

                if sub_obj.IsNull:
                    field_data = None
                elif sub_obj.IsValid and not sub_obj.IsFree:
                    if sub_obj.Type:
                        for sub_field in sub_obj.Type.Fields:
                            field_data.append(
                                _iter_field(
                                    runtime, sub_obj, sub_field, visited_objects
                                )
                            )
                    else:
                        field_data = None
                else:
                    field_data = None
            elif field.IsValueType:
                field_data = {}
                value_obj = obj.ReadValueTypeField(field.Name)
                for sub_field in value_obj.get_Type().Fields:
                    sub_field_name = _remove_backing_field_string(sub_field.Name)
                    field_data[sub_field_name] = _iter_field(
                        runtime, value_obj, sub_field, visited_objects
                    )

    return field_data


@lru_cache
def parse_obj(runtime, obj, console) -> Dict:
    output = {}

    # Helps with recursion.
    visited_objects = set()

    try:
        for field in obj.Type.Fields:
            field_name = _remove_backing_field_string(field.Name)
            output[field_name] = _iter_field(runtime, obj, field, visited_objects)

        return output
    except RecursionError:
        console.print_exception(show_locals=True)
        console.print(
            f"Recursion error happened in field {field.Name}. Logic needs to be fixed to handle this type"
        )
    except Exception:
        console.print_exception()
