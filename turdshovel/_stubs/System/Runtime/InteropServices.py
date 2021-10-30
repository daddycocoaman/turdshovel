# encoding: utf-8
# module System.Runtime.InteropServices calls itself InteropServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Memory, Version=4.0.1.1, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class _Attribute:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _Attribute, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _Attribute, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _Attribute) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _Attribute, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AllowReversePInvokeCallsAttribute(Attribute, _Attribute):
    """ AllowReversePInvokeCallsAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Architecture(Enum, IComparable, IFormattable, IConvertible):
    """ enum Architecture, values: Arm (2), Arm64 (3), X64 (1), X86 (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Arm = None
    Arm64 = None
    value__ = None
    X64 = None
    X86 = None


class ArrayWithOffset(object):
    """ ArrayWithOffset(array: object, offset: int) """
    def Equals(self, obj):
        """
        Equals(self: ArrayWithOffset, obj: object) -> bool
        Equals(self: ArrayWithOffset, obj: ArrayWithOffset) -> bool
        """
        pass

    def GetArray(self):
        """ GetArray(self: ArrayWithOffset) -> object """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ArrayWithOffset) -> int """
        pass

    def GetOffset(self):
        """ GetOffset(self: ArrayWithOffset) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, array, offset):
        """
        __new__[ArrayWithOffset]() -> ArrayWithOffset
        
        __new__(cls: type, array: object, offset: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class AssemblyRegistrationFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) AssemblyRegistrationFlags, values: None (0), SetCodeBase (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    None = None
    SetCodeBase = None
    value__ = None


class AutomationProxyAttribute(Attribute, _Attribute):
    """ AutomationProxyAttribute(val: bool) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, val):
        """ __new__(cls: type, val: bool) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: AutomationProxyAttribute) -> bool

"""



class BestFitMappingAttribute(Attribute, _Attribute):
    """ BestFitMappingAttribute(BestFitMapping: bool) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, BestFitMapping):
        """ __new__(cls: type, BestFitMapping: bool) """
        pass

    BestFitMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BestFitMapping(self: BestFitMappingAttribute) -> bool

"""


    ThrowOnUnmappableChar = None


class BINDPTR(object):
    # no doc
    lpfuncdesc = None
    lptcomp = None
    lpvardesc = None


class BIND_OPTS(object):
    # no doc
    cbStruct = None
    dwTickCountDeadline = None
    grfFlags = None
    grfMode = None


class BStrWrapper(object):
    """
    BStrWrapper(value: str)
    BStrWrapper(value: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__(cls: type, value: str)
        __new__(cls: type, value: object)
        """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedObject(self: BStrWrapper) -> str

"""



class CALLCONV(Enum, IComparable, IFormattable, IConvertible):
    """ enum CALLCONV, values: CC_CDECL (1), CC_MACPASCAL (3), CC_MAX (9), CC_MPWCDECL (7), CC_MPWPASCAL (8), CC_MSCPASCAL (2), CC_PASCAL (2), CC_RESERVED (5), CC_STDCALL (4), CC_SYSCALL (6) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CC_CDECL = None
    CC_MACPASCAL = None
    CC_MAX = None
    CC_MPWCDECL = None
    CC_MPWPASCAL = None
    CC_MSCPASCAL = None
    CC_PASCAL = None
    CC_RESERVED = None
    CC_STDCALL = None
    CC_SYSCALL = None
    value__ = None


class CallingConvention(Enum, IComparable, IFormattable, IConvertible):
    """ enum CallingConvention, values: Cdecl (2), FastCall (5), StdCall (3), ThisCall (4), Winapi (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Cdecl = None
    FastCall = None
    StdCall = None
    ThisCall = None
    value__ = None
    Winapi = None


class CharSet(Enum, IComparable, IFormattable, IConvertible):
    """ enum CharSet, values: Ansi (2), Auto (4), None (1), Unicode (3) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Ansi = None
    Auto = None
    None = None
    Unicode = None
    value__ = None


class ClassInterfaceAttribute(Attribute, _Attribute):
    """
    ClassInterfaceAttribute(classInterfaceType: ClassInterfaceType)
    ClassInterfaceAttribute(classInterfaceType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classInterfaceType):
        """
        __new__(cls: type, classInterfaceType: ClassInterfaceType)
        __new__(cls: type, classInterfaceType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ClassInterfaceAttribute) -> ClassInterfaceType

"""



class ClassInterfaceType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ClassInterfaceType, values: AutoDispatch (1), AutoDual (2), None (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AutoDispatch = None
    AutoDual = None
    None = None
    value__ = None


class CoClassAttribute(Attribute, _Attribute):
    """ CoClassAttribute(coClass: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, coClass):
        """ __new__(cls: type, coClass: Type) """
        pass

    CoClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoClass(self: CoClassAttribute) -> Type

"""



class ComAliasNameAttribute(Attribute, _Attribute):
    """ ComAliasNameAttribute(alias: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, alias):
        """ __new__(cls: type, alias: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ComAliasNameAttribute) -> str

"""



class ComCompatibleVersionAttribute(Attribute, _Attribute):
    """ ComCompatibleVersionAttribute(major: int, minor: int, build: int, revision: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor, build, revision):
        """ __new__(cls: type, major: int, minor: int, build: int, revision: int) """
        pass

    BuildNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BuildNumber(self: ComCompatibleVersionAttribute) -> int

"""

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorVersion(self: ComCompatibleVersionAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorVersion(self: ComCompatibleVersionAttribute) -> int

"""

    RevisionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RevisionNumber(self: ComCompatibleVersionAttribute) -> int

"""



class ComConversionLossAttribute(Attribute, _Attribute):
    """ ComConversionLossAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComDefaultInterfaceAttribute(Attribute, _Attribute):
    """ ComDefaultInterfaceAttribute(defaultInterface: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, defaultInterface):
        """ __new__(cls: type, defaultInterface: Type) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ComDefaultInterfaceAttribute) -> Type

"""



class ComEventInterfaceAttribute(Attribute, _Attribute):
    """ ComEventInterfaceAttribute(SourceInterface: Type, EventProvider: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, SourceInterface, EventProvider):
        """ __new__(cls: type, SourceInterface: Type, EventProvider: Type) """
        pass

    EventProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventProvider(self: ComEventInterfaceAttribute) -> Type

"""

    SourceInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceInterface(self: ComEventInterfaceAttribute) -> Type

"""



class ComEventsHelper(object):
    # no doc
    @staticmethod
    def Combine(rcw, iid, dispid, d):
        """ Combine(rcw: object, iid: Guid, dispid: int, d: Delegate) """
        pass

    @staticmethod
    def Remove(rcw, iid, dispid, d):
        """ Remove(rcw: object, iid: Guid, dispid: int, d: Delegate) -> Delegate """
        pass

    __all__ = [
        'Combine',
        'Remove',
    ]


class ExternalException(SystemException, ISerializable, _Exception):
    """
    ExternalException()
    ExternalException(message: str)
    ExternalException(message: str, inner: Exception)
    ExternalException(message: str, errorCode: int)
    """
    def ToString(self):
        """ ToString(self: ExternalException) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorCode(self: ExternalException) -> int

"""


    SerializeObjectState = None


class COMException(ExternalException, ISerializable, _Exception):
    """
    COMException()
    COMException(message: str)
    COMException(message: str, inner: Exception)
    COMException(message: str, errorCode: int)
    """
    def ToString(self):
        """ ToString(self: COMException) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ComImportAttribute(Attribute, _Attribute):
    """ ComImportAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComInterfaceType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ComInterfaceType, values: InterfaceIsDual (0), InterfaceIsIDispatch (2), InterfaceIsIInspectable (3), InterfaceIsIUnknown (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    InterfaceIsDual = None
    InterfaceIsIDispatch = None
    InterfaceIsIInspectable = None
    InterfaceIsIUnknown = None
    value__ = None


class ComMemberType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ComMemberType, values: Method (0), PropGet (1), PropSet (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Method = None
    PropGet = None
    PropSet = None
    value__ = None


class ComRegisterFunctionAttribute(Attribute, _Attribute):
    """ ComRegisterFunctionAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComSourceInterfacesAttribute(Attribute, _Attribute):
    """
    ComSourceInterfacesAttribute(sourceInterfaces: str)
    ComSourceInterfacesAttribute(sourceInterface: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type, sourceInterface4: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, sourceInterfaces: str)
        __new__(cls: type, sourceInterface: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type, sourceInterface4: Type)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ComSourceInterfacesAttribute) -> str

"""



class ComUnregisterFunctionAttribute(Attribute, _Attribute):
    """ ComUnregisterFunctionAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ComVisibleAttribute(Attribute, _Attribute):
    """ ComVisibleAttribute(visibility: bool) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, visibility):
        """ __new__(cls: type, visibility: bool) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ComVisibleAttribute) -> bool

"""



class CONNECTDATA(object):
    # no doc
    dwCookie = None
    pUnk = None


class CriticalHandle(CriticalFinalizerObject, IDisposable):
    # no doc
    def Close(self):
        """ Close(self: CriticalHandle) """
        pass

    def Dispose(self):
        """ Dispose(self: CriticalHandle) """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: CriticalHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """ SetHandle(self: CriticalHandle, handle: IntPtr) """
        pass

    def SetHandleAsInvalid(self):
        """ SetHandleAsInvalid(self: CriticalHandle) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, invalidHandleValue: IntPtr) """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: CriticalHandle) -> bool

"""

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInvalid(self: CriticalHandle) -> bool

"""


    handle = None


class CurrencyWrapper(object):
    """
    CurrencyWrapper(obj: Decimal)
    CurrencyWrapper(obj: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """
        __new__(cls: type, obj: Decimal)
        __new__(cls: type, obj: object)
        """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedObject(self: CurrencyWrapper) -> Decimal

"""



class CustomQueryInterfaceMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum CustomQueryInterfaceMode, values: Allow (1), Ignore (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Allow = None
    Ignore = None
    value__ = None


class CustomQueryInterfaceResult(Enum, IComparable, IFormattable, IConvertible):
    """ enum CustomQueryInterfaceResult, values: Failed (2), Handled (0), NotHandled (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Failed = None
    Handled = None
    NotHandled = None
    value__ = None


class DefaultCharSetAttribute(Attribute, _Attribute):
    """ DefaultCharSetAttribute(charSet: CharSet) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, charSet):
        """ __new__(cls: type, charSet: CharSet) """
        pass

    CharSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CharSet(self: DefaultCharSetAttribute) -> CharSet

"""



class DefaultDllImportSearchPathsAttribute(Attribute, _Attribute):
    """ DefaultDllImportSearchPathsAttribute(paths: DllImportSearchPath) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, paths):
        """ __new__(cls: type, paths: DllImportSearchPath) """
        pass

    Paths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Paths(self: DefaultDllImportSearchPathsAttribute) -> DllImportSearchPath

"""



class DefaultParameterValueAttribute(Attribute, _Attribute):
    """ DefaultParameterValueAttribute(value: object) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: object) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DefaultParameterValueAttribute) -> object

"""



class DESCKIND(Enum, IComparable, IFormattable, IConvertible):
    """ enum DESCKIND, values: DESCKIND_FUNCDESC (1), DESCKIND_IMPLICITAPPOBJ (4), DESCKIND_MAX (5), DESCKIND_NONE (0), DESCKIND_TYPECOMP (3), DESCKIND_VARDESC (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DESCKIND_FUNCDESC = None
    DESCKIND_IMPLICITAPPOBJ = None
    DESCKIND_MAX = None
    DESCKIND_NONE = None
    DESCKIND_TYPECOMP = None
    DESCKIND_VARDESC = None
    value__ = None


class DispatchWrapper(object):
    """ DispatchWrapper(obj: object) """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedObject(self: DispatchWrapper) -> object

"""



class DispIdAttribute(Attribute, _Attribute):
    """ DispIdAttribute(dispId: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dispId):
        """ __new__(cls: type, dispId: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DispIdAttribute) -> int

"""



class DISPPARAMS(object):
    # no doc
    cArgs = None
    cNamedArgs = None
    rgdispidNamedArgs = None
    rgvarg = None


class DllImportAttribute(Attribute, _Attribute):
    """ DllImportAttribute(dllName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dllName):
        """ __new__(cls: type, dllName: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DllImportAttribute) -> str

"""


    BestFitMapping = None
    CallingConvention = None
    CharSet = None
    EntryPoint = None
    ExactSpelling = None
    PreserveSig = None
    SetLastError = None
    ThrowOnUnmappableChar = None


class DllImportSearchPath(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) DllImportSearchPath, values: ApplicationDirectory (512), AssemblyDirectory (2), LegacyBehavior (0), SafeDirectories (4096), System32 (2048), UseDllDirectoryForDependencies (256), UserDirectories (1024) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ApplicationDirectory = None
    AssemblyDirectory = None
    LegacyBehavior = None
    SafeDirectories = None
    System32 = None
    UseDllDirectoryForDependencies = None
    UserDirectories = None
    value__ = None


class ELEMDESC(object):
    # no doc
    desc = None
    DESCUNION = None
    tdesc = None


class ErrorWrapper(object):
    """
    ErrorWrapper(errorCode: int)
    ErrorWrapper(errorCode: object)
    ErrorWrapper(e: Exception)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, errorCode: int)
        __new__(cls: type, errorCode: object)
        __new__(cls: type, e: Exception)
        """
        pass

    ErrorCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorCode(self: ErrorWrapper) -> int

"""



class EXCEPINFO(object):
    # no doc
    bstrDescription = None
    bstrHelpFile = None
    bstrSource = None
    dwHelpContext = None
    pfnDeferredFillIn = None
    pvReserved = None
    wCode = None
    wReserved = None


class ExporterEventKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum ExporterEventKind, values: ERROR_REFTOINVALIDASSEMBLY (2), NOTIF_CONVERTWARNING (1), NOTIF_TYPECONVERTED (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ERROR_REFTOINVALIDASSEMBLY = None
    NOTIF_CONVERTWARNING = None
    NOTIF_TYPECONVERTED = None
    value__ = None


class ExtensibleClassFactory(object):
    # no doc
    @staticmethod
    def RegisterObjectCreationCallback(callback):
        """ RegisterObjectCreationCallback(callback: ObjectCreationDelegate) """
        pass


class FieldOffsetAttribute(Attribute, _Attribute):
    """ FieldOffsetAttribute(offset: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, offset):
        """ __new__(cls: type, offset: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: FieldOffsetAttribute) -> int

"""



class FILETIME(object):
    # no doc
    dwHighDateTime = None
    dwLowDateTime = None


class FUNCDESC(object):
    # no doc
    callconv = None
    cParams = None
    cParamsOpt = None
    cScodes = None
    elemdescFunc = None
    funckind = None
    invkind = None
    lprgelemdescParam = None
    lprgscode = None
    memid = None
    oVft = None
    wFuncFlags = None


class FUNCFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) FUNCFLAGS, values: FUNCFLAG_FBINDABLE (4), FUNCFLAG_FDEFAULTBIND (32), FUNCFLAG_FDEFAULTCOLLELEM (256), FUNCFLAG_FDISPLAYBIND (16), FUNCFLAG_FHIDDEN (64), FUNCFLAG_FIMMEDIATEBIND (4096), FUNCFLAG_FNONBROWSABLE (1024), FUNCFLAG_FREPLACEABLE (2048), FUNCFLAG_FREQUESTEDIT (8), FUNCFLAG_FRESTRICTED (1), FUNCFLAG_FSOURCE (2), FUNCFLAG_FUIDEFAULT (512), FUNCFLAG_FUSESGETLASTERROR (128) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FUNCFLAG_FBINDABLE = None
    FUNCFLAG_FDEFAULTBIND = None
    FUNCFLAG_FDEFAULTCOLLELEM = None
    FUNCFLAG_FDISPLAYBIND = None
    FUNCFLAG_FHIDDEN = None
    FUNCFLAG_FIMMEDIATEBIND = None
    FUNCFLAG_FNONBROWSABLE = None
    FUNCFLAG_FREPLACEABLE = None
    FUNCFLAG_FREQUESTEDIT = None
    FUNCFLAG_FRESTRICTED = None
    FUNCFLAG_FSOURCE = None
    FUNCFLAG_FUIDEFAULT = None
    FUNCFLAG_FUSESGETLASTERROR = None
    value__ = None


class FUNCKIND(Enum, IComparable, IFormattable, IConvertible):
    """ enum FUNCKIND, values: FUNC_DISPATCH (4), FUNC_NONVIRTUAL (2), FUNC_PUREVIRTUAL (1), FUNC_STATIC (3), FUNC_VIRTUAL (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FUNC_DISPATCH = None
    FUNC_NONVIRTUAL = None
    FUNC_PUREVIRTUAL = None
    FUNC_STATIC = None
    FUNC_VIRTUAL = None
    value__ = None


class GCHandle(object):
    # no doc
    def AddrOfPinnedObject(self):
        """ AddrOfPinnedObject(self: GCHandle) -> IntPtr """
        pass

    @staticmethod
    def Alloc(value, type=None):
        """
        Alloc(value: object) -> GCHandle
        Alloc(value: object, type: GCHandleType) -> GCHandle
        """
        pass

    def Equals(self, o):
        """ Equals(self: GCHandle, o: object) -> bool """
        pass

    def Free(self):
        """ Free(self: GCHandle) """
        pass

    @staticmethod
    def FromIntPtr(value):
        """ FromIntPtr(value: IntPtr) -> GCHandle """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GCHandle) -> int """
        pass

    @staticmethod
    def ToIntPtr(value):
        """ ToIntPtr(value: GCHandle) -> IntPtr """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsAllocated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAllocated(self: GCHandle) -> bool

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: GCHandle) -> object

Set: Target(self: GCHandle) = value
"""



class GCHandleType(Enum, IComparable, IFormattable, IConvertible):
    """ enum GCHandleType, values: Normal (2), Pinned (3), Weak (0), WeakTrackResurrection (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Normal = None
    Pinned = None
    value__ = None
    Weak = None
    WeakTrackResurrection = None


class GuidAttribute(Attribute, _Attribute):
    """ GuidAttribute(guid: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GuidAttribute) -> str

"""



class HandleCollector(object):
    """
    HandleCollector(name: str, initialThreshold: int)
    HandleCollector(name: str, initialThreshold: int, maximumThreshold: int)
    """
    def Add(self):
        """ Add(self: HandleCollector) """
        pass

    def Remove(self):
        """ Remove(self: HandleCollector) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, initialThreshold, maximumThreshold=None):
        """
        __new__(cls: type, name: str, initialThreshold: int)
        __new__(cls: type, name: str, initialThreshold: int, maximumThreshold: int)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: HandleCollector) -> int

"""

    InitialThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialThreshold(self: HandleCollector) -> int

"""

    MaximumThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumThreshold(self: HandleCollector) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HandleCollector) -> str

"""



class HandleRef(object):
    """ HandleRef(wrapper: object, handle: IntPtr) """
    @staticmethod
    def ToIntPtr(value):
        """ ToIntPtr(value: HandleRef) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, wrapper, handle):
        """
        __new__[HandleRef]() -> HandleRef
        
        __new__(cls: type, wrapper: object, handle: IntPtr)
        """
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: HandleRef) -> IntPtr

"""

    Wrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wrapper(self: HandleRef) -> object

"""



class ICustomAdapter:
    # no doc
    def GetUnderlyingObject(self):
        """ GetUnderlyingObject(self: ICustomAdapter) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomFactory:
    # no doc
    def CreateInstance(self, serverType):
        """ CreateInstance(self: ICustomFactory, serverType: Type) -> MarshalByRefObject """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomMarshaler:
    # no doc
    def CleanUpManagedData(self, ManagedObj):
        """ CleanUpManagedData(self: ICustomMarshaler, ManagedObj: object) """
        pass

    def CleanUpNativeData(self, pNativeData):
        """ CleanUpNativeData(self: ICustomMarshaler, pNativeData: IntPtr) """
        pass

    def GetNativeDataSize(self):
        """ GetNativeDataSize(self: ICustomMarshaler) -> int """
        pass

    def MarshalManagedToNative(self, ManagedObj):
        """ MarshalManagedToNative(self: ICustomMarshaler, ManagedObj: object) -> IntPtr """
        pass

    def MarshalNativeToManaged(self, pNativeData):
        """ MarshalNativeToManaged(self: ICustomMarshaler, pNativeData: IntPtr) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomQueryInterface:
    # no doc
    def GetInterface(self, iid, ppv):
        """ GetInterface(self: ICustomQueryInterface, iid: Guid) -> (CustomQueryInterfaceResult, Guid, IntPtr) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDispatchImplAttribute(Attribute, _Attribute):
    """
    IDispatchImplAttribute(implType: IDispatchImplType)
    IDispatchImplAttribute(implType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, implType):
        """
        __new__(cls: type, implType: IDispatchImplType)
        __new__(cls: type, implType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: IDispatchImplAttribute) -> IDispatchImplType

