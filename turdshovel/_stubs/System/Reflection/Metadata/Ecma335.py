# encoding: utf-8
# module System.Reflection.Metadata.Ecma335 calls itself Ecma335
# from System.Reflection.Metadata, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ArrayShapeEncoder(object):
    """ ArrayShapeEncoder(builder: BlobBuilder) """
    def Shape(self, rank, sizes, lowerBounds):
        """ Shape(self: ArrayShapeEncoder, rank: int, sizes: ImmutableArray[int], lowerBounds: ImmutableArray[int]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[ArrayShapeEncoder]() -> ArrayShapeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: ArrayShapeEncoder) -> BlobBuilder

"""



class BlobEncoder(object):
    """ BlobEncoder(builder: BlobBuilder) """
    def CustomAttributeSignature(self, fixedArguments, namedArguments):
        """
        CustomAttributeSignature(self: BlobEncoder) -> (FixedArgumentsEncoder, CustomAttributeNamedArgumentsEncoder)
        
            Encodes custom attribute signature blob.
         Returns a pair of encoders that must be used in the order they appear in the parameter list.
        CustomAttributeSignature(self: BlobEncoder, fixedArguments: Action[FixedArgumentsEncoder], namedArguments: Action[CustomAttributeNamedArgumentsEncoder])
        """
        pass

    def FieldSignature(self):
        """
        FieldSignature(self: BlobEncoder) -> SignatureTypeEncoder
        
            Encodes field signature blob.
            Returns: Encoder of the field type.
        """
        pass

    def LocalVariableSignature(self, variableCount):
        """
        LocalVariableSignature(self: BlobEncoder, variableCount: int) -> LocalVariablesEncoder
        
            Encodes local variable signature.
        
            variableCount: Number of local variables.
            Returns: Encoder of a sequence of local variables.
        """
        pass

    def MethodSignature(self, convention, genericParameterCount, isInstanceMethod):
        """
        MethodSignature(self: BlobEncoder, convention: SignatureCallingConvention, genericParameterCount: int, isInstanceMethod: bool) -> MethodSignatureEncoder
        
            Encodes method signature blob.
        
            convention: Calling convention.
            genericParameterCount: Number of generic parameters.
            isInstanceMethod: ue to encode an instance method signature, lse to encode a static method signature.
            Returns: An encoder of the rest of the signature including return value and parameters.
        """
        pass

    def MethodSpecificationSignature(self, genericArgumentCount):
        """
        MethodSpecificationSignature(self: BlobEncoder, genericArgumentCount: int) -> GenericTypeArgumentsEncoder
        
            Encodes method specification signature blob.
        
            genericArgumentCount: Number of generic arguments.
            Returns: Encoder of generic arguments.
        """
        pass

    def PermissionSetArguments(self, argumentCount):
        """
        PermissionSetArguments(self: BlobEncoder, argumentCount: int) -> NamedArgumentsEncoder
        
            Encodes permission set arguments.
        
            argumentCount: Number of arguments in the set.
            Returns: Encoder of the arguments of the set.
        """
        pass

    def PermissionSetBlob(self, attributeCount):
        """
        PermissionSetBlob(self: BlobEncoder, attributeCount: int) -> PermissionSetEncoder
        
            Encodes a permission set blob.
        
            attributeCount: Number of attributes in the set.
            Returns: Permission set encoder.
        """
        pass

    def PropertySignature(self, isInstanceProperty):
        """
        PropertySignature(self: BlobEncoder, isInstanceProperty: bool) -> MethodSignatureEncoder
        
            Encodes property signature blob.
        
            isInstanceProperty: ue to encode an instance property signature, lse to encode a static property signature.
            Returns: An encoder of the rest of the signature including return value and parameters, which has the same structure as method signature.
        """
        pass

    def TypeSpecificationSignature(self):
        """
        TypeSpecificationSignature(self: BlobEncoder) -> SignatureTypeEncoder
        
            Encodes type specification signature.
            Returns: Type encoder of the structured type represented by the type specification (it shall not encode a primitive type).
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[BlobEncoder]() -> BlobEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: BlobEncoder) -> BlobBuilder

"""



class CodedIndex(object):
    # no doc
    @staticmethod
    def CustomAttributeType(handle):
        """
        CustomAttributeType(handle: EntityHandle) -> int
        
            Calculates a CustomAttributeType coded index for the specified handle.
        
            handle: System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle
        """
        pass

    @staticmethod
    def HasConstant(handle):
        """
        HasConstant(handle: EntityHandle) -> int
        
            Calculates a HasConstant coded index for the specified handle.
        
            handle: System.Reflection.Metadata.ParameterHandle, System.Reflection.Metadata.FieldDefinitionHandle, or System.Reflection.Metadata.PropertyDefinitionHandle
        """
        pass

    @staticmethod
    def HasCustomAttribute(handle):
        """
        HasCustomAttribute(handle: EntityHandle) -> int
        
            Calculates a HasCustomAttribute coded index for the specified handle.
        
            handle: System.Reflection.Metadata.MethodDefinitionHandle, System.Reflection.Metadata.FieldDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, 
             System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.ParameterHandle, System.Reflection.Metadata.InterfaceImplementationHandle, 
             System.Reflection.Metadata.MemberReferenceHandle, System.Reflection.Metadata.ModuleDefinitionHandle, System.Reflection.Metadata.DeclarativeSecurityAttributeHandle, 
             System.Reflection.Metadata.PropertyDefinitionHandle, System.Reflection.Metadata.EventDefinitionHandle, System.Reflection.Metadata.StandaloneSignatureHandle, 
             System.Reflection.Metadata.ModuleReferenceHandle, System.Reflection.Metadata.TypeSpecificationHandle, System.Reflection.Metadata.AssemblyDefinitionHandle, 
             System.Reflection.Metadata.AssemblyReferenceHandle, System.Reflection.Metadata.AssemblyFileHandle, System.Reflection.Metadata.ExportedTypeHandle, 
             System.Reflection.Metadata.ManifestResourceHandle, System.Reflection.Metadata.GenericParameterHandle, System.Reflection.Metadata.GenericParameterConstraintHandle or 
             System.Reflection.Metadata.MethodSpecificationHandle.
        """
        pass

    @staticmethod
    def HasCustomDebugInformation(handle):
        """
        HasCustomDebugInformation(handle: EntityHandle) -> int
        
            Calculates a HasCustomDebugInformation coded index for the specified handle.
        
            handle: System.Reflection.Metadata.MethodDefinitionHandle, System.Reflection.Metadata.FieldDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, 
             System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.ParameterHandle, System.Reflection.Metadata.InterfaceImplementationHandle, 
             System.Reflection.Metadata.MemberReferenceHandle, System.Reflection.Metadata.ModuleDefinitionHandle, System.Reflection.Metadata.DeclarativeSecurityAttributeHandle, 
             System.Reflection.Metadata.PropertyDefinitionHandle, System.Reflection.Metadata.EventDefinitionHandle, System.Reflection.Metadata.StandaloneSignatureHandle, 
             System.Reflection.Metadata.ModuleReferenceHandle, System.Reflection.Metadata.TypeSpecificationHandle, System.Reflection.Metadata.AssemblyDefinitionHandle, 
             System.Reflection.Metadata.AssemblyReferenceHandle, System.Reflection.Metadata.AssemblyFileHandle, System.Reflection.Metadata.ExportedTypeHandle, 
             System.Reflection.Metadata.ManifestResourceHandle, System.Reflection.Metadata.GenericParameterHandle, System.Reflection.Metadata.GenericParameterConstraintHandle, 
             System.Reflection.Metadata.MethodSpecificationHandle, System.Reflection.Metadata.DocumentHandle, System.Reflection.Metadata.LocalScopeHandle, 
             System.Reflection.Metadata.LocalVariableHandle, System.Reflection.Metadata.LocalConstantHandle or System.Reflection.Metadata.ImportScopeHandle.
        """
        pass

    @staticmethod
    def HasDeclSecurity(handle):
        """
        HasDeclSecurity(handle: EntityHandle) -> int
        
            Calculates a HasDeclSecurity coded index for the specified handle.
        
            handle: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.MethodDefinitionHandle, or System.Reflection.Metadata.AssemblyDefinitionHandle
        """
        pass

    @staticmethod
    def HasFieldMarshal(handle):
        """
        HasFieldMarshal(handle: EntityHandle) -> int
        
            Calculates a HasFieldMarshal coded index for the specified handle.
        
            handle: System.Reflection.Metadata.ParameterHandle or System.Reflection.Metadata.FieldDefinitionHandle
        """
        pass

    @staticmethod
    def HasSemantics(handle):
        """
        HasSemantics(handle: EntityHandle) -> int
        
            Calculates a HasSemantics coded index for the specified handle.
        
            handle: System.Reflection.Metadata.EventDefinitionHandle or System.Reflection.Metadata.PropertyDefinitionHandle
        """
        pass

    @staticmethod
    def Implementation(handle):
        """
        Implementation(handle: EntityHandle) -> int
        
            Calculates an implementation coded index for the specified handle.
        
            handle: System.Reflection.Metadata.AssemblyFileHandle, System.Reflection.Metadata.ExportedTypeHandle or System.Reflection.Metadata.AssemblyReferenceHandle
        """
        pass

    @staticmethod
    def MemberForwarded(handle):
        """
        MemberForwarded(handle: EntityHandle) -> int
        
            Calculates a MemberForwarded coded index for the specified handle.
        
            handle: System.Reflection.Metadata.FieldDefinition, System.Reflection.Metadata.MethodDefinition
        """
        pass

    @staticmethod
    def MemberRefParent(handle):
        """
        MemberRefParent(handle: EntityHandle) -> int
        
            Calculates a MemberRefParent coded index for the specified handle.
        
            handle: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, System.Reflection.Metadata.ModuleReferenceHandle, 
             System.Reflection.Metadata.MethodDefinitionHandle, or System.Reflection.Metadata.TypeSpecificationHandle.
        """
        pass

    @staticmethod
    def MethodDefOrRef(handle):
        """
        MethodDefOrRef(handle: EntityHandle) -> int
        
            Calculates a MethodDefOrRef coded index for the specified handle.
        
            handle: System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle
        """
        pass

    @staticmethod
    def ResolutionScope(handle):
        """
        ResolutionScope(handle: EntityHandle) -> int
        
            Calculates a ResolutionScope coded index for the specified handle.
        
            handle: System.Reflection.Metadata.ModuleDefinitionHandle, System.Reflection.Metadata.ModuleReferenceHandle, System.Reflection.Metadata.AssemblyReferenceHandle or 
             System.Reflection.Metadata.TypeReferenceHandle
        """
        pass

    @staticmethod
    def TypeDefOrRef(handle):
        """
        TypeDefOrRef(handle: EntityHandle) -> int
        
            Calculates a TypeDefOrRef coded index for the specified handle.
        
            handle: System.Reflection.Metadata.TypeDefinitionHandle or System.Reflection.Metadata.TypeReferenceHandle
        """
        pass

    @staticmethod
    def TypeDefOrRefOrSpec(handle):
        """
        TypeDefOrRefOrSpec(handle: EntityHandle) -> int
        
            Calculates a TypeDefOrRefOrSpec coded index for the specified handle.
        
            handle: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle or System.Reflection.Metadata.TypeSpecificationHandle
        """
        pass

    @staticmethod
    def TypeOrMethodDef(handle):
        """
        TypeOrMethodDef(handle: EntityHandle) -> int
        
            Calculates a TypeOrMethodDef coded index for the specified handle.
        
            handle: System.Reflection.Metadata.TypeDefinitionHandle or System.Reflection.Metadata.MethodDefinitionHandle
        """
        pass

    __all__ = [
        'CustomAttributeType',
        'HasConstant',
        'HasCustomAttribute',
        'HasCustomDebugInformation',
        'HasDeclSecurity',
        'HasFieldMarshal',
        'HasSemantics',
        'Implementation',
        'MemberForwarded',
        'MemberRefParent',
        'MethodDefOrRef',
        'ResolutionScope',
        'TypeDefOrRef',
        'TypeDefOrRefOrSpec',
        'TypeOrMethodDef',
    ]


