# encoding: utf-8
# module Microsoft.Diagnostics.Runtime.Implementation calls itself Implementation
# from Microsoft.Diagnostics.Runtime, Version=2.0.5.1201, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ClrmdAppDomain(ClrAppDomain):
    """
    ClrmdAppDomain(runtime: ClrRuntime, data: IAppDomainData)
    ClrmdAppDomain(runtime: ClrRuntime, helpers: IAppDomainHelpers, address: UInt64)
    """
    @staticmethod # known case of __new__
    def __new__(self, runtime, *__args):
        """
        __new__(cls: type, runtime: ClrRuntime, data: IAppDomainData)
        __new__(cls: type, runtime: ClrRuntime, helpers: IAppDomainHelpers, address: UInt64)
        """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ClrmdAppDomain) -> UInt64

"""

    ApplicationBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplicationBase(self: ClrmdAppDomain) -> str

"""

    ConfigurationFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationFile(self: ClrmdAppDomain) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ClrmdAppDomain) -> int

"""

    Modules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modules(self: ClrmdAppDomain) -> ImmutableArray[ClrModule]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdAppDomain) -> str

"""

    Runtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Runtime(self: ClrmdAppDomain) -> ClrRuntime

"""



class ClrmdType(ClrType, IEquatable[ClrType]):
    """ ClrmdType(heap: ClrHeap, baseType: ClrType, module: ClrModule, data: ITypeData, name: str) """
    def AsEnum(self):
        """ AsEnum(self: ClrmdType) -> ClrEnum """
        pass

    def EnumerateGenericParameters(self):
        """ EnumerateGenericParameters(self: ClrmdType) -> IEnumerable[ClrGenericParameter] """
        pass

    def EnumerateInterfaces(self):
        """ EnumerateInterfaces(self: ClrmdType) -> IEnumerable[ClrInterface] """
        pass

    @staticmethod
    def FixGenerics(name):
        """ FixGenerics(name: str) -> str """
        pass

    def GetArrayElementAddress(self, objRef, index):
        """ GetArrayElementAddress(self: ClrmdType, objRef: UInt64, index: int) -> UInt64 """
        pass

    def GetFieldByName(self, name):
        """ GetFieldByName(self: ClrmdType, name: str) -> ClrInstanceField """
        pass

    def GetStaticFieldByName(self, name):
        """ GetStaticFieldByName(self: ClrmdType, name: str) -> ClrStaticField """
        pass

    def IsFinalizeSuppressed(self, obj):
        """ IsFinalizeSuppressed(self: ClrmdType, obj: UInt64) -> bool """
        pass

    def ReadArrayElements(self, objRef, start, count):
        """ ReadArrayElements[T](self: ClrmdType, objRef: UInt64, start: int, count: int) -> Array[T] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, heap, baseType, module, data, name):
        """ __new__(cls: type, heap: ClrHeap, baseType: ClrType, module: ClrModule, data: ITypeData, name: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    AssemblyLoadContextAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyLoadContextAddress(self: ClrmdType) -> UInt64

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: ClrmdType) -> ClrType

"""

    ClrObjectHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClrObjectHelpers(self: ClrmdType) -> IClrObjectHelpers

"""

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: ClrmdType) -> int

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: ClrmdType) -> ClrType

"""

    ContainsPointers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsPointers(self: ClrmdType) -> bool

"""

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: ClrmdType) -> ClrElementType

"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fields(self: ClrmdType) -> ImmutableArray[ClrInstanceField]

"""

    GCDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCDesc(self: ClrmdType) -> GCDesc

"""

    Heap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Heap(self: ClrmdType) -> ClrHeap

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: ClrmdType) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArray(self: ClrmdType) -> bool

"""

    IsCollectible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCollectible(self: ClrmdType) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnum(self: ClrmdType) -> bool

"""

    IsException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsException(self: ClrmdType) -> bool

"""

    IsFinalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinalizable(self: ClrmdType) -> bool

"""

    IsFree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFree(self: ClrmdType) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInterface(self: ClrmdType) -> bool

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdType) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdType) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdType) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdType) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSealed(self: ClrmdType) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShared(self: ClrmdType) -> bool

"""

    IsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsString(self: ClrmdType) -> bool

"""

    LoaderAllocatorHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoaderAllocatorHandle(self: ClrmdType) -> UInt64

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: ClrmdType) -> int

"""

    Methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Methods(self: ClrmdType) -> ImmutableArray[ClrMethod]

"""

    MethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodTable(self: ClrmdType) -> UInt64

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: ClrmdType) -> ClrModule

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdType) -> str

"""

    Shared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shared(self: ClrmdType) -> bool

"""

    StaticFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticFields(self: ClrmdType) -> ImmutableArray[ClrStaticField]

"""

    StaticSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticSize(self: ClrmdType) -> int

"""



class ClrmdArrayType(ClrmdType, IEquatable[ClrType]):
    """ ClrmdArrayType(heap: ClrHeap, baseType: ClrType, module: ClrModule, data: ITypeData, name: str) """
    def GetArrayElementAddress(self, objRef, index):
        """ GetArrayElementAddress(self: ClrmdArrayType, objRef: UInt64, index: int) -> UInt64 """
        pass

    def ReadArrayElements(self, objRef, start, count):
        """ ReadArrayElements[T](self: ClrmdArrayType, objRef: UInt64, start: int, count: int) -> Array[T] """
        pass

    def SetComponentType(self, type):
        """ SetComponentType(self: ClrmdArrayType, type: ClrType) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, heap, baseType, module, data, name):
        """ __new__(cls: type, heap: ClrHeap, baseType: ClrType, module: ClrModule, data: ITypeData, name: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: ClrmdArrayType) -> int

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: ClrmdArrayType) -> ClrType

"""

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ClrmdConstructedType(ClrType, IEquatable[ClrType]):
    """ ClrmdConstructedType(componentType: ClrType, ranks: int, pointer: bool) """
    def AsEnum(self):
        """ AsEnum(self: ClrmdConstructedType) -> ClrEnum """
        pass

    def EnumerateInterfaces(self):
        """ EnumerateInterfaces(self: ClrmdConstructedType) -> IEnumerable[ClrInterface] """
        pass

    def GetArrayElementAddress(self, objRef, index):
        """ GetArrayElementAddress(self: ClrmdConstructedType, objRef: UInt64, index: int) -> UInt64 """
        pass

    def GetFieldByName(self, name):
        """ GetFieldByName(self: ClrmdConstructedType, name: str) -> ClrInstanceField """
        pass

    def GetStaticFieldByName(self, name):
        """ GetStaticFieldByName(self: ClrmdConstructedType, name: str) -> ClrStaticField """
        pass

    def IsFinalizeSuppressed(self, obj):
        """ IsFinalizeSuppressed(self: ClrmdConstructedType, obj: UInt64) -> bool """
        pass

    def ReadArrayElements(self, objRef, start, count):
        """ ReadArrayElements[T](self: ClrmdConstructedType, objRef: UInt64, start: int, count: int) -> Array[T] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, componentType, ranks, pointer):
        """ __new__(cls: type, componentType: ClrType, ranks: int, pointer: bool) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: ClrmdConstructedType) -> ClrType

