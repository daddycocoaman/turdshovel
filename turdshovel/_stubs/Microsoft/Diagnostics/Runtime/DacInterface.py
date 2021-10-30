# encoding: utf-8
# module Microsoft.Diagnostics.Runtime.DacInterface calls itself DacInterface
# from Microsoft.Diagnostics.Runtime, Version=2.0.5.1201, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AppDomainData(object):
    # no doc
    Address = None
    AssemblyCount = None
    DomainLocalBlock = None
    DomainLocalModules = None
    FailedAssemblyCount = None
    HighFrequencyHeap = None
    Id = None
    LowFrequencyHeap = None
    SecurityDescriptor = None
    Stage = None
    StubHeap = None


class AppDomainStoreData(object):
    # no doc
    AppDomainCount = None
    SharedDomain = None
    SystemDomain = None


class AssemblyData(object):
    # no doc
    Address = None
    AppDomain = None
    AssemblySecurityDescriptor = None
    ClassLoader = None
    Dynamic = None
    IsDomainNeutral = None
    LoadContext = None
    LocationFlags = None
    ModuleCount = None
    ParentDomain = None


class CcwData(object):
    # no doc
    CCWAddress = None
    Handle = None
    HasStrongRef = None
    HasWeakReference = None
    InterfaceCount = None
    IsAggregated = None
    IsExtendsCOMObject = None
    IsGlobalPegged = None
    IsNeutered = None
    IsPegged = None
    JupiterRefCount = None
    ManagedObject = None
    OuterIUnknown = None
    RefCount = None


class ClrDataAddress(object):
    """
    A representation of CLR's CLRDATA_ADDRESS, which is a signed 64bit integer.
                Unfortunately this can cause issues when inspecting 32bit processes, since
                if the highest bit is set the value will be sign-extended.  This struct is
                meant to
    
    ClrDataAddress(value: Int64)
    """
    @staticmethod # known case of __new__
    def __new__(self, value):
        """
        __new__[ClrDataAddress]() -> ClrDataAddress
        
        __new__(cls: type, value: Int64)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets raw value of this address.  May be sign-extended if inspecting a 32bit process.

Get: Value(self: ClrDataAddress) -> Int64

"""



class ClrDataMethod(CallableCOMWrapper, IDisposable):
    """ ClrDataMethod(library: DacLibrary, pUnk: IntPtr) """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def GetILToNativeMap(self):
        """ GetILToNativeMap(self: ClrDataMethod) -> Array[ILToNativeMap] """
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
    def __new__(self, library, pUnk):
        """ __new__(cls: type, library: DacLibrary, pUnk: IntPtr) """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ClrDataModule(CallableCOMWrapper, IDisposable):
    """ ClrDataModule(library: DacLibrary, pUnknown: IntPtr) """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def GetFileName(self):
        """ GetFileName(self: ClrDataModule) -> str """
        pass

    def GetModuleData(self, data):
        """ GetModuleData(self: ClrDataModule) -> (HResult, ExtendedModuleData) """
        pass

    def GetName(self):
        """ GetName(self: ClrDataModule) -> str """
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
    def __new__(self, library, pUnknown):
        """ __new__(cls: type, library: DacLibrary, pUnknown: IntPtr) """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ClrDataProcess(CallableCOMWrapper, IDisposable):
    """
    This is an undocumented, untested, and unsupported interface.  Do not use.
    
    ClrDataProcess(library: DacLibrary, pUnknown: IntPtr)
    ClrDataProcess(library: DacLibrary, toClone: CallableCOMWrapper)
    """
    def CreateStackWalk(self, id, flags):
        """ CreateStackWalk(self: ClrDataProcess, id: UInt32, flags: UInt32) -> ClrStackWalk """
        pass

    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def EnumerateMethodInstancesByAddress(self, addr):
        """ EnumerateMethodInstancesByAddress(self: ClrDataProcess, addr: ClrDataAddress) -> IEnumerable[ClrDataMethod] """
        pass

    def Flush(self):
        """ Flush(self: ClrDataProcess) """
        pass

    def GetSOSDacInterface(self):
        """ GetSOSDacInterface(self: ClrDataProcess) -> SOSDac """
        pass

    def GetSOSDacInterface6(self):
        """ GetSOSDacInterface6(self: ClrDataProcess) -> SOSDac6 """
        pass

    def GetSOSDacInterface8(self):
        """ GetSOSDacInterface8(self: ClrDataProcess) -> SOSDac8 """
        pass

    def Request(self, reqCode, input, output):
        """ Request(self: ClrDataProcess, reqCode: UInt32, input: ReadOnlySpan[Byte], output: Span[Byte]) -> HResult """
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
    def __new__(self, library, *__args):
        """
        __new__(cls: type, library: DacLibrary, pUnknown: IntPtr)
        __new__(cls: type, library: DacLibrary, toClone: CallableCOMWrapper)
        """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ClrStackWalk(CallableCOMWrapper, IDisposable):
    """ ClrStackWalk(library: DacLibrary, pUnk: IntPtr) """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def GetContext(self, contextFlags, contextBufSize, contextSize, buffer):
        """ GetContext(self: ClrStackWalk, contextFlags: UInt32, contextBufSize: int, buffer: Array[Byte]) -> (HResult, int) """
        pass

    def GetFrameVtable(self):
        """ GetFrameVtable(self: ClrStackWalk) -> ClrDataAddress """
        pass

    def Next(self):
        """ Next(self: ClrStackWalk) -> HResult """
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
    def __new__(self, library, pUnk):
        """ __new__(cls: type, library: DacLibrary, pUnk: IntPtr) """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CodeHeaderData(object):
    # no doc
    ColdRegionSize = None
    ColdRegionStart = None
    GCInfo = None
    HotRegionSize = None
    JITType = None
    MethodDesc = None
    MethodSize = None
    MethodStart = None