class ControlFlowBuilder(object):
    """ ControlFlowBuilder() """
    def AddCatchRegion(self, tryStart, tryEnd, handlerStart, handlerEnd, catchType):
        """
        AddCatchRegion(self: ControlFlowBuilder, tryStart: LabelHandle, tryEnd: LabelHandle, handlerStart: LabelHandle, handlerEnd: LabelHandle, catchType: EntityHandle)
            Adds catch region.
        
            tryStart: Label marking the first instruction of the try block.
            tryEnd: Label marking the instruction immediately following the try block.
            handlerStart: Label marking the first instruction of the handler.
            handlerEnd: Label marking the instruction immediately following the handler.
            catchType: The type of exception to be caught: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle or 
             System.Reflection.Metadata.TypeSpecificationHandle.
        """
        pass

    def AddFaultRegion(self, tryStart, tryEnd, handlerStart, handlerEnd):
        """
        AddFaultRegion(self: ControlFlowBuilder, tryStart: LabelHandle, tryEnd: LabelHandle, handlerStart: LabelHandle, handlerEnd: LabelHandle)
            Adds fault region.
        
            tryStart: Label marking the first instruction of the try block.
            tryEnd: Label marking the instruction immediately following the try block.
            handlerStart: Label marking the first instruction of the handler.
            handlerEnd: Label marking the instruction immediately following the handler.
        """
        pass

    def AddFilterRegion(self, tryStart, tryEnd, handlerStart, handlerEnd, filterStart):
        """
        AddFilterRegion(self: ControlFlowBuilder, tryStart: LabelHandle, tryEnd: LabelHandle, handlerStart: LabelHandle, handlerEnd: LabelHandle, filterStart: LabelHandle)
            Adds catch region.
        
            tryStart: Label marking the first instruction of the try block.
            tryEnd: Label marking the instruction immediately following the try block.
            handlerStart: Label marking the first instruction of the handler.
            handlerEnd: Label marking the instruction immediately following the handler.
            filterStart: Label marking the first instruction of the filter block.
        """
        pass

    def AddFinallyRegion(self, tryStart, tryEnd, handlerStart, handlerEnd):
        """
        AddFinallyRegion(self: ControlFlowBuilder, tryStart: LabelHandle, tryEnd: LabelHandle, handlerStart: LabelHandle, handlerEnd: LabelHandle)
            Adds finally region.
        
            tryStart: Label marking the first instruction of the try block.
            tryEnd: Label marking the instruction immediately following the try block.
            handlerStart: Label marking the first instruction of the handler.
            handlerEnd: Label marking the instruction immediately following the handler.
        """
        pass


class CustomAttributeArrayTypeEncoder(object):
    """ CustomAttributeArrayTypeEncoder(builder: BlobBuilder) """
    def ElementType(self):
        """ ElementType(self: CustomAttributeArrayTypeEncoder) -> CustomAttributeElementTypeEncoder """
        pass

    def ObjectArray(self):
        """ ObjectArray(self: CustomAttributeArrayTypeEncoder) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[CustomAttributeArrayTypeEncoder]() -> CustomAttributeArrayTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: CustomAttributeArrayTypeEncoder) -> BlobBuilder

"""



class CustomAttributeElementTypeEncoder(object):
    """ CustomAttributeElementTypeEncoder(builder: BlobBuilder) """
    def Boolean(self):
        """ Boolean(self: CustomAttributeElementTypeEncoder) """
        pass

    def Byte(self):
        """ Byte(self: CustomAttributeElementTypeEncoder) """
        pass

    def Char(self):
        """ Char(self: CustomAttributeElementTypeEncoder) """
        pass

    def Double(self):
        """ Double(self: CustomAttributeElementTypeEncoder) """
        pass

    def Enum(self, enumTypeName):
        """ Enum(self: CustomAttributeElementTypeEncoder, enumTypeName: str) """
        pass

    def Int16(self):
        """ Int16(self: CustomAttributeElementTypeEncoder) """
        pass

    def Int32(self):
        """ Int32(self: CustomAttributeElementTypeEncoder) """
        pass

    def Int64(self):
        """ Int64(self: CustomAttributeElementTypeEncoder) """
        pass

    def PrimitiveType(self, type):
        """ PrimitiveType(self: CustomAttributeElementTypeEncoder, type: PrimitiveSerializationTypeCode) """
        pass

    def SByte(self):
        """ SByte(self: CustomAttributeElementTypeEncoder) """
        pass

    def Single(self):
        """ Single(self: CustomAttributeElementTypeEncoder) """
        pass

    def String(self):
        """ String(self: CustomAttributeElementTypeEncoder) """
        pass

    def SystemType(self):
        """ SystemType(self: CustomAttributeElementTypeEncoder) """
        pass

    def UInt16(self):
        """ UInt16(self: CustomAttributeElementTypeEncoder) """
        pass

    def UInt32(self):
        """ UInt32(self: CustomAttributeElementTypeEncoder) """
        pass

    def UInt64(self):
        """ UInt64(self: CustomAttributeElementTypeEncoder) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[CustomAttributeElementTypeEncoder]() -> CustomAttributeElementTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: CustomAttributeElementTypeEncoder) -> BlobBuilder

"""



class CustomAttributeNamedArgumentsEncoder(object):
    """ CustomAttributeNamedArgumentsEncoder(builder: BlobBuilder) """
    def Count(self, count):
        """ Count(self: CustomAttributeNamedArgumentsEncoder, count: int) -> NamedArgumentsEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[CustomAttributeNamedArgumentsEncoder]() -> CustomAttributeNamedArgumentsEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: CustomAttributeNamedArgumentsEncoder) -> BlobBuilder

"""



class CustomModifiersEncoder(object):
    """ CustomModifiersEncoder(builder: BlobBuilder) """
    def AddModifier(self, type, isOptional):
        """
        AddModifier(self: CustomModifiersEncoder, type: EntityHandle, isOptional: bool) -> CustomModifiersEncoder
        
            Encodes a custom modifier.
        
            type: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle or System.Reflection.Metadata.TypeSpecificationHandle.
            isOptional: Is optional modifier.
            Returns: Encoder of subsequent modifiers.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[CustomModifiersEncoder]() -> CustomModifiersEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: CustomModifiersEncoder) -> BlobBuilder

"""



class EditAndContinueLogEntry(object, IEquatable[EditAndContinueLogEntry]):
    """ EditAndContinueLogEntry(handle: EntityHandle, operation: EditAndContinueOperation) """
    def Equals(self, *__args):
        """
        Equals(self: EditAndContinueLogEntry, obj: object) -> bool
        Equals(self: EditAndContinueLogEntry, other: EditAndContinueLogEntry) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EditAndContinueLogEntry) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, handle, operation):
        """
        __new__(cls: type, handle: EntityHandle, operation: EditAndContinueOperation)
        __new__[EditAndContinueLogEntry]() -> EditAndContinueLogEntry
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: EditAndContinueLogEntry) -> EntityHandle

"""

    Operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Operation(self: EditAndContinueLogEntry) -> EditAndContinueOperation

"""



class EditAndContinueOperation(Enum, IComparable, IFormattable, IConvertible):
    """ enum EditAndContinueOperation, values: AddEvent (5), AddField (2), AddMethod (1), AddParameter (3), AddProperty (4), Default (0) """
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

    AddEvent = None
    AddField = None
    AddMethod = None
    AddParameter = None
    AddProperty = None
    Default = None
    value__ = None


class ExceptionRegionEncoder(object):
    # no doc
    def Add(self, kind, tryOffset, tryLength, handlerOffset, handlerLength, catchType, filterOffset):
        """
        Add(self: ExceptionRegionEncoder, kind: ExceptionRegionKind, tryOffset: int, tryLength: int, handlerOffset: int, handlerLength: int, catchType: EntityHandle, filterOffset: int) -> ExceptionRegionEncoder
        
            Adds an exception clause.
        
            kind: Clause kind.
            tryOffset: Try block start offset.
            tryLength: Try block length.
            handlerOffset: Handler start offset.
            handlerLength: Handler length.
            catchType: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle or System.Reflection.Metadata.TypeSpecificationHandle, or nil if kind is not 
             System.Reflection.Metadata.ExceptionRegionKind.Catch
        
            filterOffset: Offset of the filter block, or 0 if the kind is not System.Reflection.Metadata.ExceptionRegionKind.Filter.
            Returns: Encoder for the next clause.
        """
        pass

    def AddCatch(self, tryOffset, tryLength, handlerOffset, handlerLength, catchType):
        """
        AddCatch(self: ExceptionRegionEncoder, tryOffset: int, tryLength: int, handlerOffset: int, handlerLength: int, catchType: EntityHandle) -> ExceptionRegionEncoder
        
            Adds a fault clause.
        
            tryOffset: Try block start offset.
            tryLength: Try block length.
            handlerOffset: Handler start offset.
            handlerLength: Handler length.
            catchType: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle or System.Reflection.Metadata.TypeSpecificationHandle.
            Returns: Encoder for the next clause.
        """
        pass

    def AddFault(self, tryOffset, tryLength, handlerOffset, handlerLength):
        """
        AddFault(self: ExceptionRegionEncoder, tryOffset: int, tryLength: int, handlerOffset: int, handlerLength: int) -> ExceptionRegionEncoder
        
            Adds a fault clause.
        
            tryOffset: Try block start offset.
            tryLength: Try block length.
            handlerOffset: Handler start offset.
            handlerLength: Handler length.
            Returns: Encoder for the next clause.
        """
        pass

    def AddFilter(self, tryOffset, tryLength, handlerOffset, handlerLength, filterOffset):
        """
        AddFilter(self: ExceptionRegionEncoder, tryOffset: int, tryLength: int, handlerOffset: int, handlerLength: int, filterOffset: int) -> ExceptionRegionEncoder
        
            Adds a fault clause.
        
            tryOffset: Try block start offset.
            tryLength: Try block length.
            handlerOffset: Handler start offset.
            handlerLength: Handler length.
            filterOffset: Offset of the filter block.
            Returns: Encoder for the next clause.
        """
        pass

    def AddFinally(self, tryOffset, tryLength, handlerOffset, handlerLength):
        """
        AddFinally(self: ExceptionRegionEncoder, tryOffset: int, tryLength: int, handlerOffset: int, handlerLength: int) -> ExceptionRegionEncoder
        
            Adds a finally clause.
        
            tryOffset: Try block start offset.
            tryLength: Try block length.
            handlerOffset: Handler start offset.
            handlerLength: Handler length.
            Returns: Encoder for the next clause.
        """
        pass

    @staticmethod
    def IsSmallExceptionRegion(startOffset, length):
        """
        IsSmallExceptionRegion(startOffset: int, length: int) -> bool
        
            Returns ue if the region fits small format.
        
            startOffset: Start offset of the region.
            length: Length of the region.
        """
        pass

    @staticmethod
    def IsSmallRegionCount(exceptionRegionCount):
        """
        IsSmallRegionCount(exceptionRegionCount: int) -> bool
        
            Returns ue if the number of exception regions first small format.
        
            exceptionRegionCount: Number of exception regions.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The underlying builder.

Get: Builder(self: ExceptionRegionEncoder) -> BlobBuilder

"""

    HasSmallFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ue if the encoder uses small format.

Get: HasSmallFormat(self: ExceptionRegionEncoder) -> bool

"""



class ExportedTypeExtensions(object):
    """ Provides an extension method to access the TypeDefinitionId column of the ExportedType table. """
    @staticmethod
    def GetTypeDefinitionId(exportedType):
        """
        GetTypeDefinitionId(exportedType: ExportedType) -> int
        
            Gets a hint at the likely row number of the target type in the TypeDef table of its module.
         If the namespaces and names do not match, resolution falls back to a full search of the 
             target TypeDef table. Ignored and should be zero if System.Reflection.Metadata.ExportedType.IsForwarder is ue.
        """
        pass

    __all__ = [
        'GetTypeDefinitionId',
    ]


class FixedArgumentsEncoder(object):
    """ FixedArgumentsEncoder(builder: BlobBuilder) """
    def AddArgument(self):
        """ AddArgument(self: FixedArgumentsEncoder) -> LiteralEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[FixedArgumentsEncoder]() -> FixedArgumentsEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: FixedArgumentsEncoder) -> BlobBuilder

"""



class FunctionPointerAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum FunctionPointerAttributes, values: HasExplicitThis (96), HasThis (32), None (0) """
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

    HasExplicitThis = None
    HasThis = None
    None = None
    value__ = None


class GenericTypeArgumentsEncoder(object):
    """ GenericTypeArgumentsEncoder(builder: BlobBuilder) """
    def AddArgument(self):
        """ AddArgument(self: GenericTypeArgumentsEncoder) -> SignatureTypeEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[GenericTypeArgumentsEncoder]() -> GenericTypeArgumentsEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: GenericTypeArgumentsEncoder) -> BlobBuilder

"""



class HeapIndex(Enum, IComparable, IFormattable, IConvertible):
    """ enum HeapIndex, values: Blob (2), Guid (3), String (1), UserString (0) """
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

    Blob = None
    Guid = None
    String = None
    UserString = None
    value__ = None