"""



class IDispatchImplType(Enum, IComparable, IFormattable, IConvertible):
    """ enum IDispatchImplType, values: CompatibleImpl (2), InternalImpl (1), SystemDefinedImpl (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CompatibleImpl = None
    InternalImpl = None
    SystemDefinedImpl = None
    value__ = None


class IDLDESC(object):
    # no doc
    dwReserved = None
    wIDLFlags = None


class IDLFLAG(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) IDLFLAG, values: IDLFLAG_FIN (1), IDLFLAG_FLCID (4), IDLFLAG_FOUT (2), IDLFLAG_FRETVAL (8), IDLFLAG_NONE (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IDLFLAG_FIN = None
    IDLFLAG_FLCID = None
    IDLFLAG_FOUT = None
    IDLFLAG_FRETVAL = None
    IDLFLAG_NONE = None
    value__ = None


class IMPLTYPEFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) IMPLTYPEFLAGS, values: IMPLTYPEFLAG_FDEFAULT (1), IMPLTYPEFLAG_FDEFAULTVTABLE (8), IMPLTYPEFLAG_FRESTRICTED (4), IMPLTYPEFLAG_FSOURCE (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IMPLTYPEFLAG_FDEFAULT = None
    IMPLTYPEFLAG_FDEFAULTVTABLE = None
    IMPLTYPEFLAG_FRESTRICTED = None
    IMPLTYPEFLAG_FSOURCE = None
    value__ = None


class ImportedFromTypeLibAttribute(Attribute, _Attribute):
    """ ImportedFromTypeLibAttribute(tlbFile: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tlbFile):
        """ __new__(cls: type, tlbFile: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ImportedFromTypeLibAttribute) -> str

"""



class ImporterEventKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum ImporterEventKind, values: ERROR_REFTOINVALIDTYPELIB (2), NOTIF_CONVERTWARNING (1), NOTIF_TYPECONVERTED (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ERROR_REFTOINVALIDTYPELIB = None
    NOTIF_CONVERTWARNING = None
    NOTIF_TYPECONVERTED = None
    value__ = None


class InAttribute(Attribute, _Attribute):
    """ InAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InterfaceTypeAttribute(Attribute, _Attribute):
    """
    InterfaceTypeAttribute(interfaceType: ComInterfaceType)
    InterfaceTypeAttribute(interfaceType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, interfaceType):
        """
        __new__(cls: type, interfaceType: ComInterfaceType)
        __new__(cls: type, interfaceType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: InterfaceTypeAttribute) -> ComInterfaceType

"""



class InvalidComObjectException(SystemException, ISerializable, _Exception):
    """
    InvalidComObjectException()
    InvalidComObjectException(message: str)
    InvalidComObjectException(message: str, inner: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class InvalidOleVariantTypeException(SystemException, ISerializable, _Exception):
    """
    InvalidOleVariantTypeException()
    InvalidOleVariantTypeException(message: str)
    InvalidOleVariantTypeException(message: str, inner: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class INVOKEKIND(Enum, IComparable, IFormattable, IConvertible):
    """ enum INVOKEKIND, values: INVOKE_FUNC (1), INVOKE_PROPERTYGET (2), INVOKE_PROPERTYPUT (4), INVOKE_PROPERTYPUTREF (8) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    INVOKE_FUNC = None
    INVOKE_PROPERTYGET = None
    INVOKE_PROPERTYPUT = None
    INVOKE_PROPERTYPUTREF = None
    value__ = None


class IRegistrationServices:
    # no doc
    def GetManagedCategoryGuid(self):
        """ GetManagedCategoryGuid(self: IRegistrationServices) -> Guid """
        pass

    def GetProgIdForType(self, type):
        """ GetProgIdForType(self: IRegistrationServices, type: Type) -> str """
        pass

    def GetRegistrableTypesInAssembly(self, assembly):
        """ GetRegistrableTypesInAssembly(self: IRegistrationServices, assembly: Assembly) -> Array[Type] """
        pass

    def RegisterAssembly(self, assembly, flags):
        """ RegisterAssembly(self: IRegistrationServices, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool """
        pass

    def RegisterTypeForComClients(self, type, g):
        """ RegisterTypeForComClients(self: IRegistrationServices, type: Type, g: Guid) -> Guid """
        pass

    def TypeRepresentsComType(self, type):
        """ TypeRepresentsComType(self: IRegistrationServices, type: Type) -> bool """
        pass

    def TypeRequiresRegistration(self, type):
        """ TypeRequiresRegistration(self: IRegistrationServices, type: Type) -> bool """
        pass

    def UnregisterAssembly(self, assembly):
        """ UnregisterAssembly(self: IRegistrationServices, assembly: Assembly) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibConverter:
    # no doc
    def ConvertAssemblyToTypeLib(self, assembly, typeLibName, flags, notifySink):
        """ ConvertAssemblyToTypeLib(self: ITypeLibConverter, assembly: Assembly, typeLibName: str, flags: TypeLibExporterFlags, notifySink: ITypeLibExporterNotifySink) -> object """
        pass

    def ConvertTypeLibToAssembly(self, typeLib, asmFileName, flags, notifySink, publicKey, keyPair, *__args):
        """
        ConvertTypeLibToAssembly(self: ITypeLibConverter, typeLib: object, asmFileName: str, flags: TypeLibImporterFlags, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, asmNamespace: str, asmVersion: Version) -> AssemblyBuilder
        ConvertTypeLibToAssembly(self: ITypeLibConverter, typeLib: object, asmFileName: str, flags: int, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, unsafeInterfaces: bool) -> AssemblyBuilder
        """
        pass

    def GetPrimaryInteropAssembly(self, g, major, minor, lcid, asmName, asmCodeBase):
        """ GetPrimaryInteropAssembly(self: ITypeLibConverter, g: Guid, major: int, minor: int, lcid: int) -> (bool, str, str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibExporterNameProvider:
    # no doc
    def GetNames(self):
        """ GetNames(self: ITypeLibExporterNameProvider) -> Array[str] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibExporterNotifySink:
    # no doc
    def ReportEvent(self, eventKind, eventCode, eventMsg):
        """ ReportEvent(self: ITypeLibExporterNotifySink, eventKind: ExporterEventKind, eventCode: int, eventMsg: str) """
        pass

    def ResolveRef(self, assembly):
        """ ResolveRef(self: ITypeLibExporterNotifySink, assembly: Assembly) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ITypeLibImporterNotifySink:
    # no doc
    def ReportEvent(self, eventKind, eventCode, eventMsg):
        """ ReportEvent(self: ITypeLibImporterNotifySink, eventKind: ImporterEventKind, eventCode: int, eventMsg: str) """
        pass

    def ResolveRef(self, typeLib):
        """ ResolveRef(self: ITypeLibImporterNotifySink, typeLib: object) -> Assembly """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LayoutKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum LayoutKind, values: Auto (3), Explicit (2), Sequential (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Auto = None
    Explicit = None
    Sequential = None
    value__ = None


class LCIDConversionAttribute(Attribute, _Attribute):
    """ LCIDConversionAttribute(lcid: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, lcid):
        """ __new__(cls: type, lcid: int) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: LCIDConversionAttribute) -> int

"""



class LIBFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) LIBFLAGS, values: LIBFLAG_FCONTROL (2), LIBFLAG_FHASDISKIMAGE (8), LIBFLAG_FHIDDEN (4), LIBFLAG_FRESTRICTED (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LIBFLAG_FCONTROL = None
    LIBFLAG_FHASDISKIMAGE = None
    LIBFLAG_FHIDDEN = None
    LIBFLAG_FRESTRICTED = None
    value__ = None


class ManagedToNativeComInteropStubAttribute(Attribute, _Attribute):
    """ ManagedToNativeComInteropStubAttribute(classType: Type, methodName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classType, methodName):
        """ __new__(cls: type, classType: Type, methodName: str) """
        pass

    ClassType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassType(self: ManagedToNativeComInteropStubAttribute) -> Type

"""

    MethodName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodName(self: ManagedToNativeComInteropStubAttribute) -> str

"""



class Marshal(object):
    # no doc
    @staticmethod
    def AddRef(pUnk):
        """ AddRef(pUnk: IntPtr) -> int """
        pass

    @staticmethod
    def AllocCoTaskMem(cb):
        """ AllocCoTaskMem(cb: int) -> IntPtr """
        pass

    @staticmethod
    def AllocHGlobal(cb):
        """
        AllocHGlobal(cb: IntPtr) -> IntPtr
        AllocHGlobal(cb: int) -> IntPtr
        """
        pass

    @staticmethod
    def AreComObjectsAvailableForCleanup():
        """ AreComObjectsAvailableForCleanup() -> bool """
        pass

    @staticmethod
    def BindToMoniker(monikerName):
        """ BindToMoniker(monikerName: str) -> object """
        pass

    @staticmethod
    def ChangeWrapperHandleStrength(otp, fIsWeak):
        """ ChangeWrapperHandleStrength(otp: object, fIsWeak: bool) """
        pass

    @staticmethod
    def CleanupUnusedObjectsInCurrentContext():
        """ CleanupUnusedObjectsInCurrentContext() """
        pass

    @staticmethod
    def Copy(source, *__args):
        """ Copy(source: Array[int], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Char], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Int16], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Int64], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Single], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[float], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Byte], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[IntPtr], startIndex: int, destination: IntPtr, length: int)Copy(source: IntPtr, destination: Array[int], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Char], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Int16], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Int64], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Single], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[float], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Byte], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[IntPtr], startIndex: int, length: int) """
        pass

    @staticmethod
    def CreateAggregatedObject(pOuter, o):
        """
        CreateAggregatedObject(pOuter: IntPtr, o: object) -> IntPtr
        CreateAggregatedObject[T](pOuter: IntPtr, o: T) -> IntPtr
        """
        pass

    @staticmethod
    def CreateWrapperOfType(o, t=None):
        """
        CreateWrapperOfType(o: object, t: Type) -> object
        CreateWrapperOfType[(T, TWrapper)](o: T) -> TWrapper
        """
        pass

    @staticmethod
    def DestroyStructure(ptr, structuretype=None):
        """ DestroyStructure[T](ptr: IntPtr)DestroyStructure(ptr: IntPtr, structuretype: Type) """
        pass

    @staticmethod
    def FinalReleaseComObject(o):
        """ FinalReleaseComObject(o: object) -> int """
        pass

    @staticmethod
    def FreeBSTR(ptr):
        """ FreeBSTR(ptr: IntPtr) """
        pass

    @staticmethod
    def FreeCoTaskMem(ptr):
        """ FreeCoTaskMem(ptr: IntPtr) """
        pass

    @staticmethod
    def FreeHGlobal(hglobal):
        """ FreeHGlobal(hglobal: IntPtr) """
        pass

    @staticmethod
    def GenerateGuidForType(type):
        """ GenerateGuidForType(type: Type) -> Guid """
        pass

    @staticmethod
    def GenerateProgIdForType(type):
        """ GenerateProgIdForType(type: Type) -> str """
        pass

    @staticmethod
    def GetActiveObject(progID):
        """ GetActiveObject(progID: str) -> object """
        pass

    @staticmethod
    def GetComInterfaceForObject(o, T=None, mode=None):
        """
        GetComInterfaceForObject(o: object, T: Type) -> IntPtr
        GetComInterfaceForObject(o: object, T: Type, mode: CustomQueryInterfaceMode) -> IntPtr
        GetComInterfaceForObject[(T, TInterface)](o: T) -> IntPtr
        """
        pass

    @staticmethod
    def GetComInterfaceForObjectInContext(o, t):
        """ GetComInterfaceForObjectInContext(o: object, t: Type) -> IntPtr """
        pass

    @staticmethod
    def GetComObjectData(obj, key):
        """ GetComObjectData(obj: object, key: object) -> object """
        pass

    @staticmethod
    def GetComSlotForMethodInfo(m):
        """ GetComSlotForMethodInfo(m: MemberInfo) -> int """
        pass

    @staticmethod
    def GetDelegateForFunctionPointer(ptr, t=None):
        """
        GetDelegateForFunctionPointer(ptr: IntPtr, t: Type) -> Delegate
        GetDelegateForFunctionPointer[TDelegate](ptr: IntPtr) -> TDelegate
        """
        pass

    @staticmethod
    def GetEndComSlot(t):
        """ GetEndComSlot(t: Type) -> int """
        pass

    @staticmethod
    def GetExceptionCode():
        """ GetExceptionCode() -> int """
        pass

    @staticmethod
    def GetExceptionForHR(errorCode, errorInfo=None):
        """
        GetExceptionForHR(errorCode: int) -> Exception
        GetExceptionForHR(errorCode: int, errorInfo: IntPtr) -> Exception
        """
        pass

    @staticmethod
    def GetExceptionPointers():
        """ GetExceptionPointers() -> IntPtr """
        pass

    @staticmethod
    def GetFunctionPointerForDelegate(d):
        """
        GetFunctionPointerForDelegate(d: Delegate) -> IntPtr
        GetFunctionPointerForDelegate[TDelegate](d: TDelegate) -> IntPtr
        """
        pass

    @staticmethod
    def GetHINSTANCE(m):
        """ GetHINSTANCE(m: Module) -> IntPtr """
        pass

    @staticmethod
    def GetHRForException(e):
        """ GetHRForException(e: Exception) -> int """
        pass

    @staticmethod
    def GetHRForLastWin32Error():
        """ GetHRForLastWin32Error() -> int """
        pass

    @staticmethod
    def GetIDispatchForObject(o):
        """ GetIDispatchForObject(o: object) -> IntPtr """
        pass

    @staticmethod
    def GetIDispatchForObjectInContext(o):
        """ GetIDispatchForObjectInContext(o: object) -> IntPtr """
        pass

    @staticmethod
    def GetITypeInfoForType(t):
        """ GetITypeInfoForType(t: Type) -> IntPtr """
        pass

    @staticmethod
    def GetIUnknownForObject(o):
        """ GetIUnknownForObject(o: object) -> IntPtr """
        pass

    @staticmethod
    def GetIUnknownForObjectInContext(o):
        """ GetIUnknownForObjectInContext(o: object) -> IntPtr """
        pass

    @staticmethod
    def GetLastWin32Error():
        """ GetLastWin32Error() -> int """
        pass

    @staticmethod
    def GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap, pbSignature, cbSignature):
        """ GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int) -> IntPtr """
        pass

    @staticmethod
    def GetMethodInfoForComSlot(t, slot, memberType):
        """ GetMethodInfoForComSlot(t: Type, slot: int, memberType: ComMemberType) -> (MemberInfo, ComMemberType) """
        pass

    @staticmethod
    def GetNativeVariantForObject(obj, pDstNativeVariant):
        """ GetNativeVariantForObject(obj: object, pDstNativeVariant: IntPtr)GetNativeVariantForObject[T](obj: T, pDstNativeVariant: IntPtr) """
        pass

    @staticmethod
    def GetObjectForIUnknown(pUnk):
        """ GetObjectForIUnknown(pUnk: IntPtr) -> object """
        pass

    @staticmethod
    def GetObjectForNativeVariant(pSrcNativeVariant):
        """
        GetObjectForNativeVariant(pSrcNativeVariant: IntPtr) -> object
        GetObjectForNativeVariant[T](pSrcNativeVariant: IntPtr) -> T
        """
        pass

    @staticmethod
    def GetObjectsForNativeVariants(aSrcNativeVariant, cVars):
        """
        GetObjectsForNativeVariants(aSrcNativeVariant: IntPtr, cVars: int) -> Array[object]
        GetObjectsForNativeVariants[T](aSrcNativeVariant: IntPtr, cVars: int) -> Array[T]
        """
        pass

    @staticmethod
    def GetStartComSlot(t):
        """ GetStartComSlot(t: Type) -> int """
        pass

    @staticmethod
    def GetThreadFromFiberCookie(cookie):
        """ GetThreadFromFiberCookie(cookie: int) -> Thread """
        pass

    @staticmethod
    def GetTypedObjectForIUnknown(pUnk, t):
        """ GetTypedObjectForIUnknown(pUnk: IntPtr, t: Type) -> object """
        pass

    @staticmethod
    def GetTypeForITypeInfo(piTypeInfo):
        """ GetTypeForITypeInfo(piTypeInfo: IntPtr) -> Type """
        pass

    @staticmethod
    def GetTypeFromCLSID(clsid):
        """ GetTypeFromCLSID(clsid: Guid) -> Type """
        pass

    @staticmethod
    def GetTypeInfoName(*__args):
        """
        GetTypeInfoName(pTI: UCOMITypeInfo) -> str
        GetTypeInfoName(typeInfo: ITypeInfo) -> str
        """
        pass

    @staticmethod
    def GetTypeLibGuid(*__args):
        """
        GetTypeLibGuid(pTLB: UCOMITypeLib) -> Guid
        GetTypeLibGuid(typelib: ITypeLib) -> Guid
        """
        pass

    @staticmethod
    def GetTypeLibGuidForAssembly(asm):
        """ GetTypeLibGuidForAssembly(asm: Assembly) -> Guid """
        pass

    @staticmethod
    def GetTypeLibLcid(*__args):
        """
        GetTypeLibLcid(pTLB: UCOMITypeLib) -> int
        GetTypeLibLcid(typelib: ITypeLib) -> int
        """
        pass

    @staticmethod
    def GetTypeLibName(*__args):
        """
        GetTypeLibName(pTLB: UCOMITypeLib) -> str
        GetTypeLibName(typelib: ITypeLib) -> str
        """
        pass

    @staticmethod
    def GetTypeLibVersionForAssembly(inputAssembly, majorVersion, minorVersion):
        """ GetTypeLibVersionForAssembly(inputAssembly: Assembly) -> (int, int) """
        pass

    @staticmethod
    def GetUniqueObjectForIUnknown(unknown):
        """ GetUniqueObjectForIUnknown(unknown: IntPtr) -> object """
        pass

    @staticmethod
    def GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap, pbSignature, cbSignature):
        """ GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int) -> IntPtr """
        pass

    @staticmethod
    def IsComObject(o):
        """ IsComObject(o: object) -> bool """
        pass

    @staticmethod
    def IsTypeVisibleFromCom(t):
        """ IsTypeVisibleFromCom(t: Type) -> bool """
        pass

    @staticmethod
    def NumParamBytes(m):
        """ NumParamBytes(m: MethodInfo) -> int """
        pass

    @staticmethod
    def OffsetOf(*__args):
        """
        OffsetOf(t: Type, fieldName: str) -> IntPtr
        OffsetOf[T](fieldName: str) -> IntPtr
        """
        pass

    @staticmethod
    def Prelink(m):
        """ Prelink(m: MethodInfo) """
        pass

    @staticmethod
    def PrelinkAll(c):
        """ PrelinkAll(c: Type) """
        pass

    @staticmethod
    def PtrToStringAnsi(ptr, len=None):
        """
        PtrToStringAnsi(ptr: IntPtr) -> str
        PtrToStringAnsi(ptr: IntPtr, len: int) -> str
        """
        pass

    @staticmethod
    def PtrToStringAuto(ptr, len=None):
        """
        PtrToStringAuto(ptr: IntPtr, len: int) -> str
        PtrToStringAuto(ptr: IntPtr) -> str
        """
        pass

    @staticmethod
    def PtrToStringBSTR(ptr):
        """ PtrToStringBSTR(ptr: IntPtr) -> str """
        pass

    @staticmethod
    def PtrToStringUni(ptr, len=None):
        """
        PtrToStringUni(ptr: IntPtr, len: int) -> str
        PtrToStringUni(ptr: IntPtr) -> str
        """
        pass

    @staticmethod
    def PtrToStructure(ptr, *__args):
        """
        PtrToStructure(ptr: IntPtr, structure: object)PtrToStructure(ptr: IntPtr, structureType: Type) -> object
        PtrToStructure[T](ptr: IntPtr, structure: T)PtrToStructure[T](ptr: IntPtr) -> T
        """
        pass

    @staticmethod
    def QueryInterface(pUnk, iid, ppv):
        """ QueryInterface(pUnk: IntPtr, iid: Guid) -> (int, Guid, IntPtr) """
        pass

    @staticmethod
    def ReadByte(ptr, ofs=None):
        """
        ReadByte(ptr: IntPtr, ofs: int) -> Byte
        ReadByte(ptr: IntPtr) -> Byte
        ReadByte(ptr: object, ofs: int) -> Byte
        """
        pass

    @staticmethod
    def ReadInt16(ptr, ofs=None):
        """
        ReadInt16(ptr: IntPtr, ofs: int) -> Int16
        ReadInt16(ptr: IntPtr) -> Int16
        ReadInt16(ptr: object, ofs: int) -> Int16
        """
        pass

    @staticmethod
    def ReadInt32(ptr, ofs=None):
        """
        ReadInt32(ptr: IntPtr, ofs: int) -> int
        ReadInt32(ptr: IntPtr) -> int
        ReadInt32(ptr: object, ofs: int) -> int
        """
        pass

    @staticmethod
    def ReadInt64(ptr, ofs=None):
        """
        ReadInt64(ptr: IntPtr, ofs: int) -> Int64
        ReadInt64(ptr: IntPtr) -> Int64
        ReadInt64(ptr: object, ofs: int) -> Int64
        """
        pass

    @staticmethod
    def ReadIntPtr(ptr, ofs=None):
        """
        ReadIntPtr(ptr: object, ofs: int) -> IntPtr
        ReadIntPtr(ptr: IntPtr, ofs: int) -> IntPtr
        ReadIntPtr(ptr: IntPtr) -> IntPtr
        """
        pass

    @staticmethod
    def ReAllocCoTaskMem(pv, cb):
        """ ReAllocCoTaskMem(pv: IntPtr, cb: int) -> IntPtr """
        pass

    @staticmethod
    def ReAllocHGlobal(pv, cb):
        """ ReAllocHGlobal(pv: IntPtr, cb: IntPtr) -> IntPtr """
        pass

    @staticmethod
    def Release(pUnk):
        """ Release(pUnk: IntPtr) -> int """
        pass

    @staticmethod
    def ReleaseComObject(o):
        """ ReleaseComObject(o: object) -> int """
        pass

    @staticmethod
    def ReleaseThreadCache():
        """ ReleaseThreadCache() """
        pass

    @staticmethod
    def SecureStringToBSTR(s):
        """ SecureStringToBSTR(s: SecureString) -> IntPtr """
        pass

    @staticmethod
    def SecureStringToCoTaskMemAnsi(s):
        """ SecureStringToCoTaskMemAnsi(s: SecureString) -> IntPtr """
        pass

    @staticmethod
    def SecureStringToCoTaskMemUnicode(s):
        """ SecureStringToCoTaskMemUnicode(s: SecureString) -> IntPtr """
        pass

    @staticmethod
    def SecureStringToGlobalAllocAnsi(s):
        """ SecureStringToGlobalAllocAnsi(s: SecureString) -> IntPtr """
        pass

    @staticmethod
    def SecureStringToGlobalAllocUnicode(s):
        """ SecureStringToGlobalAllocUnicode(s: SecureString) -> IntPtr """
        pass

    @staticmethod
    def SetComObjectData(obj, key, data):
        """ SetComObjectData(obj: object, key: object, data: object) -> bool """
        pass

    @staticmethod
    def SizeOf(*__args):
        """
        SizeOf(structure: object) -> int
        SizeOf(t: Type) -> int
        SizeOf[T](structure: T) -> int
        SizeOf[T]() -> int
        """
        pass

    @staticmethod
    def StringToBSTR(s):
        """ StringToBSTR(s: str) -> IntPtr """
        pass

    @staticmethod
    def StringToCoTaskMemAnsi(s):
        """ StringToCoTaskMemAnsi(s: str) -> IntPtr """
        pass

    @staticmethod
    def StringToCoTaskMemAuto(s):
        """ StringToCoTaskMemAuto(s: str) -> IntPtr """
        pass

    @staticmethod
    def StringToCoTaskMemUni(s):
        """ StringToCoTaskMemUni(s: str) -> IntPtr """
        pass

    @staticmethod
    def StringToHGlobalAnsi(s):
        """ StringToHGlobalAnsi(s: str) -> IntPtr """
        pass

    @staticmethod
    def StringToHGlobalAuto(s):
        """ StringToHGlobalAuto(s: str) -> IntPtr """
        pass

    @staticmethod
    def StringToHGlobalUni(s):
        """ StringToHGlobalUni(s: str) -> IntPtr """
        pass

    @staticmethod
    def StructureToPtr(structure, ptr, fDeleteOld):
        """ StructureToPtr[T](structure: T, ptr: IntPtr, fDeleteOld: bool)StructureToPtr(structure: object, ptr: IntPtr, fDeleteOld: bool) """
        pass

    @staticmethod
    def ThrowExceptionForHR(errorCode, errorInfo=None):
        """ ThrowExceptionForHR(errorCode: int)ThrowExceptionForHR(errorCode: int, errorInfo: IntPtr) """
        pass

    @staticmethod
    def UnsafeAddrOfPinnedArrayElement(arr, index):
        """
        UnsafeAddrOfPinnedArrayElement[T](arr: Array[T], index: int) -> IntPtr
        UnsafeAddrOfPinnedArrayElement(arr: Array, index: int) -> IntPtr
        """
        pass

    @staticmethod
    def WriteByte(ptr, *__args):
        """ WriteByte(ptr: IntPtr, ofs: int, val: Byte)WriteByte(ptr: IntPtr, val: Byte)WriteByte(ofs: int, val: Byte) -> object """
        pass

    @staticmethod
    def WriteInt16(ptr, *__args):
        """
        WriteInt16(ptr: IntPtr, ofs: int, val: Int16)WriteInt16(ptr: IntPtr, val: Int16)WriteInt16(ptr: IntPtr, ofs: int, val: Char)WriteInt16(ofs: int, val: Char) -> object
        WriteInt16(ptr: IntPtr, val: Char)WriteInt16(ofs: int, val: Int16) -> object
        """
        pass

    @staticmethod
    def WriteInt32(ptr, *__args):
        """ WriteInt32(ptr: IntPtr, ofs: int, val: int)WriteInt32(ptr: IntPtr, val: int)WriteInt32(ofs: int, val: int) -> object """
        pass

    @staticmethod
    def WriteInt64(ptr, *__args):
        """ WriteInt64(ptr: IntPtr, ofs: int, val: Int64)WriteInt64(ptr: IntPtr, val: Int64)WriteInt64(ofs: int, val: Int64) -> object """
        pass

    @staticmethod
    def WriteIntPtr(ptr, *__args):
        """
        WriteIntPtr(ptr: IntPtr, ofs: int, val: IntPtr)WriteIntPtr(ofs: int, val: IntPtr) -> object
        WriteIntPtr(ptr: IntPtr, val: IntPtr)
        """
        pass

    @staticmethod
    def ZeroFreeBSTR(s):
        """ ZeroFreeBSTR(s: IntPtr) """
        pass

    @staticmethod
    def ZeroFreeCoTaskMemAnsi(s):
        """ ZeroFreeCoTaskMemAnsi(s: IntPtr) """
        pass

    @staticmethod
    def ZeroFreeCoTaskMemUnicode(s):
        """ ZeroFreeCoTaskMemUnicode(s: IntPtr) """
        pass

    @staticmethod
    def ZeroFreeGlobalAllocAnsi(s):
        """ ZeroFreeGlobalAllocAnsi(s: IntPtr) """
        pass

    @staticmethod
    def ZeroFreeGlobalAllocUnicode(s):
        """ ZeroFreeGlobalAllocUnicode(s: IntPtr) """
        pass

    SystemDefaultCharSize = 2
    SystemMaxDBCSCharSize = 1
    __all__ = [
        'AddRef',
        'AllocCoTaskMem',
        'AllocHGlobal',
        'AreComObjectsAvailableForCleanup',
        'BindToMoniker',
        'ChangeWrapperHandleStrength',
        'CleanupUnusedObjectsInCurrentContext',
        'Copy',
        'CreateAggregatedObject',
        'CreateWrapperOfType',
        'DestroyStructure',
        'FinalReleaseComObject',
        'FreeBSTR',
        'FreeCoTaskMem',
        'FreeHGlobal',
        'GenerateGuidForType',
        'GenerateProgIdForType',
        'GetActiveObject',
        'GetComInterfaceForObject',
        'GetComInterfaceForObjectInContext',
        'GetComObjectData',
        'GetComSlotForMethodInfo',
        'GetDelegateForFunctionPointer',
        'GetEndComSlot',
        'GetExceptionCode',
        'GetExceptionForHR',
        'GetExceptionPointers',
        'GetFunctionPointerForDelegate',
        'GetHINSTANCE',
        'GetHRForException',
        'GetHRForLastWin32Error',
        'GetIDispatchForObject',
        'GetIDispatchForObjectInContext',
        'GetITypeInfoForType',
        'GetIUnknownForObject',
        'GetIUnknownForObjectInContext',
        'GetLastWin32Error',
        'GetManagedThunkForUnmanagedMethodPtr',
        'GetMethodInfoForComSlot',
        'GetNativeVariantForObject',
        'GetObjectForIUnknown',
        'GetObjectForNativeVariant',
        'GetObjectsForNativeVariants',
        'GetStartComSlot',
        'GetThreadFromFiberCookie',
        'GetTypedObjectForIUnknown',
        'GetTypeForITypeInfo',
        'GetTypeFromCLSID',
        'GetTypeInfoName',
        'GetTypeLibGuid',
        'GetTypeLibGuidForAssembly',
        'GetTypeLibLcid',
        'GetTypeLibName',
        'GetTypeLibVersionForAssembly',
        'GetUniqueObjectForIUnknown',
        'GetUnmanagedThunkForManagedMethodPtr',
        'IsComObject',
        'IsTypeVisibleFromCom',
        'NumParamBytes',
        'OffsetOf',
        'Prelink',
        'PrelinkAll',
        'PtrToStringAnsi',
        'PtrToStringAuto',
        'PtrToStringBSTR',
        'PtrToStringUni',
        'PtrToStructure',
        'QueryInterface',
        'ReadByte',
        'ReadInt16',
        'ReadInt32',
        'ReadInt64',
        'ReadIntPtr',
        'ReAllocCoTaskMem',
        'ReAllocHGlobal',
        'Release',
        'ReleaseComObject',
        'ReleaseThreadCache',
        'SecureStringToBSTR',
        'SecureStringToCoTaskMemAnsi',
        'SecureStringToCoTaskMemUnicode',
        'SecureStringToGlobalAllocAnsi',
        'SecureStringToGlobalAllocUnicode',
        'SetComObjectData',
        'SizeOf',
        'StringToBSTR',
        'StringToCoTaskMemAnsi',
        'StringToCoTaskMemAuto',
        'StringToCoTaskMemUni',
        'StringToHGlobalAnsi',
        'StringToHGlobalAuto',
        'StringToHGlobalUni',
        'StructureToPtr',
        'SystemDefaultCharSize',
        'SystemMaxDBCSCharSize',
        'ThrowExceptionForHR',
        'UnsafeAddrOfPinnedArrayElement',
        'WriteByte',
        'WriteInt16',
        'WriteInt32',
        'WriteInt64',
        'WriteIntPtr',
        'ZeroFreeBSTR',
        'ZeroFreeCoTaskMemAnsi',
        'ZeroFreeCoTaskMemUnicode',
        'ZeroFreeGlobalAllocAnsi',
        'ZeroFreeGlobalAllocUnicode',
    ]


class MarshalAsAttribute(Attribute, _Attribute):
    """
    MarshalAsAttribute(unmanagedType: UnmanagedType)
    MarshalAsAttribute(unmanagedType: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedType):
        """
        __new__(cls: type, unmanagedType: UnmanagedType)
        __new__(cls: type, unmanagedType: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MarshalAsAttribute) -> UnmanagedType

"""


    ArraySubType = None
    IidParameterIndex = None
    MarshalCookie = None
    MarshalType = None
    MarshalTypeRef = None
    SafeArraySubType = None
    SafeArrayUserDefinedSubType = None
    SizeConst = None
    SizeParamIndex = None


class MarshalDirectiveException(SystemException, ISerializable, _Exception):
    """
    MarshalDirectiveException()
    MarshalDirectiveException(message: str)
    MarshalDirectiveException(message: str, inner: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class MemoryMarshal(object):
    # no doc
    @staticmethod
    def AsBytes(span):
        """
        AsBytes[T](span: Span[T]) -> Span[Byte]
        AsBytes[T](span: ReadOnlySpan[T]) -> ReadOnlySpan[Byte]
        """
        pass

    @staticmethod
    def AsMemory(memory):
        """ AsMemory[T](memory: ReadOnlyMemory[T]) -> Memory[T] """
        pass

    @staticmethod
    def Cast(span):
        """
        Cast[(TFrom, TTo)](span: Span[TFrom]) -> Span[TTo]
        Cast[(TFrom, TTo)](span: ReadOnlySpan[TFrom]) -> ReadOnlySpan[TTo]
        """
        pass

    @staticmethod
    def CreateFromPinnedArray(array, start, length):
        """ CreateFromPinnedArray[T](array: Array[T], start: int, length: int) -> Memory[T] """
        pass

    @staticmethod
    def GetReference(span):
        """
        GetReference[T](span: Span[T]) -> T
        GetReference[T](span: ReadOnlySpan[T]) -> T
        """
        pass

    @staticmethod
    def Read(source):
        """ Read[T](source: ReadOnlySpan[Byte]) -> T """
        pass

    @staticmethod
    def ToEnumerable(memory):
        """ ToEnumerable[T](memory: ReadOnlyMemory[T]) -> IEnumerable[T] """
        pass

    @staticmethod
    def TryGetArray(memory, segment):
        """ TryGetArray[T](memory: ReadOnlyMemory[T]) -> (bool, ArraySegment[T]) """
        pass

    @staticmethod
    def TryGetMemoryManager(memory, manager, start=None, length=None):
# Error generating skeleton for function TryGetMemoryManager: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def TryGetString(memory, text, start, length):
        """ TryGetString(memory: ReadOnlyMemory[Char]) -> (bool, str, int, int) """
        pass

    @staticmethod
    def TryRead(source, value):
        """ TryRead[T](source: ReadOnlySpan[Byte]) -> (bool, T) """
        pass

    @staticmethod
    def TryWrite(destination, value):
        """ TryWrite[T](destination: Span[Byte], value: T) -> (bool, T) """
        pass

    @staticmethod
    def Write(destination, value):
        """ Write[T](destination: Span[Byte], value: T) -> T """
        pass

    __all__ = [
        'AsBytes',
        'AsMemory',
        'Cast',
        'CreateFromPinnedArray',
        'GetReference',
        'Read',
        'ToEnumerable',
        'TryGetArray',
        'TryGetMemoryManager',
        'TryGetString',
        'TryRead',
        'TryWrite',
        'Write',
    ]


class ObjectCreationDelegate(MulticastDelegate, ICloneable, ISerializable):
    """ ObjectCreationDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, aggregator, callback, object):
        """ BeginInvoke(self: ObjectCreationDelegate, aggregator: IntPtr, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ObjectCreationDelegate, result: IAsyncResult) -> IntPtr """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, aggregator):
        """ Invoke(self: ObjectCreationDelegate, aggregator: IntPtr) -> IntPtr """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """ RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class OptionalAttribute(Attribute, _Attribute):
    """ OptionalAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class OSPlatform(object, IEquatable[OSPlatform]):
    # no doc
    @staticmethod
    def Create(osPlatform):
        """ Create(osPlatform: str) -> OSPlatform """
        pass

    def Equals(self, *__args):
        """
        Equals(self: OSPlatform, other: OSPlatform) -> bool
        Equals(self: OSPlatform, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: OSPlatform) -> int """
        pass

    def ToString(self):
        """ ToString(self: OSPlatform) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Linux = None
    OSX = None
    Windows = None


class OutAttribute(Attribute, _Attribute):
    """ OutAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PARAMDESC(object):
    # no doc
    lpVarValue = None
    wParamFlags = None


class PARAMFLAG(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) PARAMFLAG, values: PARAMFLAG_FHASCUSTDATA (64), PARAMFLAG_FHASDEFAULT (32), PARAMFLAG_FIN (1), PARAMFLAG_FLCID (4), PARAMFLAG_FOPT (16), PARAMFLAG_FOUT (2), PARAMFLAG_FRETVAL (8), PARAMFLAG_NONE (0) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    PARAMFLAG_FHASCUSTDATA = None
    PARAMFLAG_FHASDEFAULT = None
    PARAMFLAG_FIN = None
    PARAMFLAG_FLCID = None
    PARAMFLAG_FOPT = None
    PARAMFLAG_FOUT = None
    PARAMFLAG_FRETVAL = None
    PARAMFLAG_NONE = None
    value__ = None


class PreserveSigAttribute(Attribute, _Attribute):
    """ PreserveSigAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class PrimaryInteropAssemblyAttribute(Attribute, _Attribute):
    """ PrimaryInteropAssemblyAttribute(major: int, minor: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor):
        """ __new__(cls: type, major: int, minor: int) """
        pass

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorVersion(self: PrimaryInteropAssemblyAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorVersion(self: PrimaryInteropAssemblyAttribute) -> int

"""



class ProgIdAttribute(Attribute, _Attribute):
    """ ProgIdAttribute(progId: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, progId):
        """ __new__(cls: type, progId: str) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ProgIdAttribute) -> str

"""



class RegistrationClassContext(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RegistrationClassContext, values: DisableActivateAsActivator (32768), EnableActivateAsActivator (65536), EnableCodeDownload (8192), FromDefaultContext (131072), InProcessHandler (2), InProcessHandler16 (32), InProcessServer (1), InProcessServer16 (8), LocalServer (4), NoCodeDownload (1024), NoCustomMarshal (4096), NoFailureLog (16384), RemoteServer (16), Reserved1 (64), Reserved2 (128), Reserved3 (256), Reserved4 (512), Reserved5 (2048) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DisableActivateAsActivator = None
    EnableActivateAsActivator = None
    EnableCodeDownload = None
    FromDefaultContext = None
    InProcessHandler = None
    InProcessHandler16 = None
    InProcessServer = None
    InProcessServer16 = None
    LocalServer = None
    NoCodeDownload = None
    NoCustomMarshal = None
    NoFailureLog = None
    RemoteServer = None
    Reserved1 = None
    Reserved2 = None
    Reserved3 = None
    Reserved4 = None
    Reserved5 = None
    value__ = None


class RegistrationConnectionType(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) RegistrationConnectionType, values: MultipleUse (1), MultiSeparate (2), SingleUse (0), Surrogate (8), Suspended (4) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    MultipleUse = None
    MultiSeparate = None
    SingleUse = None
    Surrogate = None
    Suspended = None
    value__ = None


class RegistrationServices(object, IRegistrationServices):
    """ RegistrationServices() """
    def GetManagedCategoryGuid(self):
        """ GetManagedCategoryGuid(self: RegistrationServices) -> Guid """
        pass

    def GetProgIdForType(self, type):
        """ GetProgIdForType(self: RegistrationServices, type: Type) -> str """
        pass

    def GetRegistrableTypesInAssembly(self, assembly):
        """ GetRegistrableTypesInAssembly(self: RegistrationServices, assembly: Assembly) -> Array[Type] """
        pass

    def RegisterAssembly(self, assembly, flags):
        """ RegisterAssembly(self: RegistrationServices, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool """
        pass

    def RegisterTypeForComClients(self, type, *__args):
        """
        RegisterTypeForComClients(self: RegistrationServices, type: Type, g: Guid) -> Guid
        RegisterTypeForComClients(self: RegistrationServices, type: Type, classContext: RegistrationClassContext, flags: RegistrationConnectionType) -> int
        """
        pass

    def TypeRepresentsComType(self, type):
        """ TypeRepresentsComType(self: RegistrationServices, type: Type) -> bool """
        pass

    def TypeRequiresRegistration(self, type):
        """ TypeRequiresRegistration(self: RegistrationServices, type: Type) -> bool """
        pass

    def UnregisterAssembly(self, assembly):
        """ UnregisterAssembly(self: RegistrationServices, assembly: Assembly) -> bool """
        pass

    def UnregisterTypeForComClients(self, cookie):
        """ UnregisterTypeForComClients(self: RegistrationServices, cookie: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class RuntimeEnvironment(object):
    """ RuntimeEnvironment() """
    @staticmethod
    def FromGlobalAccessCache(a):
        """ FromGlobalAccessCache(a: Assembly) -> bool """
        pass

    @staticmethod
    def GetRuntimeDirectory():
        """ GetRuntimeDirectory() -> str """
        pass

    @staticmethod
    def GetRuntimeInterfaceAsIntPtr(clsid, riid):
        """ GetRuntimeInterfaceAsIntPtr(clsid: Guid, riid: Guid) -> IntPtr """
        pass

    @staticmethod
    def GetRuntimeInterfaceAsObject(clsid, riid):
        """ GetRuntimeInterfaceAsObject(clsid: Guid, riid: Guid) -> object """
        pass

    @staticmethod
    def GetSystemVersion():
        """ GetSystemVersion() -> str """
        pass

    SystemConfigurationFile = 'C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\config\\machine.config'


class RuntimeInformation(object):
    # no doc
    @staticmethod
    def IsOSPlatform(osPlatform):
        """ IsOSPlatform(osPlatform: OSPlatform) -> bool """
        pass

    FrameworkDescription = '.NET Framework 4.8.4420.0'
    OSArchitecture = None
    OSDescription = 'Microsoft Windows 10.0.22000 '
    ProcessArchitecture = None
    __all__ = [
        'IsOSPlatform',
    ]


class SafeArrayRankMismatchException(SystemException, ISerializable, _Exception):
    """
    SafeArrayRankMismatchException()
    SafeArrayRankMismatchException(message: str)
    SafeArrayRankMismatchException(message: str, inner: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class SafeArrayTypeMismatchException(SystemException, ISerializable, _Exception):
    """
    SafeArrayTypeMismatchException()
    SafeArrayTypeMismatchException(message: str)
    SafeArrayTypeMismatchException(message: str, inner: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class SafeHandle(CriticalFinalizerObject, IDisposable):
    # no doc
    def Close(self):
        """ Close(self: SafeHandle) """
        pass

    def DangerousAddRef(self, success):
        """ DangerousAddRef(self: SafeHandle, success: bool) -> bool """
        pass

    def DangerousGetHandle(self):
        """ DangerousGetHandle(self: SafeHandle) -> IntPtr """
        pass

    def DangerousRelease(self):
        """ DangerousRelease(self: SafeHandle) """
        pass

    def Dispose(self):
        """ Dispose(self: SafeHandle) """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeHandle) -> bool """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """ SetHandle(self: SafeHandle, handle: IntPtr) """
        pass

    def SetHandleAsInvalid(self):
        """ SetHandleAsInvalid(self: SafeHandle) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, invalidHandleValue: IntPtr, ownsHandle: bool) """
        pass

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: SafeHandle) -> bool

"""

    IsInvalid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInvalid(self: SafeHandle) -> bool

"""


    handle = None


class SafeBuffer(SafeHandleZeroOrMinusOneIsInvalid, IDisposable):
    # no doc
    def AcquirePointer(self, pointer):
        """ AcquirePointer(self: SafeBuffer, pointer: Byte*) -> Byte* """
        pass

    def Dispose(self):
        """ Dispose(self: SafeHandle, disposing: bool) """
        pass

    def Initialize(self, *__args):
        """ Initialize(self: SafeBuffer, numBytes: UInt64)Initialize(self: SafeBuffer, numElements: UInt32, sizeOfEachElement: UInt32)Initialize[T](self: SafeBuffer, numElements: UInt32) """
        pass

    def Read(self, byteOffset):
        """ Read[T](self: SafeBuffer, byteOffset: UInt64) -> T """
        pass

    def ReadArray(self, byteOffset, array, index, count):
        """ ReadArray[T](self: SafeBuffer, byteOffset: UInt64, array: Array[T], index: int, count: int) """
        pass

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeHandle) -> bool """
        pass

    def ReleasePointer(self):
        """ ReleasePointer(self: SafeBuffer) """
        pass

    def SetHandle(self, *args): #cannot find CLR method
        """ SetHandle(self: SafeHandle, handle: IntPtr) """
        pass

    def Write(self, byteOffset, value):
        """ Write[T](self: SafeBuffer, byteOffset: UInt64, value: T) """
        pass

    def WriteArray(self, byteOffset, array, index, count):
        """ WriteArray[T](self: SafeBuffer, byteOffset: UInt64, array: Array[T], index: int, count: int) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, ownsHandle: bool) """
        pass

    ByteLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ByteLength(self: SafeBuffer) -> UInt64

"""


    handle = None


class SEHException(ExternalException, ISerializable, _Exception):
    """
    SEHException()
    SEHException(message: str)
    SEHException(message: str, inner: Exception)
    """
    def CanResume(self):
        """ CanResume(self: SEHException) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, inner=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class SequenceMarshal(object):
    # no doc
    @staticmethod
    def TryGetArray(sequence, segment):
        """ TryGetArray[T](sequence: ReadOnlySequence[T]) -> (bool, ArraySegment[T]) """
        pass

    @staticmethod
    def TryGetReadOnlyMemory(sequence, memory):
        """ TryGetReadOnlyMemory[T](sequence: ReadOnlySequence[T]) -> (bool, ReadOnlyMemory[T]) """
        pass

    @staticmethod
    def TryGetReadOnlySequenceSegment(sequence, startSegment, startIndex, endSegment, endIndex):
        """ TryGetReadOnlySequenceSegment[T](sequence: ReadOnlySequence[T]) -> (bool, ReadOnlySequenceSegment[T], int, ReadOnlySequenceSegment[T], int) """
        pass

    __all__ = [
        'TryGetArray',
        'TryGetReadOnlyMemory',
        'TryGetReadOnlySequenceSegment',
    ]


class SetWin32ContextInIDispatchAttribute(Attribute, _Attribute):
    """ SetWin32ContextInIDispatchAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class StandardOleMarshalObject(MarshalByRefObject, IMarshal):
    # no doc
    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class STATSTG(object):
    # no doc
    atime = None
    cbSize = None
    clsid = None
    ctime = None
    grfLocksSupported = None
    grfMode = None
    grfStateBits = None
    mtime = None
    pwcsName = None
    reserved = None
    type = None


class StructLayoutAttribute(Attribute, _Attribute):
    """
    StructLayoutAttribute(layoutKind: LayoutKind)
    StructLayoutAttribute(layoutKind: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, layoutKind):
        """
        __new__(cls: type, layoutKind: LayoutKind)
        __new__(cls: type, layoutKind: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: StructLayoutAttribute) -> LayoutKind

"""


    CharSet = None
    Pack = None
    Size = None


class SYSKIND(Enum, IComparable, IFormattable, IConvertible):
    """ enum SYSKIND, values: SYS_MAC (2), SYS_WIN16 (0), SYS_WIN32 (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SYS_MAC = None
    SYS_WIN16 = None
    SYS_WIN32 = None
    value__ = None


class TYPEATTR(object):
    # no doc
    cbAlignment = None
    cbSizeInstance = None
    cbSizeVft = None
    cFuncs = None
    cImplTypes = None
    cVars = None
    dwReserved = None
    guid = None
    idldescType = None
    lcid = None
    lpstrSchema = None
    MEMBER_ID_NIL = -1
    memidConstructor = None
    memidDestructor = None
    tdescAlias = None
    typekind = None
    wMajorVerNum = None
    wMinorVerNum = None
    wTypeFlags = None


class TYPEDESC(object):
    # no doc
    lpValue = None
    vt = None


class TYPEFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TYPEFLAGS, values: TYPEFLAG_FAGGREGATABLE (1024), TYPEFLAG_FAPPOBJECT (1), TYPEFLAG_FCANCREATE (2), TYPEFLAG_FCONTROL (32), TYPEFLAG_FDISPATCHABLE (4096), TYPEFLAG_FDUAL (64), TYPEFLAG_FHIDDEN (16), TYPEFLAG_FLICENSED (4), TYPEFLAG_FNONEXTENSIBLE (128), TYPEFLAG_FOLEAUTOMATION (256), TYPEFLAG_FPREDECLID (8), TYPEFLAG_FPROXY (16384), TYPEFLAG_FREPLACEABLE (2048), TYPEFLAG_FRESTRICTED (512), TYPEFLAG_FREVERSEBIND (8192) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    TYPEFLAG_FAGGREGATABLE = None
    TYPEFLAG_FAPPOBJECT = None
    TYPEFLAG_FCANCREATE = None
    TYPEFLAG_FCONTROL = None
    TYPEFLAG_FDISPATCHABLE = None
    TYPEFLAG_FDUAL = None
    TYPEFLAG_FHIDDEN = None
    TYPEFLAG_FLICENSED = None
    TYPEFLAG_FNONEXTENSIBLE = None
    TYPEFLAG_FOLEAUTOMATION = None
    TYPEFLAG_FPREDECLID = None
    TYPEFLAG_FPROXY = None
    TYPEFLAG_FREPLACEABLE = None
    TYPEFLAG_FRESTRICTED = None
    TYPEFLAG_FREVERSEBIND = None
    value__ = None


class TypeIdentifierAttribute(Attribute, _Attribute):
    """
    TypeIdentifierAttribute()
    TypeIdentifierAttribute(scope: str, identifier: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, scope=None, identifier=None):
        """
        __new__(cls: type)
        __new__(cls: type, scope: str, identifier: str)
        """
        pass

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: TypeIdentifierAttribute) -> str

"""

    Scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scope(self: TypeIdentifierAttribute) -> str

"""



class TYPEKIND(Enum, IComparable, IFormattable, IConvertible):
    """ enum TYPEKIND, values: TKIND_ALIAS (6), TKIND_COCLASS (5), TKIND_DISPATCH (4), TKIND_ENUM (0), TKIND_INTERFACE (3), TKIND_MAX (8), TKIND_MODULE (2), TKIND_RECORD (1), TKIND_UNION (7) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    TKIND_ALIAS = None
    TKIND_COCLASS = None
    TKIND_DISPATCH = None
    TKIND_ENUM = None
    TKIND_INTERFACE = None
    TKIND_MAX = None
    TKIND_MODULE = None
    TKIND_RECORD = None
    TKIND_UNION = None
    value__ = None


class TYPELIBATTR(object):
    # no doc
    guid = None
    lcid = None
    syskind = None
    wLibFlags = None
    wMajorVerNum = None
    wMinorVerNum = None


class TypeLibConverter(object, ITypeLibConverter):
    """ TypeLibConverter() """
    def ConvertAssemblyToTypeLib(self, assembly, strTypeLibName, flags, notifySink):
        """ ConvertAssemblyToTypeLib(self: TypeLibConverter, assembly: Assembly, strTypeLibName: str, flags: TypeLibExporterFlags, notifySink: ITypeLibExporterNotifySink) -> object """
        pass

    def ConvertTypeLibToAssembly(self, typeLib, asmFileName, flags, notifySink, publicKey, keyPair, *__args):
        """
        ConvertTypeLibToAssembly(self: TypeLibConverter, typeLib: object, asmFileName: str, flags: int, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, unsafeInterfaces: bool) -> AssemblyBuilder
        ConvertTypeLibToAssembly(self: TypeLibConverter, typeLib: object, asmFileName: str, flags: TypeLibImporterFlags, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, asmNamespace: str, asmVersion: Version) -> AssemblyBuilder
        """
        pass

    def GetPrimaryInteropAssembly(self, g, major, minor, lcid, asmName, asmCodeBase):
        """ GetPrimaryInteropAssembly(self: TypeLibConverter, g: Guid, major: int, minor: int, lcid: int) -> (bool, str, str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class TypeLibExporterFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TypeLibExporterFlags, values: CallerResolvedReferences (2), ExportAs32Bit (16), ExportAs64Bit (32), None (0), OldNames (4), OnlyReferenceRegistered (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CallerResolvedReferences = None
    ExportAs32Bit = None
    ExportAs64Bit = None
    None = None
    OldNames = None
    OnlyReferenceRegistered = None
    value__ = None


class TypeLibFuncAttribute(Attribute, _Attribute):
    """
    TypeLibFuncAttribute(flags: TypeLibFuncFlags)
    TypeLibFuncAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibFuncFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: TypeLibFuncAttribute) -> TypeLibFuncFlags

"""



class TypeLibFuncFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TypeLibFuncFlags, values: FBindable (4), FDefaultBind (32), FDefaultCollelem (256), FDisplayBind (16), FHidden (64), FImmediateBind (4096), FNonBrowsable (1024), FReplaceable (2048), FRequestEdit (8), FRestricted (1), FSource (2), FUiDefault (512), FUsesGetLastError (128) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FBindable = None
    FDefaultBind = None
    FDefaultCollelem = None
    FDisplayBind = None
    FHidden = None
    FImmediateBind = None
    FNonBrowsable = None
    FReplaceable = None
    FRequestEdit = None
    FRestricted = None
    FSource = None
    FUiDefault = None
    FUsesGetLastError = None
    value__ = None


class TypeLibImportClassAttribute(Attribute, _Attribute):
    """ TypeLibImportClassAttribute(importClass: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, importClass):
        """ __new__(cls: type, importClass: Type) """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: TypeLibImportClassAttribute) -> str

"""



class TypeLibImporterFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TypeLibImporterFlags, values: ImportAsAgnostic (2048), ImportAsArm (16384), ImportAsItanium (1024), ImportAsX64 (512), ImportAsX86 (256), NoDefineVersionResource (8192), None (0), PreventClassMembers (16), PrimaryInteropAssembly (1), ReflectionOnlyLoading (4096), SafeArrayAsSystemArray (4), SerializableValueClasses (32), TransformDispRetVals (8), UnsafeInterfaces (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ImportAsAgnostic = None
    ImportAsArm = None
    ImportAsItanium = None
    ImportAsX64 = None
    ImportAsX86 = None
    NoDefineVersionResource = None
    None = None
    PreventClassMembers = None
    PrimaryInteropAssembly = None
    ReflectionOnlyLoading = None
    SafeArrayAsSystemArray = None
    SerializableValueClasses = None
    TransformDispRetVals = None
    UnsafeInterfaces = None
    value__ = None


class TypeLibTypeAttribute(Attribute, _Attribute):
    """
    TypeLibTypeAttribute(flags: TypeLibTypeFlags)
    TypeLibTypeAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibTypeFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: TypeLibTypeAttribute) -> TypeLibTypeFlags

"""



class TypeLibTypeFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TypeLibTypeFlags, values: FAggregatable (1024), FAppObject (1), FCanCreate (2), FControl (32), FDispatchable (4096), FDual (64), FHidden (16), FLicensed (4), FNonExtensible (128), FOleAutomation (256), FPreDeclId (8), FReplaceable (2048), FRestricted (512), FReverseBind (8192) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FAggregatable = None
    FAppObject = None
    FCanCreate = None
    FControl = None
    FDispatchable = None
    FDual = None
    FHidden = None
    FLicensed = None
    FNonExtensible = None
    FOleAutomation = None
    FPreDeclId = None
    FReplaceable = None
    FRestricted = None
    FReverseBind = None
    value__ = None


class TypeLibVarAttribute(Attribute, _Attribute):
    """
    TypeLibVarAttribute(flags: TypeLibVarFlags)
    TypeLibVarAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibVarFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: TypeLibVarAttribute) -> TypeLibVarFlags

"""



class TypeLibVarFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TypeLibVarFlags, values: FBindable (4), FDefaultBind (32), FDefaultCollelem (256), FDisplayBind (16), FHidden (64), FImmediateBind (4096), FNonBrowsable (1024), FReadOnly (1), FReplaceable (2048), FRequestEdit (8), FRestricted (128), FSource (2), FUiDefault (512) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    FBindable = None
    FDefaultBind = None
    FDefaultCollelem = None
    FDisplayBind = None
    FHidden = None
    FImmediateBind = None
    FNonBrowsable = None
    FReadOnly = None
    FReplaceable = None
    FRequestEdit = None
    FRestricted = None
    FSource = None
    FUiDefault = None
    value__ = None


class TypeLibVersionAttribute(Attribute, _Attribute):
    """ TypeLibVersionAttribute(major: int, minor: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor):
        """ __new__(cls: type, major: int, minor: int) """
        pass

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorVersion(self: TypeLibVersionAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorVersion(self: TypeLibVersionAttribute) -> int

"""



class UCOMIBindCtx:
    # no doc
    def EnumObjectParam(self, ppenum):
        """ EnumObjectParam(self: UCOMIBindCtx) -> UCOMIEnumString """
        pass

    def GetBindOptions(self, pbindopts):
        """ GetBindOptions(self: UCOMIBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS """
        pass

    def GetObjectParam(self, pszKey, ppunk):
        """ GetObjectParam(self: UCOMIBindCtx, pszKey: str) -> object """
        pass

    def GetRunningObjectTable(self, pprot):
        """ GetRunningObjectTable(self: UCOMIBindCtx) -> UCOMIRunningObjectTable """
        pass

    def RegisterObjectBound(self, punk):
        """ RegisterObjectBound(self: UCOMIBindCtx, punk: object) """
        pass

    def RegisterObjectParam(self, pszKey, punk):
        """ RegisterObjectParam(self: UCOMIBindCtx, pszKey: str, punk: object) """
        pass

    def ReleaseBoundObjects(self):
        """ ReleaseBoundObjects(self: UCOMIBindCtx) """
        pass

    def RevokeObjectBound(self, punk):
        """ RevokeObjectBound(self: UCOMIBindCtx, punk: object) """
        pass

    def RevokeObjectParam(self, pszKey):
        """ RevokeObjectParam(self: UCOMIBindCtx, pszKey: str) """
        pass

    def SetBindOptions(self, pbindopts):
        """ SetBindOptions(self: UCOMIBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIConnectionPoint:
    # no doc
    def Advise(self, pUnkSink, pdwCookie):
        """ Advise(self: UCOMIConnectionPoint, pUnkSink: object) -> int """
        pass

    def EnumConnections(self, ppEnum):
        """ EnumConnections(self: UCOMIConnectionPoint) -> UCOMIEnumConnections """
        pass

    def GetConnectionInterface(self, pIID):
        """ GetConnectionInterface(self: UCOMIConnectionPoint) -> Guid """
        pass

    def GetConnectionPointContainer(self, ppCPC):
        """ GetConnectionPointContainer(self: UCOMIConnectionPoint) -> UCOMIConnectionPointContainer """
        pass

    def Unadvise(self, dwCookie):
        """ Unadvise(self: UCOMIConnectionPoint, dwCookie: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIConnectionPointContainer:
    # no doc
    def EnumConnectionPoints(self, ppEnum):
        """ EnumConnectionPoints(self: UCOMIConnectionPointContainer) -> UCOMIEnumConnectionPoints """
        pass

    def FindConnectionPoint(self, riid, ppCP):
        """ FindConnectionPoint(self: UCOMIConnectionPointContainer, riid: Guid) -> (Guid, UCOMIConnectionPoint) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumConnectionPoints:
    # no doc
    def Clone(self, ppenum):
        """ Clone(self: UCOMIEnumConnectionPoints) -> UCOMIEnumConnectionPoints """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """ Next(self: UCOMIEnumConnectionPoints, celt: int) -> (int, Array[UCOMIConnectionPoint], int) """
        pass

    def Reset(self):
        """ Reset(self: UCOMIEnumConnectionPoints) -> int """
        pass

    def Skip(self, celt):
        """ Skip(self: UCOMIEnumConnectionPoints, celt: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumConnections:
    # no doc
    def Clone(self, ppenum):
        """ Clone(self: UCOMIEnumConnections) -> UCOMIEnumConnections """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """ Next(self: UCOMIEnumConnections, celt: int) -> (int, Array[CONNECTDATA], int) """
        pass

    def Reset(self):
        """ Reset(self: UCOMIEnumConnections) """
        pass

    def Skip(self, celt):
        """ Skip(self: UCOMIEnumConnections, celt: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumMoniker:
    # no doc
    def Clone(self, ppenum):
        """ Clone(self: UCOMIEnumMoniker) -> UCOMIEnumMoniker """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """ Next(self: UCOMIEnumMoniker, celt: int) -> (int, Array[UCOMIMoniker], int) """
        pass

    def Reset(self):
        """ Reset(self: UCOMIEnumMoniker) -> int """
        pass

    def Skip(self, celt):
        """ Skip(self: UCOMIEnumMoniker, celt: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumString:
    # no doc
    def Clone(self, ppenum):
        """ Clone(self: UCOMIEnumString) -> UCOMIEnumString """
        pass

    def Next(self, celt, rgelt, pceltFetched):
        """ Next(self: UCOMIEnumString, celt: int) -> (int, Array[str], int) """
        pass

    def Reset(self):
        """ Reset(self: UCOMIEnumString) -> int """
        pass

    def Skip(self, celt):
        """ Skip(self: UCOMIEnumString, celt: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIEnumVARIANT:
    # no doc
    def Clone(self, ppenum):
        """ Clone(self: UCOMIEnumVARIANT, ppenum: int) """
        pass

    def Next(self, celt, rgvar, pceltFetched):
        """ Next(self: UCOMIEnumVARIANT, celt: int, rgvar: int, pceltFetched: int) -> int """
        pass

    def Reset(self):
        """ Reset(self: UCOMIEnumVARIANT) -> int """
        pass

    def Skip(self, celt):
        """ Skip(self: UCOMIEnumVARIANT, celt: int) -> int """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIMoniker:
    # no doc
    def BindToObject(self, pbc, pmkToLeft, riidResult, ppvResult):
        """ BindToObject(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riidResult: Guid) -> (Guid, object) """
        pass

    def BindToStorage(self, pbc, pmkToLeft, riid, ppvObj):
        """ BindToStorage(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riid: Guid) -> (Guid, object) """
        pass

    def CommonPrefixWith(self, pmkOther, ppmkPrefix):
        """ CommonPrefixWith(self: UCOMIMoniker, pmkOther: UCOMIMoniker) -> UCOMIMoniker """
        pass

    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric, ppmkComposite):
        """ ComposeWith(self: UCOMIMoniker, pmkRight: UCOMIMoniker, fOnlyIfNotGeneric: bool) -> UCOMIMoniker """
        pass

    def Enum(self, fForward, ppenumMoniker):
        """ Enum(self: UCOMIMoniker, fForward: bool) -> UCOMIEnumMoniker """
        pass

    def GetClassID(self, pClassID):
        """ GetClassID(self: UCOMIMoniker) -> Guid """
        pass

    def GetDisplayName(self, pbc, pmkToLeft, ppszDisplayName):
        """ GetDisplayName(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker) -> str """
        pass

    def GetSizeMax(self, pcbSize):
        """ GetSizeMax(self: UCOMIMoniker) -> Int64 """
        pass

    def GetTimeOfLastChange(self, pbc, pmkToLeft, pFileTime):
        """ GetTimeOfLastChange(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker) -> FILETIME """
        pass

    def Hash(self, pdwHash):
        """ Hash(self: UCOMIMoniker) -> int """
        pass

    def Inverse(self, ppmk):
        """ Inverse(self: UCOMIMoniker) -> UCOMIMoniker """
        pass

    def IsDirty(self):
        """ IsDirty(self: UCOMIMoniker) -> int """
        pass

    def IsEqual(self, pmkOtherMoniker):
        """ IsEqual(self: UCOMIMoniker, pmkOtherMoniker: UCOMIMoniker) """
        pass

    def IsRunning(self, pbc, pmkToLeft, pmkNewlyRunning):
        """ IsRunning(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pmkNewlyRunning: UCOMIMoniker) """
        pass

    def IsSystemMoniker(self, pdwMksys):
        """ IsSystemMoniker(self: UCOMIMoniker) -> int """
        pass

    def Load(self, pStm):
        """ Load(self: UCOMIMoniker, pStm: UCOMIStream) """
        pass

    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName, pchEaten, ppmkOut):
        """ ParseDisplayName(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pszDisplayName: str) -> (int, UCOMIMoniker) """
        pass

    def Reduce(self, pbc, dwReduceHowFar, ppmkToLeft, ppmkReduced):
        """ Reduce(self: UCOMIMoniker, pbc: UCOMIBindCtx, dwReduceHowFar: int, ppmkToLeft: UCOMIMoniker) -> (UCOMIMoniker, UCOMIMoniker) """
        pass

    def RelativePathTo(self, pmkOther, ppmkRelPath):
        """ RelativePathTo(self: UCOMIMoniker, pmkOther: UCOMIMoniker) -> UCOMIMoniker """
        pass

    def Save(self, pStm, fClearDirty):
        """ Save(self: UCOMIMoniker, pStm: UCOMIStream, fClearDirty: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIPersistFile:
    # no doc
    def GetClassID(self, pClassID):
        """ GetClassID(self: UCOMIPersistFile) -> Guid """
        pass

    def GetCurFile(self, ppszFileName):
        """ GetCurFile(self: UCOMIPersistFile) -> str """
        pass

    def IsDirty(self):
        """ IsDirty(self: UCOMIPersistFile) -> int """
        pass

    def Load(self, pszFileName, dwMode):
        """ Load(self: UCOMIPersistFile, pszFileName: str, dwMode: int) """
        pass

    def Save(self, pszFileName, fRemember):
        """ Save(self: UCOMIPersistFile, pszFileName: str, fRemember: bool) """
        pass

    def SaveCompleted(self, pszFileName):
        """ SaveCompleted(self: UCOMIPersistFile, pszFileName: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIRunningObjectTable:
    # no doc
    def EnumRunning(self, ppenumMoniker):
        """ EnumRunning(self: UCOMIRunningObjectTable) -> UCOMIEnumMoniker """
        pass

    def GetObject(self, pmkObjectName, ppunkObject):
        """ GetObject(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) -> object """
        pass

    def GetTimeOfLastChange(self, pmkObjectName, pfiletime):
        """ GetTimeOfLastChange(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) -> FILETIME """
        pass

    def IsRunning(self, pmkObjectName):
        """ IsRunning(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) """
        pass

    def NoteChangeTime(self, dwRegister, pfiletime):
        """ NoteChangeTime(self: UCOMIRunningObjectTable, dwRegister: int, pfiletime: FILETIME) -> FILETIME """
        pass

    def Register(self, grfFlags, punkObject, pmkObjectName, pdwRegister):
        """ Register(self: UCOMIRunningObjectTable, grfFlags: int, punkObject: object, pmkObjectName: UCOMIMoniker) -> int """
        pass

    def Revoke(self, dwRegister):
        """ Revoke(self: UCOMIRunningObjectTable, dwRegister: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMIStream:
    # no doc
    def Clone(self, ppstm):
        """ Clone(self: UCOMIStream) -> UCOMIStream """
        pass

    def Commit(self, grfCommitFlags):
        """ Commit(self: UCOMIStream, grfCommitFlags: int) """
        pass

    def CopyTo(self, pstm, cb, pcbRead, pcbWritten):
        """ CopyTo(self: UCOMIStream, pstm: UCOMIStream, cb: Int64, pcbRead: IntPtr, pcbWritten: IntPtr) """
        pass

    def LockRegion(self, libOffset, cb, dwLockType):
        """ LockRegion(self: UCOMIStream, libOffset: Int64, cb: Int64, dwLockType: int) """
        pass

    def Read(self, pv, cb, pcbRead):
        """ Read(self: UCOMIStream, cb: int, pcbRead: IntPtr) -> Array[Byte] """
        pass

    def Revert(self):
        """ Revert(self: UCOMIStream) """
        pass

    def Seek(self, dlibMove, dwOrigin, plibNewPosition):
        """ Seek(self: UCOMIStream, dlibMove: Int64, dwOrigin: int, plibNewPosition: IntPtr) """
        pass

    def SetSize(self, libNewSize):
        """ SetSize(self: UCOMIStream, libNewSize: Int64) """
        pass

    def Stat(self, pstatstg, grfStatFlag):
        """ Stat(self: UCOMIStream, grfStatFlag: int) -> STATSTG """
        pass

    def UnlockRegion(self, libOffset, cb, dwLockType):
        """ UnlockRegion(self: UCOMIStream, libOffset: Int64, cb: Int64, dwLockType: int) """
        pass

    def Write(self, pv, cb, pcbWritten):
        """ Write(self: UCOMIStream, pv: Array[Byte], cb: int, pcbWritten: IntPtr) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMITypeComp:
    # no doc
    def Bind(self, szName, lHashVal, wFlags, ppTInfo, pDescKind, pBindPtr):
        """ Bind(self: UCOMITypeComp, szName: str, lHashVal: int, wFlags: Int16) -> (UCOMITypeInfo, DESCKIND, BINDPTR) """
        pass

    def BindType(self, szName, lHashVal, ppTInfo, ppTComp):
        """ BindType(self: UCOMITypeComp, szName: str, lHashVal: int) -> (UCOMITypeInfo, UCOMITypeComp) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMITypeInfo:
    # no doc
    def AddressOfMember(self, memid, invKind, ppv):
        """ AddressOfMember(self: UCOMITypeInfo, memid: int, invKind: INVOKEKIND) -> IntPtr """
        pass

    def CreateInstance(self, pUnkOuter, riid, ppvObj):
        """ CreateInstance(self: UCOMITypeInfo, pUnkOuter: object, riid: Guid) -> (Guid, object) """
        pass

    def GetContainingTypeLib(self, ppTLB, pIndex):
        """ GetContainingTypeLib(self: UCOMITypeInfo) -> (UCOMITypeLib, int) """
        pass

    def GetDllEntry(self, memid, invKind, pBstrDllName, pBstrName, pwOrdinal):
        """ GetDllEntry(self: UCOMITypeInfo, memid: int, invKind: INVOKEKIND) -> (str, str, Int16) """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """ GetDocumentation(self: UCOMITypeInfo, index: int) -> (str, str, int, str) """
        pass

    def GetFuncDesc(self, index, ppFuncDesc):
        """ GetFuncDesc(self: UCOMITypeInfo, index: int) -> IntPtr """
        pass

    def GetIDsOfNames(self, rgszNames, cNames, pMemId):
        """ GetIDsOfNames(self: UCOMITypeInfo, rgszNames: Array[str], cNames: int) -> Array[int] """
        pass

    def GetImplTypeFlags(self, index, pImplTypeFlags):
        """ GetImplTypeFlags(self: UCOMITypeInfo, index: int) -> int """
        pass

    def GetMops(self, memid, pBstrMops):
        """ GetMops(self: UCOMITypeInfo, memid: int) -> str """
        pass

    def GetNames(self, memid, rgBstrNames, cMaxNames, pcNames):
        """ GetNames(self: UCOMITypeInfo, memid: int, cMaxNames: int) -> (Array[str], int) """
        pass

    def GetRefTypeInfo(self, hRef, ppTI):
        """ GetRefTypeInfo(self: UCOMITypeInfo, hRef: int) -> UCOMITypeInfo """
        pass

    def GetRefTypeOfImplType(self, index, href):
        """ GetRefTypeOfImplType(self: UCOMITypeInfo, index: int) -> int """
        pass

    def GetTypeAttr(self, ppTypeAttr):
        """ GetTypeAttr(self: UCOMITypeInfo) -> IntPtr """
        pass

    def GetTypeComp(self, ppTComp):
        """ GetTypeComp(self: UCOMITypeInfo) -> UCOMITypeComp """
        pass

    def GetVarDesc(self, index, ppVarDesc):
        """ GetVarDesc(self: UCOMITypeInfo, index: int) -> IntPtr """
        pass

    def Invoke(self, pvInstance, memid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: UCOMITypeInfo, pvInstance: object, memid: int, wFlags: Int16, pDispParams: DISPPARAMS) -> (DISPPARAMS, object, EXCEPINFO, int) """
        pass

    def ReleaseFuncDesc(self, pFuncDesc):
        """ ReleaseFuncDesc(self: UCOMITypeInfo, pFuncDesc: IntPtr) """
        pass

    def ReleaseTypeAttr(self, pTypeAttr):
        """ ReleaseTypeAttr(self: UCOMITypeInfo, pTypeAttr: IntPtr) """
        pass

    def ReleaseVarDesc(self, pVarDesc):
        """ ReleaseVarDesc(self: UCOMITypeInfo, pVarDesc: IntPtr) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UCOMITypeLib:
    # no doc
    def FindName(self, szNameBuf, lHashVal, ppTInfo, rgMemId, pcFound):
        """ FindName(self: UCOMITypeLib, szNameBuf: str, lHashVal: int, pcFound: Int16) -> (Array[UCOMITypeInfo], Array[int], Int16) """
        pass

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile):
        """ GetDocumentation(self: UCOMITypeLib, index: int) -> (str, str, int, str) """
        pass

    def GetLibAttr(self, ppTLibAttr):
        """ GetLibAttr(self: UCOMITypeLib) -> IntPtr """
        pass

    def GetTypeComp(self, ppTComp):
        """ GetTypeComp(self: UCOMITypeLib) -> UCOMITypeComp """
        pass

    def GetTypeInfo(self, index, ppTI):
        """ GetTypeInfo(self: UCOMITypeLib, index: int) -> UCOMITypeInfo """
        pass

    def GetTypeInfoCount(self):
        """ GetTypeInfoCount(self: UCOMITypeLib) -> int """
        pass

    def GetTypeInfoOfGuid(self, guid, ppTInfo):
        """ GetTypeInfoOfGuid(self: UCOMITypeLib, guid: Guid) -> (Guid, UCOMITypeInfo) """
        pass

    def GetTypeInfoType(self, index, pTKind):
        """ GetTypeInfoType(self: UCOMITypeLib, index: int) -> TYPEKIND """
        pass

    def IsName(self, szNameBuf, lHashVal):
        """ IsName(self: UCOMITypeLib, szNameBuf: str, lHashVal: int) -> bool """
        pass

    def ReleaseTLibAttr(self, pTLibAttr):
        """ ReleaseTLibAttr(self: UCOMITypeLib, pTLibAttr: IntPtr) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class UnknownWrapper(object):
    """ UnknownWrapper(obj: object) """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedObject(self: UnknownWrapper) -> object

"""



class UnmanagedFunctionPointerAttribute(Attribute, _Attribute):
    """ UnmanagedFunctionPointerAttribute(callingConvention: CallingConvention) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, callingConvention):
        """ __new__(cls: type, callingConvention: CallingConvention) """
        pass

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CallingConvention(self: UnmanagedFunctionPointerAttribute) -> CallingConvention

"""


    BestFitMapping = None
    CharSet = None
    SetLastError = None
    ThrowOnUnmappableChar = None


class UnmanagedType(Enum, IComparable, IFormattable, IConvertible):
    """ enum UnmanagedType, values: AnsiBStr (35), AsAny (40), Bool (2), BStr (19), ByValArray (30), ByValTStr (23), Currency (15), CustomMarshaler (44), Error (45), FunctionPtr (38), HString (47), I1 (3), I2 (5), I4 (7), I8 (9), IDispatch (26), IInspectable (46), Interface (28), IUnknown (25), LPArray (42), LPStr (20), LPStruct (43), LPTStr (22), LPUTF8Str (48), LPWStr (21), R4 (11), R8 (12), SafeArray (29), Struct (27), SysInt (31), SysUInt (32), TBStr (36), U1 (4), U2 (6), U4 (8), U8 (10), VariantBool (37), VBByRefStr (34) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AnsiBStr = None
    AsAny = None
    Bool = None
    BStr = None
    ByValArray = None
    ByValTStr = None
    Currency = None
    CustomMarshaler = None
    Error = None
    FunctionPtr = None
    HString = None
    I1 = None
    I2 = None
    I4 = None
    I8 = None
    IDispatch = None
    IInspectable = None
    Interface = None
    IUnknown = None
    LPArray = None
    LPStr = None
    LPStruct = None
    LPTStr = None
    LPUTF8Str = None
    LPWStr = None
    R4 = None
    R8 = None
    SafeArray = None
    Struct = None
    SysInt = None
    SysUInt = None
    TBStr = None
    U1 = None
    U2 = None
    U4 = None
    U8 = None
    value__ = None
    VariantBool = None
    VBByRefStr = None


class VARDESC(object):
    # no doc
    DESCUNION = None
    elemdescVar = None
    lpstrSchema = None
    memid = None
    varkind = None
    wVarFlags = None


class VarEnum(Enum, IComparable, IFormattable, IConvertible):
    """ enum VarEnum, values: VT_ARRAY (8192), VT_BLOB (65), VT_BLOB_OBJECT (70), VT_BOOL (11), VT_BSTR (8), VT_BYREF (16384), VT_CARRAY (28), VT_CF (71), VT_CLSID (72), VT_CY (6), VT_DATE (7), VT_DECIMAL (14), VT_DISPATCH (9), VT_EMPTY (0), VT_ERROR (10), VT_FILETIME (64), VT_HRESULT (25), VT_I1 (16), VT_I2 (2), VT_I4 (3), VT_I8 (20), VT_INT (22), VT_LPSTR (30), VT_LPWSTR (31), VT_NULL (1), VT_PTR (26), VT_R4 (4), VT_R8 (5), VT_RECORD (36), VT_SAFEARRAY (27), VT_STORAGE (67), VT_STORED_OBJECT (69), VT_STREAM (66), VT_STREAMED_OBJECT (68), VT_UI1 (17), VT_UI2 (18), VT_UI4 (19), VT_UI8 (21), VT_UINT (23), VT_UNKNOWN (13), VT_USERDEFINED (29), VT_VARIANT (12), VT_VECTOR (4096), VT_VOID (24) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    value__ = None
    VT_ARRAY = None
    VT_BLOB = None
    VT_BLOB_OBJECT = None
    VT_BOOL = None
    VT_BSTR = None
    VT_BYREF = None
    VT_CARRAY = None
    VT_CF = None
    VT_CLSID = None
    VT_CY = None
    VT_DATE = None
    VT_DECIMAL = None
    VT_DISPATCH = None
    VT_EMPTY = None
    VT_ERROR = None
    VT_FILETIME = None
    VT_HRESULT = None
    VT_I1 = None
    VT_I2 = None
    VT_I4 = None
    VT_I8 = None
    VT_INT = None
    VT_LPSTR = None
    VT_LPWSTR = None
    VT_NULL = None
    VT_PTR = None
    VT_R4 = None
    VT_R8 = None
    VT_RECORD = None
    VT_SAFEARRAY = None
    VT_STORAGE = None
    VT_STORED_OBJECT = None
    VT_STREAM = None
    VT_STREAMED_OBJECT = None
    VT_UI1 = None
    VT_UI2 = None
    VT_UI4 = None
    VT_UI8 = None
    VT_UINT = None
    VT_UNKNOWN = None
    VT_USERDEFINED = None
    VT_VARIANT = None
    VT_VECTOR = None
    VT_VOID = None


class VARFLAGS(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) VARFLAGS, values: VARFLAG_FBINDABLE (4), VARFLAG_FDEFAULTBIND (32), VARFLAG_FDEFAULTCOLLELEM (256), VARFLAG_FDISPLAYBIND (16), VARFLAG_FHIDDEN (64), VARFLAG_FIMMEDIATEBIND (4096), VARFLAG_FNONBROWSABLE (1024), VARFLAG_FREADONLY (1), VARFLAG_FREPLACEABLE (2048), VARFLAG_FREQUESTEDIT (8), VARFLAG_FRESTRICTED (128), VARFLAG_FSOURCE (2), VARFLAG_FUIDEFAULT (512) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    value__ = None
    VARFLAG_FBINDABLE = None
    VARFLAG_FDEFAULTBIND = None
    VARFLAG_FDEFAULTCOLLELEM = None
    VARFLAG_FDISPLAYBIND = None
    VARFLAG_FHIDDEN = None
    VARFLAG_FIMMEDIATEBIND = None
    VARFLAG_FNONBROWSABLE = None
    VARFLAG_FREADONLY = None
    VARFLAG_FREPLACEABLE = None
    VARFLAG_FREQUESTEDIT = None
    VARFLAG_FRESTRICTED = None
    VARFLAG_FSOURCE = None
    VARFLAG_FUIDEFAULT = None


class VariantWrapper(object):
    """ VariantWrapper(obj: object) """
    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: object) """
        pass

    WrappedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedObject(self: VariantWrapper) -> object

"""



class _Activator:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _Activator, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _Activator, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _Activator) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _Activator, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Assembly:
    # no doc
    def CreateInstance(self, typeName, ignoreCase=None, bindingAttr=None, binder=None, args=None, culture=None, activationAttributes=None):
        """
        CreateInstance(self: _Assembly, typeName: str) -> object
        CreateInstance(self: _Assembly, typeName: str, ignoreCase: bool) -> object
        CreateInstance(self: _Assembly, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        """
        pass

    def Equals(self, other):
        """ Equals(self: _Assembly, other: object) -> bool """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _Assembly, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _Assembly, inherit: bool) -> Array[object]
        """
        pass

    def GetExportedTypes(self):
        """ GetExportedTypes(self: _Assembly) -> Array[Type] """
        pass

    def GetFile(self, name):
        """ GetFile(self: _Assembly, name: str) -> FileStream """
        pass

    def GetFiles(self, getResourceModules=None):
        """
        GetFiles(self: _Assembly) -> Array[FileStream]
        GetFiles(self: _Assembly, getResourceModules: bool) -> Array[FileStream]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _Assembly) -> int """
        pass

    def GetLoadedModules(self, getResourceModules=None):
        """
        GetLoadedModules(self: _Assembly) -> Array[Module]
        GetLoadedModules(self: _Assembly, getResourceModules: bool) -> Array[Module]
        """
        pass

    def GetManifestResourceInfo(self, resourceName):
        """ GetManifestResourceInfo(self: _Assembly, resourceName: str) -> ManifestResourceInfo """
        pass

    def GetManifestResourceNames(self):
        """ GetManifestResourceNames(self: _Assembly) -> Array[str] """
        pass

    def GetManifestResourceStream(self, *__args):
        """
        GetManifestResourceStream(self: _Assembly, type: Type, name: str) -> Stream
        GetManifestResourceStream(self: _Assembly, name: str) -> Stream
        """
        pass

    def GetModule(self, name):
        """ GetModule(self: _Assembly, name: str) -> Module """
        pass

    def GetModules(self, getResourceModules=None):
        """
        GetModules(self: _Assembly) -> Array[Module]
        GetModules(self: _Assembly, getResourceModules: bool) -> Array[Module]
        """
        pass

    def GetName(self, copiedName=None):
        """
        GetName(self: _Assembly) -> AssemblyName
        GetName(self: _Assembly, copiedName: bool) -> AssemblyName
        """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: _Assembly, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetReferencedAssemblies(self):
        """ GetReferencedAssemblies(self: _Assembly) -> Array[AssemblyName] """
        pass

    def GetSatelliteAssembly(self, culture, version=None):
        """
        GetSatelliteAssembly(self: _Assembly, culture: CultureInfo) -> Assembly
        GetSatelliteAssembly(self: _Assembly, culture: CultureInfo, version: Version) -> Assembly
        """
        pass

    def GetType(self, name=None, throwOnError=None, ignoreCase=None):
        """
        GetType(self: _Assembly) -> Type
        GetType(self: _Assembly, name: str) -> Type
        GetType(self: _Assembly, name: str, throwOnError: bool) -> Type
        GetType(self: _Assembly, name: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        pass

    def GetTypes(self):
        """ GetTypes(self: _Assembly) -> Array[Type] """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _Assembly, attributeType: Type, inherit: bool) -> bool """
        pass

    def LoadModule(self, moduleName, rawModule, rawSymbolStore=None):
        """
        LoadModule(self: _Assembly, moduleName: str, rawModule: Array[Byte]) -> Module
        LoadModule(self: _Assembly, moduleName: str, rawModule: Array[Byte], rawSymbolStore: Array[Byte]) -> Module
        """
        pass

    def ToString(self):
        """ ToString(self: _Assembly) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeBase(self: _Assembly) -> str

"""

    EntryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryPoint(self: _Assembly) -> MethodInfo

"""

    EscapedCodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EscapedCodeBase(self: _Assembly) -> str

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Evidence(self: _Assembly) -> Evidence

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: _Assembly) -> str

"""

    GlobalAssemblyCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAssemblyCache(self: _Assembly) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: _Assembly) -> str

"""


    ModuleResolve = None


class _AssemblyBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _AssemblyBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _AssemblyBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _AssemblyBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _AssemblyBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _AssemblyName:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _AssemblyName, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _AssemblyName, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _AssemblyName) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _AssemblyName, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ConstructorBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _ConstructorBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _ConstructorBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _ConstructorBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _ConstructorBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ConstructorInfo:
    # no doc
    def Equals(self, other):
        """ Equals(self: _ConstructorInfo, other: object) -> bool """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _ConstructorInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _ConstructorInfo, inherit: bool) -> Array[object]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _ConstructorInfo) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _ConstructorInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetMethodImplementationFlags(self):
        """ GetMethodImplementationFlags(self: _ConstructorInfo) -> MethodImplAttributes """
        pass

    def GetParameters(self):
        """ GetParameters(self: _ConstructorInfo) -> Array[ParameterInfo] """
        pass

    def GetType(self):
        """ GetType(self: _ConstructorInfo) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _ConstructorInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _ConstructorInfo) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _ConstructorInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def Invoke_2(self, obj, invokeAttr, binder, parameters, culture):
        """ Invoke_2(self: _ConstructorInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object """
        pass

    def Invoke_3(self, obj, parameters):
        """ Invoke_3(self: _ConstructorInfo, obj: object, parameters: Array[object]) -> object """
        pass

    def Invoke_4(self, invokeAttr, binder, parameters, culture):
        """ Invoke_4(self: _ConstructorInfo, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object """
        pass

    def Invoke_5(self, parameters):
        """ Invoke_5(self: _ConstructorInfo, parameters: Array[object]) -> object """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _ConstructorInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def ToString(self):
        """ ToString(self: _ConstructorInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _ConstructorInfo) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CallingConvention(self: _ConstructorInfo) -> CallingConventions

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _ConstructorInfo) -> Type

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: _ConstructorInfo) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssembly(self: _ConstructorInfo) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConstructor(self: _ConstructorInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamily(self: _ConstructorInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyAndAssembly(self: _ConstructorInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyOrAssembly(self: _ConstructorInfo) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinal(self: _ConstructorInfo) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHideBySig(self: _ConstructorInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: _ConstructorInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: _ConstructorInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _ConstructorInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: _ConstructorInfo) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVirtual(self: _ConstructorInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _ConstructorInfo) -> MemberTypes

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodHandle(self: _ConstructorInfo) -> RuntimeMethodHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _ConstructorInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _ConstructorInfo) -> Type

"""



class _CustomAttributeBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _CustomAttributeBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _CustomAttributeBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _CustomAttributeBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _CustomAttributeBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _EnumBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _EnumBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _EnumBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _EnumBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _EnumBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _EventBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _EventBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _EventBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _EventBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _EventBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _EventInfo:
    # no doc
    def AddEventHandler(self, target, handler):
        """ AddEventHandler(self: _EventInfo, target: object, handler: Delegate) """
        pass

    def Equals(self, other):
        """ Equals(self: _EventInfo, other: object) -> bool """
        pass

    def GetAddMethod(self, nonPublic=None):
        """
        GetAddMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        GetAddMethod(self: _EventInfo) -> MethodInfo
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _EventInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _EventInfo, inherit: bool) -> Array[object]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _EventInfo) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _EventInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetRaiseMethod(self, nonPublic=None):
        """
        GetRaiseMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        GetRaiseMethod(self: _EventInfo) -> MethodInfo
        """
        pass

    def GetRemoveMethod(self, nonPublic=None):
        """
        GetRemoveMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        GetRemoveMethod(self: _EventInfo) -> MethodInfo
        """
        pass

    def GetType(self):
        """ GetType(self: _EventInfo) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _EventInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _EventInfo) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _EventInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _EventInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def RemoveEventHandler(self, target, handler):
        """ RemoveEventHandler(self: _EventInfo, target: object, handler: Delegate) """
        pass

    def ToString(self):
        """ ToString(self: _EventInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _EventInfo) -> EventAttributes

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _EventInfo) -> Type