"""

    ClrObjectHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClrObjectHelpers(self: ClrmdConstructedType) -> IClrObjectHelpers

"""

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: ClrmdConstructedType) -> int

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: ClrmdConstructedType) -> ClrType

"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: ClrmdConstructedType) -> ClrElementType

"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fields(self: ClrmdConstructedType) -> ImmutableArray[ClrInstanceField]

"""

    GCDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCDesc(self: ClrmdConstructedType) -> GCDesc

"""

    Heap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Heap(self: ClrmdConstructedType) -> ClrHeap

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: ClrmdConstructedType) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArray(self: ClrmdConstructedType) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnum(self: ClrmdConstructedType) -> bool

"""

    IsFinalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinalizable(self: ClrmdConstructedType) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInterface(self: ClrmdConstructedType) -> bool

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdConstructedType) -> bool

"""

    IsPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointer(self: ClrmdConstructedType) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdConstructedType) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdConstructedType) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdConstructedType) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSealed(self: ClrmdConstructedType) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShared(self: ClrmdConstructedType) -> bool

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: ClrmdConstructedType) -> int

"""

    Methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Methods(self: ClrmdConstructedType) -> ImmutableArray[ClrMethod]

"""

    MethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodTable(self: ClrmdConstructedType) -> UInt64

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: ClrmdConstructedType) -> ClrModule

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdConstructedType) -> str

"""

    StaticFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticFields(self: ClrmdConstructedType) -> ImmutableArray[ClrStaticField]

"""

    StaticSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticSize(self: ClrmdConstructedType) -> int

"""



class ClrmdDependentHandle(ClrHandle, IClrRoot):
    """ ClrmdDependentHandle(parent: ClrAppDomain, address: UInt64, obj: ClrObject, dependent: ClrObject) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parent, address, obj, dependent):
        """ __new__(cls: type, parent: ClrAppDomain, address: UInt64, obj: ClrObject, dependent: ClrObject) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ClrmdDependentHandle) -> UInt64

"""

    AppDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomain(self: ClrmdDependentHandle) -> ClrAppDomain

"""

    Dependent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dependent(self: ClrmdDependentHandle) -> ClrObject

"""

    HandleKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HandleKind(self: ClrmdDependentHandle) -> ClrHandleKind

"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: ClrmdDependentHandle) -> ClrObject

"""

    ReferenceCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceCount(self: ClrmdDependentHandle) -> UInt32

"""



class ClrmdField(ClrInstanceField):
    """ ClrmdField(containingType: ClrType, data: IFieldData) """
    def GetAddress(self, objRef, interior=None):
        """ GetAddress(self: ClrmdField, objRef: UInt64, interior: bool) -> UInt64 """
        pass

    def Read(self, objRef, interior):
        """ Read[T](self: ClrmdField, objRef: UInt64, interior: bool) -> T """
        pass

    def ReadObject(self, objRef, interior):
        """ ReadObject(self: ClrmdField, objRef: UInt64, interior: bool) -> ClrObject """
        pass

    def ReadString(self, objRef, interior):
        """ ReadString(self: ClrmdField, objRef: UInt64, interior: bool) -> str """
        pass

    def ReadStruct(self, objRef, interior):
        """ ReadStruct(self: ClrmdField, objRef: UInt64, interior: bool) -> ClrValueType """
        pass

    @staticmethod # known case of __new__
    def __new__(self, containingType, data):
        """ __new__(cls: type, containingType: ClrType, data: IFieldData) """
        pass

    ContainingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainingType(self: ClrmdField) -> ClrType

"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: ClrmdField) -> ClrElementType

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdField) -> bool

"""

    IsObjectReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsObjectReference(self: ClrmdField) -> bool

"""

    IsPrimitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrimitive(self: ClrmdField) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdField) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdField) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdField) -> bool

"""

    IsValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValueType(self: ClrmdField) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdField) -> str

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: ClrmdField) -> int

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: ClrmdField) -> int

"""

    Token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Token(self: ClrmdField) -> int

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ClrmdField) -> ClrType

"""



class ClrmdGenericType(ClrType, IEquatable[ClrType]):
    """
    This represents a ClrType for which we cannot get information from the dac.  In theory we shouldn't need this
                type, but in practice there are fields which do not report a type.  This allows us to provide a non-null, semi
                meaningful type even though it's not as accurate or specific as we wish it would be.
    
    ClrmdGenericType(helpers: IClrObjectHelpers, heap: ClrHeap, module: ClrModule, clrGenericParameter: ClrGenericParameter)
    """
    def AsEnum(self):
        """ AsEnum(self: ClrmdGenericType) -> ClrEnum """
        pass

    def EnumerateInterfaces(self):
        """ EnumerateInterfaces(self: ClrmdGenericType) -> IEnumerable[ClrInterface] """
        pass

    def GetArrayElementAddress(self, objRef, index):
        """ GetArrayElementAddress(self: ClrmdGenericType, objRef: UInt64, index: int) -> UInt64 """
        pass

    def GetFieldByName(self, name):
        """ GetFieldByName(self: ClrmdGenericType, name: str) -> ClrInstanceField """
        pass

    def GetStaticFieldByName(self, name):
        """ GetStaticFieldByName(self: ClrmdGenericType, name: str) -> ClrStaticField """
        pass

    def IsFinalizeSuppressed(self, obj):
        """ IsFinalizeSuppressed(self: ClrmdGenericType, obj: UInt64) -> bool """
        pass

    def ReadArrayElements(self, objRef, start, count):
        """ ReadArrayElements[T](self: ClrmdGenericType, objRef: UInt64, start: int, count: int) -> Array[T] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, helpers, heap, module, clrGenericParameter):
        """ __new__(cls: type, helpers: IClrObjectHelpers, heap: ClrHeap, module: ClrModule, clrGenericParameter: ClrGenericParameter) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: ClrmdGenericType) -> ClrType

"""

    ClrObjectHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClrObjectHelpers(self: ClrmdGenericType) -> IClrObjectHelpers

"""

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: ClrmdGenericType) -> int

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: ClrmdGenericType) -> ClrType

"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: ClrmdGenericType) -> ClrElementType

"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fields(self: ClrmdGenericType) -> ImmutableArray[ClrInstanceField]

"""

    GCDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCDesc(self: ClrmdGenericType) -> GCDesc

"""

    GenericParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenericParameter(self: ClrmdGenericType) -> ClrGenericParameter

"""

    Heap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Heap(self: ClrmdGenericType) -> ClrHeap

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: ClrmdGenericType) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArray(self: ClrmdGenericType) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnum(self: ClrmdGenericType) -> bool

"""

    IsFinalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinalizable(self: ClrmdGenericType) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInterface(self: ClrmdGenericType) -> bool

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdGenericType) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdGenericType) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdGenericType) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdGenericType) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSealed(self: ClrmdGenericType) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShared(self: ClrmdGenericType) -> bool

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: ClrmdGenericType) -> int

"""

    Methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Methods(self: ClrmdGenericType) -> ImmutableArray[ClrMethod]