class InstructionEncoder(object):
    """
    Encodes instructions.
    
    InstructionEncoder(codeBuilder: BlobBuilder, controlFlowBuilder: ControlFlowBuilder)
    """
    def Branch(self, code, label):
        """
        Branch(self: InstructionEncoder, code: ILOpCode, label: LabelHandle)
            Encodes a branch instruction.
        
            code: Branch instruction to encode.
            label: Label of the target location in instruction stream.
        """
        pass

    def Call(self, methodHandle):
        """
        Call(self: InstructionEncoder, methodHandle: EntityHandle)
            Encodes call instruction and its operand.
        Call(self: InstructionEncoder, methodHandle: MethodDefinitionHandle)
            Encodes call instruction and its operand.
        Call(self: InstructionEncoder, methodHandle: MethodSpecificationHandle)
            Encodes call instruction and its operand.
        Call(self: InstructionEncoder, methodHandle: MemberReferenceHandle)
            Encodes call instruction and its operand.
        """
        pass

    def CallIndirect(self, signature):
        """
        CallIndirect(self: InstructionEncoder, signature: StandaloneSignatureHandle)
            Encodes calli instruction and its operand.
        """
        pass

    def DefineLabel(self):
        """
        DefineLabel(self: InstructionEncoder) -> LabelHandle
        
            Defines a label that can later be used to mark and refer to a location in the instruction stream.
            Returns: Label handle.
        """
        pass

    def LoadArgument(self, argumentIndex):
        """
        LoadArgument(self: InstructionEncoder, argumentIndex: int)
            Encodes argument load instruction.
        
            argumentIndex: Index of the argument.
        """
        pass

    def LoadArgumentAddress(self, argumentIndex):
        """
        LoadArgumentAddress(self: InstructionEncoder, argumentIndex: int)
            Encodes argument address load instruction.
        
            argumentIndex: Index of the argument.
        """
        pass

    def LoadConstantI4(self, value):
        """
        LoadConstantI4(self: InstructionEncoder, value: int)
            Encodes System.Int32 constant load instruction.
        """
        pass

    def LoadConstantI8(self, value):
        """
        LoadConstantI8(self: InstructionEncoder, value: Int64)
            Encodes System.Int64 constant load instruction.
        """
        pass

    def LoadConstantR4(self, value):
        """
        LoadConstantR4(self: InstructionEncoder, value: Single)
            Encodes System.Single constant load instruction.
        """
        pass

    def LoadConstantR8(self, value):
        """
        LoadConstantR8(self: InstructionEncoder, value: float)
            Encodes System.Double constant load instruction.
        """
        pass

    def LoadLocal(self, slotIndex):
        """
        LoadLocal(self: InstructionEncoder, slotIndex: int)
            Encodes local variable load instruction.
        
            slotIndex: Index of the local variable slot.
        """
        pass

    def LoadLocalAddress(self, slotIndex):
        """
        LoadLocalAddress(self: InstructionEncoder, slotIndex: int)
            Encodes local variable address load instruction.
        
            slotIndex: Index of the local variable slot.
        """
        pass

    def LoadString(self, handle):
        """
        LoadString(self: InstructionEncoder, handle: UserStringHandle)
            Encodes ldstr instruction and its operand.
        """
        pass

    def MarkLabel(self, label):
        """
        MarkLabel(self: InstructionEncoder, label: LabelHandle)
            Associates specified label with the current IL offset.
        
            label: Label to mark.
        """
        pass

    def OpCode(self, code):
        """
        OpCode(self: InstructionEncoder, code: ILOpCode)
            Encodes specified op-code.
        """
        pass

    def StoreArgument(self, argumentIndex):
        """
        StoreArgument(self: InstructionEncoder, argumentIndex: int)
            Encodes argument store instruction.
        
            argumentIndex: Index of the argument.
        """
        pass

    def StoreLocal(self, slotIndex):
        """
        StoreLocal(self: InstructionEncoder, slotIndex: int)
            Encodes local variable store instruction.
        
            slotIndex: Index of the local variable slot.
        """
        pass

    def Token(self, *__args):
        """
        Token(self: InstructionEncoder, handle: EntityHandle)
            Encodes a token.
        Token(self: InstructionEncoder, token: int)
            Encodes a token.
        """
        pass

    def __call__(self, *args): #cannot find CLR method
        """
        Call(self: InstructionEncoder, methodHandle: EntityHandle)
            Encodes call instruction and its operand.
        Call(self: InstructionEncoder, methodHandle: MethodDefinitionHandle)
            Encodes call instruction and its operand.
        Call(self: InstructionEncoder, methodHandle: MethodSpecificationHandle)
            Encodes call instruction and its operand.
        Call(self: InstructionEncoder, methodHandle: MemberReferenceHandle)
            Encodes call instruction and its operand.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, codeBuilder, controlFlowBuilder):
        """
        __new__(cls: type, codeBuilder: BlobBuilder, controlFlowBuilder: ControlFlowBuilder)
        __new__[InstructionEncoder]() -> InstructionEncoder
        """
        pass

    CodeBuilder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Underlying builder where encoded instructions are written to.

Get: CodeBuilder(self: InstructionEncoder) -> BlobBuilder

"""

    ControlFlowBuilder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Builder tracking labels, branches and exception handlers.

Get: ControlFlowBuilder(self: InstructionEncoder) -> ControlFlowBuilder

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Offset of the next encoded instruction.

Get: Offset(self: InstructionEncoder) -> int

"""



class LabelHandle(object, IEquatable[LabelHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: LabelHandle, other: LabelHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        Equals(self: LabelHandle, obj: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: LabelHandle) -> int """
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

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """1-based id identifying the label within the context of a System.Reflection.Metadata.Ecma335.ControlFlowBuilder.

Get: Id(self: LabelHandle) -> int

"""

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: LabelHandle) -> bool

"""



class LiteralEncoder(object):
    """
    Provides methods for encoding literals.
    
    LiteralEncoder(builder: BlobBuilder)
    """
    def Scalar(self):
        """
        Scalar(self: LiteralEncoder) -> ScalarEncoder
        
            Returns the encoder used to encode the literal value.
            Returns: The encoder of the literal value.
        """
        pass

    def TaggedScalar(self, type, scalar):
        """
        TaggedScalar(self: LiteralEncoder) -> (CustomAttributeElementTypeEncoder, ScalarEncoder)
        
            Returns a pair of encoders that must be used to encode the type and value of a literal in the order they appear in the parameter list.
        TaggedScalar(self: LiteralEncoder, type: Action[CustomAttributeElementTypeEncoder], scalar: Action[ScalarEncoder])
        """
        pass

    def TaggedVector(self, arrayType, vector):
        """
        TaggedVector(self: LiteralEncoder) -> (CustomAttributeArrayTypeEncoder, VectorEncoder)
        
            Returns a pair of encoders that must be used to encode the type and the items of a vector literal in the order they appear in the parameter list.
        TaggedVector(self: LiteralEncoder, arrayType: Action[CustomAttributeArrayTypeEncoder], vector: Action[VectorEncoder])
        """
        pass

    def Vector(self):
        """
        Vector(self: LiteralEncoder) -> VectorEncoder
        
            Gets a vector encoder used to encode the items of a vector.
            Returns: A vector encoder used to encode the items of a vector.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[LiteralEncoder]() -> LiteralEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: LiteralEncoder) -> BlobBuilder

"""



class LiteralsEncoder(object):
    """ LiteralsEncoder(builder: BlobBuilder) """
    def AddLiteral(self):
        """ AddLiteral(self: LiteralsEncoder) -> LiteralEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[LiteralsEncoder]() -> LiteralsEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: LiteralsEncoder) -> BlobBuilder

"""



class LocalVariablesEncoder(object):
    """ LocalVariablesEncoder(builder: BlobBuilder) """
    def AddVariable(self):
        """ AddVariable(self: LocalVariablesEncoder) -> LocalVariableTypeEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[LocalVariablesEncoder]() -> LocalVariablesEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: LocalVariablesEncoder) -> BlobBuilder

"""



class LocalVariableTypeEncoder(object):
    """ LocalVariableTypeEncoder(builder: BlobBuilder) """
    def CustomModifiers(self):
        """ CustomModifiers(self: LocalVariableTypeEncoder) -> CustomModifiersEncoder """
        pass

    def Type(self, isByRef, isPinned):
        """ Type(self: LocalVariableTypeEncoder, isByRef: bool, isPinned: bool) -> SignatureTypeEncoder """
        pass

    def TypedReference(self):
        """ TypedReference(self: LocalVariableTypeEncoder) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[LocalVariableTypeEncoder]() -> LocalVariableTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: LocalVariableTypeEncoder) -> BlobBuilder