"""

    EventHandlerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventHandlerType(self: _EventInfo) -> Type

"""

    IsMulticast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMulticast(self: _EventInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _EventInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _EventInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _EventInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _EventInfo) -> Type

"""



class _Exception:
    # no doc
    def Equals(self, obj):
        """ Equals(self: _Exception, obj: object) -> bool """
        pass

    def GetBaseException(self):
        """ GetBaseException(self: _Exception) -> Exception """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _Exception) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: _Exception, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetType(self):
        """ GetType(self: _Exception) -> Type """
        pass

    def ToString(self):
        """ ToString(self: _Exception) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    HelpLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpLink(self: _Exception) -> str

Set: HelpLink(self: _Exception) = value
"""

    InnerException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerException(self: _Exception) -> Exception

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: _Exception) -> str

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: _Exception) -> str

Set: Source(self: _Exception) = value
"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackTrace(self: _Exception) -> str

"""

    TargetSite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetSite(self: _Exception) -> MethodBase

"""



class _FieldBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _FieldBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _FieldBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _FieldBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _FieldBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _FieldInfo:
    # no doc
    def Equals(self, other):
        """ Equals(self: _FieldInfo, other: object) -> bool """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _FieldInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _FieldInfo, inherit: bool) -> Array[object]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _FieldInfo) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _FieldInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetType(self):
        """ GetType(self: _FieldInfo) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _FieldInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _FieldInfo) -> UInt32 """
        pass

    def GetValue(self, obj):
        """ GetValue(self: _FieldInfo, obj: object) -> object """
        pass

    def GetValueDirect(self, obj):
        """ GetValueDirect(self: _FieldInfo, obj: TypedReference) -> object """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _FieldInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _FieldInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def SetValue(self, obj, value, invokeAttr=None, binder=None, culture=None):
        """ SetValue(self: _FieldInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo)SetValue(self: _FieldInfo, obj: object, value: object) """
        pass

    def SetValueDirect(self, obj, value):
        """ SetValueDirect(self: _FieldInfo, obj: TypedReference, value: object) """
        pass

    def ToString(self):
        """ ToString(self: _FieldInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _FieldInfo) -> FieldAttributes

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _FieldInfo) -> Type