class CodeHeapType(Enum, IComparable, IFormattable, IConvertible):
    """ enum CodeHeapType, values: Host (1), Loader (0), Unknown (2) """
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

    Host = None
    Loader = None
    Unknown = None
    value__ = None


class COMInterfacePointerData(object):
    # no doc
    ComContext = None
    InterfacePointer = None
    MethodTable = None


class CommonMethodTables(object):
    # no doc
    ArrayMethodTable = None
    ExceptionMethodTable = None
    FreeMethodTable = None
    ObjectMethodTable = None
    StringMethodTable = None


class DomainLocalModuleData(object):
    # no doc
    AppDomainAddress = None
    ClassData = None
    DynamicClassTable = None
    GCStaticDataStart = None
    ModuleID = None
    NonGCStaticDataStart = None


class ExtendedModuleData(object):
    # no doc
    InMemoryPdbAddress = None
    InMemoryPdbSize = None
    IsDynamic = None
    IsFlatLayout = None
    IsInMemory = None
    LoadedPEAddress = None
    LoadedPESize = None
    PEFile = None


class FieldData(object):
    # no doc
    ElementType = None
    FieldToken = None
    IsContextLocal = None
    IsStatic = None
    IsThreadLocal = None
    MTOfEnclosingClass = None
    NextField = None
    Offset = None
    SigType = None
    TypeMethodTable = None
    TypeModule = None
    TypeToken = None


class FieldInfo(object):
    # no doc
    ContextStaticOffset = None
    ContextStaticsSize = None
    FirstFieldAddress = None
    NumInstanceFields = None
    NumStaticFields = None
    NumThreadStaticFields = None


class GCInfo(object):
    # no doc
    GCStructuresValid = None
    HeapCount = None
    MaxGeneration = None
    ServerMode = None


class GenerationData(object):
    # no doc
    AllocationContextLimit = None
    AllocationContextPointer = None
    AllocationStart = None
    StartSegment = None


class HandleData(object):
    # no doc
    AppDomain = None
    Handle = None
    IsPegged = None
    JupiterRefCount = None
    RefCount = None
    Secondary = None
    StrongReference = None
    Type = None


class HeapDetails(object):
    # no doc
    EphemeralAllocContextLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EphemeralAllocContextLimit(self: HeapDetails) -> UInt64

"""

    EphemeralAllocContextPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EphemeralAllocContextPtr(self: HeapDetails) -> UInt64

"""

    FQAllObjectsStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FQAllObjectsStart(self: HeapDetails) -> UInt64

"""

    FQAllObjectsStop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FQAllObjectsStop(self: HeapDetails) -> UInt64

"""

    FQRootsStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FQRootsStart(self: HeapDetails) -> UInt64