"""



class MetadataAggregator(object):
    """
    MetadataAggregator(baseReader: MetadataReader, deltaReaders: IReadOnlyList[MetadataReader])
    MetadataAggregator(baseTableRowCounts: IReadOnlyList[int], baseHeapSizes: IReadOnlyList[int], deltaReaders: IReadOnlyList[MetadataReader])
    """
    def GetGenerationHandle(self, handle, generation):
        """
        GetGenerationHandle(self: MetadataAggregator, handle: Handle) -> (Handle, int)
        
            Calculates the handle of the entity within the metadata generation it is defined in, given a handle of an entity in an aggregate metadata.
        
            handle: Handle of an entity in an aggregate metadata.
            Returns: Handle of the entity within the metadata generation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, baseReader: MetadataReader, deltaReaders: IReadOnlyList[MetadataReader])
        __new__(cls: type, baseTableRowCounts: IReadOnlyList[int], baseHeapSizes: IReadOnlyList[int], deltaReaders: IReadOnlyList[MetadataReader])
        """
        pass


class MetadataBuilder(object):
    """
    The MetadataBuilder class reads and writes metadata for an assembly in a highly performant manner. It is designed for use by compilers and other assembly generation tools.
    
    MetadataBuilder(userStringHeapStartOffset: int, stringHeapStartOffset: int, blobHeapStartOffset: int, guidHeapStartOffset: int)
    """
    def AddAssembly(self, name, version, culture, publicKey, flags, hashAlgorithm):
        """ AddAssembly(self: MetadataBuilder, name: StringHandle, version: Version, culture: StringHandle, publicKey: BlobHandle, flags: AssemblyFlags, hashAlgorithm: AssemblyHashAlgorithm) -> AssemblyDefinitionHandle """
        pass

    def AddAssemblyFile(self, name, hashValue, containsMetadata):
        """ AddAssemblyFile(self: MetadataBuilder, name: StringHandle, hashValue: BlobHandle, containsMetadata: bool) -> AssemblyFileHandle """
        pass

    def AddAssemblyReference(self, name, version, culture, publicKeyOrToken, flags, hashValue):
        """ AddAssemblyReference(self: MetadataBuilder, name: StringHandle, version: Version, culture: StringHandle, publicKeyOrToken: BlobHandle, flags: AssemblyFlags, hashValue: BlobHandle) -> AssemblyReferenceHandle """
        pass

    def AddConstant(self, parent, value):
        """
        AddConstant(self: MetadataBuilder, parent: EntityHandle, value: object) -> ConstantHandle
        
            Adds a default value for a parameter, field or property.
        
            parent: The parent entity handle, which can be one of the following: System.Reflection.Metadata.ParameterHandle, System.Reflection.Metadata.FieldDefinitionHandle, or 
             System.Reflection.Metadata.PropertyDefinitionHandle.
        
            value: The constant value.
            Returns: A handle to the added constant.
        """
        pass

    def AddCustomAttribute(self, parent, constructor, value):
        """
        AddCustomAttribute(self: MetadataBuilder, parent: EntityHandle, constructor: EntityHandle, value: BlobHandle) -> CustomAttributeHandle
        
            Adds a custom attribute.
        
            parent: An entity to attach the custom attribute to: a System.Reflection.Metadata.MethodDefinitionHandle, System.Reflection.Metadata.FieldDefinitionHandle, 
             System.Reflection.Metadata.TypeReferenceHandle, System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.ParameterHandle, 
             System.Reflection.Metadata.InterfaceImplementationHandle, System.Reflection.Metadata.MemberReferenceHandle, System.Reflection.Metadata.ModuleDefinitionHandle, 
             System.Reflection.Metadata.DeclarativeSecurityAttributeHandle, System.Reflection.Metadata.PropertyDefinitionHandle, System.Reflection.Metadata.EventDefinitionHandle, 
             System.Reflection.Metadata.StandaloneSignatureHandle, System.Reflection.Metadata.ModuleReferenceHandle, System.Reflection.Metadata.TypeSpecificationHandle, 
             System.Reflection.Metadata.AssemblyDefinitionHandle, System.Reflection.Metadata.AssemblyReferenceHandle, System.Reflection.Metadata.AssemblyFileHandle, 
             System.Reflection.Metadata.ExportedTypeHandle, System.Reflection.Metadata.ManifestResourceHandle, System.Reflection.Metadata.GenericParameterHandle, 
             System.Reflection.Metadata.GenericParameterConstraintHandle, or a System.Reflection.Metadata.MethodSpecificationHandle.
        
            constructor: A custom attribute constructor: a System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle.
            value: A custom attribute value blob.
            Returns: A handle to the added custom attribute.
        """
        pass

    def AddCustomDebugInformation(self, parent, kind, value):
        """
        AddCustomDebugInformation(self: MetadataBuilder, parent: EntityHandle, kind: GuidHandle, value: BlobHandle) -> CustomDebugInformationHandle
        
            Adds custom debug information.
        
            parent: An entity to attach the debug information to: a System.Reflection.Metadata.MethodDefinitionHandle, System.Reflection.Metadata.FieldDefinitionHandle, 
             System.Reflection.Metadata.TypeReferenceHandle, System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.ParameterHandle, 
             System.Reflection.Metadata.InterfaceImplementationHandle, System.Reflection.Metadata.MemberReferenceHandle, System.Reflection.Metadata.ModuleDefinitionHandle, 
             System.Reflection.Metadata.DeclarativeSecurityAttributeHandle, System.Reflection.Metadata.PropertyDefinitionHandle, System.Reflection.Metadata.EventDefinitionHandle, 
             System.Reflection.Metadata.StandaloneSignatureHandle, System.Reflection.Metadata.ModuleReferenceHandle, System.Reflection.Metadata.TypeSpecificationHandle, 
             System.Reflection.Metadata.AssemblyDefinitionHandle, System.Reflection.Metadata.AssemblyReferenceHandle, System.Reflection.Metadata.AssemblyFileHandle, 
             System.Reflection.Metadata.ExportedTypeHandle, System.Reflection.Metadata.ManifestResourceHandle, System.Reflection.Metadata.GenericParameterHandle, 
             System.Reflection.Metadata.GenericParameterConstraintHandle, System.Reflection.Metadata.MethodSpecificationHandle, System.Reflection.Metadata.DocumentHandle, 
             System.Reflection.Metadata.LocalScopeHandle, System.Reflection.Metadata.LocalVariableHandle, System.Reflection.Metadata.LocalConstantHandle, or a 
             System.Reflection.Metadata.ImportScopeHandle.
        
            kind: The information kind. Determines the structure of the value blob.
            value: The custom debug information blob.
            Returns: A handle to the added custom debug information.
        """
        pass

    def AddDeclarativeSecurityAttribute(self, parent, action, permissionSet):
        """
        AddDeclarativeSecurityAttribute(self: MetadataBuilder, parent: EntityHandle, action: DeclarativeSecurityAction, permissionSet: BlobHandle) -> DeclarativeSecurityAttributeHandle
        
            Adds a declarative security attribute to a type, method, or assembly.
        
            parent: The parent entity handle, which can be one of the following: a System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.MethodDefinitionHandle, or a 
             System.Reflection.Metadata.AssemblyDefinitionHandle.
        
            action: A declarative security action.
            permissionSet: The permission set blob.
            Returns: A handle to the added declarative security attribute.
        """
        pass

    def AddDocument(self, name, hashAlgorithm, hash, language):
        """
        AddDocument(self: MetadataBuilder, name: BlobHandle, hashAlgorithm: GuidHandle, hash: BlobHandle, language: GuidHandle) -> DocumentHandle
        
            Adds document debug information.
        
            name: The document name blob.
            hashAlgorithm: THe GUID of the hash algorithm used to calculate the value of hash.
            hash: The hash of the document content.
            language: The GUID of the language.
            Returns: A handle to the added document.
        """
        pass

    def AddEncLogEntry(self, entity, code):
        """ AddEncLogEntry(self: MetadataBuilder, entity: EntityHandle, code: EditAndContinueOperation) """
        pass

    def AddEncMapEntry(self, entity):
        """ AddEncMapEntry(self: MetadataBuilder, entity: EntityHandle) """
        pass

    def AddEvent(self, attributes, name, type):
        """
        AddEvent(self: MetadataBuilder, attributes: EventAttributes, name: StringHandle, type: EntityHandle) -> EventDefinitionHandle
        
            Adds an event definition.
        
            attributes: The event attributes.
            name: The event name.
            type: The type of the event: a System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, or System.Reflection.Metadata.TypeSpecificationHandle.
            Returns: A handle to the added event definition.
        """
        pass

    def AddEventMap(self, declaringType, eventList):
        """ AddEventMap(self: MetadataBuilder, declaringType: TypeDefinitionHandle, eventList: EventDefinitionHandle) """
        pass

    def AddExportedType(self, attributes, namespace, name, implementation, typeDefinitionId):
        """
        AddExportedType(self: MetadataBuilder, attributes: TypeAttributes, namespace: StringHandle, name: StringHandle, implementation: EntityHandle, typeDefinitionId: int) -> ExportedTypeHandle
        
            Adds an exported type.
        
            attributes: The type attributes.
            namespace: The type namespace.
            name: The type name.
            implementation: The implementation entity handle, which can be one of the following: an System.Reflection.Metadata.AssemblyFileHandle, System.Reflection.Metadata.ExportedTypeHandle, or 
             System.Reflection.Metadata.AssemblyReferenceHandle.
        
            typeDefinitionId: The type definition ID.
            Returns: A handle to the added exported type.
        """
        pass

    def AddFieldDefinition(self, attributes, name, signature):
        """
        AddFieldDefinition(self: MetadataBuilder, attributes: FieldAttributes, name: StringHandle, signature: BlobHandle) -> FieldDefinitionHandle
        
            Adds a field definition.
        
            attributes: The field attributes.
            name: The field name.
            signature: The field signature. Use System.Reflection.Metadata.Ecma335.BlobEncoder.FieldSignature to construct the blob.
            Returns: A handle to the added field definition.
        """
        pass

    def AddFieldLayout(self, field, offset):
        """
        AddFieldLayout(self: MetadataBuilder, field: FieldDefinitionHandle, offset: int)
            Defines a field layout of a field definition.
        
            field: The field definition handle.
            offset: The byte offset of the field within the declaring type instance.
        """
        pass

    def AddFieldRelativeVirtualAddress(self, field, offset):
        """
        AddFieldRelativeVirtualAddress(self: MetadataBuilder, field: FieldDefinitionHandle, offset: int)
            Adds a mapping from a field to its initial value stored in the PE image.
        
            field: The field definition handle.
            offset: The offset within the block in the PE image that stores initial values of mapped fields (usually in the .text section).
        """
        pass

    def AddGenericParameter(self, parent, attributes, name, index):
        """
        AddGenericParameter(self: MetadataBuilder, parent: EntityHandle, attributes: GenericParameterAttributes, name: StringHandle, index: int) -> GenericParameterHandle
        
            Adds a generic parameter definition.
        
            parent: The parent entity handle, which can be either a System.Reflection.Metadata.TypeDefinitionHandle or System.Reflection.Metadata.MethodDefinitionHandle.
            attributes: The generic parameter attributes.
            name: The parameter name.
            index: The zero-based parameter index.
            Returns: A handle to the added generic parameter.
        """
        pass

    def AddGenericParameterConstraint(self, genericParameter, constraint):
        """
        AddGenericParameterConstraint(self: MetadataBuilder, genericParameter: GenericParameterHandle, constraint: EntityHandle) -> GenericParameterConstraintHandle
        
            Adds a type constraint to a generic parameter.
        
            genericParameter: The generic parameter to constrain.
            constraint: The type constraint, which can be one of the following: a System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle or a 
             System.Reflection.Metadata.TypeSpecificationHandle.
        
            Returns: A handle to the added generic parameter constraint.
        """
        pass

    def AddImportScope(self, parentScope, imports):
        """
        AddImportScope(self: MetadataBuilder, parentScope: ImportScopeHandle, imports: BlobHandle) -> ImportScopeHandle
        
            Adds local scope debug information.
        
            parentScope: The parent scope handle.
            imports: The import scope handle.
            Returns: A handle to the added import scope.
        """
        pass

    def AddInterfaceImplementation(self, type, implementedInterface):
        """
        AddInterfaceImplementation(self: MetadataBuilder, type: TypeDefinitionHandle, implementedInterface: EntityHandle) -> InterfaceImplementationHandle
        
            Adds an interface implementation to a type.
        
            type: The type implementing the interface.
            implementedInterface: The interface being implemented, which can be one of the following: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, or 
             System.Reflection.Metadata.TypeSpecificationHandle.
        
            Returns: A handle to the added interface implementation.
        """
        pass

    def AddLocalConstant(self, name, signature):
        """
        AddLocalConstant(self: MetadataBuilder, name: StringHandle, signature: BlobHandle) -> LocalConstantHandle
        
            Adds local constant debug information.
        
            name: The name of the variable.
            signature: The LocalConstantSig blob.
            Returns: A handle to the added local constant.
        """
        pass

    def AddLocalScope(self, method, importScope, variableList, constantList, startOffset, length):
        """
        AddLocalScope(self: MetadataBuilder, method: MethodDefinitionHandle, importScope: ImportScopeHandle, variableList: LocalVariableHandle, constantList: LocalConstantHandle, startOffset: int, length: int) -> LocalScopeHandle
        
            Adds local scope debug information.
        
            method: The containing method.
            importScope: The handle of the associated import scope.
            variableList: If the scope declares variables, set this to the handle of the first one. Otherwise, set this to the handle of the first variable declared by the next scope definition. If no scope 
             defines any variables, stem.Reflection.Metadata.Ecma335.MetadataTokens.LocalVariableHandle(1).
        
            constantList: If the scope declares constants, set this the handle of the first one. Otherwise, set this to the handle of the first constant declared by the next scope definition. If no scope 
             defines any constants, stem.Reflection.Metadata.Ecma335.MetadataTokens.LocalConstantHandle(1).
        
            startOffset: The offset of the first instruction covered by the scope.
            length: The length (in bytes) of the scope.
            Returns: A handle to the added local scope.
        """
        pass

    def AddLocalVariable(self, attributes, index, name):
        """
        AddLocalVariable(self: MetadataBuilder, attributes: LocalVariableAttributes, index: int, name: StringHandle) -> LocalVariableHandle
        
            Adds local variable debug information.
        
            attributes: The local variable attributes.
            index: The zero-base index of the local variable in the local signature.
            name: The name of the variable.
            Returns: A handle to the added local variable.
        """
        pass

    def AddManifestResource(self, attributes, name, implementation, offset):
        """
        AddManifestResource(self: MetadataBuilder, attributes: ManifestResourceAttributes, name: StringHandle, implementation: EntityHandle, offset: UInt32) -> ManifestResourceHandle
        
            Adds a manifest resource.
        
            attributes: The manifest resource attributes.
            name: The name of the manifest resource.
            implementation: The implementation entity handle, which can be one of the following: System.Reflection.Metadata.AssemblyFileHandle, System.Reflection.Metadata.AssemblyReferenceHandle, or ll.
            offset: Specifies the byte offset within the referenced file at which this resource record begins.
            Returns: A handle to the added manifest resource.
        """
        pass

    def AddMarshallingDescriptor(self, parent, descriptor):
        """
        AddMarshallingDescriptor(self: MetadataBuilder, parent: EntityHandle, descriptor: BlobHandle)
            Adds marshalling information to a field or a parameter.
        
            parent: The parent entity handle, which can be one of the following: System.Reflection.Metadata.ParameterHandle or System.Reflection.Metadata.FieldDefinitionHandle.
            descriptor: The descriptor blob.
        """
        pass

    def AddMemberReference(self, parent, name, signature):
        """
        AddMemberReference(self: MetadataBuilder, parent: EntityHandle, name: StringHandle, signature: BlobHandle) -> MemberReferenceHandle
        
            Adds a MemberRef table row.
        
            parent: The containing entity, which can be one of the following: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, 
             System.Reflection.Metadata.ModuleReferenceHandle, System.Reflection.Metadata.MethodDefinitionHandle, or System.Reflection.Metadata.TypeSpecificationHandle.
        
            name: The member name.
            signature: The member signature.
            Returns: A handle to the added member reference.
        """
        pass

    def AddMethodDebugInformation(self, document, sequencePoints):
        """
        AddMethodDebugInformation(self: MetadataBuilder, document: DocumentHandle, sequencePoints: BlobHandle) -> MethodDebugInformationHandle
        
            Adds method debug information.
        
            document: The handle of a single document containing all sequence points of the method, or ll if the method doesn't have sequence points or spans multiple documents.
            sequencePoints: The sequence Points blob, or ll if the method doesn't have sequence points.
            Returns: A handle to the added method debug information.
        """
        pass

    def AddMethodDefinition(self, attributes, implAttributes, name, signature, bodyOffset, parameterList):
        """
        AddMethodDefinition(self: MetadataBuilder, attributes: MethodAttributes, implAttributes: MethodImplAttributes, name: StringHandle, signature: BlobHandle, bodyOffset: int, parameterList: ParameterHandle) -> MethodDefinitionHandle
        
            Adds a method definition.
        
            attributes: The method attributes.
            implAttributes: The method implementation attributes.
            name: The method name.
            signature: The method signature.
            bodyOffset: Offset within the block in the PE image that stores method bodies (the IL stream), or -1 if the method doesn't have a body.
            parameterList: If the method declares parameters in the Params table, set this to the handle of the first one. Otherwise, set this to the handle of the first parameter declared by the next method 
             definition. If no parameters are declared in the module, stem.Reflection.Metadata.Ecma335.MetadataTokens.ParameterHandle(1).
        
            Returns: A handle to the added method definition.
        """
        pass

    def AddMethodImplementation(self, type, methodBody, methodDeclaration):
        """
        AddMethodImplementation(self: MetadataBuilder, type: TypeDefinitionHandle, methodBody: EntityHandle, methodDeclaration: EntityHandle) -> MethodImplementationHandle
        
            Defines an implementation for a method declaration within a type.
        
            type: The type definition.
            methodBody: The method body entity handle, which can be one of the following: System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle.
            methodDeclaration: The method declaration entity handle, which can be one of the following: System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle.
            Returns: A handle to the added method implementation.
        """
        pass

    def AddMethodImport(self, method, attributes, name, module):
        """
        AddMethodImport(self: MetadataBuilder, method: MethodDefinitionHandle, attributes: MethodImportAttributes, name: StringHandle, module: ModuleReferenceHandle)
            Adds import information to a method definition.
        
            method: The method definition handle.
            attributes: The method import attributes.
            name: The unmanaged method name.
            module: The module containing the unmanaged method.
        """
        pass

    def AddMethodSemantics(self, association, semantics, methodDefinition):
        """
        AddMethodSemantics(self: MetadataBuilder, association: EntityHandle, semantics: MethodSemanticsAttributes, methodDefinition: MethodDefinitionHandle)
            Associates a method (a getter, a setter, an adder, etc.) with a property or an event.
        
            association: The association entity handle, which can be one of the following: System.Reflection.Metadata.EventDefinitionHandle or System.Reflection.Metadata.PropertyDefinitionHandle.
            semantics: The method semantics attributes.
            methodDefinition: The method definition.
        """
        pass

    def AddMethodSpecification(self, method, instantiation):
        """
        AddMethodSpecification(self: MetadataBuilder, method: EntityHandle, instantiation: BlobHandle) -> MethodSpecificationHandle
        
            Adds a method specification (an instantiation).
        
            method: The generic method entity handle, which can be one of the following: System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle.
            instantiation: The instantiation blob encoding the generic arguments of the method.
            Returns: A handle to the added method specification.
        """
        pass

    def AddModule(self, generation, moduleName, mvid, encId, encBaseId):
        """ AddModule(self: MetadataBuilder, generation: int, moduleName: StringHandle, mvid: GuidHandle, encId: GuidHandle, encBaseId: GuidHandle) -> ModuleDefinitionHandle """
        pass

    def AddModuleReference(self, moduleName):
        """ AddModuleReference(self: MetadataBuilder, moduleName: StringHandle) -> ModuleReferenceHandle """
        pass

    def AddNestedType(self, type, enclosingType):
        """
        AddNestedType(self: MetadataBuilder, type: TypeDefinitionHandle, enclosingType: TypeDefinitionHandle)
            Defines a nesting relationship to specified type definitions.
        
            type: The nested type definition handle.
            enclosingType: The enclosing type definition handle.
        """
        pass

    def AddParameter(self, attributes, name, sequenceNumber):
        """
        AddParameter(self: MetadataBuilder, attributes: ParameterAttributes, name: StringHandle, sequenceNumber: int) -> ParameterHandle
        
            Adds a parameter definition.
        
            attributes: The parameter attributes.
            name: Optional. The parameter name.
            sequenceNumber: The sequence number of the parameter. A value of 0 refers to the owner method's return type; its parameters are then numbered from 1 onward.
            Returns: A handle to the added parameter.
        """
        pass

    def AddProperty(self, attributes, name, signature):
        """
        AddProperty(self: MetadataBuilder, attributes: PropertyAttributes, name: StringHandle, signature: BlobHandle) -> PropertyDefinitionHandle
        
            Adds a property definition.
        
            attributes: The property attributes.
            name: The property name.
            signature: The signature of the property.
            Returns: A handle to the added property definition.
        """
        pass

    def AddPropertyMap(self, declaringType, propertyList):
        """ AddPropertyMap(self: MetadataBuilder, declaringType: TypeDefinitionHandle, propertyList: PropertyDefinitionHandle) """
        pass

    def AddStandaloneSignature(self, signature):
        """ AddStandaloneSignature(self: MetadataBuilder, signature: BlobHandle) -> StandaloneSignatureHandle """
        pass

    def AddStateMachineMethod(self, moveNextMethod, kickoffMethod):
        """
        AddStateMachineMethod(self: MetadataBuilder, moveNextMethod: MethodDefinitionHandle, kickoffMethod: MethodDefinitionHandle)
            Adds state machine method debug information.
        
            moveNextMethod: The handle of the veNext method of the state machine (the compiler-generated method).
            kickoffMethod: The handle of the kickoff method (the user defined iterator/async method).
        """
        pass

    def AddTypeDefinition(self, attributes, namespace, name, baseType, fieldList, methodList):
        """
        AddTypeDefinition(self: MetadataBuilder, attributes: TypeAttributes, namespace: StringHandle, name: StringHandle, baseType: EntityHandle, fieldList: FieldDefinitionHandle, methodList: MethodDefinitionHandle) -> TypeDefinitionHandle
        
            Adds a type definition.
        
            attributes: The type attributes.
            namespace: The type namespace.
            name: The type name.
            baseType: The base type entity handle, which can be one of the following: System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, 
             System.Reflection.Metadata.TypeSpecificationHandle, or ll.
        
            fieldList: If the type declares fields, set this to the handle of the first one. Otherwise, set this to the handle of the first field declared by the next type definition. If no type defines 
             any fields in the module, stem.Reflection.Metadata.Ecma335.MetadataTokens.FieldDefinitionHandle(1).
        
            methodList: If the type declares methods, the handle of the first one. Otherwise, the handle of the first method declared by the next type definition. If no type defines any methods in the 
             module, stem.Reflection.Metadata.Ecma335.MetadataTokens.MethodDefinitionHandle(1).
        
            Returns: A handle to the added type definition.
        """
        pass

    def AddTypeLayout(self, type, packingSize, size):
        """
        AddTypeLayout(self: MetadataBuilder, type: TypeDefinitionHandle, packingSize: UInt16, size: UInt32)
            Defines a type layout of a type definition.
        
            type: The type definition.
            packingSize: Specifies that fields should be placed within the type instance at byte addresses which are a multiple of packingSize, or at natural alignment for that field type, whichever is 
             smaller. Its value should be one of the following: 0, 1, 2, 4, 8, 16, 32, 64, or 128. A value of zero indicates that the packing size used should match the default for the current 
             platform.
        
            size: Indicates a minimum size of the type instance and is intended to allow for padding. The amount of memory allocated is the maximum of the size calculated from the layout and size. 
             Note that if this directive applies to a value type, then the size will be less than 1 MB.
        """
        pass

    def AddTypeReference(self, resolutionScope, namespace, name):
        """
        AddTypeReference(self: MetadataBuilder, resolutionScope: EntityHandle, namespace: StringHandle, name: StringHandle) -> TypeReferenceHandle
        
            Adds a type reference.
        
            resolutionScope: The entity declaring the target type, which can be one of the following: System.Reflection.Metadata.ModuleDefinitionHandle, System.Reflection.Metadata.ModuleReferenceHandle, 
             System.Reflection.Metadata.AssemblyReferenceHandle, System.Reflection.Metadata.TypeReferenceHandle, or ll.
        
            namespace: The type reference namespace.
            name: The type reference name.
            Returns: A handle to the added type reference.
        """
        pass

    def AddTypeSpecification(self, signature):
        """ AddTypeSpecification(self: MetadataBuilder, signature: BlobHandle) -> TypeSpecificationHandle """
        pass

    def GetOrAddBlob(self, value):
        """
        GetOrAddBlob(self: MetadataBuilder, value: BlobBuilder) -> BlobHandle
        
            Adds the specified blob from an immutable byte array to the Blob heap, if it's not there already.
        
            value: The blob builder instance containing the blob.
            Returns: A handle to the added or existing blob.
        GetOrAddBlob(self: MetadataBuilder, value: Array[Byte]) -> BlobHandle
        
            Adds the specified blob to the Blob heap, if it's not there already.
        
            value: The array containing the blob.
            Returns: A handle to the added or existing blob.
        GetOrAddBlob(self: MetadataBuilder, value: ImmutableArray[Byte]) -> BlobHandle
        """
        pass

    def GetOrAddBlobUTF16(self, value):
        """
        GetOrAddBlobUTF16(self: MetadataBuilder, value: str) -> BlobHandle
        
            Encodes a string using UTF16 encoding to a blob and adds it to the Blob heap, if it's not there already.
        
            value: The string to add.
            Returns: A handle to the added or existing blob.
        """
        pass

    def GetOrAddBlobUTF8(self, value, allowUnpairedSurrogates):
        """
        GetOrAddBlobUTF8(self: MetadataBuilder, value: str, allowUnpairedSurrogates: bool) -> BlobHandle
        
            Encodes a string using UTF8 encoding to a blob and adds it to the Blob heap, if it's not there already.
        
            value: The value to add.
            allowUnpairedSurrogates: ue to encode the unpaired surrogates as specified; lse to replace them with the U+FFFD character.
            Returns: A handle to the added or existing blob.
        """
        pass

    def GetOrAddConstantBlob(self, value):
        """
        GetOrAddConstantBlob(self: MetadataBuilder, value: object) -> BlobHandle
        
            Encodes a constant value to a blob and adds it to the Blob heap, if it's not there already. Uses UTF16 to encode string constants.
        
            value: The constant value to add.
            Returns: A handle to the added or existing blob.
        """
        pass

    def GetOrAddDocumentName(self, value):
        """
        GetOrAddDocumentName(self: MetadataBuilder, value: str) -> BlobHandle
        
            Encodes a debug document name and adds it to the Blob heap, if it's not there already.
        
            value: The document name to add.
            Returns: A handle to the added or existing document name blob.
        """
        pass

    def GetOrAddGuid(self, guid):
        """
        GetOrAddGuid(self: MetadataBuilder, guid: Guid) -> GuidHandle
        
            Adds the specified Guid to the Guid heap, if it's not there already.
        
            guid: The Guid to add.
            Returns: A handle to the added or existing Guid.
        """
        pass

    def GetOrAddString(self, value):
        """
        GetOrAddString(self: MetadataBuilder, value: str) -> StringHandle
        
            Adds the specified string to the string heap, if it's not there already.
        
            value: The string to add.
            Returns: A handle to the added or existing string.
        """
        pass

    def GetOrAddUserString(self, value):
        """
        GetOrAddUserString(self: MetadataBuilder, value: str) -> UserStringHandle
        
            Adds the specified string to the user string heap, if it's not there already.
        
            value: The string to add.
            Returns: A handle to the added or existing string. This value may be used in System.Reflection.Metadata.Ecma335.InstructionEncoder.LoadString(System.Reflection.Metadata.UserStringHandle).
        """
        pass

    def GetRowCount(self, table):
        """
        GetRowCount(self: MetadataBuilder, table: TableIndex) -> int
        
            Returns the current number of items in the specified table.
        
            table: The table index.
            Returns: The number of items in the table.
        """
        pass

    def GetRowCounts(self):
        """
        GetRowCounts(self: MetadataBuilder) -> ImmutableArray[int]
        
            Returns the current number of items in each table.
            Returns: An array of size System.Reflection.Metadata.Ecma335.MetadataTokens.TableCount, with each item filled with the current row count of the corresponding table.
        """
        pass

    def ReserveGuid(self):
        """
        ReserveGuid(self: MetadataBuilder) -> ReservedBlob[GuidHandle]
        
            Reserves space on the Guid heap for a GUID.
            Returns: A handle to the reserved Guid and a System.Reflection.Metadata.Blob representing the GUID blob as stored on the heap.
        """
        pass

    def ReserveUserString(self, length):
        """
        ReserveUserString(self: MetadataBuilder, length: int) -> ReservedBlob[UserStringHandle]
        
            Reserves space on the user string heap for a string of the specified length.
        
            length: The number of characters to reserve.
            Returns: A handle to the reserved user string and a System.Reflection.Metadata.Blob representing the entire User String blob (including its length and terminal character). The handle may be 
             used in System.Reflection.Metadata.Ecma335.InstructionEncoder.LoadString(System.Reflection.Metadata.UserStringHandle).
         Use 
             System.Reflection.Metadata.BlobWriter.WriteUserString(System.String) to fill in the blob content.
        """
        pass

    def SetCapacity(self, *__args):
        """
        SetCapacity(self: MetadataBuilder, table: TableIndex, rowCount: int)
            Sets the capacity of the specified table.
        
            table: The table index.
            rowCount: The number of rows in the table.
        SetCapacity(self: MetadataBuilder, heap: HeapIndex, byteCount: int)
            Sets the capacity of the specified heap.
        
            heap: The heap index.
            byteCount: The number of bytes.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, userStringHeapStartOffset, stringHeapStartOffset, blobHeapStartOffset, guidHeapStartOffset):
        """ __new__(cls: type, userStringHeapStartOffset: int, stringHeapStartOffset: int, blobHeapStartOffset: int, guidHeapStartOffset: int) """
        pass