"""

    MethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodTable(self: ClrmdGenericType) -> UInt64

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: ClrmdGenericType) -> ClrModule

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdGenericType) -> str

"""

    StaticFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticFields(self: ClrmdGenericType) -> ImmutableArray[ClrStaticField]

"""

    StaticSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticSize(self: ClrmdGenericType) -> int

"""



class ClrmdHandle(ClrHandle, IClrRoot):
    """ ClrmdHandle(parent: ClrAppDomain, address: UInt64, obj: ClrObject, kind: ClrHandleKind) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parent, address, obj, kind):
        """ __new__(cls: type, parent: ClrAppDomain, address: UInt64, obj: ClrObject, kind: ClrHandleKind) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ClrmdHandle) -> UInt64

"""

    AppDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomain(self: ClrmdHandle) -> ClrAppDomain

"""

    Dependent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dependent(self: ClrmdHandle) -> ClrObject

"""

    HandleKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HandleKind(self: ClrmdHandle) -> ClrHandleKind

"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: ClrmdHandle) -> ClrObject

"""

    ReferenceCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceCount(self: ClrmdHandle) -> UInt32

"""



class ClrmdHeap(ClrHeap):
    """ ClrmdHeap(runtime: ClrRuntime, data: IHeapData) """
    def ClearCachedData(self):
        """ ClearCachedData(self: ClrmdHeap) """
        pass

    def EnumerateAllocationContexts(self):
        """ EnumerateAllocationContexts(self: ClrmdHeap) -> IEnumerable[MemoryRange] """
        pass

    def EnumerateFinalizableObjects(self):
        """ EnumerateFinalizableObjects(self: ClrmdHeap) -> IEnumerable[ClrObject] """
        pass

    def EnumerateFinalizerRoots(self):
        """ EnumerateFinalizerRoots(self: ClrmdHeap) -> IEnumerable[ClrFinalizerRoot] """
        pass

    def EnumerateObjectReferences(self, obj, type, carefully, considerDependantHandles):
        """ EnumerateObjectReferences(self: ClrmdHeap, obj: UInt64, type: ClrType, carefully: bool, considerDependantHandles: bool) -> IEnumerable[ClrObject] """
        pass

    def EnumerateObjects(self):
        """ EnumerateObjects(self: ClrmdHeap) -> IEnumerable[ClrObject] """
        pass

    def EnumerateReferencesWithFields(self, obj, type, carefully, considerDependantHandles):
        """ EnumerateReferencesWithFields(self: ClrmdHeap, obj: UInt64, type: ClrType, carefully: bool, considerDependantHandles: bool) -> IEnumerable[ClrReference] """
        pass

    def EnumerateRoots(self):
        """ EnumerateRoots(self: ClrmdHeap) -> IEnumerable[IClrRoot] """
        pass

    def GetComFlags(self, obj):
        """ GetComFlags(self: ClrmdHeap, obj: UInt64) -> SyncBlockComFlags """
        pass

    def GetObjectSize(self, objRef, type):
        """ GetObjectSize(self: ClrmdHeap, objRef: UInt64, type: ClrType) -> UInt64 """
        pass

    def GetObjectType(self, objRef):
        """ GetObjectType(self: ClrmdHeap, objRef: UInt64) -> ClrType """
        pass

    def GetSegmentByAddress(self, address):
        """ GetSegmentByAddress(self: ClrmdHeap, address: UInt64) -> ClrSegment """
        pass

    def GetSyncBlock(self, obj):
        """ GetSyncBlock(self: ClrmdHeap, obj: UInt64) -> SyncBlock """
        pass

    def SkipAllocationContext(self, seg, address):
        """ SkipAllocationContext(self: ClrmdHeap, seg: ClrSegment, address: UInt64) -> UInt64 """
        pass

    @staticmethod # known case of __new__
    def __new__(self, runtime, data):
        """ __new__(cls: type, runtime: ClrRuntime, data: IHeapData) """
        pass

    CanWalkHeap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWalkHeap(self: ClrmdHeap) -> bool

"""

    ExceptionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionType(self: ClrmdHeap) -> ClrType

"""

    FreeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FreeType(self: ClrmdHeap) -> ClrType

"""

    IsServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsServer(self: ClrmdHeap) -> bool

"""

    LogicalHeapCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalHeapCount(self: ClrmdHeap) -> int

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: ClrmdHeap) -> ClrType

"""

    Runtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Runtime(self: ClrmdHeap) -> ClrRuntime

"""

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: ClrmdHeap) -> ImmutableArray[ClrSegment]

"""

    StringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringType(self: ClrmdHeap) -> ClrType

"""



class ClrmdMethod(ClrMethod, IEquatable[ClrMethod]):
    """ ClrmdMethod(type: ClrType, data: IMethodData) """
    def GetILOffset(self, addr):
        """ GetILOffset(self: ClrmdMethod, addr: UInt64) -> int """
        pass

    def ToString(self):
        """ ToString(self: ClrmdMethod) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, data):
        """ __new__(cls: type, type: ClrType, data: IMethodData) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CompilationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompilationType(self: ClrmdMethod) -> MethodCompilationType

"""

    HotColdInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HotColdInfo(self: ClrmdMethod) -> HotColdRegions

"""

    IL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IL(self: ClrmdMethod) -> ILInfo

"""

    ILOffsetMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ILOffsetMap(self: ClrmdMethod) -> ImmutableArray[ILToNativeMap]

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: ClrmdMethod) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinal(self: ClrmdMethod) -> bool

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdMethod) -> bool

"""

    IsPInvoke = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPInvoke(self: ClrmdMethod) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdMethod) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdMethod) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdMethod) -> bool

"""

    IsRTSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRTSpecialName(self: ClrmdMethod) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: ClrmdMethod) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: ClrmdMethod) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVirtual(self: ClrmdMethod) -> bool

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: ClrmdMethod) -> int

"""

    MethodDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodDesc(self: ClrmdMethod) -> UInt64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdMethod) -> str

"""

    NativeCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NativeCode(self: ClrmdMethod) -> UInt64

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Signature(self: ClrmdMethod) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ClrmdMethod) -> ClrType

"""



class ClrmdModule(ClrModule, IEquatable[ClrModule]):
    """
    ClrmdModule(parent: ClrAppDomain, data: IModuleData)
    ClrmdModule(parent: ClrAppDomain, helpers: IModuleHelpers, addr: UInt64)
    """
    def EnumerateTypeDefToMethodTableMap(self):
        """ EnumerateTypeDefToMethodTableMap(self: ClrmdModule) -> IEnumerable[ValueTuple[UInt64, int]] """
        pass

    def GetTypeByName(self, name):
        """ GetTypeByName(self: ClrmdModule, name: str) -> ClrType """
        pass

    def ResolveToken(self, typeDefOrRefToken):
        """ ResolveToken(self: ClrmdModule, typeDefOrRefToken: int) -> ClrType """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parent, *__args):
        """
        __new__(cls: type, parent: ClrAppDomain, data: IModuleData)
        __new__(cls: type, parent: ClrAppDomain, helpers: IModuleHelpers, addr: UInt64)
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ClrmdModule) -> UInt64