"""

    FQRootsStop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FQRootsStop(self: HeapDetails) -> UInt64

"""


    Address = None
    Allocated = None
    BackgroundSavedHighestAddress = None
    BackgroundSavedLowestAddress = None
    CAllocateLH = None
    CardTable = None
    EphemeralHeapSegment = None
    FinalizationFillPointers = None
    GenerationTable = None
    HighestAddress = None
    LowestAddress = None
    MarkArray = None
    NextSweepObj = None
    SavedSweepEphemeralSeg = None
    SavedSweepEphemeralStart = None


class JitCodeHeapInfo(object):
    # no doc
    Address = None
    CurrentAddress = None
    Type = None


class JitManagerInfo(object):
    # no doc
    Address = None
    HeapList = None
    Type = None


class MetadataImport(CallableCOMWrapper, IDisposable):
    """ MetadataImport(library: DacLibrary, pUnknown: IntPtr) """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def EnumerateFields(self, token):
        """ EnumerateFields(self: MetadataImport, token: int) -> IEnumerable[int] """
        pass

    def EnumerateGenericParams(self, token):
        """ EnumerateGenericParams(self: MetadataImport, token: int) -> IEnumerable[int] """
        pass

    def EnumerateInterfaceImpls(self, token):
        """ EnumerateInterfaceImpls(self: MetadataImport, token: int) -> IEnumerable[int] """
        pass

    def GetCustomAttributeByName(self, token, name, data, cbData):
        """ GetCustomAttributeByName(self: MetadataImport, token: int, name: str) -> (HResult, IntPtr, UInt32) """
        pass

    def GetFieldProps(self, token, name, attrs, ppvSigBlob, pcbSigBlob, pdwCPlusTypeFlag, ppValue):
        """ GetFieldProps(self: MetadataImport, token: int) -> (HResult, str, FieldAttributes, IntPtr, int, int, IntPtr) """
        pass

    def GetGenericParamProps(self, token, index, attributes, name):
        """ GetGenericParamProps(self: MetadataImport, token: int) -> (bool, int, GenericParameterAttributes, str) """
        pass

    def GetInterfaceImplProps(self, token, mdClass, mdInterface):
        """ GetInterfaceImplProps(self: MetadataImport, token: int) -> (HResult, int, int) """
        pass

    def GetMethodAttributes(self, token):
        """ GetMethodAttributes(self: MetadataImport, token: int) -> MethodAttributes """
        pass

    def GetNestedClassProperties(self, token, enclosing):
        """ GetNestedClassProperties(self: MetadataImport, token: int) -> (HResult, int) """
        pass

    def GetRva(self, token):
        """ GetRva(self: MetadataImport, token: int) -> UInt32 """
        pass

    def GetSigFromToken(self, token):
        """ GetSigFromToken(self: MetadataImport, token: int) -> SigParser """
        pass

    def GetTypeDefProperties(self, token, name, attributes, mdParent):
        """ GetTypeDefProperties(self: MetadataImport, token: int) -> (HResult, str, TypeAttributes, int) """
        pass

    def GetTypeRefName(self, token):
        """ GetTypeRefName(self: MetadataImport, token: int) -> str """
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
    def __new__(self, library, pUnknown):
        """ __new__(cls: type, library: DacLibrary, pUnknown: IntPtr) """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    IID_IMetaDataImport = None


class MethodDescData(object):
    # no doc
    AddressOfNativeCodeSlot = None
    GCInfo = None
    GCStressCodeCopy = None
    HasNativeCode = None
    IsDynamic = None
    JittedRejitVersions = None
    ManagedDynamicMethodObject = None
    MDToken = None
    MethodDesc = None
    MethodTable = None
    Module = None
    NativeCodeAddr = None
    RejitDataCurrent = None
    RejitDataRequested = None
    RequestedIP = None
    SlotNumber = None


class MethodTableCollectibleData(object):
    # no doc
    Collectible = None
    LoaderAllocatorObjectHandle = None


class MethodTableData(object):
    # no doc
    AttrClass = None
    BaseSize = None
    ComponentSize = None
    ContainsPointers = None
    Dynamic = None
    EEClass = None
    IsFree = None
    Module = None
    NumInterfaces = None
    NumMethods = None
    NumVirtuals = None
    NumVtableSlots = None
    ParentMethodTable = None
    Shared = None
    Token = None