"""

    FieldHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldHandle(self: _FieldInfo) -> RuntimeFieldHandle

"""

    FieldType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldType(self: _FieldInfo) -> Type

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssembly(self: _FieldInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamily(self: _FieldInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyAndAssembly(self: _FieldInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyOrAssembly(self: _FieldInfo) -> bool

"""

    IsInitOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInitOnly(self: _FieldInfo) -> bool

"""

    IsLiteral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiteral(self: _FieldInfo) -> bool

"""

    IsNotSerialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNotSerialized(self: _FieldInfo) -> bool

"""

    IsPinvokeImpl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinvokeImpl(self: _FieldInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: _FieldInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: _FieldInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _FieldInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: _FieldInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _FieldInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _FieldInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _FieldInfo) -> Type

"""



class _ILGenerator:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _ILGenerator, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _ILGenerator, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _ILGenerator) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _ILGenerator, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _LocalBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _LocalBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _LocalBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _LocalBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _LocalBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _MemberInfo:
    # no doc
    def Equals(self, other):
        """ Equals(self: _MemberInfo, other: object) -> bool """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _MemberInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _MemberInfo, inherit: bool) -> Array[object]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _MemberInfo) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _MemberInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetType(self):
        """ GetType(self: _MemberInfo) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _MemberInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _MemberInfo) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _MemberInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _MemberInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def ToString(self):
        """ ToString(self: _MemberInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _MemberInfo) -> Type

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _MemberInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _MemberInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _MemberInfo) -> Type

"""



class _MethodBase:
    # no doc
    def Equals(self, other):
        """ Equals(self: _MethodBase, other: object) -> bool """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _MethodBase, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _MethodBase, inherit: bool) -> Array[object]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _MethodBase) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _MethodBase, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetMethodImplementationFlags(self):
        """ GetMethodImplementationFlags(self: _MethodBase) -> MethodImplAttributes """
        pass

    def GetParameters(self):
        """ GetParameters(self: _MethodBase) -> Array[ParameterInfo] """
        pass

    def GetType(self):
        """ GetType(self: _MethodBase) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _MethodBase, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _MethodBase) -> UInt32 """
        pass

    def Invoke(self, *__args):
        """
        Invoke(self: _MethodBase, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        Invoke(self: _MethodBase, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        Invoke(self: _MethodBase, obj: object, parameters: Array[object]) -> object
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _MethodBase, attributeType: Type, inherit: bool) -> bool """
        pass

    def ToString(self):
        """ ToString(self: _MethodBase) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _MethodBase) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CallingConvention(self: _MethodBase) -> CallingConventions

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _MethodBase) -> Type

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: _MethodBase) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssembly(self: _MethodBase) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConstructor(self: _MethodBase) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamily(self: _MethodBase) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyAndAssembly(self: _MethodBase) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyOrAssembly(self: _MethodBase) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinal(self: _MethodBase) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHideBySig(self: _MethodBase) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: _MethodBase) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: _MethodBase) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _MethodBase) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: _MethodBase) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVirtual(self: _MethodBase) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _MethodBase) -> MemberTypes

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodHandle(self: _MethodBase) -> RuntimeMethodHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _MethodBase) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _MethodBase) -> Type

"""