"""

    AppDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomain(self: ClrmdModule) -> ClrAppDomain

"""

    AssemblyAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyAddress(self: ClrmdModule) -> UInt64

"""

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyName(self: ClrmdModule) -> str

"""

    DebuggingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DebuggingMode(self: ClrmdModule) -> DebuggingModes

"""

    ImageBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageBase(self: ClrmdModule) -> UInt64

"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDynamic(self: ClrmdModule) -> bool

"""

    IsPEFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPEFile(self: ClrmdModule) -> bool

"""

    Layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layout(self: ClrmdModule) -> ModuleLayout

"""

    MetadataAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataAddress(self: ClrmdModule) -> UInt64

"""

    MetadataImport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataImport(self: ClrmdModule) -> MetadataImport

"""

    MetadataLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataLength(self: ClrmdModule) -> UInt64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdModule) -> str

"""

    Pdb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pdb(self: ClrmdModule) -> PdbInfo

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: ClrmdModule) -> UInt64

"""



class ClrmdPrimitiveType(ClrType, IEquatable[ClrType]):
    """ ClrmdPrimitiveType(helpers: ITypeHelpers, module: ClrModule, heap: ClrHeap, type: ClrElementType) """
    def AsEnum(self):
        """ AsEnum(self: ClrmdPrimitiveType) -> ClrEnum """
        pass

    def EnumerateInterfaces(self):
        """ EnumerateInterfaces(self: ClrmdPrimitiveType) -> IEnumerable[ClrInterface] """
        pass

    def GetArrayElementAddress(self, objRef, index):
        """ GetArrayElementAddress(self: ClrmdPrimitiveType, objRef: UInt64, index: int) -> UInt64 """
        pass

    def GetFieldByName(self, name):
        """ GetFieldByName(self: ClrmdPrimitiveType, name: str) -> ClrInstanceField """
        pass

    def GetStaticFieldByName(self, name):
        """ GetStaticFieldByName(self: ClrmdPrimitiveType, name: str) -> ClrStaticField """
        pass

    def IsFinalizeSuppressed(self, obj):
        """ IsFinalizeSuppressed(self: ClrmdPrimitiveType, obj: UInt64) -> bool """
        pass

    def ReadArrayElements(self, objRef, start, count):
        """ ReadArrayElements[T](self: ClrmdPrimitiveType, objRef: UInt64, start: int, count: int) -> Array[T] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, helpers, module, heap, type):
        """ __new__(cls: type, helpers: ITypeHelpers, module: ClrModule, heap: ClrHeap, type: ClrElementType) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: ClrmdPrimitiveType) -> ClrType

"""

    ClrObjectHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClrObjectHelpers(self: ClrmdPrimitiveType) -> IClrObjectHelpers

"""

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: ClrmdPrimitiveType) -> int

"""

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: ClrmdPrimitiveType) -> ClrType

"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: ClrmdPrimitiveType) -> ClrElementType

"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fields(self: ClrmdPrimitiveType) -> ImmutableArray[ClrInstanceField]

"""

    GCDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCDesc(self: ClrmdPrimitiveType) -> GCDesc

"""

    Heap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Heap(self: ClrmdPrimitiveType) -> ClrHeap

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: ClrmdPrimitiveType) -> bool

"""

    IsArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArray(self: ClrmdPrimitiveType) -> bool

"""

    IsEnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnum(self: ClrmdPrimitiveType) -> bool

"""

    IsFinalizable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinalizable(self: ClrmdPrimitiveType) -> bool

"""

    IsInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInterface(self: ClrmdPrimitiveType) -> bool

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdPrimitiveType) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdPrimitiveType) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdPrimitiveType) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdPrimitiveType) -> bool

"""

    IsSealed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSealed(self: ClrmdPrimitiveType) -> bool

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShared(self: ClrmdPrimitiveType) -> bool

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: ClrmdPrimitiveType) -> int

"""

    Methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Methods(self: ClrmdPrimitiveType) -> ImmutableArray[ClrMethod]

"""

    MethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodTable(self: ClrmdPrimitiveType) -> UInt64

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: ClrmdPrimitiveType) -> ClrModule

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdPrimitiveType) -> str

"""

    StaticFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticFields(self: ClrmdPrimitiveType) -> ImmutableArray[ClrStaticField]

"""

    StaticSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticSize(self: ClrmdPrimitiveType) -> int

"""



class ClrmdRefCountedHandle(ClrHandle, IClrRoot):
    """ ClrmdRefCountedHandle(parent: ClrAppDomain, address: UInt64, obj: ClrObject, refCount: UInt32) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parent, address, obj, refCount):
        """ __new__(cls: type, parent: ClrAppDomain, address: UInt64, obj: ClrObject, refCount: UInt32) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ClrmdRefCountedHandle) -> UInt64

"""

    AppDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomain(self: ClrmdRefCountedHandle) -> ClrAppDomain

"""

    Dependent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dependent(self: ClrmdRefCountedHandle) -> ClrObject

"""

    HandleKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HandleKind(self: ClrmdRefCountedHandle) -> ClrHandleKind

"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: ClrmdRefCountedHandle) -> ClrObject

"""

    ReferenceCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceCount(self: ClrmdRefCountedHandle) -> UInt32

"""



class ClrmdRuntime(ClrRuntime, IDisposable):
    """ ClrmdRuntime(info: ClrInfo, dac: DacLibrary, helpers: IRuntimeHelpers) """
    def Dispose(self):
        """ Dispose(self: ClrmdRuntime, disposing: bool) """
        pass

    def EnumerateHandles(self):
        """ EnumerateHandles(self: ClrmdRuntime) -> IEnumerable[ClrHandle] """
        pass

    def EnumerateModules(self):
        """ EnumerateModules(self: ClrmdRuntime) -> IEnumerable[ClrModule] """
        pass

    def FlushCachedData(self):
        """
        FlushCachedData(self: ClrmdRuntime)
            Flushes the DAC cache.  This function must be called any time you expect to call the same function
                    but expect different results.  For example, after walking the heap, 
             you need to call Flush before
                    attempting to walk the heap again.
        """
        pass

    def GetJitHelperFunctionName(self, ip):
        """ GetJitHelperFunctionName(self: ClrmdRuntime, ip: UInt64) -> str """
        pass

    def GetMethodByHandle(self, methodHandle):
        """ GetMethodByHandle(self: ClrmdRuntime, methodHandle: UInt64) -> ClrMethod """
        pass

    def GetMethodByInstructionPointer(self, ip):
        """ GetMethodByInstructionPointer(self: ClrmdRuntime, ip: UInt64) -> ClrMethod """
        pass

    def GetTypeByMethodTable(self, methodTable):
        """
        GetTypeByMethodTable(self: ClrmdRuntime, methodTable: UInt64) -> ClrType
        
            Gets the Microsoft.Diagnostics.Runtime.ClrType corresponding to the given MethodTable.
        
            methodTable: The ClrType.MethodTable for the requested type.
            Returns: A ClrType object, or ll if no such type exists.
        """
        pass

    def Initialize(self):
        """ Initialize(self: ClrmdRuntime) """
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
    def __new__(self, info, dac, helpers):
        """ __new__(cls: type, info: ClrInfo, dac: DacLibrary, helpers: IRuntimeHelpers) """
        pass

    AppDomains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppDomains(self: ClrmdRuntime) -> ImmutableArray[ClrAppDomain]