class ModuleData(object):
    # no doc
    Address = None
    Assembly = None
    BaseClassIndex = None
    FieldDefToDescMap = None
    FileReferencesMap = None
    ILBase = None
    IsPEFile = None
    IsReflection = None
    LookupTableHeap = None
    ManifestModuleReferencesMap = None
    MemberRefToDescMap = None
    MetadataSize = None
    MetadataStart = None
    MethodDefToDescMap = None
    ModuleID = None
    ModuleIndex = None
    PEFile = None
    ThunkHeap = None
    TransientFlags = None
    TypeDefToMethodTableMap = None
    TypeRefToMethodTableMap = None


class ObjectData(object, IObjectData):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ArrayBoundsPointer = None
    ArrayDataPointer = None
    ArrayLowerBoundsPointer = None
    CCW = None
    ComponentSize = None
    ElementType = None
    ElementTypeHandle = None
    MethodTable = None
    NumComponents = None
    ObjectType = None
    Rank = None
    RCW = None
    Size = None


class RcwData(object):
    # no doc
    CreatorThread = None
    CTXCookie = None
    IdentityPointer = None
    InterfaceCount = None
    IsAggregated = None
    IsContained = None
    IsDisconnected = None
    IsFreeThreaded = None
    IsJupiterObject = None
    IUnknownPointer = None
    JupiterObject = None
    ManagedObject = None
    RefCount = None
    SupportsIInspectable = None
    VTablePointer = None


class RejitData(object):
    # no doc

class SegmentData(object):
    # no doc
    Address = None
    Allocated = None
    BackgroundAllocated = None
    Committed = None
    Flags = None
    Heap = None
    HighAllocMark = None
    Next = None
    Reserved = None
    Start = None
    Used = None