class MetadataReaderExtensions(object):
    """ Provides extension methods for working with certain raw elements of the ECMA-335 metadata tables and heaps. """
    @staticmethod
    def GetEditAndContinueLogEntries(reader):
        """
        GetEditAndContinueLogEntries(reader: MetadataReader) -> IEnumerable[EditAndContinueLogEntry]
        
            Enumerates entries of EnC log.
        """
        pass

    @staticmethod
    def GetEditAndContinueMapEntries(reader):
        """
        GetEditAndContinueMapEntries(reader: MetadataReader) -> IEnumerable[EntityHandle]
        
            Enumerates entries of EnC map.
        """
        pass

    @staticmethod
    def GetHeapMetadataOffset(reader, heapIndex):
        """
        GetHeapMetadataOffset(reader: MetadataReader, heapIndex: HeapIndex) -> int
        
            Returns the offset from the start of metadata to the specified heap.
        """
        pass

    @staticmethod
    def GetHeapSize(reader, heapIndex):
        """
        GetHeapSize(reader: MetadataReader, heapIndex: HeapIndex) -> int
        
            Returns the size of the specified heap.
        """
        pass

    @staticmethod
    def GetNextHandle(reader, handle):
        """
        GetNextHandle(reader: MetadataReader, handle: UserStringHandle) -> UserStringHandle
        
            Returns the a handle to the UserString that follows the given one in the UserString heap or a nil handle if it is the last one.
        GetNextHandle(reader: MetadataReader, handle: BlobHandle) -> BlobHandle
        
            Returns the handle to the System.Reflection.Metadata.Blob that follows the given one in the System.Reflection.Metadata.Blob heap or a nil handle if it is the last one.
        GetNextHandle(reader: MetadataReader, handle: StringHandle) -> StringHandle
        
            Returns the a handle to the string that follows the given one in the string heap, or a nil handle if it is the last one.
        """
        pass

    @staticmethod
    def GetTableMetadataOffset(reader, tableIndex):
        """
        GetTableMetadataOffset(reader: MetadataReader, tableIndex: TableIndex) -> int
        
            Returns the offset from the start of metadata to the specified table.
        """
        pass

    @staticmethod
    def GetTableRowCount(reader, tableIndex):
        """
        GetTableRowCount(reader: MetadataReader, tableIndex: TableIndex) -> int
        
            Returns the number of rows in the specified table.
        """
        pass

    @staticmethod
    def GetTableRowSize(reader, tableIndex):
        """
        GetTableRowSize(reader: MetadataReader, tableIndex: TableIndex) -> int
        
            Returns the size of a row in the specified table.
        """
        pass

    @staticmethod
    def GetTypesWithEvents(reader):
        """
        GetTypesWithEvents(reader: MetadataReader) -> IEnumerable[TypeDefinitionHandle]
        
            Enumerate types that define one or more events.
            Returns: The resulting sequence corresponds exactly to entries in EventMap table, i.e. n-th returned System.Reflection.Metadata.TypeDefinitionHandle is stored in n-th row of EventMap.
        """
        pass

    @staticmethod
    def GetTypesWithProperties(reader):
        """
        GetTypesWithProperties(reader: MetadataReader) -> IEnumerable[TypeDefinitionHandle]
        
            Enumerate types that define one or more properties.
            Returns: The resulting sequence corresponds exactly to entries in the property map table, that is, the n-th returned System.Reflection.Metadata.TypeDefinitionHandle is stored in n-th row of 
             the property map.
        """
        pass

    @staticmethod
    def ResolveSignatureTypeKind(reader, typeHandle, rawTypeKind):
        """
        ResolveSignatureTypeKind(reader: MetadataReader, typeHandle: EntityHandle, rawTypeKind: Byte) -> SignatureTypeKind
        
            Given a type handle and a raw type kind found in a signature blob determines whether the target type is a value type or a reference type.
        """
        pass

    __all__ = [
        'GetEditAndContinueLogEntries',
        'GetEditAndContinueMapEntries',
        'GetHeapMetadataOffset',
        'GetHeapSize',
        'GetNextHandle',
        'GetTableMetadataOffset',
        'GetTableRowCount',
        'GetTableRowSize',
        'GetTypesWithEvents',
        'GetTypesWithProperties',
        'ResolveSignatureTypeKind',
    ]