"""

    BaseClassLibrary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseClassLibrary(self: ClrmdRuntime) -> ClrModule

"""

    ClrInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClrInfo(self: ClrmdRuntime) -> ClrInfo

"""

    DacLibrary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DacLibrary(self: ClrmdRuntime) -> DacLibrary

"""

    DataTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTarget(self: ClrmdRuntime) -> DataTarget

"""

    Heap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Heap(self: ClrmdRuntime) -> ClrHeap

"""

    IsThreadSafe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsThreadSafe(self: ClrmdRuntime) -> bool

"""

    SharedDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SharedDomain(self: ClrmdRuntime) -> ClrAppDomain

"""

    SystemDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SystemDomain(self: ClrmdRuntime) -> ClrAppDomain

"""

    Threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Threads(self: ClrmdRuntime) -> ImmutableArray[ClrThread]

"""



class ClrmdSegment(ClrSegment):
    """ ClrmdSegment(heap: ClrmdHeap, helpers: IHeapHelpers, data: ISegmentData) """
    def EnumerateObjects(self):
        """ EnumerateObjects(self: ClrmdSegment) -> IEnumerable[ClrObject] """
        pass

    def GetNextObjectAddress(self, addr):
        """ GetNextObjectAddress(self: ClrmdSegment, addr: UInt64) -> UInt64 """
        pass

    def GetPreviousObjectAddress(self, addr):
        """ GetPreviousObjectAddress(self: ClrmdSegment, addr: UInt64) -> UInt64 """
        pass

    @staticmethod # known case of __new__
    def __new__(self, heap, helpers, data):
        """ __new__(cls: type, heap: ClrmdHeap, helpers: IHeapHelpers, data: ISegmentData) """
        pass

    CommittedMemory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommittedMemory(self: ClrmdSegment) -> MemoryRange

"""

    FirstObjectAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstObjectAddress(self: ClrmdSegment) -> UInt64

"""

    Generation0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Generation0(self: ClrmdSegment) -> MemoryRange

"""

    Generation1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Generation1(self: ClrmdSegment) -> MemoryRange

"""

    Generation2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Generation2(self: ClrmdSegment) -> MemoryRange

"""

    Heap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Heap(self: ClrmdSegment) -> ClrHeap

"""

    IsEphemeralSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEphemeralSegment(self: ClrmdSegment) -> bool

"""

    IsLargeObjectSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLargeObjectSegment(self: ClrmdSegment) -> bool

"""

    IsPinnedObjectSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinnedObjectSegment(self: ClrmdSegment) -> bool

"""

    LogicalHeap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalHeap(self: ClrmdSegment) -> int

"""

    ObjectRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectRange(self: ClrmdSegment) -> MemoryRange

"""

    ReservedMemory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReservedMemory(self: ClrmdSegment) -> MemoryRange

"""



class ClrmdStaticField(ClrStaticField):
    """ ClrmdStaticField(containingType: ClrType, data: IFieldData) """
    def GetAddress(self, domain):
        """ GetAddress(self: ClrmdStaticField, domain: ClrAppDomain) -> UInt64 """
        pass

    def IsInitialized(self, appDomain):
        """ IsInitialized(self: ClrmdStaticField, appDomain: ClrAppDomain) -> bool """
        pass

    def Read(self, appDomain):
        """ Read[T](self: ClrmdStaticField, appDomain: ClrAppDomain) -> T """
        pass

    def ReadObject(self, appDomain):
        """ ReadObject(self: ClrmdStaticField, appDomain: ClrAppDomain) -> ClrObject """
        pass

    def ReadString(self, appDomain):
        """ ReadString(self: ClrmdStaticField, appDomain: ClrAppDomain) -> str """
        pass

    def ReadStruct(self, appDomain):
        """ ReadStruct(self: ClrmdStaticField, appDomain: ClrAppDomain) -> ClrValueType """
        pass

    @staticmethod # known case of __new__
    def __new__(self, containingType, data):
        """ __new__(cls: type, containingType: ClrType, data: IFieldData) """
        pass

    ContainingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainingType(self: ClrmdStaticField) -> ClrType

"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: ClrmdStaticField) -> ClrElementType

"""

    IsInternal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternal(self: ClrmdStaticField) -> bool

"""

    IsObjectReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsObjectReference(self: ClrmdStaticField) -> bool

"""

    IsPrimitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrimitive(self: ClrmdStaticField) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: ClrmdStaticField) -> bool

"""

    IsProtected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProtected(self: ClrmdStaticField) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: ClrmdStaticField) -> bool

"""

    IsValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValueType(self: ClrmdStaticField) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClrmdStaticField) -> str

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: ClrmdStaticField) -> int

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: ClrmdStaticField) -> int

"""

    Token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Token(self: ClrmdStaticField) -> int

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ClrmdStaticField) -> ClrType

"""



class ClrmdThread(ClrThread):
    """ ClrmdThread(data: IThreadData, runtime: ClrRuntime, currentDomain: ClrAppDomain) """
    def EnumerateStackRoots(self):
        """ EnumerateStackRoots(self: ClrmdThread) -> IEnumerable[IClrStackRoot] """
        pass

    def EnumerateStackTrace(self, includeContext):
        """ EnumerateStackTrace(self: ClrmdThread, includeContext: bool) -> IEnumerable[ClrStackFrame] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, data, runtime, currentDomain):
        """ __new__(cls: type, data: IThreadData, runtime: ClrRuntime, currentDomain: ClrAppDomain) """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ClrmdThread) -> UInt64

"""

    CurrentAppDomain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAppDomain(self: ClrmdThread) -> ClrAppDomain

"""

    CurrentException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentException(self: ClrmdThread) -> ClrException

"""

    GCMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GCMode(self: ClrmdThread) -> GCMode

"""

    IsAborted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAborted(self: ClrmdThread) -> bool

"""

    IsAbortRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbortRequested(self: ClrmdThread) -> bool

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAlive(self: ClrmdThread) -> bool

"""

    IsBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBackground(self: ClrmdThread) -> bool

"""

    IsCoInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCoInitialized(self: ClrmdThread) -> bool

"""

    IsDebugSuspended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDebugSuspended(self: ClrmdThread) -> bool

"""

    IsFinalizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinalizer(self: ClrmdThread) -> bool

"""

    IsGCSuspendPending = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGCSuspendPending(self: ClrmdThread) -> bool

"""

    IsMTA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMTA(self: ClrmdThread) -> bool

"""

    IsSTA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSTA(self: ClrmdThread) -> bool

"""

    IsUnstarted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnstarted(self: ClrmdThread) -> bool

"""

    IsUserSuspended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserSuspended(self: ClrmdThread) -> bool

"""

    LockCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockCount(self: ClrmdThread) -> UInt32

"""

    ManagedThreadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManagedThreadId(self: ClrmdThread) -> int