class _MethodBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _MethodBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _MethodBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _MethodBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _MethodBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _MethodInfo:
    # no doc
    def Equals(self, other):
        """ Equals(self: _MethodInfo, other: object) -> bool """
        pass

    def GetBaseDefinition(self):
        """ GetBaseDefinition(self: _MethodInfo) -> MethodInfo """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _MethodInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _MethodInfo, inherit: bool) -> Array[object]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _MethodInfo) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _MethodInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetMethodImplementationFlags(self):
        """ GetMethodImplementationFlags(self: _MethodInfo) -> MethodImplAttributes """
        pass

    def GetParameters(self):
        """ GetParameters(self: _MethodInfo) -> Array[ParameterInfo] """
        pass

    def GetType(self):
        """ GetType(self: _MethodInfo) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _MethodInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _MethodInfo) -> UInt32 """
        pass

    def Invoke(self, *__args):
        """
        Invoke(self: _MethodInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        Invoke(self: _MethodInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        Invoke(self: _MethodInfo, obj: object, parameters: Array[object]) -> object
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _MethodInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def ToString(self):
        """ ToString(self: _MethodInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _MethodInfo) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CallingConvention(self: _MethodInfo) -> CallingConventions

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _MethodInfo) -> Type

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: _MethodInfo) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssembly(self: _MethodInfo) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConstructor(self: _MethodInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamily(self: _MethodInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyAndAssembly(self: _MethodInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyOrAssembly(self: _MethodInfo) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinal(self: _MethodInfo) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHideBySig(self: _MethodInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: _MethodInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: _MethodInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _MethodInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: _MethodInfo) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVirtual(self: _MethodInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _MethodInfo) -> MemberTypes

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodHandle(self: _MethodInfo) -> RuntimeMethodHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _MethodInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _MethodInfo) -> Type

"""

    ReturnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnType(self: _MethodInfo) -> Type

"""

    ReturnTypeCustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnTypeCustomAttributes(self: _MethodInfo) -> ICustomAttributeProvider

"""



class _MethodRental:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _MethodRental, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _MethodRental, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _MethodRental) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _MethodRental, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Module:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _Module, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _Module, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _Module) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _Module, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ModuleBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _ModuleBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _ModuleBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _ModuleBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _ModuleBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ParameterBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _ParameterBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _ParameterBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _ParameterBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _ParameterBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _ParameterInfo:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _ParameterInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _ParameterInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _ParameterInfo) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _ParameterInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _PropertyBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _PropertyBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _PropertyBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _PropertyBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _PropertyBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _PropertyInfo:
    # no doc
    def Equals(self, other):
        """ Equals(self: _PropertyInfo, other: object) -> bool """
        pass

    def GetAccessors(self, nonPublic=None):
        """
        GetAccessors(self: _PropertyInfo, nonPublic: bool) -> Array[MethodInfo]
        GetAccessors(self: _PropertyInfo) -> Array[MethodInfo]
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _PropertyInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _PropertyInfo, inherit: bool) -> Array[object]
        """
        pass

    def GetGetMethod(self, nonPublic=None):
        """
        GetGetMethod(self: _PropertyInfo, nonPublic: bool) -> MethodInfo
        GetGetMethod(self: _PropertyInfo) -> MethodInfo
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _PropertyInfo) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _PropertyInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetIndexParameters(self):
        """ GetIndexParameters(self: _PropertyInfo) -> Array[ParameterInfo] """
        pass

    def GetSetMethod(self, nonPublic=None):
        """
        GetSetMethod(self: _PropertyInfo, nonPublic: bool) -> MethodInfo
        GetSetMethod(self: _PropertyInfo) -> MethodInfo
        """
        pass

    def GetType(self):
        """ GetType(self: _PropertyInfo) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _PropertyInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _PropertyInfo) -> UInt32 """
        pass

    def GetValue(self, obj, *__args):
        """
        GetValue(self: _PropertyInfo, obj: object, index: Array[object]) -> object
        GetValue(self: _PropertyInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) -> object
        """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _PropertyInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _PropertyInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def SetValue(self, obj, value, *__args):
        """ SetValue(self: _PropertyInfo, obj: object, value: object, index: Array[object])SetValue(self: _PropertyInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) """
        pass

    def ToString(self):
        """ ToString(self: _PropertyInfo) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _PropertyInfo) -> PropertyAttributes

"""

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: _PropertyInfo) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: _PropertyInfo) -> bool

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _PropertyInfo) -> Type

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _PropertyInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _PropertyInfo) -> MemberTypes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _PropertyInfo) -> str

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: _PropertyInfo) -> Type

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _PropertyInfo) -> Type