class MetadataRootBuilder(object):
    """
    Builder of a Metadata Root to be embedded in a Portable Executable image.
    
    MetadataRootBuilder(tablesAndHeaps: MetadataBuilder, metadataVersion: str, suppressValidation: bool)
    """
    def Serialize(self, builder, methodBodyStreamRva, mappedFieldDataStreamRva):
        """
        Serialize(self: MetadataRootBuilder, builder: BlobBuilder, methodBodyStreamRva: int, mappedFieldDataStreamRva: int)
            Serializes metadata root content into the given System.Reflection.Metadata.BlobBuilder.
        
            builder: Builder to write to.
            methodBodyStreamRva: The relative virtual address of the start of the method body stream. Used to calculate the final value of RVA fields of MethodDef table.
            mappedFieldDataStreamRva: The relative virtual address of the start of the field init data stream. Used to calculate the final value of RVA fields of FieldRVA table.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tablesAndHeaps, metadataVersion, suppressValidation):
        """ __new__(cls: type, tablesAndHeaps: MetadataBuilder, metadataVersion: str, suppressValidation: bool) """
        pass

    MetadataVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The metadata version.

Get: MetadataVersion(self: MetadataRootBuilder) -> str

"""

    Sizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns sizes of various metadata structures.

Get: Sizes(self: MetadataRootBuilder) -> MetadataSizes

"""

    SuppressValidation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Determines if basic validation of metadata tables should be suppressed. The validation verifies that entries in the tables were added in order required by the ECMA specification. It does not enforce all specification requirements on metadata tables.

Get: SuppressValidation(self: MetadataRootBuilder) -> bool

"""



class MetadataSizes(object):
    """ Provides information on sizes of various metadata structures. """
    def GetAlignedHeapSize(self, index):
        """
        GetAlignedHeapSize(self: MetadataSizes, index: HeapIndex) -> int
        
            Returns aligned size of the specified heap.
        """
        pass

    ExternalRowCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """External table row count.

Get: ExternalRowCounts(self: MetadataSizes) -> ImmutableArray[int]

"""

    HeapSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Exact (unaligned) heap sizes.

Get: HeapSizes(self: MetadataSizes) -> ImmutableArray[int]

"""

    RowCounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Table row counts.

Get: RowCounts(self: MetadataSizes) -> ImmutableArray[int]

"""



class MetadataTokens(object):
    # no doc
    @staticmethod
    def AssemblyFileHandle(rowNumber):
        """ AssemblyFileHandle(rowNumber: int) -> AssemblyFileHandle """
        pass

    @staticmethod
    def AssemblyReferenceHandle(rowNumber):
        """ AssemblyReferenceHandle(rowNumber: int) -> AssemblyReferenceHandle """
        pass

    @staticmethod
    def BlobHandle(offset):
        """ BlobHandle(offset: int) -> BlobHandle """
        pass

    @staticmethod
    def ConstantHandle(rowNumber):
        """ ConstantHandle(rowNumber: int) -> ConstantHandle """
        pass

    @staticmethod
    def CustomAttributeHandle(rowNumber):
        """ CustomAttributeHandle(rowNumber: int) -> CustomAttributeHandle """
        pass

    @staticmethod
    def CustomDebugInformationHandle(rowNumber):
        """ CustomDebugInformationHandle(rowNumber: int) -> CustomDebugInformationHandle """
        pass

    @staticmethod
    def DeclarativeSecurityAttributeHandle(rowNumber):
        """ DeclarativeSecurityAttributeHandle(rowNumber: int) -> DeclarativeSecurityAttributeHandle """
        pass

    @staticmethod
    def DocumentHandle(rowNumber):
        """ DocumentHandle(rowNumber: int) -> DocumentHandle """
        pass

    @staticmethod
    def DocumentNameBlobHandle(offset):
        """ DocumentNameBlobHandle(offset: int) -> DocumentNameBlobHandle """
        pass

    @staticmethod
    def EntityHandle(*__args):
        """
        EntityHandle(token: int) -> EntityHandle
        
            Creates an entity handle from a token value.
        EntityHandle(tableIndex: TableIndex, rowNumber: int) -> EntityHandle
        
            Creates an System.Reflection.Metadata.EntityHandle from a token value.
        """
        pass

    @staticmethod
    def EventDefinitionHandle(rowNumber):
        """ EventDefinitionHandle(rowNumber: int) -> EventDefinitionHandle """
        pass

    @staticmethod
    def ExportedTypeHandle(rowNumber):
        """ ExportedTypeHandle(rowNumber: int) -> ExportedTypeHandle """
        pass

    @staticmethod
    def FieldDefinitionHandle(rowNumber):
        """ FieldDefinitionHandle(rowNumber: int) -> FieldDefinitionHandle """
        pass

    @staticmethod
    def GenericParameterConstraintHandle(rowNumber):
        """ GenericParameterConstraintHandle(rowNumber: int) -> GenericParameterConstraintHandle """
        pass

    @staticmethod
    def GenericParameterHandle(rowNumber):
        """ GenericParameterHandle(rowNumber: int) -> GenericParameterHandle """
        pass

    @staticmethod
    def GetHeapOffset(*__args):
        """
        GetHeapOffset(reader: MetadataReader, handle: Handle) -> int
        
            Gets the offset of metadata heap data that corresponds to the specified handle in the context of reader.
            Returns: Zero based offset, or -1 if handle isn't a metadata heap handle.
        GetHeapOffset(handle: Handle) -> int
        
            Gets the offset of metadata heap data that corresponds to the specified handle.
            Returns: An offset in the corresponding heap, or -1 if handle can only be interpreted in a context of a specific System.Reflection.Metadata.MetadataReader or 
             System.Reflection.Metadata.Ecma335.MetadataBuilder.
        
        GetHeapOffset(handle: BlobHandle) -> int
        
            Gets the offset of metadata heap data that corresponds to the specified handle.
            Returns: Zero based offset, or -1 if handle can only be interpreted in a context of a specific System.Reflection.Metadata.MetadataReader or System.Reflection.Metadata.Ecma335.MetadataBuilder.
        GetHeapOffset(handle: GuidHandle) -> int
        
            Gets the offset of metadata heap data that corresponds to the specified handle.
            Returns: 1-based index into the #Guid heap. Unlike other heaps, which are essentially byte arrays, the #Guid heap is an array of 16-byte GUIDs.
        GetHeapOffset(handle: UserStringHandle) -> int
        
            Gets the offset of metadata heap data that corresponds to the specified handle.
            Returns: Zero-based offset.
        GetHeapOffset(handle: StringHandle) -> int
        
            Gets the offset of metadata heap data that corresponds to the specified handle.
            Returns: Zero-based offset, or -1 if handle can only be interpreted in a context of a specific System.Reflection.Metadata.MetadataReader or System.Reflection.Metadata.Ecma335.MetadataBuilder.
        """
        pass

    @staticmethod
    def GetRowNumber(*__args):
        """
        GetRowNumber(reader: MetadataReader, handle: EntityHandle) -> int
        
            Gets the row number of a metadata table entry that corresponds to the specified handle in the context of reader.
            Returns: One based row number.
        GetRowNumber(handle: EntityHandle) -> int
        
            Gets the row number of a metadata table entry that corresponds to the specified handle.
            Returns: One based row number, or -1 if handle can only be interpreted in a context of a specific System.Reflection.Metadata.MetadataReader.
         See 
             System.Reflection.Metadata.Ecma335.MetadataTokens.GetRowNumber(System.Reflection.Metadata.MetadataReader,System.Reflection.Metadata.EntityHandle).
        """
        pass

    @staticmethod
    def GetToken(*__args):
        """
        GetToken(reader: MetadataReader, handle: EntityHandle) -> int
        
            Gets the metadata token of the specified handle in the context of reader.
            Returns: Metadata token.
        GetToken(reader: MetadataReader, handle: Handle) -> int
        
            Gets the metadata token of the specified handle in the context of reader.
            Returns: Metadata token.
        GetToken(handle: Handle) -> int
        
            Gets the metadata token of the specified handle.
            Returns: Metadata token, or 0 if handle can only be interpreted in a context of a specific System.Reflection.Metadata.MetadataReader.
        GetToken(handle: EntityHandle) -> int
        
            Gets the metadata token of the specified handle.
            Returns: Metadata token, or 0 if handle can only be interpreted in a context of a specific System.Reflection.Metadata.MetadataReader.
        """
        pass

    @staticmethod
    def GuidHandle(offset):
        """ GuidHandle(offset: int) -> GuidHandle """
        pass

    @staticmethod
    def Handle(*__args):
        """
        Handle(token: int) -> Handle
        
            Creates a handle from a token value.
        Handle(tableIndex: TableIndex, rowNumber: int) -> EntityHandle
        
            Creates an System.Reflection.Metadata.EntityHandle from a token value.
        """
        pass

    @staticmethod
    def ImportScopeHandle(rowNumber):
        """ ImportScopeHandle(rowNumber: int) -> ImportScopeHandle """
        pass

    @staticmethod
    def InterfaceImplementationHandle(rowNumber):
        """ InterfaceImplementationHandle(rowNumber: int) -> InterfaceImplementationHandle """
        pass

    @staticmethod
    def LocalConstantHandle(rowNumber):
        """ LocalConstantHandle(rowNumber: int) -> LocalConstantHandle """
        pass

    @staticmethod
    def LocalScopeHandle(rowNumber):
        """ LocalScopeHandle(rowNumber: int) -> LocalScopeHandle """
        pass

    @staticmethod
    def LocalVariableHandle(rowNumber):
        """ LocalVariableHandle(rowNumber: int) -> LocalVariableHandle """
        pass

    @staticmethod
    def ManifestResourceHandle(rowNumber):
        """ ManifestResourceHandle(rowNumber: int) -> ManifestResourceHandle """
        pass

    @staticmethod
    def MemberReferenceHandle(rowNumber):
        """ MemberReferenceHandle(rowNumber: int) -> MemberReferenceHandle """
        pass

    @staticmethod
    def MethodDebugInformationHandle(rowNumber):
        """ MethodDebugInformationHandle(rowNumber: int) -> MethodDebugInformationHandle """
        pass

    @staticmethod
    def MethodDefinitionHandle(rowNumber):
        """ MethodDefinitionHandle(rowNumber: int) -> MethodDefinitionHandle """
        pass

    @staticmethod
    def MethodImplementationHandle(rowNumber):
        """ MethodImplementationHandle(rowNumber: int) -> MethodImplementationHandle """
        pass

    @staticmethod
    def MethodSpecificationHandle(rowNumber):
        """ MethodSpecificationHandle(rowNumber: int) -> MethodSpecificationHandle """
        pass

    @staticmethod
    def ModuleReferenceHandle(rowNumber):
        """ ModuleReferenceHandle(rowNumber: int) -> ModuleReferenceHandle """
        pass

    @staticmethod
    def ParameterHandle(rowNumber):
        """ ParameterHandle(rowNumber: int) -> ParameterHandle """
        pass

    @staticmethod
    def PropertyDefinitionHandle(rowNumber):
        """ PropertyDefinitionHandle(rowNumber: int) -> PropertyDefinitionHandle """
        pass

    @staticmethod
    def StandaloneSignatureHandle(rowNumber):
        """ StandaloneSignatureHandle(rowNumber: int) -> StandaloneSignatureHandle """
        pass

    @staticmethod
    def StringHandle(offset):
        """ StringHandle(offset: int) -> StringHandle """
        pass

    @staticmethod
    def TryGetHeapIndex(type, index):
        """
        TryGetHeapIndex(type: HandleKind) -> (bool, HeapIndex)
        
            Gets the System.Reflection.Metadata.Ecma335.HeapIndex of the heap corresponding to the specified System.Reflection.Metadata.HandleKind.
        
            type: Handle type.
            Returns: ue if the handle type corresponds to an Ecma335 heap; lse otherwise.
        """
        pass

    @staticmethod
    def TryGetTableIndex(type, index):
        """
        TryGetTableIndex(type: HandleKind) -> (bool, TableIndex)
        
            Gets the System.Reflection.Metadata.Ecma335.TableIndex of the table corresponding to the specified System.Reflection.Metadata.HandleKind.
        
            type: Handle type.
            Returns: ue if the handle type corresponds to an Ecma335 or Portable PDB table; lse otherwise.
        """
        pass

    @staticmethod
    def TypeDefinitionHandle(rowNumber):
        """ TypeDefinitionHandle(rowNumber: int) -> TypeDefinitionHandle """
        pass

    @staticmethod
    def TypeReferenceHandle(rowNumber):
        """ TypeReferenceHandle(rowNumber: int) -> TypeReferenceHandle """
        pass

    @staticmethod
    def TypeSpecificationHandle(rowNumber):
        """ TypeSpecificationHandle(rowNumber: int) -> TypeSpecificationHandle """
        pass

    @staticmethod
    def UserStringHandle(offset):
        """ UserStringHandle(offset: int) -> UserStringHandle """
        pass

    HeapCount = 4
    TableCount = 64
    __all__ = [
        'AssemblyFileHandle',
        'AssemblyReferenceHandle',
        'BlobHandle',
        'ConstantHandle',
        'CustomAttributeHandle',
        'CustomDebugInformationHandle',
        'DeclarativeSecurityAttributeHandle',
        'DocumentHandle',
        'DocumentNameBlobHandle',
        'EntityHandle',
        'EventDefinitionHandle',
        'ExportedTypeHandle',
        'FieldDefinitionHandle',
        'GenericParameterConstraintHandle',
        'GenericParameterHandle',
        'GetHeapOffset',
        'GetRowNumber',
        'GetToken',
        'GuidHandle',
        'Handle',
        'HeapCount',
        'ImportScopeHandle',
        'InterfaceImplementationHandle',
        'LocalConstantHandle',
        'LocalScopeHandle',
        'LocalVariableHandle',
        'ManifestResourceHandle',
        'MemberReferenceHandle',
        'MethodDebugInformationHandle',
        'MethodDefinitionHandle',
        'MethodImplementationHandle',
        'MethodSpecificationHandle',
        'ModuleReferenceHandle',
        'ParameterHandle',
        'PropertyDefinitionHandle',
        'StandaloneSignatureHandle',
        'StringHandle',
        'TableCount',
        'TryGetHeapIndex',
        'TryGetTableIndex',
        'TypeDefinitionHandle',
        'TypeReferenceHandle',
        'TypeSpecificationHandle',
        'UserStringHandle',
    ]