"""

    OSThreadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OSThreadId(self: ClrmdThread) -> UInt32

"""

    Runtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Runtime(self: ClrmdThread) -> ClrRuntime

"""

    StackBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackBase(self: ClrmdThread) -> UInt64

"""

    StackLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackLimit(self: ClrmdThread) -> UInt64

"""



class ComSyncBlock(SyncBlock):
    """ ComSyncBlock(obj: UInt64, comFlags: UInt32) """
    @staticmethod # known case of __new__
    def __new__(self, obj, comFlags):
        """ __new__(cls: type, obj: UInt64, comFlags: UInt32) """
        pass

    ComFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComFlags(self: ComSyncBlock) -> SyncBlockComFlags

"""

    IsComCallWrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsComCallWrapper(self: ComSyncBlock) -> bool

"""

    IsComClassFactory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsComClassFactory(self: ComSyncBlock) -> bool

"""

    IsRuntimeCallWrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRuntimeCallWrapper(self: ComSyncBlock) -> bool

"""



class FinalizerQueueSegment(object):
    """ FinalizerQueueSegment(start: UInt64, end: UInt64) """
    @staticmethod # known case of __new__
    def __new__(self, start, end):
        """
        __new__[FinalizerQueueSegment]() -> FinalizerQueueSegment
        
        __new__(cls: type, start: UInt64, end: UInt64)
        """
        pass

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: End(self: FinalizerQueueSegment) -> UInt64

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Start(self: FinalizerQueueSegment) -> UInt64

"""



class FullSyncBlock(SyncBlock):
    """ FullSyncBlock(syncBlk: SyncBlockData) -> SyncBlockData """
    @staticmethod # known case of __new__
    def __new__(self, syncBlk):
        """ __new__(cls: type, syncBlk: SyncBlockData) -> SyncBlockData """
        pass

    ComFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComFlags(self: FullSyncBlock) -> SyncBlockComFlags

"""

    HoldingThreadAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HoldingThreadAddress(self: FullSyncBlock) -> UInt64

"""

    IsComCallWrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsComCallWrapper(self: FullSyncBlock) -> bool

"""

    IsComClassFactory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsComClassFactory(self: FullSyncBlock) -> bool

"""

    IsMonitorHeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMonitorHeld(self: FullSyncBlock) -> bool

"""

    IsRuntimeCallWrapper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRuntimeCallWrapper(self: FullSyncBlock) -> bool

"""

    RecursionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecursionCount(self: FullSyncBlock) -> int

"""

    WaitingThreadCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaitingThreadCount(self: FullSyncBlock) -> int

"""



class HeapWalkStep(object):
    """ This struct represents a single step in Microsoft.Diagnostics.Runtime.Implementation.ClrmdHeap's heap walk.  This is used for diagnostic purposes. """
    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: HeapWalkStep) -> UInt64

Set: Address(self: HeapWalkStep) = value
"""

    BaseSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseSize(self: HeapWalkStep) -> int

Set: BaseSize(self: HeapWalkStep) = value
"""

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: HeapWalkStep) -> int

Set: ComponentSize(self: HeapWalkStep) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: HeapWalkStep) -> UInt32

Set: Count(self: HeapWalkStep) = value
"""

    MethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodTable(self: HeapWalkStep) -> UInt64

Set: MethodTable(self: HeapWalkStep) = value
"""



class IAppDomainData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: IAppDomainData) -> UInt64

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Helpers(self: IAppDomainData) -> IAppDomainHelpers

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: IAppDomainData) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAppDomainData) -> str

"""



class IAppDomainHelpers:
    # no doc
    def EnumerateModules(self, domain):
        """ EnumerateModules(self: IAppDomainHelpers, domain: ClrAppDomain) -> IEnumerable[ClrModule] """
        pass

    def GetApplicationBase(self, domain):
        """ GetApplicationBase(self: IAppDomainHelpers, domain: ClrAppDomain) -> str """
        pass

    def GetConfigFile(self, domain):
        """ GetConfigFile(self: IAppDomainHelpers, domain: ClrAppDomain) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICcwData:
    # no doc
    def GetInterfaces(self):
        """ GetInterfaces(self: ICcwData) -> ImmutableArray[ComInterfaceData] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: ICcwData) -> UInt64

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: ICcwData) -> UInt64

"""

    IUnknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IUnknown(self: ICcwData) -> UInt64

"""

    JupiterRefCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JupiterRefCount(self: ICcwData) -> int

"""

    Object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Object(self: ICcwData) -> UInt64

"""

    RefCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefCount(self: ICcwData) -> int

"""



class IClrObjectHelpers:
    # no doc
    def ReadString(self, addr, maxLength):
        """ ReadString(self: IClrObjectHelpers, addr: UInt64, maxLength: int) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IClrObjectHelpers) -> IDataReader

"""

    ExceptionHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionHelpers(self: IClrObjectHelpers) -> IExceptionHelpers

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: IClrObjectHelpers) -> ITypeFactory

"""



class IExceptionHelpers:
    # no doc
    def GetExceptionStackTrace(self, thread, obj):
        """ GetExceptionStackTrace(self: IExceptionHelpers, thread: ClrThread, obj: ClrObject) -> ImmutableArray[ClrStackFrame] """
        pass

    def GetHResultOffset(self, type):
        """ GetHResultOffset(self: IExceptionHelpers, type: ClrType) -> UInt32 """
        pass

    def GetInnerExceptionOffset(self, type):
        """ GetInnerExceptionOffset(self: IExceptionHelpers, type: ClrType) -> UInt32 """
        pass

    def GetMessageOffset(self, type):
        """ GetMessageOffset(self: IExceptionHelpers, type: ClrType) -> UInt32 """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IExceptionHelpers) -> IDataReader

"""



class IFieldData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: IFieldData) -> ClrElementType

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Helpers(self: IFieldData) -> IFieldHelpers

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: IFieldData) -> int

"""

    Token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Token(self: IFieldData) -> int

"""

    TypeMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeMethodTable(self: IFieldData) -> UInt64

"""



class IFieldHelpers:
    # no doc
    def GetStaticFieldAddress(self, field, appDomain):
        """ GetStaticFieldAddress(self: IFieldHelpers, field: ClrStaticField, appDomain: ClrAppDomain) -> UInt64 """
        pass

    def ReadProperties(self, parentType, token, name, attributes, sigParser):
        """ ReadProperties(self: IFieldHelpers, parentType: ClrType, token: int) -> (bool, str, FieldAttributes, SigParser) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IFieldHelpers) -> IDataReader

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: IFieldHelpers) -> ITypeFactory

"""



class IHeapData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ArrayMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayMethodTable(self: IHeapData) -> UInt64

"""

    CanWalkHeap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWalkHeap(self: IHeapData) -> bool

"""

    ExceptionMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionMethodTable(self: IHeapData) -> UInt64

"""

    FreeMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FreeMethodTable(self: IHeapData) -> UInt64

"""

    HeapHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeapHelpers(self: IHeapData) -> IHeapHelpers

"""

    IsServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsServer(self: IHeapData) -> bool

"""

    LogicalHeapCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalHeapCount(self: IHeapData) -> int

"""

    ObjectMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectMethodTable(self: IHeapData) -> UInt64