"""



class _SignatureHelper:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _SignatureHelper, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _SignatureHelper, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _SignatureHelper) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _SignatureHelper, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Thread:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _Thread, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _Thread, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _Thread) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _Thread, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _Type:
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: _Type, other: object) -> bool
        Equals(self: _Type, o: Type) -> bool
        """
        pass

    def FindInterfaces(self, filter, filterCriteria):
        """ FindInterfaces(self: _Type, filter: TypeFilter, filterCriteria: object) -> Array[Type] """
        pass

    def FindMembers(self, memberType, bindingAttr, filter, filterCriteria):
        """ FindMembers(self: _Type, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: object) -> Array[MemberInfo] """
        pass

    def GetArrayRank(self):
        """ GetArrayRank(self: _Type) -> int """
        pass

    def GetConstructor(self, *__args):
        """
        GetConstructor(self: _Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        GetConstructor(self: _Type, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        GetConstructor(self: _Type, types: Array[Type]) -> ConstructorInfo
        """
        pass

    def GetConstructors(self, bindingAttr=None):
        """
        GetConstructors(self: _Type, bindingAttr: BindingFlags) -> Array[ConstructorInfo]
        GetConstructors(self: _Type) -> Array[ConstructorInfo]
        """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: _Type, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _Type, inherit: bool) -> Array[object]
        """
        pass

    def GetDefaultMembers(self):
        """ GetDefaultMembers(self: _Type) -> Array[MemberInfo] """
        pass

    def GetElementType(self):
        """ GetElementType(self: _Type) -> Type """
        pass

    def GetEvent(self, name, bindingAttr=None):
        """
        GetEvent(self: _Type, name: str, bindingAttr: BindingFlags) -> EventInfo
        GetEvent(self: _Type, name: str) -> EventInfo
        """
        pass

    def GetEvents(self, bindingAttr=None):
        """
        GetEvents(self: _Type) -> Array[EventInfo]
        GetEvents(self: _Type, bindingAttr: BindingFlags) -> Array[EventInfo]
        """
        pass

    def GetField(self, name, bindingAttr=None):
        """
        GetField(self: _Type, name: str, bindingAttr: BindingFlags) -> FieldInfo
        GetField(self: _Type, name: str) -> FieldInfo
        """
        pass

    def GetFields(self, bindingAttr=None):
        """
        GetFields(self: _Type, bindingAttr: BindingFlags) -> Array[FieldInfo]
        GetFields(self: _Type) -> Array[FieldInfo]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: _Type) -> int """
        pass

    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _Type, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetInterface(self, name, ignoreCase=None):
        """
        GetInterface(self: _Type, name: str, ignoreCase: bool) -> Type
        GetInterface(self: _Type, name: str) -> Type
        """
        pass

    def GetInterfaceMap(self, interfaceType):
        """ GetInterfaceMap(self: _Type, interfaceType: Type) -> InterfaceMapping """
        pass

    def GetInterfaces(self):
        """ GetInterfaces(self: _Type) -> Array[Type] """
        pass

    def GetMember(self, name, *__args):
        """
        GetMember(self: _Type, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMember(self: _Type, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMember(self: _Type, name: str) -> Array[MemberInfo]
        """
        pass

    def GetMembers(self, bindingAttr=None):
        """
        GetMembers(self: _Type, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMembers(self: _Type) -> Array[MemberInfo]
        """
        pass

    def GetMethod(self, name, *__args):
        """
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags) -> MethodInfo
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: _Type, name: str, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: _Type, name: str, types: Array[Type]) -> MethodInfo
        GetMethod(self: _Type, name: str) -> MethodInfo
        """
        pass

    def GetMethods(self, bindingAttr=None):
        """
        GetMethods(self: _Type, bindingAttr: BindingFlags) -> Array[MethodInfo]
        GetMethods(self: _Type) -> Array[MethodInfo]
        """
        pass

    def GetNestedType(self, name, bindingAttr=None):
        """
        GetNestedType(self: _Type, name: str, bindingAttr: BindingFlags) -> Type
        GetNestedType(self: _Type, name: str) -> Type
        """
        pass

    def GetNestedTypes(self, bindingAttr=None):
        """
        GetNestedTypes(self: _Type, bindingAttr: BindingFlags) -> Array[Type]
        GetNestedTypes(self: _Type) -> Array[Type]
        """
        pass

    def GetProperties(self, bindingAttr=None):
        """
        GetProperties(self: _Type, bindingAttr: BindingFlags) -> Array[PropertyInfo]
        GetProperties(self: _Type) -> Array[PropertyInfo]
        """
        pass

    def GetProperty(self, name, *__args):
        """
        GetProperty(self: _Type, name: str, bindingAttr: BindingFlags) -> PropertyInfo
        GetProperty(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        GetProperty(self: _Type, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        GetProperty(self: _Type, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo
        GetProperty(self: _Type, name: str, types: Array[Type]) -> PropertyInfo
        GetProperty(self: _Type, name: str, returnType: Type) -> PropertyInfo
        GetProperty(self: _Type, name: str) -> PropertyInfo
        """
        pass

    def GetType(self):
        """ GetType(self: _Type) -> Type """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _Type, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _Type) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _Type, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def InvokeMember(self, name, invokeAttr, binder, target, args, *__args):
        """
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], culture: CultureInfo) -> object
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object]) -> object
        """
        pass

    def IsAssignableFrom(self, c):
        """ IsAssignableFrom(self: _Type, c: Type) -> bool """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: _Type, attributeType: Type, inherit: bool) -> bool """
        pass

    def IsInstanceOfType(self, o):
        """ IsInstanceOfType(self: _Type, o: object) -> bool """
        pass

    def IsSubclassOf(self, c):
        """ IsSubclassOf(self: _Type, c: Type) -> bool """
        pass

    def ToString(self):
        """ ToString(self: _Type) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Assembly(self: _Type) -> Assembly

"""

    AssemblyQualifiedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyQualifiedName(self: _Type) -> str