class SOSDac(CallableCOMWrapper, IDisposable):
    """
    This is an undocumented, untested, and unsupported interface.  Do not use.
    
    SOSDac(library: DacLibrary, ptr: IntPtr)
    SOSDac(lib: DacLibrary, toClone: CallableCOMWrapper)
    """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def EnumerateHandles(self, types=None):
        """
        EnumerateHandles(self: SOSDac, *types: Array[ClrHandleKind]) -> SOSHandleEnum
        EnumerateHandles(self: SOSDac) -> SOSHandleEnum
        """
        pass

    def EnumerateStackRefs(self, osThreadId):
        """ EnumerateStackRefs(self: SOSDac, osThreadId: UInt32) -> SOSStackRefEnum """
        pass

    def GetAppBase(self, domain):
        """ GetAppBase(self: SOSDac, domain: UInt64) -> str """
        pass

    def GetAppDomainData(self, addr, data):
        """ GetAppDomainData(self: SOSDac, addr: UInt64) -> (HResult, AppDomainData) """
        pass

    def GetAppDomainList(self, count):
        """ GetAppDomainList(self: SOSDac, count: int) -> Array[ClrDataAddress] """
        pass

    def GetAppDomainName(self, appDomain):
        """ GetAppDomainName(self: SOSDac, appDomain: UInt64) -> str """
        pass

    def GetAppDomainStoreData(self, data):
        """ GetAppDomainStoreData(self: SOSDac) -> (HResult, AppDomainStoreData) """
        pass

    def GetAssemblyData(self, domain, assembly, data):
        """ GetAssemblyData(self: SOSDac, domain: UInt64, assembly: UInt64) -> (HResult, AssemblyData) """
        pass

    def GetAssemblyList(self, appDomain, count=None):
        """
        GetAssemblyList(self: SOSDac, appDomain: UInt64) -> Array[ClrDataAddress]
        GetAssemblyList(self: SOSDac, appDomain: UInt64, count: int) -> Array[ClrDataAddress]
        """
        pass

    def GetAssemblyName(self, assembly):
        """ GetAssemblyName(self: SOSDac, assembly: UInt64) -> str """
        pass

    def GetCCWData(self, ccw, data):
        """ GetCCWData(self: SOSDac, ccw: UInt64) -> (HResult, CcwData) """
        pass

    def GetCCWInterfaces(self, ccw, count):
        """ GetCCWInterfaces(self: SOSDac, ccw: UInt64, count: int) -> Array[COMInterfacePointerData] """
        pass

    def GetClrDataModule(self, module):
        """ GetClrDataModule(self: SOSDac, module: UInt64) -> ClrDataModule """
        pass

    def GetCodeHeaderData(self, ip, codeHeaderData):
        """ GetCodeHeaderData(self: SOSDac, ip: UInt64) -> (HResult, CodeHeaderData) """
        pass

    def GetCodeHeapList(self, jitManager):
        """ GetCodeHeapList(self: SOSDac, jitManager: UInt64) -> Array[JitCodeHeapInfo] """
        pass

    def GetCommonMethodTables(self, commonMTs):
        """ GetCommonMethodTables(self: SOSDac) -> (HResult, CommonMethodTables) """
        pass

    def GetConfigFile(self, domain):
        """ GetConfigFile(self: SOSDac, domain: UInt64) -> str """
        pass

    def GetDomainLocalModuleDataFromAppDomain(self, appDomain, id, data):
        """ GetDomainLocalModuleDataFromAppDomain(self: SOSDac, appDomain: UInt64, id: int) -> (HResult, DomainLocalModuleData) """
        pass

    def GetDomainLocalModuleDataFromModule(self, module, data):
        """ GetDomainLocalModuleDataFromModule(self: SOSDac, module: UInt64) -> (HResult, DomainLocalModuleData) """
        pass

    def GetFieldData(self, fieldDesc, data):
        """ GetFieldData(self: SOSDac, fieldDesc: UInt64) -> (HResult, FieldData) """
        pass

    def GetFieldInfo(self, mt, data):
        """ GetFieldInfo(self: SOSDac, mt: UInt64) -> (HResult, FieldInfo) """
        pass

    def GetFrameName(self, vtable):
        """ GetFrameName(self: SOSDac, vtable: UInt64) -> str """
        pass

    def GetGCHeapData(self, data):
        """ GetGCHeapData(self: SOSDac) -> (HResult, GCInfo) """
        pass

    def GetHeapList(self, heapCount):
        """ GetHeapList(self: SOSDac, heapCount: int) -> Array[ClrDataAddress] """
        pass

    def GetILForModule(self, moduleAddr, rva):
        """ GetILForModule(self: SOSDac, moduleAddr: UInt64, rva: UInt32) -> UInt64 """
        pass

    def GetJitHelperFunctionName(self, addr):
        """ GetJitHelperFunctionName(self: SOSDac, addr: UInt64) -> str """
        pass

    def GetJitManagers(self):
        """ GetJitManagers(self: SOSDac) -> Array[JitManagerInfo] """
        pass

    def GetMetadataImport(self, module):
        """ GetMetadataImport(self: SOSDac, module: UInt64) -> MetadataImport """
        pass

    def GetMethodDescData(self, md, ip, data):
        """ GetMethodDescData(self: SOSDac, md: UInt64, ip: UInt64) -> (HResult, MethodDescData) """
        pass

    def GetMethodDescFromToken(self, module, token):
        """ GetMethodDescFromToken(self: SOSDac, module: UInt64, token: int) -> UInt64 """
        pass

    def GetMethodDescName(self, md):
        """ GetMethodDescName(self: SOSDac, md: UInt64) -> str """
        pass

    def GetMethodDescPtrFromFrame(self, frame):
        """ GetMethodDescPtrFromFrame(self: SOSDac, frame: UInt64) -> ClrDataAddress """
        pass

    def GetMethodDescPtrFromIP(self, frame):
        """ GetMethodDescPtrFromIP(self: SOSDac, frame: UInt64) -> ClrDataAddress """
        pass

    def GetMethodTableByEEClass(self, eeclass):
        """ GetMethodTableByEEClass(self: SOSDac, eeclass: UInt64) -> ClrDataAddress """
        pass

    def GetMethodTableData(self, addr, data):
        """ GetMethodTableData(self: SOSDac, addr: UInt64) -> (HResult, MethodTableData) """
        pass

    def GetMethodTableName(self, mt):
        """ GetMethodTableName(self: SOSDac, mt: UInt64) -> str """
        pass

    def GetMethodTableSlot(self, mt, slot):
        """ GetMethodTableSlot(self: SOSDac, mt: UInt64, slot: UInt32) -> UInt64 """
        pass

    def GetModuleData(self, module, data):
        """ GetModuleData(self: SOSDac, module: UInt64) -> (HResult, ModuleData) """
        pass

    def GetModuleList(self, assembly, count=None):
        """
        GetModuleList(self: SOSDac, assembly: UInt64) -> Array[ClrDataAddress]
        GetModuleList(self: SOSDac, assembly: UInt64, count: int) -> Array[ClrDataAddress]
        """
        pass

    def GetObjectData(self, obj, data):
        """ GetObjectData(self: SOSDac, obj: UInt64) -> (HResult, ObjectData) """
        pass

    def GetPEFileName(self, pefile):
        """ GetPEFileName(self: SOSDac, pefile: UInt64) -> str """
        pass

    def GetRCWData(self, rcw, data):
        """ GetRCWData(self: SOSDac, rcw: UInt64) -> (HResult, RcwData) """
        pass

    def GetRCWInterfaces(self, ccw, count):
        """ GetRCWInterfaces(self: SOSDac, ccw: UInt64, count: int) -> Array[COMInterfacePointerData] """
        pass

    def GetRejitData(self, md, ip):
        """ GetRejitData(self: SOSDac, md: UInt64, ip: UInt64) -> Array[RejitData] """
        pass

    def GetSegmentData(self, addr, data):
        """ GetSegmentData(self: SOSDac, addr: UInt64) -> (HResult, SegmentData) """
        pass

    def GetServerHeapDetails(self, addr, data):
        """ GetServerHeapDetails(self: SOSDac, addr: UInt64) -> (HResult, HeapDetails) """
        pass

    def GetSyncBlockData(self, index, data):
        """ GetSyncBlockData(self: SOSDac, index: int) -> (HResult, SyncBlockData) """
        pass

    def GetThreadData(self, address, data):
        """ GetThreadData(self: SOSDac, address: UInt64) -> (HResult, ThreadData) """
        pass

    def GetThreadFromThinlockId(self, id):
        """ GetThreadFromThinlockId(self: SOSDac, id: UInt32) -> ClrDataAddress """
        pass

    def GetThreadLocalModuleData(self, thread, index, data):
        """ GetThreadLocalModuleData(self: SOSDac, thread: UInt64, index: UInt32) -> (HResult, ThreadLocalModuleData) """
        pass

    def GetThreadPoolData(self, data):
        """ GetThreadPoolData(self: SOSDac) -> (HResult, ThreadPoolData) """
        pass

    def GetThreadStoreData(self, data):
        """ GetThreadStoreData(self: SOSDac) -> (HResult, ThreadStoreData) """
        pass

    def GetTlsIndex(self):
        """ GetTlsIndex(self: SOSDac) -> UInt32 """
        pass

    def GetWksHeapDetails(self, data):
        """ GetWksHeapDetails(self: SOSDac) -> (HResult, HeapDetails) """
        pass

    def GetWorkRequestData(self, request, data):
        """ GetWorkRequestData(self: SOSDac, request: UInt64) -> (HResult, WorkRequestData) """
        pass

    def TraverseLoaderHeap(self, heap, callback):
        """ TraverseLoaderHeap(self: SOSDac, heap: UInt64, callback: LoaderHeapTraverse) -> HResult """
        pass

    def TraverseModuleMap(self, mt, module, traverse):
        """ TraverseModuleMap(self: SOSDac, mt: ModuleMapTraverseKind, module: UInt64, traverse: ModuleMapTraverse) -> HResult """
        pass

    def TraverseStubHeap(self, heap, type, callback):
        """ TraverseStubHeap(self: SOSDac, heap: UInt64, type: int, callback: LoaderHeapTraverse) -> HResult """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, library: DacLibrary, ptr: IntPtr)
        __new__(cls: type, lib: DacLibrary, toClone: CallableCOMWrapper)
        """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    LoaderHeapTraverse = None
    ModuleMapTraverse = None
    ModuleMapTraverseKind = None


class SOSDac6(CallableCOMWrapper, IDisposable):
    """
    This is an undocumented, untested, and unsupported interface.  Do not use.
    
    SOSDac6(library: DacLibrary, ptr: IntPtr)
    SOSDac6(toClone: CallableCOMWrapper)
    """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def GetMethodTableCollectibleData(self, mt, data):
        """ GetMethodTableCollectibleData(self: SOSDac6, mt: UInt64) -> (HResult, MethodTableCollectibleData) """
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
    def __new__(self, *__args):
        """
        __new__(cls: type, library: DacLibrary, ptr: IntPtr)
        __new__(cls: type, toClone: CallableCOMWrapper)
        """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SOSDac8(CallableCOMWrapper, IDisposable):
    """
    This is an undocumented, untested, and unsupported interface.  Do not use.
    
    SOSDac8(library: DacLibrary, ptr: IntPtr)
    """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def GetAssemblyLoadContext(self, methodTable, assemblyLoadContext):
        """ GetAssemblyLoadContext(self: SOSDac8, methodTable: ClrDataAddress) -> (HResult, ClrDataAddress) """
        pass

    def GetFinalizationFillPointers(self, heap=None):
        """
        GetFinalizationFillPointers(self: SOSDac8) -> Array[ClrDataAddress]
        GetFinalizationFillPointers(self: SOSDac8, heap: UInt64) -> Array[ClrDataAddress]
        """
        pass

    def GetGenerationTable(self, heap=None):
        """
        GetGenerationTable(self: SOSDac8) -> Array[GenerationData]
        GetGenerationTable(self: SOSDac8, heap: UInt64) -> Array[GenerationData]
        """
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
    def __new__(self, library, ptr):
        """ __new__(cls: type, library: DacLibrary, ptr: IntPtr) """
        pass

    GenerationCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenerationCount(self: SOSDac8) -> int

"""

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SOSHandleEnum(CallableCOMWrapper, IDisposable):
    """ SOSHandleEnum(library: DacLibrary, pUnk: IntPtr) """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def ReadHandles(self, handles):
        """ ReadHandles(self: SOSHandleEnum, handles: Span[HandleData]) -> int """
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
    def __new__(self, library, pUnk):
        """ __new__(cls: type, library: DacLibrary, pUnk: IntPtr) """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SOSStackRefEnum(CallableCOMWrapper, IDisposable):
    """ SOSStackRefEnum(library: DacLibrary, pUnk: IntPtr) """
    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper, disposing: bool) """
        pass

    def ReadStackReferences(self, stackRefs):
        """ ReadStackReferences(self: SOSStackRefEnum, stackRefs: Span[StackRefData]) -> int """
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
    def __new__(self, library, pUnk):
        """ __new__(cls: type, library: DacLibrary, pUnk: IntPtr) """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class StackRefData(object):
    # no doc
    Address = None
    Flags = None
    HasRegisterInformation = None
    Object = None
    Offset = None
    Register = None
    Source = None
    SourceType = None
    StackPointer = None


class SyncBlockData(object):
    # no doc
    AdditionalThreadCount = None
    Address = None
    AppDomain = None
    COMFlags = None
    Free = None
    HoldingThread = None
    MonitorHeld = None
    Object = None
    Recursion = None
    TotalSyncBlockCount = None


class ThreadData(object):
    # no doc
    AllocationContextLimit = None
    AllocationContextPointer = None
    Context = None
    Domain = None
    FiberData = None
    FirstNestedException = None
    Frame = None
    LastThrownObjectHandle = None
    LockCount = None
    ManagedThreadId = None
    NextThread = None
    OSThreadId = None
    PreemptiveGCDisabled = None
    State = None
    Teb = None


class ThreadLocalModuleData(object):
    # no doc
    ClassData = None
    DynamicClassTable = None
    GCStaticDataStart = None
    ModuleIndex = None
    NonGCStaticDataStart = None
    ThreadAddress = None


class ThreadPoolData(object):
    # no doc
    AsyncTimerCallbackCompletionFPtr = None
    CpuUtilization = None
    CurrentLimitTotalCPThreads = None
    FirstUnmanagedWorkRequest = None
    HillClimbingLog = None
    HillClimbingLogFirstIndex = None
    HillClimbingLogSize = None
    MaxFreeCPThreads = None
    MaxLimitTotalCPThreads = None
    MaxLimitTotalWorkerThreads = None
    MinLimitTotalCPThreads = None
    MinLimitTotalWorkerThreads = None
    NumCPThreads = None
    NumFreeCPThreads = None
    NumIdleWorkerThreads = None
    NumRetiredCPThreads = None
    NumRetiredWorkerThreads = None
    NumTimers = None
    NumWorkingWorkerThreads = None


class ThreadStoreData(object):
    # no doc
    BackgroundThreadCount = None
    DeadThreadCount = None
    FinalizerThread = None
    FirstThread = None
    GCThread = None
    HostConfig = None
    PendingThreadCount = None
    ThreadCount = None
    UnstartedThreadCount = None


class WorkRequestData(object):
    # no doc
    Context = None
    Function = None
    NextWorkRequest = None