"""

    StringMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringMethodTable(self: IHeapData) -> UInt64

"""



class IHeapHelpers:
    # no doc
    def CreateSegments(self, clrHeap, segemnts, allocationContexts, fqRoots, fqObjects):
        """ CreateSegments(self: IHeapHelpers, clrHeap: ClrHeap) -> (bool, ImmutableArray[ClrSegment], ImmutableArray[MemoryRange], ImmutableArray[FinalizerQueueSegment], ImmutableArray[FinalizerQueueSegment]) """
        pass

    def EnumerateDependentHandleLinks(self):
        """ EnumerateDependentHandleLinks(self: IHeapHelpers) -> IEnumerable[ValueTuple[UInt64, UInt64]] """
        pass

    def GetSyncBlocks(self, comSyncBlocks, fullSyncBlocks, emptySyncBlocks):
        """ GetSyncBlocks(self: IHeapHelpers) -> (bool, List[ComSyncBlock], List[FullSyncBlock], List[UInt64]) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IHeapHelpers) -> IDataReader

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: IHeapHelpers) -> ITypeFactory

"""



class IMethodData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ColdSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColdSize(self: IMethodData) -> UInt32

"""

    ColdStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColdStart(self: IMethodData) -> UInt64

"""

    CompilationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompilationType(self: IMethodData) -> MethodCompilationType

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Helpers(self: IMethodData) -> IMethodHelpers

"""

    HotSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HotSize(self: IMethodData) -> UInt32

"""

    HotStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HotStart(self: IMethodData) -> UInt64

"""

    MethodDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodDesc(self: IMethodData) -> UInt64

"""

    Token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Token(self: IMethodData) -> int

"""



class IMethodHelpers:
    # no doc
    def GetILForModule(self, address, rva):
        """ GetILForModule(self: IMethodHelpers, address: UInt64, rva: UInt32) -> UInt64 """
        pass

    def GetILMap(self, nativeCode, hotColdInfo):
        """ GetILMap(self: IMethodHelpers, nativeCode: UInt64, hotColdInfo: HotColdRegions) -> (ImmutableArray[ILToNativeMap], HotColdRegions) """
        pass

    def GetSignature(self, methodDesc, signature):
        """ GetSignature(self: IMethodHelpers, methodDesc: UInt64) -> (bool, str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IMethodHelpers) -> IDataReader

"""



class IModuleData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: IModuleData) -> UInt64

"""

    AssemblyAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyAddress(self: IModuleData) -> UInt64

"""

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyName(self: IModuleData) -> str

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: IModuleData) -> str

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Helpers(self: IModuleData) -> IModuleHelpers

"""

    ILImageBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ILImageBase(self: IModuleData) -> UInt64

"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDynamic(self: IModuleData) -> bool

"""

    IsFlatLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFlatLayout(self: IModuleData) -> bool

"""

    IsPEFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPEFile(self: IModuleData) -> bool

"""

    IsReflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReflection(self: IModuleData) -> bool

"""

    MetadataLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataLength(self: IModuleData) -> UInt64

"""

    MetadataStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataStart(self: IModuleData) -> UInt64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IModuleData) -> str

"""

    PEImageBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PEImageBase(self: IModuleData) -> UInt64

"""

    SimpleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimpleName(self: IModuleData) -> str

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: IModuleData) -> UInt64

"""



class IModuleHelpers:
    # no doc
    def GetMetadataImport(self, module):
        """ GetMetadataImport(self: IModuleHelpers, module: ClrModule) -> MetadataImport """
        pass

    def GetSortedTypeDefMap(self, module):
        """ GetSortedTypeDefMap(self: IModuleHelpers, module: ClrModule) -> Array[ValueTuple[UInt64, int]] """
        pass

    def GetSortedTypeRefMap(self, module):
        """ GetSortedTypeRefMap(self: IModuleHelpers, module: ClrModule) -> Array[ValueTuple[UInt64, int]] """
        pass

    def GetTypeName(self, mt):
        """ GetTypeName(self: IModuleHelpers, mt: UInt64) -> str """
        pass

    def TryGetType(self, mt):
        """ TryGetType(self: IModuleHelpers, mt: UInt64) -> ClrType """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IModuleHelpers) -> IDataReader

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: IModuleHelpers) -> ITypeFactory

"""



class IObjectData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CCW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CCW(self: IObjectData) -> UInt64

"""

    DataPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataPointer(self: IObjectData) -> UInt64

"""

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: IObjectData) -> ClrElementType

"""

    ElementTypeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementTypeHandle(self: IObjectData) -> UInt64

"""

    RCW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RCW(self: IObjectData) -> UInt64

"""



class IRcwData:
    # no doc
    def GetInterfaces(self):
        """ GetInterfaces(self: IRcwData) -> ImmutableArray[ComInterfaceData] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: IRcwData) -> UInt64

"""

    CreatorThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreatorThread(self: IRcwData) -> UInt64

"""

    Disconnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Disconnected(self: IRcwData) -> bool

"""

    IUnknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IUnknown(self: IRcwData) -> UInt64

"""

    ManagedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManagedObject(self: IRcwData) -> UInt64

"""

    RefCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefCount(self: IRcwData) -> int

"""

    VTablePointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VTablePointer(self: IRcwData) -> UInt64

"""



class IRuntimeHelpers(IDisposable):
    # no doc
    def EnumerateHandleTable(self, runtime):
        """ EnumerateHandleTable(self: IRuntimeHelpers, runtime: ClrRuntime) -> IEnumerable[ClrHandle] """
        pass

    def FlushCachedData(self):
        """ FlushCachedData(self: IRuntimeHelpers) """
        pass

    def GetAppDomains(self, runtime, system, shared):
        """ GetAppDomains(self: IRuntimeHelpers, runtime: ClrRuntime) -> (ImmutableArray[ClrAppDomain], ClrAppDomain, ClrAppDomain) """
        pass

    def GetBaseClassLibrary(self, runtime):
        """ GetBaseClassLibrary(self: IRuntimeHelpers, runtime: ClrRuntime) -> ClrModule """
        pass

    def GetJitHelperFunctionName(self, ip):
        """ GetJitHelperFunctionName(self: IRuntimeHelpers, ip: UInt64) -> str """
        pass

    def GetMethodDesc(self, ip):
        """ GetMethodDesc(self: IRuntimeHelpers, ip: UInt64) -> UInt64 """
        pass

    def GetThreads(self, runtime):
        """ GetThreads(self: IRuntimeHelpers, runtime: ClrRuntime) -> ImmutableArray[ClrThread] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IRuntimeHelpers) -> IDataReader

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: IRuntimeHelpers) -> ITypeFactory

"""



class ISegmentData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BaseAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseAddress(self: ISegmentData) -> UInt64

"""

    CommittedEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommittedEnd(self: ISegmentData) -> UInt64

"""

    End = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: End(self: ISegmentData) -> UInt64

"""

    Gen0Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gen0Length(self: ISegmentData) -> UInt64

"""

    Gen0Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gen0Start(self: ISegmentData) -> UInt64