class MethodBodyAttributes(Enum, IComparable, IFormattable, IConvertible):
    """
    Defines method body attributes.
    
    enum (flags) MethodBodyAttributes, values: InitLocals (1), None (0)
    """
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

    InitLocals = None
    None = None
    value__ = None


class MethodBodyStreamEncoder(object):
    """
    Provides an encoder for a method body stream.
    
    MethodBodyStreamEncoder(builder: BlobBuilder)
    """
    def AddMethodBody(self, *__args):
        """
        AddMethodBody(self: MethodBodyStreamEncoder, codeSize: int, maxStack: int, exceptionRegionCount: int, hasSmallExceptionRegions: bool, localVariablesSignature: StandaloneSignatureHandle, attributes: MethodBodyAttributes) -> MethodBody
        
            Encodes a method body and adds it to the method body stream, using the provided code size, maximum stack size, number of exception regions, local variables' signature handle, method 
             body attributes and allowing to indicate whether the exception regions should be encoded in small format or not.
        
        
            codeSize: The number of bytes to be reserved for instructions.
            maxStack: The maximum stack size.
            exceptionRegionCount: The number of exception regions.
            hasSmallExceptionRegions: ue if the exception regions should be encoded in small format; lse otherwise.
            localVariablesSignature: The local variables' signature handle.
            attributes: The method body attributes.
            Returns: The offset of the encoded body within the method body stream.
        AddMethodBody(self: MethodBodyStreamEncoder, codeSize: int, maxStack: int, exceptionRegionCount: int, hasSmallExceptionRegions: bool, localVariablesSignature: StandaloneSignatureHandle, attributes: MethodBodyAttributes, hasDynamicStackAllocation: bool) -> MethodBody
        
            Encodes a method body and adds it to the method body stream, using the provided code size, maximum stack size, number of exception regions, local variables' signature handle, method 
             body attributes, allowing to indicate whether the exception regions should be encoded in small format or not, and allowing to indicate whether the method should allocate from the 
             dynamic local memory pool or not.
        
        
            codeSize: The number of bytes to be reserved for instructions.
            maxStack: The maximum stack size.
            exceptionRegionCount: The number of exception regions.
            hasSmallExceptionRegions: ue if the exception regions should be encoded in small format; lse otherwise.
            localVariablesSignature: The local variables' signature handle.
            attributes: The method body attributes.
            hasDynamicStackAllocation: ue if the method allocates from the dynamic local memory pool (the calloc instruction); lse otherwise.
            Returns: The offset of the encoded body within the method body stream.
        AddMethodBody(self: MethodBodyStreamEncoder, instructionEncoder: InstructionEncoder, maxStack: int, localVariablesSignature: StandaloneSignatureHandle, attributes: MethodBodyAttributes) -> int
        
            Encodes a method body and adds it to the method body stream.
        
            instructionEncoder: The instruction encoder.
            maxStack: The maximum stack size.
            localVariablesSignature: The local variables' signature handle.
            attributes: The method body attributes.
            Returns: The offset of the encoded body within the method body stream.
        AddMethodBody(self: MethodBodyStreamEncoder, instructionEncoder: InstructionEncoder, maxStack: int, localVariablesSignature: StandaloneSignatureHandle, attributes: MethodBodyAttributes, hasDynamicStackAllocation: bool) -> int
        
            Encodes a method body and adds it to the method body stream, using the provided instruction encoder, maximum stack size, local variables' signature handle, method body attributes, 
             and allowing to indicate whether the method should allocate from the dynamic local memory pool or not.
        
        
            instructionEncoder: The instruction encoder.
            maxStack: The maximum stack size.
            localVariablesSignature: The local variables' signature handle.
            attributes: The method body attributes.
            hasDynamicStackAllocation: ue if the method allocates from the dynamic local memory pool (the IL contains the calloc instruction); lse otherwise.
            Returns: The offset of the encoded body within the method body stream.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[MethodBodyStreamEncoder]() -> MethodBodyStreamEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: MethodBodyStreamEncoder) -> BlobBuilder

"""


    MethodBody = None


class MethodSignatureEncoder(object):
    """
    Provides an encoder for method signatures.
    
    MethodSignatureEncoder(builder: BlobBuilder, hasVarArgs: bool)
    """
    def Parameters(self, parameterCount, returnType, parameters):
        """
        Parameters(self: MethodSignatureEncoder, parameterCount: int) -> (ReturnTypeEncoder, ParametersEncoder)
        
            Encodes the provided return type and parameters, which must be used in the order they appear in the parameter list.
        
            parameterCount: The number of parameters.
        Parameters(self: MethodSignatureEncoder, parameterCount: int, returnType: Action[ReturnTypeEncoder], parameters: Action[ParametersEncoder])
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder, hasVarArgs):
        """
        __new__(cls: type, builder: BlobBuilder, hasVarArgs: bool)
        __new__[MethodSignatureEncoder]() -> MethodSignatureEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: MethodSignatureEncoder) -> BlobBuilder

"""

    HasVarArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasVarArgs(self: MethodSignatureEncoder) -> bool

"""



class NamedArgumentsEncoder(object):
    """ NamedArgumentsEncoder(builder: BlobBuilder) """
    def AddArgument(self, isField, type, name, literal):
        """
        AddArgument(self: NamedArgumentsEncoder, isField: bool) -> (NamedArgumentTypeEncoder, NameEncoder, LiteralEncoder)
        
            Encodes a named argument (a field or property) and returns three encoders that must be used in the order they appear in the parameter list.
        
            isField: ue to encode a field, lse to encode a property.
        AddArgument(self: NamedArgumentsEncoder, isField: bool, type: Action[NamedArgumentTypeEncoder], name: Action[NameEncoder], literal: Action[LiteralEncoder])
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[NamedArgumentsEncoder]() -> NamedArgumentsEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: NamedArgumentsEncoder) -> BlobBuilder

"""



class NamedArgumentTypeEncoder(object):
    """ NamedArgumentTypeEncoder(builder: BlobBuilder) """
    def Object(self):
        """ Object(self: NamedArgumentTypeEncoder) """
        pass

    def ScalarType(self):
        """ ScalarType(self: NamedArgumentTypeEncoder) -> CustomAttributeElementTypeEncoder """
        pass

    def SZArray(self):
        """ SZArray(self: NamedArgumentTypeEncoder) -> CustomAttributeArrayTypeEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[NamedArgumentTypeEncoder]() -> NamedArgumentTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: NamedArgumentTypeEncoder) -> BlobBuilder

"""



class NameEncoder(object):
    """ NameEncoder(builder: BlobBuilder) """
    def Name(self, name):
        """ Name(self: NameEncoder, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[NameEncoder]() -> NameEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: NameEncoder) -> BlobBuilder

"""



class ParametersEncoder(object):
    """ ParametersEncoder(builder: BlobBuilder, hasVarArgs: bool) """
    def AddParameter(self):
        """ AddParameter(self: ParametersEncoder) -> ParameterTypeEncoder """
        pass

    def StartVarArgs(self):
        """ StartVarArgs(self: ParametersEncoder) -> ParametersEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder, hasVarArgs):
        """
        __new__(cls: type, builder: BlobBuilder, hasVarArgs: bool)
        __new__[ParametersEncoder]() -> ParametersEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: ParametersEncoder) -> BlobBuilder

"""

    HasVarArgs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasVarArgs(self: ParametersEncoder) -> bool

"""



class ParameterTypeEncoder(object):
    """ ParameterTypeEncoder(builder: BlobBuilder) """
    def CustomModifiers(self):
        """ CustomModifiers(self: ParameterTypeEncoder) -> CustomModifiersEncoder """
        pass

    def Type(self, isByRef):
        """ Type(self: ParameterTypeEncoder, isByRef: bool) -> SignatureTypeEncoder """
        pass

    def TypedReference(self):
        """ TypedReference(self: ParameterTypeEncoder) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[ParameterTypeEncoder]() -> ParameterTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: ParameterTypeEncoder) -> BlobBuilder

"""



class PermissionSetEncoder(object):
    """ PermissionSetEncoder(builder: BlobBuilder) """
    def AddPermission(self, typeName, encodedArguments):
        """
        AddPermission(self: PermissionSetEncoder, typeName: str, encodedArguments: ImmutableArray[Byte]) -> PermissionSetEncoder
        AddPermission(self: PermissionSetEncoder, typeName: str, encodedArguments: BlobBuilder) -> PermissionSetEncoder
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[PermissionSetEncoder]() -> PermissionSetEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: PermissionSetEncoder) -> BlobBuilder

"""