"""

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: _Type) -> TypeAttributes

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: _Type) -> Type

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: _Type) -> Type

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: _Type) -> str

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: _Type) -> Guid

"""

    HasElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasElementType(self: _Type) -> bool

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: _Type) -> bool

"""

    IsAnsiClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAnsiClass(self: _Type) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArray(self: _Type) -> bool

"""

    IsAutoClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutoClass(self: _Type) -> bool

"""

    IsAutoLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutoLayout(self: _Type) -> bool

"""

    IsByRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsByRef(self: _Type) -> bool

"""

    IsClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClass(self: _Type) -> bool

"""

    IsCOMObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCOMObject(self: _Type) -> bool

"""

    IsContextful = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsContextful(self: _Type) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnum(self: _Type) -> bool

"""

    IsExplicitLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsExplicitLayout(self: _Type) -> bool

"""

    IsImport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsImport(self: _Type) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInterface(self: _Type) -> bool

"""

    IsLayoutSequential = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayoutSequential(self: _Type) -> bool

"""

    IsMarshalByRef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMarshalByRef(self: _Type) -> bool

"""

    IsNestedAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedAssembly(self: _Type) -> bool

"""

    IsNestedFamANDAssem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedFamANDAssem(self: _Type) -> bool

"""

    IsNestedFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedFamily(self: _Type) -> bool

"""

    IsNestedFamORAssem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedFamORAssem(self: _Type) -> bool

"""

    IsNestedPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedPrivate(self: _Type) -> bool

"""

    IsNestedPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNestedPublic(self: _Type) -> bool

"""

    IsNotPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNotPublic(self: _Type) -> bool

"""

    IsPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointer(self: _Type) -> bool

"""

    IsPrimitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrimitive(self: _Type) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: _Type) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSealed(self: _Type) -> bool

"""

    IsSerializable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSerializable(self: _Type) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: _Type) -> bool

"""

    IsUnicodeClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnicodeClass(self: _Type) -> bool

"""

    IsValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValueType(self: _Type) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: _Type) -> MemberTypes

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: _Type) -> Module

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: _Type) -> str

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Namespace(self: _Type) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: _Type) -> Type

"""

    TypeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeHandle(self: _Type) -> RuntimeTypeHandle

"""

    TypeInitializer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeInitializer(self: _Type) -> ConstructorInfo

"""

    UnderlyingSystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnderlyingSystemType(self: _Type) -> Type

"""



class _TypeBuilder:
    # no doc
    def GetIDsOfNames(self, riid, rgszNames, cNames, lcid, rgDispId):
        """ GetIDsOfNames(self: _TypeBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        pass

    def GetTypeInfo(self, iTInfo, lcid, ppTInfo):
        """ GetTypeInfo(self: _TypeBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        pass

    def GetTypeInfoCount(self, pcTInfo):
        """ GetTypeInfoCount(self: _TypeBuilder) -> UInt32 """
        pass

    def Invoke(self, dispIdMember, riid, lcid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr):
        """ Invoke(self: _TypeBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


# variables with complex values