"""

    Gen1Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gen1Length(self: ISegmentData) -> UInt64

"""

    Gen1Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gen1Start(self: ISegmentData) -> UInt64

"""

    Gen2Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gen2Length(self: ISegmentData) -> UInt64

"""

    Gen2Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gen2Start(self: ISegmentData) -> UInt64

"""

    IsEphemeralSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEphemeralSegment(self: ISegmentData) -> bool

"""

    IsLargeObjectSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLargeObjectSegment(self: ISegmentData) -> bool

"""

    IsPinnedObjectSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinnedObjectSegment(self: ISegmentData) -> bool

"""

    LogicalHeap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalHeap(self: ISegmentData) -> int

"""

    ReservedEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReservedEnd(self: ISegmentData) -> UInt64

"""

    Start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Start(self: ISegmentData) -> UInt64

"""



class IThreadData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Address(self: IThreadData) -> UInt64

"""

    ExceptionHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionHandle(self: IThreadData) -> UInt64

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Helpers(self: IThreadData) -> IThreadHelpers

"""

    IsFinalizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinalizer(self: IThreadData) -> bool

"""

    LockCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockCount(self: IThreadData) -> UInt32

"""

    ManagedThreadID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManagedThreadID(self: IThreadData) -> int

"""

    OSThreadID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OSThreadID(self: IThreadData) -> UInt32

"""

    Preemptive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preemptive(self: IThreadData) -> bool

"""

    StackBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackBase(self: IThreadData) -> UInt64

"""

    StackLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackLimit(self: IThreadData) -> UInt64

"""

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: IThreadData) -> int

"""



class IThreadHelpers:
    # no doc
    def EnumerateStackRoots(self, thread):
        """ EnumerateStackRoots(self: IThreadHelpers, thread: ClrThread) -> IEnumerable[IClrStackRoot] """
        pass

    def EnumerateStackTrace(self, thread, includeContext):
        """ EnumerateStackTrace(self: IThreadHelpers, thread: ClrThread, includeContext: bool) -> IEnumerable[ClrStackFrame] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: IThreadHelpers) -> IDataReader

"""

    ExceptionHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionHelpers(self: IThreadHelpers) -> IExceptionHelpers

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: IThreadHelpers) -> ITypeFactory

"""



class ITypeData:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BaseSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseSize(self: ITypeData) -> int

"""

    ComponentMethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentMethodTable(self: ITypeData) -> UInt64

"""

    ComponentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSize(self: ITypeData) -> int

"""

    ContainsPointers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsPointers(self: ITypeData) -> bool

"""

    Helpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Helpers(self: ITypeData) -> ITypeHelpers

"""

    IsShared = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShared(self: ITypeData) -> bool

"""

    MethodCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodCount(self: ITypeData) -> int

"""

    MethodTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodTable(self: ITypeData) -> UInt64

"""

    Token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Token(self: ITypeData) -> int

"""



class ITypeFactory(IDisposable):
    # no doc
    def CreateCCWForObject(self, obj):
        """ CreateCCWForObject(self: ITypeFactory, obj: UInt64) -> ComCallableWrapper """
        pass

    def CreateFieldsForType(self, type, fields, staticFields):
        """ CreateFieldsForType(self: ITypeFactory, type: ClrType) -> (bool, ImmutableArray[ClrInstanceField], ImmutableArray[ClrStaticField]) """
        pass

    def CreateMethodFromHandle(self, methodHandle):
        """ CreateMethodFromHandle(self: ITypeFactory, methodHandle: UInt64) -> ClrMethod """
        pass

    def CreateMethodsForType(self, type, methods):
        """ CreateMethodsForType(self: ITypeFactory, type: ClrType) -> (bool, ImmutableArray[ClrMethod]) """
        pass

    def CreateRCWForObject(self, obj):
        """ CreateRCWForObject(self: ITypeFactory, obj: UInt64) -> RuntimeCallableWrapper """
        pass

    def CreateSystemType(self, heap, mt, kind):
        """ CreateSystemType(self: ITypeFactory, heap: ClrHeap, mt: UInt64, kind: str) -> ClrType """
        pass

    def GetOrCreateArrayType(self, inner, ranks):
        """ GetOrCreateArrayType(self: ITypeFactory, inner: ClrType, ranks: int) -> ClrType """
        pass

    def GetOrCreateBasicType(self, basicType):
        """ GetOrCreateBasicType(self: ITypeFactory, basicType: ClrElementType) -> ClrType """
        pass

    def GetOrCreateHeap(self):
        """ GetOrCreateHeap(self: ITypeFactory) -> ClrHeap """
        pass

    def GetOrCreateModule(self, domain, address):
        """ GetOrCreateModule(self: ITypeFactory, domain: ClrAppDomain, address: UInt64) -> ClrModule """
        pass

    def GetOrCreatePointerType(self, innerType, depth):
        """ GetOrCreatePointerType(self: ITypeFactory, innerType: ClrType, depth: int) -> ClrType """
        pass

    def GetOrCreateRuntime(self):
        """ GetOrCreateRuntime(self: ITypeFactory) -> ClrRuntime """
        pass

    def GetOrCreateType(self, *__args):
        """
        GetOrCreateType(self: ITypeFactory, heap: ClrHeap, mt: UInt64, obj: UInt64) -> ClrType
        GetOrCreateType(self: ITypeFactory, mt: UInt64, obj: UInt64) -> ClrType
        """
        pass

    def GetOrCreateTypeFromSignature(self, module, parser, typeParameters, methodParameters):
        """ GetOrCreateTypeFromSignature(self: ITypeFactory, module: ClrModule, parser: SigParser, typeParameters: IEnumerable[ClrGenericParameter], methodParameters: IEnumerable[ClrGenericParameter]) -> ClrType """
        pass

    def GetOrCreateTypeFromToken(self, module, token):
        """ GetOrCreateTypeFromToken(self: ITypeFactory, module: ClrModule, token: int) -> ClrType """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsThreadSafe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsThreadSafe(self: ITypeFactory) -> bool

"""



class ITypeHelpers:
    # no doc
    def GetAssemblyLoadContextAddress(self, mt):
        """ GetAssemblyLoadContextAddress(self: ITypeHelpers, mt: UInt64) -> UInt64 """
        pass

    def GetLoaderAllocatorHandle(self, mt):
        """ GetLoaderAllocatorHandle(self: ITypeHelpers, mt: UInt64) -> UInt64 """
        pass

    def GetObjectData(self, objRef):
        """ GetObjectData(self: ITypeHelpers, objRef: UInt64) -> IObjectData """
        pass

    def GetTypeName(self, mt, name):
        """
        GetTypeName(self: ITypeHelpers, mt: UInt64) -> (bool, str)
        
            Gets the name for a type.
        
            mt: The MethodTable to request the name of.
            Returns: True if the value should be cached, false if the value should not be cached.  (This is controlled
                    by the user's string cache settings.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ClrObjectHelpers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClrObjectHelpers(self: ITypeHelpers) -> IClrObjectHelpers

"""

    DataReader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataReader(self: ITypeHelpers) -> IDataReader

"""

    Factory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Factory(self: ITypeHelpers) -> ITypeFactory

"""