class PortablePdbBuilder(object):
    """
    Represents the builder of a Portable PDB image.
    
    PortablePdbBuilder(tablesAndHeaps: MetadataBuilder, typeSystemRowCounts: ImmutableArray[int], entryPoint: MethodDefinitionHandle, idProvider: Func[IEnumerable[Blob], BlobContentId])
    """
    def Serialize(self, builder):
        """
        Serialize(self: PortablePdbBuilder, builder: BlobBuilder) -> BlobContentId
        
            Serializes portable PDB content into the given System.Reflection.Metadata.BlobBuilder.
        
            builder: The builder to write to.
            Returns: The ID of the serialized content.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tablesAndHeaps, typeSystemRowCounts, entryPoint, idProvider):
        """ __new__(cls: type, tablesAndHeaps: MetadataBuilder, typeSystemRowCounts: ImmutableArray[int], entryPoint: MethodDefinitionHandle, idProvider: Func[IEnumerable[Blob], BlobContentId]) """
        pass

    FormatVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormatVersion(self: PortablePdbBuilder) -> UInt16

"""

    IdProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdProvider(self: PortablePdbBuilder) -> Func[IEnumerable[Blob], BlobContentId]

"""

    MetadataVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataVersion(self: PortablePdbBuilder) -> str

"""



class ReturnTypeEncoder(object):
    """ ReturnTypeEncoder(builder: BlobBuilder) """
    def CustomModifiers(self):
        """ CustomModifiers(self: ReturnTypeEncoder) -> CustomModifiersEncoder """
        pass

    def Type(self, isByRef):
        """ Type(self: ReturnTypeEncoder, isByRef: bool) -> SignatureTypeEncoder """
        pass

    def TypedReference(self):
        """ TypedReference(self: ReturnTypeEncoder) """
        pass

    def Void(self):
        """ Void(self: ReturnTypeEncoder) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[ReturnTypeEncoder]() -> ReturnTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: ReturnTypeEncoder) -> BlobBuilder

"""



class ScalarEncoder(object):
    """ ScalarEncoder(builder: BlobBuilder) """
    def Constant(self, value):
        """
        Constant(self: ScalarEncoder, value: object)
            Encodes a constant literal.
        
            value: A constant of type System.Boolean, System.Byte, System.SByte, System.Int16, System.UInt16, System.Int32, System.UInt32, System.Int64, System.UInt64, System.Single, System.Double, 
             System.Char (encoded as a two-byte Unicode character), System.String (encoded as SerString), or System.Enum (encoded as the underlying integer value).
        """
        pass

    def NullArray(self):
        """
        NullArray(self: ScalarEncoder)
            Encodes a ll literal of type System.Array.
        """
        pass

    def SystemType(self, serializedTypeName):
        """
        SystemType(self: ScalarEncoder, serializedTypeName: str)
            Encodes a literal of type System.Type (which can possibly be ll).
        
            serializedTypeName: The name of the type, or ll.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[ScalarEncoder]() -> ScalarEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: ScalarEncoder) -> BlobBuilder

"""



class SignatureDecoder(object):
    """ SignatureDecoder[TType, TGenericContext](provider: ISignatureTypeProvider[TType, TGenericContext], metadataReader: MetadataReader, genericContext: TGenericContext) """
    def DecodeFieldSignature(self, blobReader):
        """
        DecodeFieldSignature(self: SignatureDecoder[TType, TGenericContext], blobReader: BlobReader) -> (TType, BlobReader)
        
            Decodes a field signature blob and advances the reader past the signature.
        
            blobReader: The blob reader positioned at a field signature.
            Returns: The decoded field type.
        """
        pass

    def DecodeLocalSignature(self, blobReader):
        """
        DecodeLocalSignature(self: SignatureDecoder[TType, TGenericContext], blobReader: BlobReader) -> (ImmutableArray[TType], BlobReader)
        
            Decodes a local variable signature blob and advances the reader past the signature.
        
            blobReader: The blob reader positioned at a local variable signature.
            Returns: The local variable types.
        """
        pass

    def DecodeMethodSignature(self, blobReader):
        """
        DecodeMethodSignature(self: SignatureDecoder[TType, TGenericContext], blobReader: BlobReader) -> (MethodSignature[TType], BlobReader)
        
            Decodes a method (definition, reference, or standalone) or a property signature blob.
        
            blobReader: A blob reader positioned at a method signature.
            Returns: The decoded method signature.
        """
        pass

    def DecodeMethodSpecificationSignature(self, blobReader):
        """
        DecodeMethodSpecificationSignature(self: SignatureDecoder[TType, TGenericContext], blobReader: BlobReader) -> (ImmutableArray[TType], BlobReader)
        
            Decodes a method specification signature blob and advances the reader past the signature.
        
            blobReader: A blob reader positioned at a valid method specification signature.
            Returns: The types used to instantiate a generic method via the method specification.
        """
        pass

    def DecodeType(self, blobReader, allowTypeSpecifications):
        """
        DecodeType(self: SignatureDecoder[TType, TGenericContext], blobReader: BlobReader, allowTypeSpecifications: bool) -> (TType, BlobReader)
        
            Decodes a type embedded in a signature and advances the reader past the type.
        
            blobReader: The blob reader positioned at the leading System.Reflection.Metadata.SignatureTypeCode.
            allowTypeSpecifications: ue to allow a System.Reflection.Metadata.TypeSpecificationHandle to follow a (CLASS | VALUETYPE) in the signature; lse otherwise.
            Returns: The decoded type.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, provider, metadataReader, genericContext):
        """
        __new__(cls: type, provider: ISignatureTypeProvider[TType, TGenericContext], metadataReader: MetadataReader, genericContext: TGenericContext)
        __new__[SignatureDecoder`2]() -> SignatureDecoder[TType, TGenericContext]
        """
        pass


class SignatureTypeEncoder(object):
    """ SignatureTypeEncoder(builder: BlobBuilder) """
    def Array(self, elementType, arrayShape):
        """
        Array(self: SignatureTypeEncoder) -> (SignatureTypeEncoder, ArrayShapeEncoder)
        
            Encodes an array type. Returns a pair of encoders that must be used in the order they appear in the parameter list.
        Array(self: SignatureTypeEncoder, elementType: Action[SignatureTypeEncoder], arrayShape: Action[ArrayShapeEncoder])
        """
        pass

    def Boolean(self):
        """ Boolean(self: SignatureTypeEncoder) """
        pass

    def Byte(self):
        """ Byte(self: SignatureTypeEncoder) """
        pass

    def Char(self):
        """ Char(self: SignatureTypeEncoder) """
        pass

    def CustomModifiers(self):
        """
        CustomModifiers(self: SignatureTypeEncoder) -> CustomModifiersEncoder
        
            Starts a signature of a type with custom modifiers.
        """
        pass

    def Double(self):
        """ Double(self: SignatureTypeEncoder) """
        pass

    def FunctionPointer(self, convention, attributes, genericParameterCount):
        """
        FunctionPointer(self: SignatureTypeEncoder, convention: SignatureCallingConvention, attributes: FunctionPointerAttributes, genericParameterCount: int) -> MethodSignatureEncoder
        
            Starts a function pointer signature.
        
            convention: Calling convention.
            attributes: Function pointer attributes.
            genericParameterCount: Generic parameter count.
        """
        pass

    def GenericInstantiation(self, genericType, genericArgumentCount, isValueType):
        """
        GenericInstantiation(self: SignatureTypeEncoder, genericType: EntityHandle, genericArgumentCount: int, isValueType: bool) -> GenericTypeArgumentsEncoder
        
            Starts a generic instantiation signature.
        
            genericType: System.Reflection.Metadata.TypeDefinitionHandle or System.Reflection.Metadata.TypeReferenceHandle.
            genericArgumentCount: Generic argument count.
            isValueType: ue to mark the type as value type, lse to mark it as a reference type in the signature.
        """
        pass

    def GenericMethodTypeParameter(self, parameterIndex):
        """
        GenericMethodTypeParameter(self: SignatureTypeEncoder, parameterIndex: int)
            Encodes a reference to type parameter of a containing generic method.
        
            parameterIndex: Parameter index.
        """
        pass

    def GenericTypeParameter(self, parameterIndex):
        """
        GenericTypeParameter(self: SignatureTypeEncoder, parameterIndex: int)
            Encodes a reference to type parameter of a containing generic type.
        
            parameterIndex: Parameter index.
        """
        pass

    def Int16(self):
        """ Int16(self: SignatureTypeEncoder) """
        pass

    def Int32(self):
        """ Int32(self: SignatureTypeEncoder) """
        pass

    def Int64(self):
        """ Int64(self: SignatureTypeEncoder) """
        pass

    def IntPtr(self):
        """ IntPtr(self: SignatureTypeEncoder) """
        pass

    def Object(self):
        """ Object(self: SignatureTypeEncoder) """
        pass

    def Pointer(self):
        """
        Pointer(self: SignatureTypeEncoder) -> SignatureTypeEncoder
        
            Starts pointer signature.
        """
        pass

    def PrimitiveType(self, type):
        """
        PrimitiveType(self: SignatureTypeEncoder, type: PrimitiveTypeCode)
            Writes primitive type code.
        
            type: Any primitive type code except for System.Reflection.Metadata.PrimitiveTypeCode.TypedReference and System.Reflection.Metadata.PrimitiveTypeCode.Void.
        """
        pass

    def SByte(self):
        """ SByte(self: SignatureTypeEncoder) """
        pass

    def Single(self):
        """ Single(self: SignatureTypeEncoder) """
        pass

    def String(self):
        """ String(self: SignatureTypeEncoder) """
        pass

    def SZArray(self):
        """
        SZArray(self: SignatureTypeEncoder) -> SignatureTypeEncoder
        
            Starts SZ array (vector) signature.
        """
        pass

    def Type(self, type, isValueType):
        """
        Type(self: SignatureTypeEncoder, type: EntityHandle, isValueType: bool)
            Encodes a reference to a type.
        
            type: System.Reflection.Metadata.TypeDefinitionHandle or System.Reflection.Metadata.TypeReferenceHandle.
            isValueType: ue to mark the type as value type, lse to mark it as a reference type in the signature.
        """
        pass

    def UInt16(self):
        """ UInt16(self: SignatureTypeEncoder) """
        pass

    def UInt32(self):
        """ UInt32(self: SignatureTypeEncoder) """
        pass

    def UInt64(self):
        """ UInt64(self: SignatureTypeEncoder) """
        pass

    def UIntPtr(self):
        """ UIntPtr(self: SignatureTypeEncoder) """
        pass

    def VoidPointer(self):
        """
        VoidPointer(self: SignatureTypeEncoder)
            Encodes a void pointer (void*).
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[SignatureTypeEncoder]() -> SignatureTypeEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: SignatureTypeEncoder) -> BlobBuilder

"""



class TableIndex(Enum, IComparable, IFormattable, IConvertible):
    """ enum TableIndex, values: Assembly (32), AssemblyOS (34), AssemblyProcessor (33), AssemblyRef (35), AssemblyRefOS (37), AssemblyRefProcessor (36), ClassLayout (15), Constant (11), CustomAttribute (12), CustomDebugInformation (55), DeclSecurity (14), Document (48), EncLog (30), EncMap (31), Event (20), EventMap (18), EventPtr (19), ExportedType (39), Field (4), FieldLayout (16), FieldMarshal (13), FieldPtr (3), FieldRva (29), File (38), GenericParam (42), GenericParamConstraint (44), ImplMap (28), ImportScope (53), InterfaceImpl (9), LocalConstant (52), LocalScope (50), LocalVariable (51), ManifestResource (40), MemberRef (10), MethodDebugInformation (49), MethodDef (6), MethodImpl (25), MethodPtr (5), MethodSemantics (24), MethodSpec (43), Module (0), ModuleRef (26), NestedClass (41), Param (8), ParamPtr (7), Property (23), PropertyMap (21), PropertyPtr (22), StandAloneSig (17), StateMachineMethod (54), TypeDef (2), TypeRef (1), TypeSpec (27) """
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

    Assembly = None
    AssemblyOS = None
    AssemblyProcessor = None
    AssemblyRef = None
    AssemblyRefOS = None
    AssemblyRefProcessor = None
    ClassLayout = None
    Constant = None
    CustomAttribute = None
    CustomDebugInformation = None
    DeclSecurity = None
    Document = None
    EncLog = None
    EncMap = None
    Event = None
    EventMap = None
    EventPtr = None
    ExportedType = None
    Field = None
    FieldLayout = None
    FieldMarshal = None
    FieldPtr = None
    FieldRva = None
    File = None
    GenericParam = None
    GenericParamConstraint = None
    ImplMap = None
    ImportScope = None
    InterfaceImpl = None
    LocalConstant = None
    LocalScope = None
    LocalVariable = None
    ManifestResource = None
    MemberRef = None
    MethodDebugInformation = None
    MethodDef = None
    MethodImpl = None
    MethodPtr = None
    MethodSemantics = None
    MethodSpec = None
    Module = None
    ModuleRef = None
    NestedClass = None
    Param = None
    ParamPtr = None
    Property = None
    PropertyMap = None
    PropertyPtr = None
    StandAloneSig = None
    StateMachineMethod = None
    TypeDef = None
    TypeRef = None
    TypeSpec = None
    value__ = None


class VectorEncoder(object):
    """ VectorEncoder(builder: BlobBuilder) """
    def Count(self, count):
        """ Count(self: VectorEncoder, count: int) -> LiteralsEncoder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builder):
        """
        __new__(cls: type, builder: BlobBuilder)
        __new__[VectorEncoder]() -> VectorEncoder
        """
        pass

    Builder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Builder(self: VectorEncoder) -> BlobBuilder

"""



