# encoding: utf-8
# module System.Reflection calls itself Reflection
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Reflection.Metadata, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AmbiguousMatchException(SystemException, ISerializable, _Exception):
    """
    AmbiguousMatchException()
    AmbiguousMatchException(message: str)
    AmbiguousMatchException(message: str, inner: Exception)
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
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ICustomAttributeProvider:
    # no doc
    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: ICustomAttributeProvider, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: ICustomAttributeProvider, inherit: bool) -> Array[object]
        """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: ICustomAttributeProvider, attributeType: Type, inherit: bool) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Assembly(object, _Assembly, IEvidenceFactory, ICustomAttributeProvider, ISerializable):
    # no doc
    def CreateInstance(self, typeName, ignoreCase=None, bindingAttr=None, binder=None, args=None, culture=None, activationAttributes=None):
        """
        CreateInstance(self: Assembly, typeName: str) -> object
        CreateInstance(self: Assembly, typeName: str, ignoreCase: bool) -> object
        CreateInstance(self: Assembly, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        """
        pass

    @staticmethod
    def CreateQualifiedName(assemblyName, typeName):
        """ CreateQualifiedName(assemblyName: str, typeName: str) -> str """
        pass

    def Equals(self, o):
        """ Equals(self: Assembly, o: object) -> bool """
        pass

    @staticmethod
    def GetAssembly(type):
        """ GetAssembly(type: Type) -> Assembly """
        pass

    @staticmethod
    def GetCallingAssembly():
        """ GetCallingAssembly() -> Assembly """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: Assembly, inherit: bool) -> Array[object]
        GetCustomAttributes(self: Assembly, attributeType: Type, inherit: bool) -> Array[object]
        """
        pass

    def GetCustomAttributesData(self):
        """ GetCustomAttributesData(self: Assembly) -> IList[CustomAttributeData] """
        pass

    @staticmethod
    def GetEntryAssembly():
        """ GetEntryAssembly() -> Assembly """
        pass

    @staticmethod
    def GetExecutingAssembly():
        """ GetExecutingAssembly() -> Assembly """
        pass

    def GetExportedTypes(self):
        """ GetExportedTypes(self: Assembly) -> Array[Type] """
        pass

    def GetFile(self, name):
        """ GetFile(self: Assembly, name: str) -> FileStream """
        pass

    def GetFiles(self, getResourceModules=None):
        """
        GetFiles(self: Assembly) -> Array[FileStream]
        GetFiles(self: Assembly, getResourceModules: bool) -> Array[FileStream]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Assembly) -> int """
        pass

    def GetLoadedModules(self, getResourceModules=None):
        """
        GetLoadedModules(self: Assembly) -> Array[Module]
        GetLoadedModules(self: Assembly, getResourceModules: bool) -> Array[Module]
        """
        pass

    def GetManifestResourceInfo(self, resourceName):
        """ GetManifestResourceInfo(self: Assembly, resourceName: str) -> ManifestResourceInfo """
        pass

    def GetManifestResourceNames(self):
        """ GetManifestResourceNames(self: Assembly) -> Array[str] """
        pass

    def GetManifestResourceStream(self, *__args):
        """
        GetManifestResourceStream(self: Assembly, type: Type, name: str) -> Stream
        GetManifestResourceStream(self: Assembly, name: str) -> Stream
        """
        pass

    def GetModule(self, name):
        """ GetModule(self: Assembly, name: str) -> Module """
        pass

    def GetModules(self, getResourceModules=None):
        """
        GetModules(self: Assembly) -> Array[Module]
        GetModules(self: Assembly, getResourceModules: bool) -> Array[Module]
        """
        pass

    def GetName(self, copiedName=None):
        """
        GetName(self: Assembly, copiedName: bool) -> AssemblyName
        GetName(self: Assembly) -> AssemblyName
        """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Assembly, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetReferencedAssemblies(self):
        """ GetReferencedAssemblies(self: Assembly) -> Array[AssemblyName] """
        pass

    def GetSatelliteAssembly(self, culture, version=None):
        """
        GetSatelliteAssembly(self: Assembly, culture: CultureInfo) -> Assembly
        GetSatelliteAssembly(self: Assembly, culture: CultureInfo, version: Version) -> Assembly
        """
        pass

    def GetType(self, name=None, throwOnError=None, ignoreCase=None):
        """
        GetType(self: Assembly, name: str) -> Type
        GetType(self: Assembly, name: str, throwOnError: bool) -> Type
        GetType(self: Assembly, name: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        pass

    def GetTypes(self):
        """ GetTypes(self: Assembly) -> Array[Type] """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: Assembly, attributeType: Type, inherit: bool) -> bool """
        pass

    @staticmethod
    def Load(*__args):
        """
        Load(assemblyString: str) -> Assembly
        Load(assemblyString: str, assemblySecurity: Evidence) -> Assembly
        Load(assemblyRef: AssemblyName) -> Assembly
        Load(assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly
        Load(rawAssembly: Array[Byte]) -> Assembly
        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte]) -> Assembly
        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityContextSource: SecurityContextSource) -> Assembly
        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityEvidence: Evidence) -> Assembly
        """
        pass

    @staticmethod
    def LoadFile(path, securityEvidence=None):
        """
        LoadFile(path: str) -> Assembly
        LoadFile(path: str, securityEvidence: Evidence) -> Assembly
        """
        pass

    @staticmethod
    def LoadFrom(assemblyFile, *__args):
        """
        LoadFrom(assemblyFile: str) -> Assembly
        LoadFrom(assemblyFile: str, securityEvidence: Evidence) -> Assembly
        LoadFrom(assemblyFile: str, securityEvidence: Evidence, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly
        LoadFrom(assemblyFile: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly
        """
        pass

    def LoadModule(self, moduleName, rawModule, rawSymbolStore=None):
        """
        LoadModule(self: Assembly, moduleName: str, rawModule: Array[Byte]) -> Module
        LoadModule(self: Assembly, moduleName: str, rawModule: Array[Byte], rawSymbolStore: Array[Byte]) -> Module
        """
        pass

    @staticmethod
    def LoadWithPartialName(partialName, securityEvidence=None):
        """
        LoadWithPartialName(partialName: str) -> Assembly
        LoadWithPartialName(partialName: str, securityEvidence: Evidence) -> Assembly
        """
        pass

    @staticmethod
    def ReflectionOnlyLoad(*__args):
        """
        ReflectionOnlyLoad(assemblyString: str) -> Assembly
        ReflectionOnlyLoad(rawAssembly: Array[Byte]) -> Assembly
        """
        pass

    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile):
        """ ReflectionOnlyLoadFrom(assemblyFile: str) -> Assembly """
        pass

    def ToString(self):
        """ ToString(self: Assembly) -> str """
        pass

    @staticmethod
    def UnsafeLoadFrom(assemblyFile):
        """ UnsafeLoadFrom(assemblyFile: str) -> Assembly """
        pass

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: Assembly) -> list """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: Assembly) -> object """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeBase(self: Assembly) -> str

"""

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomAttributes(self: Assembly) -> IEnumerable[CustomAttributeData]

"""

    DefinedTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefinedTypes(self: Assembly) -> IEnumerable[TypeInfo]

"""

    EntryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryPoint(self: Assembly) -> MethodInfo

"""

    EscapedCodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EscapedCodeBase(self: Assembly) -> str

"""

    Evidence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Evidence(self: Assembly) -> Evidence

"""

    ExportedTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedTypes(self: Assembly) -> IEnumerable[Type]

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: Assembly) -> str

"""

    GlobalAssemblyCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalAssemblyCache(self: Assembly) -> bool

"""

    HostContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostContext(self: Assembly) -> Int64

"""

    ImageRuntimeVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageRuntimeVersion(self: Assembly) -> str

"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDynamic(self: Assembly) -> bool

"""

    IsFullyTrusted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFullyTrusted(self: Assembly) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Assembly) -> str

"""

    ManifestModule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManifestModule(self: Assembly) -> Module

"""

    Modules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modules(self: Assembly) -> IEnumerable[Module]

"""

    PermissionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PermissionSet(self: Assembly) -> PermissionSet

"""

    ReflectionOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectionOnly(self: Assembly) -> bool

"""

    SecurityRuleSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecurityRuleSet(self: Assembly) -> SecurityRuleSet

"""


    ModuleResolve = None


class AssemblyAlgorithmIdAttribute(Attribute, _Attribute):
    """
    AssemblyAlgorithmIdAttribute(algorithmId: AssemblyHashAlgorithm)
    AssemblyAlgorithmIdAttribute(algorithmId: UInt32)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, algorithmId):
        """
        __new__(cls: type, algorithmId: AssemblyHashAlgorithm)
        __new__(cls: type, algorithmId: UInt32)
        """
        pass

    AlgorithmId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlgorithmId(self: AssemblyAlgorithmIdAttribute) -> UInt32

"""



class AssemblyCompanyAttribute(Attribute, _Attribute):
    """ AssemblyCompanyAttribute(company: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, company):
        """ __new__(cls: type, company: str) """
        pass

    Company = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Company(self: AssemblyCompanyAttribute) -> str

"""



class AssemblyConfigurationAttribute(Attribute, _Attribute):
    """ AssemblyConfigurationAttribute(configuration: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, configuration):
        """ __new__(cls: type, configuration: str) """
        pass

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: AssemblyConfigurationAttribute) -> str

"""



class AssemblyContentType(Enum, IComparable, IFormattable, IConvertible):
    """ enum AssemblyContentType, values: Default (0), WindowsRuntime (1) """
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

    Default = None
    value__ = None
    WindowsRuntime = None


class AssemblyCopyrightAttribute(Attribute, _Attribute):
    """ AssemblyCopyrightAttribute(copyright: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, copyright):
        """ __new__(cls: type, copyright: str) """
        pass

    Copyright = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Copyright(self: AssemblyCopyrightAttribute) -> str

"""



class AssemblyCultureAttribute(Attribute, _Attribute):
    """ AssemblyCultureAttribute(culture: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, culture):
        """ __new__(cls: type, culture: str) """
        pass

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Culture(self: AssemblyCultureAttribute) -> str

"""



class AssemblyDefaultAliasAttribute(Attribute, _Attribute):
    """ AssemblyDefaultAliasAttribute(defaultAlias: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, defaultAlias):
        """ __new__(cls: type, defaultAlias: str) """
        pass

    DefaultAlias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultAlias(self: AssemblyDefaultAliasAttribute) -> str

"""



class AssemblyDelaySignAttribute(Attribute, _Attribute):
    """ AssemblyDelaySignAttribute(delaySign: bool) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, delaySign):
        """ __new__(cls: type, delaySign: bool) """
        pass

    DelaySign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DelaySign(self: AssemblyDelaySignAttribute) -> bool

"""



class AssemblyDescriptionAttribute(Attribute, _Attribute):
    """ AssemblyDescriptionAttribute(description: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description):
        """ __new__(cls: type, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: AssemblyDescriptionAttribute) -> str

"""



class AssemblyFileVersionAttribute(Attribute, _Attribute):
    """ AssemblyFileVersionAttribute(version: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, version):
        """ __new__(cls: type, version: str) """
        pass

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AssemblyFileVersionAttribute) -> str

"""



class AssemblyFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) AssemblyFlags, values: ContentTypeMask (3584), DisableJitCompileOptimizer (16384), EnableJitCompileTracking (32768), PublicKey (1), Retargetable (256), WindowsRuntime (512) """
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

    ContentTypeMask = None
    DisableJitCompileOptimizer = None
    EnableJitCompileTracking = None
    PublicKey = None
    Retargetable = None
    value__ = None
    WindowsRuntime = None


class AssemblyFlagsAttribute(Attribute, _Attribute):
    """
    AssemblyFlagsAttribute(flags: UInt32)
    AssemblyFlagsAttribute(assemblyFlags: int)
    AssemblyFlagsAttribute(assemblyFlags: AssemblyNameFlags)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, flags: UInt32)
        __new__(cls: type, assemblyFlags: int)
        __new__(cls: type, assemblyFlags: AssemblyNameFlags)
        """
        pass

    AssemblyFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyFlags(self: AssemblyFlagsAttribute) -> int

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: AssemblyFlagsAttribute) -> UInt32

"""



class AssemblyHashAlgorithm(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the hash algorithms used for hashing assembly files and for generating the strong name.
    
    enum AssemblyHashAlgorithm, values: MD5 (32771), None (0), Sha1 (32772), Sha256 (32780), Sha384 (32781), Sha512 (32782)
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

    MD5 = None
    None = None
    Sha1 = None
    Sha256 = None
    Sha384 = None
    Sha512 = None
    value__ = None


class AssemblyInformationalVersionAttribute(Attribute, _Attribute):
    """ AssemblyInformationalVersionAttribute(informationalVersion: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, informationalVersion):
        """ __new__(cls: type, informationalVersion: str) """
        pass

    InformationalVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InformationalVersion(self: AssemblyInformationalVersionAttribute) -> str

"""



class AssemblyKeyFileAttribute(Attribute, _Attribute):
    """ AssemblyKeyFileAttribute(keyFile: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, keyFile):
        """ __new__(cls: type, keyFile: str) """
        pass

    KeyFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyFile(self: AssemblyKeyFileAttribute) -> str

"""



class AssemblyKeyNameAttribute(Attribute, _Attribute):
    """ AssemblyKeyNameAttribute(keyName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, keyName):
        """ __new__(cls: type, keyName: str) """
        pass

    KeyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyName(self: AssemblyKeyNameAttribute) -> str

"""



class AssemblyMetadataAttribute(Attribute, _Attribute):
    """ AssemblyMetadataAttribute(key: str, value: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, key, value):
        """ __new__(cls: type, key: str, value: str) """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: AssemblyMetadataAttribute) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: AssemblyMetadataAttribute) -> str

"""



class AssemblyName(object, _AssemblyName, ICloneable, ISerializable, IDeserializationCallback):
    """
    AssemblyName()
    AssemblyName(assemblyName: str)
    """
    def Clone(self):
        """ Clone(self: AssemblyName) -> object """
        pass

    @staticmethod
    def GetAssemblyName(assemblyFile):
        """ GetAssemblyName(assemblyFile: str) -> AssemblyName """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: AssemblyName, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetPublicKey(self):
        """ GetPublicKey(self: AssemblyName) -> Array[Byte] """
        pass

    def GetPublicKeyToken(self):
        """ GetPublicKeyToken(self: AssemblyName) -> Array[Byte] """
        pass

    def OnDeserialization(self, sender):
        """ OnDeserialization(self: AssemblyName, sender: object) """
        pass

    @staticmethod
    def ReferenceMatchesDefinition(reference, definition):
        """ ReferenceMatchesDefinition(reference: AssemblyName, definition: AssemblyName) -> bool """
        pass

    def SetPublicKey(self, publicKey):
        """ SetPublicKey(self: AssemblyName, publicKey: Array[Byte]) """
        pass

    def SetPublicKeyToken(self, publicKeyToken):
        """ SetPublicKeyToken(self: AssemblyName, publicKeyToken: Array[Byte]) """
        pass

    def ToString(self):
        """ ToString(self: AssemblyName) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, assemblyName=None):
        """
        __new__(cls: type)
        __new__(cls: type, assemblyName: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    CodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeBase(self: AssemblyName) -> str

Set: CodeBase(self: AssemblyName) = value
"""

    ContentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentType(self: AssemblyName) -> AssemblyContentType

Set: ContentType(self: AssemblyName) = value
"""

    CultureInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CultureInfo(self: AssemblyName) -> CultureInfo

Set: CultureInfo(self: AssemblyName) = value
"""

    CultureName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CultureName(self: AssemblyName) -> str

Set: CultureName(self: AssemblyName) = value
"""

    EscapedCodeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EscapedCodeBase(self: AssemblyName) -> str

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: AssemblyName) -> AssemblyNameFlags

Set: Flags(self: AssemblyName) = value
"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: AssemblyName) -> str

"""

    HashAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HashAlgorithm(self: AssemblyName) -> AssemblyHashAlgorithm

Set: HashAlgorithm(self: AssemblyName) = value
"""

    KeyPair = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyPair(self: AssemblyName) -> StrongNameKeyPair

Set: KeyPair(self: AssemblyName) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AssemblyName) -> str

Set: Name(self: AssemblyName) = value
"""

    ProcessorArchitecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProcessorArchitecture(self: AssemblyName) -> ProcessorArchitecture

Set: ProcessorArchitecture(self: AssemblyName) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AssemblyName) -> Version

Set: Version(self: AssemblyName) = value
"""

    VersionCompatibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VersionCompatibility(self: AssemblyName) -> AssemblyVersionCompatibility

Set: VersionCompatibility(self: AssemblyName) = value
"""



class AssemblyNameFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) AssemblyNameFlags, values: EnableJITcompileOptimizer (16384), EnableJITcompileTracking (32768), None (0), PublicKey (1), Retargetable (256) """
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

    EnableJITcompileOptimizer = None
    EnableJITcompileTracking = None
    None = None
    PublicKey = None
    Retargetable = None
    value__ = None


class AssemblyNameProxy(MarshalByRefObject):
    """ AssemblyNameProxy() """
    def GetAssemblyName(self, assemblyFile):
        """ GetAssemblyName(self: AssemblyNameProxy, assemblyFile: str) -> AssemblyName """
        pass


class AssemblyProductAttribute(Attribute, _Attribute):
    """ AssemblyProductAttribute(product: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, product):
        """ __new__(cls: type, product: str) """
        pass

    Product = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Product(self: AssemblyProductAttribute) -> str

"""



class AssemblySignatureKeyAttribute(Attribute, _Attribute):
    """ AssemblySignatureKeyAttribute(publicKey: str, countersignature: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, publicKey, countersignature):
        """ __new__(cls: type, publicKey: str, countersignature: str) """
        pass

    Countersignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Countersignature(self: AssemblySignatureKeyAttribute) -> str

"""

    PublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublicKey(self: AssemblySignatureKeyAttribute) -> str

"""



class AssemblyTitleAttribute(Attribute, _Attribute):
    """ AssemblyTitleAttribute(title: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, title):
        """ __new__(cls: type, title: str) """
        pass

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: AssemblyTitleAttribute) -> str

"""



class AssemblyTrademarkAttribute(Attribute, _Attribute):
    """ AssemblyTrademarkAttribute(trademark: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, trademark):
        """ __new__(cls: type, trademark: str) """
        pass

    Trademark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Trademark(self: AssemblyTrademarkAttribute) -> str

"""



class AssemblyVersionAttribute(Attribute, _Attribute):
    """ AssemblyVersionAttribute(version: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, version):
        """ __new__(cls: type, version: str) """
        pass

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AssemblyVersionAttribute) -> str

"""



class Binder(object):
    # no doc
    def BindToField(self, bindingAttr, match, value, culture):
        """ BindToField(self: Binder, bindingAttr: BindingFlags, match: Array[FieldInfo], value: object, culture: CultureInfo) -> FieldInfo """
        pass

    def BindToMethod(self, bindingAttr, match, args, modifiers, culture, names, state):
        """ BindToMethod(self: Binder, bindingAttr: BindingFlags, match: Array[MethodBase], args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, names: Array[str]) -> (MethodBase, Array[object], object) """
        pass

    def ChangeType(self, value, type, culture):
        """ ChangeType(self: Binder, value: object, type: Type, culture: CultureInfo) -> object """
        pass

    def ReorderArgumentArray(self, args, state):
        """ ReorderArgumentArray(self: Binder, args: Array[object], state: object) -> Array[object] """
        pass

    def SelectMethod(self, bindingAttr, match, types, modifiers):
        """ SelectMethod(self: Binder, bindingAttr: BindingFlags, match: Array[MethodBase], types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodBase """
        pass

    def SelectProperty(self, bindingAttr, match, returnType, indexes, modifiers):
        """ SelectProperty(self: Binder, bindingAttr: BindingFlags, match: Array[PropertyInfo], returnType: Type, indexes: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo """
        pass


class BindingFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) BindingFlags, values: CreateInstance (512), DeclaredOnly (2), Default (0), ExactBinding (65536), FlattenHierarchy (64), GetField (1024), GetProperty (4096), IgnoreCase (1), IgnoreReturn (16777216), Instance (4), InvokeMethod (256), NonPublic (32), OptionalParamBinding (262144), Public (16), PutDispProperty (16384), PutRefDispProperty (32768), SetField (2048), SetProperty (8192), Static (8), SuppressChangeType (131072) """
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

    CreateInstance = None
    DeclaredOnly = None
    Default = None
    ExactBinding = None
    FlattenHierarchy = None
    GetField = None
    GetProperty = None
    IgnoreCase = None
    IgnoreReturn = None
    Instance = None
    InvokeMethod = None
    NonPublic = None
    OptionalParamBinding = None
    Public = None
    PutDispProperty = None
    PutRefDispProperty = None
    SetField = None
    SetProperty = None
    Static = None
    SuppressChangeType = None
    value__ = None


class CallingConventions(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) CallingConventions, values: Any (3), ExplicitThis (64), HasThis (32), Standard (1), VarArgs (2) """
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

    Any = None
    ExplicitThis = None
    HasThis = None
    Standard = None
    value__ = None
    VarArgs = None


class MemberInfo(object, ICustomAttributeProvider, _MemberInfo):
    # no doc
    def Equals(self, obj):
        """ Equals(self: MemberInfo, obj: object) -> bool """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: MemberInfo, inherit: bool) -> Array[object]
        GetCustomAttributes(self: MemberInfo, attributeType: Type, inherit: bool) -> Array[object]
        """
        pass

    def GetCustomAttributesData(self):
        """ GetCustomAttributesData(self: MemberInfo) -> IList[CustomAttributeData] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MemberInfo) -> int """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: MemberInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomAttributes(self: MemberInfo) -> IEnumerable[CustomAttributeData]

"""

    DeclaringType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaringType(self: MemberInfo) -> Type

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: MemberInfo) -> MemberTypes

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: MemberInfo) -> int

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: MemberInfo) -> Module

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MemberInfo) -> str

"""

    ReflectedType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReflectedType(self: MemberInfo) -> Type

"""



class MethodBase(MemberInfo, ICustomAttributeProvider, _MemberInfo, _MethodBase):
    # no doc
    def Equals(self, obj):
        """ Equals(self: MethodBase, obj: object) -> bool """
        pass

    @staticmethod
    def GetCurrentMethod():
        """ GetCurrentMethod() -> MethodBase """
        pass

    def GetGenericArguments(self):
        """ GetGenericArguments(self: MethodBase) -> Array[Type] """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MethodBase) -> int """
        pass

    def GetMethodBody(self):
        """ GetMethodBody(self: MethodBase) -> MethodBody """
        pass

    @staticmethod
    def GetMethodFromHandle(handle, declaringType=None):
        """
        GetMethodFromHandle(handle: RuntimeMethodHandle) -> MethodBase
        GetMethodFromHandle(handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle) -> MethodBase
        """
        pass

    def GetMethodImplementationFlags(self):
        """ GetMethodImplementationFlags(self: MethodBase) -> MethodImplAttributes """
        pass

    def GetParameters(self):
        """ GetParameters(self: MethodBase) -> Array[ParameterInfo] """
        pass

    def Invoke(self, obj, *__args):
        """
        Invoke(self: MethodBase, obj: object, parameters: Array[object]) -> object
        Invoke(self: MethodBase, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: MethodBase) -> MethodAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CallingConvention(self: MethodBase) -> CallingConventions

"""

    ContainsGenericParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsGenericParameters(self: MethodBase) -> bool

"""

    IsAbstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAbstract(self: MethodBase) -> bool

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssembly(self: MethodBase) -> bool

"""

    IsConstructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConstructor(self: MethodBase) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamily(self: MethodBase) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyAndAssembly(self: MethodBase) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyOrAssembly(self: MethodBase) -> bool

"""

    IsFinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFinal(self: MethodBase) -> bool

"""

    IsGenericMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGenericMethod(self: MethodBase) -> bool

"""

    IsGenericMethodDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGenericMethodDefinition(self: MethodBase) -> bool

"""

    IsHideBySig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHideBySig(self: MethodBase) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: MethodBase) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: MethodBase) -> bool

"""

    IsSecurityCritical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecurityCritical(self: MethodBase) -> bool

"""

    IsSecuritySafeCritical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecuritySafeCritical(self: MethodBase) -> bool

"""

    IsSecurityTransparent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecurityTransparent(self: MethodBase) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: MethodBase) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: MethodBase) -> bool

"""

    IsVirtual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVirtual(self: MethodBase) -> bool

"""

    MethodHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodHandle(self: MethodBase) -> RuntimeMethodHandle

"""

    MethodImplementationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodImplementationFlags(self: MethodBase) -> MethodImplAttributes

"""



class ConstructorInfo(MethodBase, ICustomAttributeProvider, _MemberInfo, _MethodBase, _ConstructorInfo):
    # no doc
    def Equals(self, obj):
        """ Equals(self: ConstructorInfo, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ConstructorInfo) -> int """
        pass

    def Invoke(self, *__args):
        """
        Invoke(self: ConstructorInfo, parameters: Array[object]) -> object
        Invoke(self: ConstructorInfo, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: ConstructorInfo) -> MemberTypes

"""


    ConstructorName = '.ctor'
    TypeConstructorName = '.cctor'


class CustomAttributeData(object):
    # no doc
    def Equals(self, obj):
        """ Equals(self: CustomAttributeData, obj: object) -> bool """
        pass

    @staticmethod
    def GetCustomAttributes(target):
        """
        GetCustomAttributes(target: MemberInfo) -> IList[CustomAttributeData]
        GetCustomAttributes(target: Module) -> IList[CustomAttributeData]
        GetCustomAttributes(target: Assembly) -> IList[CustomAttributeData]
        GetCustomAttributes(target: ParameterInfo) -> IList[CustomAttributeData]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CustomAttributeData) -> int """
        pass

    def ToString(self):
        """ ToString(self: CustomAttributeData) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AttributeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeType(self: CustomAttributeData) -> Type

"""

    Constructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constructor(self: CustomAttributeData) -> ConstructorInfo

"""

    ConstructorArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConstructorArguments(self: CustomAttributeData) -> IList[CustomAttributeTypedArgument]

"""

    NamedArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamedArguments(self: CustomAttributeData) -> IList[CustomAttributeNamedArgument]

"""



class CustomAttributeExtensions(object):
    # no doc
    @staticmethod
    def GetCustomAttribute(element, *__args):
# Error generating skeleton for function GetCustomAttribute: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def GetCustomAttributes(element, *__args):
        """
        GetCustomAttributes(element: Assembly) -> IEnumerable[Attribute]
        GetCustomAttributes[T](element: ParameterInfo) -> IEnumerable[T]
        GetCustomAttributes[T](element: MemberInfo) -> IEnumerable[T]
        GetCustomAttributes[T](element: Module) -> IEnumerable[T]
        GetCustomAttributes[T](element: Assembly) -> IEnumerable[T]
        GetCustomAttributes(element: ParameterInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: ParameterInfo, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: Module, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: Assembly, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: ParameterInfo, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: ParameterInfo) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo) -> IEnumerable[Attribute]
        GetCustomAttributes(element: Module) -> IEnumerable[Attribute]
        GetCustomAttributes[T](element: MemberInfo, inherit: bool) -> IEnumerable[T]
        GetCustomAttributes[T](element: ParameterInfo, inherit: bool) -> IEnumerable[T]
        """
        pass

    @staticmethod
    def IsDefined(element, attributeType, inherit=None):
        """
        IsDefined(element: Assembly, attributeType: Type) -> bool
        IsDefined(element: Module, attributeType: Type) -> bool
        IsDefined(element: MemberInfo, attributeType: Type) -> bool
        IsDefined(element: ParameterInfo, attributeType: Type) -> bool
        IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool
        IsDefined(element: ParameterInfo, attributeType: Type, inherit: bool) -> bool
        """
        pass

    __all__ = [
        'GetCustomAttribute',
        'GetCustomAttributes',
        'IsDefined',
    ]


class CustomAttributeFormatException(FormatException, ISerializable, _Exception):
    """
    CustomAttributeFormatException()
    CustomAttributeFormatException(message: str)
    CustomAttributeFormatException(message: str, inner: Exception)
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


class CustomAttributeNamedArgument(object):
    """
    CustomAttributeNamedArgument(memberInfo: MemberInfo, value: object)
    CustomAttributeNamedArgument(memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument)
    """
    def Equals(self, obj):
        """ Equals(self: CustomAttributeNamedArgument, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CustomAttributeNamedArgument) -> int """
        pass

    def ToString(self):
        """ ToString(self: CustomAttributeNamedArgument) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, memberInfo, *__args):
        """
        __new__[CustomAttributeNamedArgument]() -> CustomAttributeNamedArgument
        
        __new__(cls: type, memberInfo: MemberInfo, value: object)
        __new__(cls: type, memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsField(self: CustomAttributeNamedArgument) -> bool

"""

    MemberInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberInfo(self: CustomAttributeNamedArgument) -> MemberInfo

"""

    MemberName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberName(self: CustomAttributeNamedArgument) -> str

"""

    TypedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypedValue(self: CustomAttributeNamedArgument) -> CustomAttributeTypedArgument

"""



class CustomAttributeTypedArgument(object):
    """
    CustomAttributeTypedArgument(argumentType: Type, value: object)
    CustomAttributeTypedArgument(value: object)
    """
    def Equals(self, obj):
        """ Equals(self: CustomAttributeTypedArgument, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CustomAttributeTypedArgument) -> int """
        pass

    def ToString(self):
        """ ToString(self: CustomAttributeTypedArgument) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[CustomAttributeTypedArgument]() -> CustomAttributeTypedArgument
        
        __new__(cls: type, argumentType: Type, value: object)
        __new__(cls: type, value: object)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ArgumentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArgumentType(self: CustomAttributeTypedArgument) -> Type

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: CustomAttributeTypedArgument) -> object

"""



class DeclarativeSecurityAction(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the security actions that can be performed using declarative security.
    
    enum DeclarativeSecurityAction, values: Assert (3), Demand (2), Deny (4), InheritanceDemand (7), LinkDemand (6), None (0), PermitOnly (5), RequestMinimum (8), RequestOptional (9), RequestRefuse (10)
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

    Assert = None
    Demand = None
    Deny = None
    InheritanceDemand = None
    LinkDemand = None
    None = None
    PermitOnly = None
    RequestMinimum = None
    RequestOptional = None
    RequestRefuse = None
    value__ = None


class DefaultMemberAttribute(Attribute, _Attribute):
    """ DefaultMemberAttribute(memberName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, memberName):
        """ __new__(cls: type, memberName: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    MemberName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberName(self: DefaultMemberAttribute) -> str

"""



class EventAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) EventAttributes, values: None (0), ReservedMask (1024), RTSpecialName (1024), SpecialName (512) """
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
    ReservedMask = None
    RTSpecialName = None
    SpecialName = None
    value__ = None


class EventInfo(MemberInfo, ICustomAttributeProvider, _MemberInfo, _EventInfo):
    # no doc
    def AddEventHandler(self, target, handler):
        """ AddEventHandler(self: EventInfo, target: object, handler: Delegate) """
        pass

    def Equals(self, obj):
        """ Equals(self: EventInfo, obj: object) -> bool """
        pass

    def GetAddMethod(self, nonPublic=None):
        """
        GetAddMethod(self: EventInfo) -> MethodInfo
        GetAddMethod(self: EventInfo, nonPublic: bool) -> MethodInfo
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EventInfo) -> int """
        pass

    def GetOtherMethods(self, nonPublic=None):
        """
        GetOtherMethods(self: EventInfo, nonPublic: bool) -> Array[MethodInfo]
        GetOtherMethods(self: EventInfo) -> Array[MethodInfo]
        """
        pass

    def GetRaiseMethod(self, nonPublic=None):
        """
        GetRaiseMethod(self: EventInfo) -> MethodInfo
        GetRaiseMethod(self: EventInfo, nonPublic: bool) -> MethodInfo
        """
        pass

    def GetRemoveMethod(self, nonPublic=None):
        """
        GetRemoveMethod(self: EventInfo) -> MethodInfo
        GetRemoveMethod(self: EventInfo, nonPublic: bool) -> MethodInfo
        """
        pass

    def RemoveEventHandler(self, target, handler):
        """ RemoveEventHandler(self: EventInfo, target: object, handler: Delegate) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    AddMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddMethod(self: EventInfo) -> MethodInfo

"""

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: EventInfo) -> EventAttributes

"""

    EventHandlerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventHandlerType(self: EventInfo) -> Type

"""

    IsMulticast = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMulticast(self: EventInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: EventInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: EventInfo) -> MemberTypes

"""

    RaiseMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RaiseMethod(self: EventInfo) -> MethodInfo

"""

    RemoveMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemoveMethod(self: EventInfo) -> MethodInfo

"""



class ExceptionHandlingClause(object):
    # no doc
    def ToString(self):
        """ ToString(self: ExceptionHandlingClause) -> str """
        pass

    CatchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CatchType(self: ExceptionHandlingClause) -> Type

"""

    FilterOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterOffset(self: ExceptionHandlingClause) -> int

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: ExceptionHandlingClause) -> ExceptionHandlingClauseOptions

"""

    HandlerLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HandlerLength(self: ExceptionHandlingClause) -> int

"""

    HandlerOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HandlerOffset(self: ExceptionHandlingClause) -> int

"""

    TryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TryLength(self: ExceptionHandlingClause) -> int

"""

    TryOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TryOffset(self: ExceptionHandlingClause) -> int

"""



class ExceptionHandlingClauseOptions(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ExceptionHandlingClauseOptions, values: Clause (0), Fault (4), Filter (1), Finally (2) """
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

    Clause = None
    Fault = None
    Filter = None
    Finally = None
    value__ = None


class FieldAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) FieldAttributes, values: Assembly (3), FamANDAssem (2), Family (4), FamORAssem (5), FieldAccessMask (7), HasDefault (32768), HasFieldMarshal (4096), HasFieldRVA (256), InitOnly (32), Literal (64), NotSerialized (128), PinvokeImpl (8192), Private (1), PrivateScope (0), Public (6), ReservedMask (38144), RTSpecialName (1024), SpecialName (512), Static (16) """
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
    FamANDAssem = None
    Family = None
    FamORAssem = None
    FieldAccessMask = None
    HasDefault = None
    HasFieldMarshal = None
    HasFieldRVA = None
    InitOnly = None
    Literal = None
    NotSerialized = None
    PinvokeImpl = None
    Private = None
    PrivateScope = None
    Public = None
    ReservedMask = None
    RTSpecialName = None
    SpecialName = None
    Static = None
    value__ = None


class FieldInfo(MemberInfo, ICustomAttributeProvider, _MemberInfo, _FieldInfo):
    # no doc
    def Equals(self, obj):
        """ Equals(self: FieldInfo, obj: object) -> bool """
        pass

    @staticmethod
    def GetFieldFromHandle(handle, declaringType=None):
        """
        GetFieldFromHandle(handle: RuntimeFieldHandle) -> FieldInfo
        GetFieldFromHandle(handle: RuntimeFieldHandle, declaringType: RuntimeTypeHandle) -> FieldInfo
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: FieldInfo) -> int """
        pass

    def GetOptionalCustomModifiers(self):
        """ GetOptionalCustomModifiers(self: FieldInfo) -> Array[Type] """
        pass

    def GetRawConstantValue(self):
        """ GetRawConstantValue(self: FieldInfo) -> object """
        pass

    def GetRequiredCustomModifiers(self):
        """ GetRequiredCustomModifiers(self: FieldInfo) -> Array[Type] """
        pass

    def GetValue(self, obj):
        """ GetValue(self: FieldInfo, obj: object) -> object """
        pass

    def GetValueDirect(self, obj):
        """ GetValueDirect(self: FieldInfo, obj: TypedReference) -> object """
        pass

    def SetValue(self, obj, value, invokeAttr=None, binder=None, culture=None):
        """ SetValue(self: FieldInfo, obj: object, value: object)SetValue(self: FieldInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo) """
        pass

    def SetValueDirect(self, obj, value):
        """ SetValueDirect(self: FieldInfo, obj: TypedReference, value: object) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: FieldInfo) -> FieldAttributes

"""

    FieldHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldHandle(self: FieldInfo) -> RuntimeFieldHandle

"""

    FieldType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldType(self: FieldInfo) -> Type

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssembly(self: FieldInfo) -> bool

"""

    IsFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamily(self: FieldInfo) -> bool

"""

    IsFamilyAndAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyAndAssembly(self: FieldInfo) -> bool

"""

    IsFamilyOrAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyOrAssembly(self: FieldInfo) -> bool

"""

    IsInitOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInitOnly(self: FieldInfo) -> bool

"""

    IsLiteral = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLiteral(self: FieldInfo) -> bool

"""

    IsNotSerialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNotSerialized(self: FieldInfo) -> bool

"""

    IsPinvokeImpl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinvokeImpl(self: FieldInfo) -> bool

"""

    IsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrivate(self: FieldInfo) -> bool

"""

    IsPublic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPublic(self: FieldInfo) -> bool

"""

    IsSecurityCritical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecurityCritical(self: FieldInfo) -> bool

"""

    IsSecuritySafeCritical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecuritySafeCritical(self: FieldInfo) -> bool

"""

    IsSecurityTransparent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSecurityTransparent(self: FieldInfo) -> bool

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: FieldInfo) -> bool

"""

    IsStatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStatic(self: FieldInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: FieldInfo) -> MemberTypes

"""



class GenericParameterAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) GenericParameterAttributes, values: Contravariant (2), Covariant (1), DefaultConstructorConstraint (16), None (0), NotNullableValueTypeConstraint (8), ReferenceTypeConstraint (4), SpecialConstraintMask (28), VarianceMask (3) """
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

    Contravariant = None
    Covariant = None
    DefaultConstructorConstraint = None
    None = None
    NotNullableValueTypeConstraint = None
    ReferenceTypeConstraint = None
    SpecialConstraintMask = None
    value__ = None
    VarianceMask = None


class ICustomTypeProvider:
    # no doc
    def GetCustomType(self):
        """ GetCustomType(self: ICustomTypeProvider) -> Type """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImageFileMachine(Enum, IComparable, IFormattable, IConvertible):
    """ enum ImageFileMachine, values: AMD64 (34404), ARM (452), I386 (332), IA64 (512) """
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

    AMD64 = None
    ARM = None
    I386 = None
    IA64 = None
    value__ = None


class InterfaceMapping(object):
    # no doc
    InterfaceMethods = None
    InterfaceType = None
    TargetMethods = None
    TargetType = None


class IntrospectionExtensions(object):
    # no doc
    @staticmethod
    def GetTypeInfo(type):
        """ GetTypeInfo(type: Type) -> TypeInfo """
        pass

    __all__ = [
        'GetTypeInfo',
    ]


class InvalidFilterCriteriaException(ApplicationException, ISerializable, _Exception):
    """
    InvalidFilterCriteriaException()
    InvalidFilterCriteriaException(message: str)
    InvalidFilterCriteriaException(message: str, inner: Exception)
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


class IReflect:
    # no doc
    def GetField(self, name, bindingAttr):
        """ GetField(self: IReflect, name: str, bindingAttr: BindingFlags) -> FieldInfo """
        pass

    def GetFields(self, bindingAttr):
        """ GetFields(self: IReflect, bindingAttr: BindingFlags) -> Array[FieldInfo] """
        pass

    def GetMember(self, name, bindingAttr):
        """ GetMember(self: IReflect, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo] """
        pass

    def GetMembers(self, bindingAttr):
        """ GetMembers(self: IReflect, bindingAttr: BindingFlags) -> Array[MemberInfo] """
        pass

    def GetMethod(self, name, bindingAttr, binder=None, types=None, modifiers=None):
        """
        GetMethod(self: IReflect, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: IReflect, name: str, bindingAttr: BindingFlags) -> MethodInfo
        """
        pass

    def GetMethods(self, bindingAttr):
        """ GetMethods(self: IReflect, bindingAttr: BindingFlags) -> Array[MethodInfo] """
        pass

    def GetProperties(self, bindingAttr):
        """ GetProperties(self: IReflect, bindingAttr: BindingFlags) -> Array[PropertyInfo] """
        pass

    def GetProperty(self, name, bindingAttr, binder=None, returnType=None, types=None, modifiers=None):
        """
        GetProperty(self: IReflect, name: str, bindingAttr: BindingFlags) -> PropertyInfo
        GetProperty(self: IReflect, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        """
        pass

    def InvokeMember(self, name, invokeAttr, binder, target, args, modifiers, culture, namedParameters):
        """ InvokeMember(self: IReflect, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    UnderlyingSystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnderlyingSystemType(self: IReflect) -> Type

"""



class IReflectableType:
    # no doc
    def GetTypeInfo(self):
        """ GetTypeInfo(self: IReflectableType) -> TypeInfo """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LocalVariableInfo(object):
    # no doc
    def ToString(self):
        """ ToString(self: LocalVariableInfo) -> str """
        pass

    IsPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinned(self: LocalVariableInfo) -> bool

"""

    LocalIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalIndex(self: LocalVariableInfo) -> int

"""

    LocalType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalType(self: LocalVariableInfo) -> Type

"""



class ManifestResourceAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ManifestResourceAttributes, values: Private (2), Public (1), VisibilityMask (7) """
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

    Private = None
    Public = None
    value__ = None
    VisibilityMask = None


class ManifestResourceInfo(object):
    """ ManifestResourceInfo(containingAssembly: Assembly, containingFileName: str, resourceLocation: ResourceLocation) """
    @staticmethod # known case of __new__
    def __new__(self, containingAssembly, containingFileName, resourceLocation):
        """ __new__(cls: type, containingAssembly: Assembly, containingFileName: str, resourceLocation: ResourceLocation) """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: ManifestResourceInfo) -> str

"""

    ReferencedAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencedAssembly(self: ManifestResourceInfo) -> Assembly

"""

    ResourceLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourceLocation(self: ManifestResourceInfo) -> ResourceLocation

"""



class MemberFilter(MulticastDelegate, ICloneable, ISerializable):
    """ MemberFilter(object: object, method: IntPtr) """
    def BeginInvoke(self, m, filterCriteria, callback, object):
        """ BeginInvoke(self: MemberFilter, m: MemberInfo, filterCriteria: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MemberFilter, result: IAsyncResult) -> bool """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, m, filterCriteria):
        """ Invoke(self: MemberFilter, m: MemberInfo, filterCriteria: object) -> bool """
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


class MemberTypes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MemberTypes, values: All (191), Constructor (1), Custom (64), Event (2), Field (4), Method (8), NestedType (128), Property (16), TypeInfo (32) """
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

    All = None
    Constructor = None
    Custom = None
    Event = None
    Field = None
    Method = None
    NestedType = None
    Property = None
    TypeInfo = None
    value__ = None


class MethodAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MethodAttributes, values: Abstract (1024), Assembly (3), CheckAccessOnOverride (512), FamANDAssem (2), Family (4), FamORAssem (5), Final (32), HasSecurity (16384), HideBySig (128), MemberAccessMask (7), NewSlot (256), PinvokeImpl (8192), Private (1), PrivateScope (0), Public (6), RequireSecObject (32768), ReservedMask (53248), ReuseSlot (0), RTSpecialName (4096), SpecialName (2048), Static (16), UnmanagedExport (8), Virtual (64), VtableLayoutMask (256) """
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

    Abstract = None
    Assembly = None
    CheckAccessOnOverride = None
    FamANDAssem = None
    Family = None
    FamORAssem = None
    Final = None
    HasSecurity = None
    HideBySig = None
    MemberAccessMask = None
    NewSlot = None
    PinvokeImpl = None
    Private = None
    PrivateScope = None
    Public = None
    RequireSecObject = None
    ReservedMask = None
    ReuseSlot = None
    RTSpecialName = None
    SpecialName = None
    Static = None
    UnmanagedExport = None
    value__ = None
    Virtual = None
    VtableLayoutMask = None


class MethodBody(object):
    # no doc
    def GetILAsByteArray(self):
        """ GetILAsByteArray(self: MethodBody) -> Array[Byte] """
        pass

    ExceptionHandlingClauses = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionHandlingClauses(self: MethodBody) -> IList[ExceptionHandlingClause]

"""

    InitLocals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitLocals(self: MethodBody) -> bool

"""

    LocalSignatureMetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalSignatureMetadataToken(self: MethodBody) -> int

"""

    LocalVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalVariables(self: MethodBody) -> IList[LocalVariableInfo]

"""

    MaxStackSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxStackSize(self: MethodBody) -> int

"""



class MethodImplAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum MethodImplAttributes, values: AggressiveInlining (256), CodeTypeMask (3), ForwardRef (16), IL (0), InternalCall (4096), Managed (0), ManagedMask (4), MaxMethodImplVal (65535), Native (1), NoInlining (8), NoOptimization (64), OPTIL (2), PreserveSig (128), Runtime (3), SecurityMitigations (1024), Synchronized (32), Unmanaged (4) """
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

    AggressiveInlining = None
    CodeTypeMask = None
    ForwardRef = None
    IL = None
    InternalCall = None
    Managed = None
    ManagedMask = None
    MaxMethodImplVal = None
    Native = None
    NoInlining = None
    NoOptimization = None
    OPTIL = None
    PreserveSig = None
    Runtime = None
    SecurityMitigations = None
    Synchronized = None
    Unmanaged = None
    value__ = None


class MethodImportAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MethodImportAttributes, values: BestFitMappingDisable (32), BestFitMappingEnable (16), BestFitMappingMask (48), CallingConventionCDecl (512), CallingConventionFastCall (1280), CallingConventionMask (1792), CallingConventionStdCall (768), CallingConventionThisCall (1024), CallingConventionWinApi (256), CharSetAnsi (2), CharSetAuto (6), CharSetMask (6), CharSetUnicode (4), ExactSpelling (1), None (0), SetLastError (64), ThrowOnUnmappableCharDisable (8192), ThrowOnUnmappableCharEnable (4096), ThrowOnUnmappableCharMask (12288) """
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

    BestFitMappingDisable = None
    BestFitMappingEnable = None
    BestFitMappingMask = None
    CallingConventionCDecl = None
    CallingConventionFastCall = None
    CallingConventionMask = None
    CallingConventionStdCall = None
    CallingConventionThisCall = None
    CallingConventionWinApi = None
    CharSetAnsi = None
    CharSetAuto = None
    CharSetMask = None
    CharSetUnicode = None
    ExactSpelling = None
    None = None
    SetLastError = None
    ThrowOnUnmappableCharDisable = None
    ThrowOnUnmappableCharEnable = None
    ThrowOnUnmappableCharMask = None
    value__ = None


class MethodInfo(MethodBase, ICustomAttributeProvider, _MemberInfo, _MethodBase, _MethodInfo):
    # no doc
    def CreateDelegate(self, delegateType, target=None):
        """
        CreateDelegate(self: MethodInfo, delegateType: Type) -> Delegate
        CreateDelegate(self: MethodInfo, delegateType: Type, target: object) -> Delegate
        """
        pass

    def Equals(self, obj):
        """ Equals(self: MethodInfo, obj: object) -> bool """
        pass

    def GetBaseDefinition(self):
        """ GetBaseDefinition(self: MethodInfo) -> MethodInfo """
        pass

    def GetGenericArguments(self):
        """ GetGenericArguments(self: MethodInfo) -> Array[Type] """
        pass

    def GetGenericMethodDefinition(self):
        """ GetGenericMethodDefinition(self: MethodInfo) -> MethodInfo """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MethodInfo) -> int """
        pass

    def MakeGenericMethod(self, typeArguments):
        """ MakeGenericMethod(self: MethodInfo, *typeArguments: Array[Type]) -> MethodInfo """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: MethodInfo) -> MemberTypes

"""

    ReturnParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnParameter(self: MethodInfo) -> ParameterInfo

"""

    ReturnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnType(self: MethodInfo) -> Type

"""

    ReturnTypeCustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnTypeCustomAttributes(self: MethodInfo) -> ICustomAttributeProvider

"""



class MethodSemanticsAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MethodSemanticsAttributes, values: Adder (8), Getter (2), Other (4), Raiser (32), Remover (16), Setter (1) """
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

    Adder = None
    Getter = None
    Other = None
    Raiser = None
    Remover = None
    Setter = None
    value__ = None


class Missing(object, ISerializable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Value = None


class Module(object, _Module, ISerializable, ICustomAttributeProvider):
    # no doc
    def Equals(self, o):
        """ Equals(self: Module, o: object) -> bool """
        pass

    def FilterTypeName(self, *args): #cannot find CLR method
        """ TypeFilter(object: object, method: IntPtr) """
        pass

    def FilterTypeNameIgnoreCase(self, *args): #cannot find CLR method
        """ TypeFilter(object: object, method: IntPtr) """
        pass

    def FindTypes(self, filter, filterCriteria):
        """ FindTypes(self: Module, filter: TypeFilter, filterCriteria: object) -> Array[Type] """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: Module, inherit: bool) -> Array[object]
        GetCustomAttributes(self: Module, attributeType: Type, inherit: bool) -> Array[object]
        """
        pass

    def GetCustomAttributesData(self):
        """ GetCustomAttributesData(self: Module) -> IList[CustomAttributeData] """
        pass

    def GetField(self, name, bindingAttr=None):
        """
        GetField(self: Module, name: str) -> FieldInfo
        GetField(self: Module, name: str, bindingAttr: BindingFlags) -> FieldInfo
        """
        pass

    def GetFields(self, bindingFlags=None):
        """
        GetFields(self: Module) -> Array[FieldInfo]
        GetFields(self: Module, bindingFlags: BindingFlags) -> Array[FieldInfo]
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Module) -> int """
        pass

    def GetMethod(self, name, *__args):
        """
        GetMethod(self: Module, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: Module, name: str, types: Array[Type]) -> MethodInfo
        GetMethod(self: Module, name: str) -> MethodInfo
        """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: Module, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo """
        pass

    def GetMethods(self, bindingFlags=None):
        """
        GetMethods(self: Module) -> Array[MethodInfo]
        GetMethods(self: Module, bindingFlags: BindingFlags) -> Array[MethodInfo]
        """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: Module, info: SerializationInfo, context: StreamingContext) """
        pass

    def GetPEKind(self, peKind, machine):
        """ GetPEKind(self: Module) -> (PortableExecutableKinds, ImageFileMachine) """
        pass

    def GetSignerCertificate(self):
        """ GetSignerCertificate(self: Module) -> X509Certificate """
        pass

    def GetType(self, className=None, *__args):
        """
        GetType(self: Module, className: str, ignoreCase: bool) -> Type
        GetType(self: Module, className: str) -> Type
        GetType(self: Module, className: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        pass

    def GetTypes(self):
        """ GetTypes(self: Module) -> Array[Type] """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: Module, attributeType: Type, inherit: bool) -> bool """
        pass

    def IsResource(self):
        """ IsResource(self: Module) -> bool """
        pass

    def ResolveField(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveField(self: Module, metadataToken: int) -> FieldInfo
        ResolveField(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> FieldInfo
        """
        pass

    def ResolveMember(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveMember(self: Module, metadataToken: int) -> MemberInfo
        ResolveMember(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> MemberInfo
        """
        pass

    def ResolveMethod(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveMethod(self: Module, metadataToken: int) -> MethodBase
        ResolveMethod(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> MethodBase
        """
        pass

    def ResolveSignature(self, metadataToken):
        """ ResolveSignature(self: Module, metadataToken: int) -> Array[Byte] """
        pass

    def ResolveString(self, metadataToken):
        """ ResolveString(self: Module, metadataToken: int) -> str """
        pass

    def ResolveType(self, metadataToken, genericTypeArguments=None, genericMethodArguments=None):
        """
        ResolveType(self: Module, metadataToken: int) -> Type
        ResolveType(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> Type
        """
        pass

    def ToString(self):
        """ ToString(self: Module) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Assembly(self: Module) -> Assembly

"""

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomAttributes(self: Module) -> IEnumerable[CustomAttributeData]

"""

    FullyQualifiedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullyQualifiedName(self: Module) -> str

"""

    MDStreamVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MDStreamVersion(self: Module) -> int

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: Module) -> int

"""

    ModuleHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModuleHandle(self: Module) -> ModuleHandle

"""

    ModuleVersionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModuleVersionId(self: Module) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Module) -> str

"""

    ScopeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScopeName(self: Module) -> str

"""



class ModuleResolveEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ ModuleResolveEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ModuleResolveEventHandler, sender: object, e: ResolveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleResolveEventHandler, result: IAsyncResult) -> Module """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleResolveEventHandler, sender: object, e: ResolveEventArgs) -> Module """
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


class ObfuscateAssemblyAttribute(Attribute, _Attribute):
    """ ObfuscateAssemblyAttribute(assemblyIsPrivate: bool) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, assemblyIsPrivate):
        """ __new__(cls: type, assemblyIsPrivate: bool) """
        pass

    AssemblyIsPrivate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyIsPrivate(self: ObfuscateAssemblyAttribute) -> bool

"""

    StripAfterObfuscation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StripAfterObfuscation(self: ObfuscateAssemblyAttribute) -> bool

Set: StripAfterObfuscation(self: ObfuscateAssemblyAttribute) = value
"""



class ObfuscationAttribute(Attribute, _Attribute):
    """ ObfuscationAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ApplyToMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyToMembers(self: ObfuscationAttribute) -> bool

Set: ApplyToMembers(self: ObfuscationAttribute) = value
"""

    Exclude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exclude(self: ObfuscationAttribute) -> bool

Set: Exclude(self: ObfuscationAttribute) = value
"""

    Feature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Feature(self: ObfuscationAttribute) -> str

Set: Feature(self: ObfuscationAttribute) = value
"""

    StripAfterObfuscation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StripAfterObfuscation(self: ObfuscationAttribute) -> bool

Set: StripAfterObfuscation(self: ObfuscationAttribute) = value
"""



class ParameterAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ParameterAttributes, values: HasDefault (4096), HasFieldMarshal (8192), In (1), Lcid (4), None (0), Optional (16), Out (2), Reserved3 (16384), Reserved4 (32768), ReservedMask (61440), Retval (8) """
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

    HasDefault = None
    HasFieldMarshal = None
    In = None
    Lcid = None
    None = None
    Optional = None
    Out = None
    Reserved3 = None
    Reserved4 = None
    ReservedMask = None
    Retval = None
    value__ = None


class ParameterInfo(object, _ParameterInfo, ICustomAttributeProvider, IObjectReference):
    # no doc
    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: ParameterInfo, inherit: bool) -> Array[object]
        GetCustomAttributes(self: ParameterInfo, attributeType: Type, inherit: bool) -> Array[object]
        """
        pass

    def GetCustomAttributesData(self):
        """ GetCustomAttributesData(self: ParameterInfo) -> IList[CustomAttributeData] """
        pass

    def GetOptionalCustomModifiers(self):
        """ GetOptionalCustomModifiers(self: ParameterInfo) -> Array[Type] """
        pass

    def GetRealObject(self, context):
        """ GetRealObject(self: ParameterInfo, context: StreamingContext) -> object """
        pass

    def GetRequiredCustomModifiers(self):
        """ GetRequiredCustomModifiers(self: ParameterInfo) -> Array[Type] """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: ParameterInfo, attributeType: Type, inherit: bool) -> bool """
        pass

    def ToString(self):
        """ ToString(self: ParameterInfo) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: ParameterInfo) -> ParameterAttributes

"""

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomAttributes(self: ParameterInfo) -> IEnumerable[CustomAttributeData]

"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: ParameterInfo) -> object

"""

    HasDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasDefaultValue(self: ParameterInfo) -> bool

"""

    IsIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIn(self: ParameterInfo) -> bool

"""

    IsLcid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLcid(self: ParameterInfo) -> bool

"""

    IsOptional = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOptional(self: ParameterInfo) -> bool

"""

    IsOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOut(self: ParameterInfo) -> bool

"""

    IsRetval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRetval(self: ParameterInfo) -> bool

"""

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member(self: ParameterInfo) -> MemberInfo

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: ParameterInfo) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ParameterInfo) -> str

"""

    ParameterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParameterType(self: ParameterInfo) -> Type

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: ParameterInfo) -> int

"""

    RawDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawDefaultValue(self: ParameterInfo) -> object

"""


    AttrsImpl = None
    ClassImpl = None
    DefaultValueImpl = None
    MemberImpl = None
    NameImpl = None
    PositionImpl = None


class ParameterModifier(object):
    """ ParameterModifier(parameterCount: int) """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parameterCount):
        """
        __new__[ParameterModifier]() -> ParameterModifier
        
        __new__(cls: type, parameterCount: int)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class Pointer(object, ISerializable):
    # no doc
    @staticmethod
    def Box(ptr, type):
        """ Box(ptr: Void*, type: Type) -> object """
        pass

    @staticmethod
    def Unbox(ptr):
        """ Unbox(ptr: object) -> Void* """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class PortableExecutableKinds(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) PortableExecutableKinds, values: ILOnly (1), NotAPortableExecutableImage (0), PE32Plus (4), Preferred32Bit (16), Required32Bit (2), Unmanaged32Bit (8) """
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

    ILOnly = None
    NotAPortableExecutableImage = None
    PE32Plus = None
    Preferred32Bit = None
    Required32Bit = None
    Unmanaged32Bit = None
    value__ = None


class ProcessorArchitecture(Enum, IComparable, IFormattable, IConvertible):
    """ enum ProcessorArchitecture, values: Amd64 (4), Arm (5), IA64 (3), MSIL (1), None (0), X86 (2) """
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

    Amd64 = None
    Arm = None
    IA64 = None
    MSIL = None
    None = None
    value__ = None
    X86 = None


class PropertyAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) PropertyAttributes, values: HasDefault (4096), None (0), Reserved2 (8192), Reserved3 (16384), Reserved4 (32768), ReservedMask (62464), RTSpecialName (1024), SpecialName (512) """
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

    HasDefault = None
    None = None
    Reserved2 = None
    Reserved3 = None
    Reserved4 = None
    ReservedMask = None
    RTSpecialName = None
    SpecialName = None
    value__ = None


class PropertyInfo(MemberInfo, ICustomAttributeProvider, _MemberInfo, _PropertyInfo):
    # no doc
    def Equals(self, obj):
        """ Equals(self: PropertyInfo, obj: object) -> bool """
        pass

    def GetAccessors(self, nonPublic=None):
        """
        GetAccessors(self: PropertyInfo) -> Array[MethodInfo]
        GetAccessors(self: PropertyInfo, nonPublic: bool) -> Array[MethodInfo]
        """
        pass

    def GetConstantValue(self):
        """ GetConstantValue(self: PropertyInfo) -> object """
        pass

    def GetGetMethod(self, nonPublic=None):
        """
        GetGetMethod(self: PropertyInfo) -> MethodInfo
        GetGetMethod(self: PropertyInfo, nonPublic: bool) -> MethodInfo
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PropertyInfo) -> int """
        pass

    def GetIndexParameters(self):
        """ GetIndexParameters(self: PropertyInfo) -> Array[ParameterInfo] """
        pass

    def GetOptionalCustomModifiers(self):
        """ GetOptionalCustomModifiers(self: PropertyInfo) -> Array[Type] """
        pass

    def GetRawConstantValue(self):
        """ GetRawConstantValue(self: PropertyInfo) -> object """
        pass

    def GetRequiredCustomModifiers(self):
        """ GetRequiredCustomModifiers(self: PropertyInfo) -> Array[Type] """
        pass

    def GetSetMethod(self, nonPublic=None):
        """
        GetSetMethod(self: PropertyInfo) -> MethodInfo
        GetSetMethod(self: PropertyInfo, nonPublic: bool) -> MethodInfo
        """
        pass

    def GetValue(self, obj, *__args):
        """
        GetValue(self: PropertyInfo, obj: object) -> object
        GetValue(self: PropertyInfo, obj: object, index: Array[object]) -> object
        GetValue(self: PropertyInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) -> object
        """
        pass

    def SetValue(self, obj, value, *__args):
        """ SetValue(self: PropertyInfo, obj: object, value: object)SetValue(self: PropertyInfo, obj: object, value: object, index: Array[object])SetValue(self: PropertyInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: PropertyInfo) -> PropertyAttributes

"""

    CanRead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRead(self: PropertyInfo) -> bool

"""

    CanWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanWrite(self: PropertyInfo) -> bool

"""

    GetMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GetMethod(self: PropertyInfo) -> MethodInfo

"""

    IsSpecialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpecialName(self: PropertyInfo) -> bool

"""

    MemberType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberType(self: PropertyInfo) -> MemberTypes

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: PropertyInfo) -> Type

"""

    SetMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetMethod(self: PropertyInfo) -> MethodInfo

"""



class ReflectionContext(object):
    # no doc
    def GetTypeForObject(self, value):
        """ GetTypeForObject(self: ReflectionContext, value: object) -> TypeInfo """
        pass

    def MapAssembly(self, assembly):
        """ MapAssembly(self: ReflectionContext, assembly: Assembly) -> Assembly """
        pass

    def MapType(self, type):
        """ MapType(self: ReflectionContext, type: TypeInfo) -> TypeInfo """
        pass


class ReflectionTypeLoadException(SystemException, ISerializable, _Exception):
    """
    ReflectionTypeLoadException(classes: Array[Type], exceptions: Array[Exception])
    ReflectionTypeLoadException(classes: Array[Type], exceptions: Array[Exception], message: str)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: ReflectionTypeLoadException, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classes, exceptions, message=None):
        """
        __new__(cls: type, classes: Array[Type], exceptions: Array[Exception])
        __new__(cls: type, classes: Array[Type], exceptions: Array[Exception], message: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    LoaderExceptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoaderExceptions(self: ReflectionTypeLoadException) -> Array[Exception]

"""

    Types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Types(self: ReflectionTypeLoadException) -> Array[Type]

"""


    SerializeObjectState = None


class ResourceAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ResourceAttributes, values: Private (2), Public (1) """
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

    Private = None
    Public = None
    value__ = None


class ResourceLocation(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ResourceLocation, values: ContainedInAnotherAssembly (2), ContainedInManifestFile (4), Embedded (1) """
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

    ContainedInAnotherAssembly = None
    ContainedInManifestFile = None
    Embedded = None
    value__ = None


class RuntimeReflectionExtensions(object):
    # no doc
    @staticmethod
    def GetMethodInfo(del):
        """ GetMethodInfo(del: Delegate) -> MethodInfo """
        pass

    @staticmethod
    def GetRuntimeBaseDefinition(method):
        """ GetRuntimeBaseDefinition(method: MethodInfo) -> MethodInfo """
        pass

    @staticmethod
    def GetRuntimeEvent(type, name):
        """ GetRuntimeEvent(type: Type, name: str) -> EventInfo """
        pass

    @staticmethod
    def GetRuntimeEvents(type):
        """ GetRuntimeEvents(type: Type) -> IEnumerable[EventInfo] """
        pass

    @staticmethod
    def GetRuntimeField(type, name):
        """ GetRuntimeField(type: Type, name: str) -> FieldInfo """
        pass

    @staticmethod
    def GetRuntimeFields(type):
        """ GetRuntimeFields(type: Type) -> IEnumerable[FieldInfo] """
        pass

    @staticmethod
    def GetRuntimeInterfaceMap(typeInfo, interfaceType):
        """ GetRuntimeInterfaceMap(typeInfo: TypeInfo, interfaceType: Type) -> InterfaceMapping """
        pass

    @staticmethod
    def GetRuntimeMethod(type, name, parameters):
        """ GetRuntimeMethod(type: Type, name: str, parameters: Array[Type]) -> MethodInfo """
        pass

    @staticmethod
    def GetRuntimeMethods(type):
        """ GetRuntimeMethods(type: Type) -> IEnumerable[MethodInfo] """
        pass

    @staticmethod
    def GetRuntimeProperties(type):
        """ GetRuntimeProperties(type: Type) -> IEnumerable[PropertyInfo] """
        pass

    @staticmethod
    def GetRuntimeProperty(type, name):
        """ GetRuntimeProperty(type: Type, name: str) -> PropertyInfo """
        pass

    __all__ = [
        'GetMethodInfo',
        'GetRuntimeBaseDefinition',
        'GetRuntimeEvent',
        'GetRuntimeEvents',
        'GetRuntimeField',
        'GetRuntimeFields',
        'GetRuntimeInterfaceMap',
        'GetRuntimeMethod',
        'GetRuntimeMethods',
        'GetRuntimeProperties',
        'GetRuntimeProperty',
    ]


class StrongNameKeyPair(object, IDeserializationCallback, ISerializable):
    """
    StrongNameKeyPair(keyPairFile: FileStream)
    StrongNameKeyPair(keyPairArray: Array[Byte])
    StrongNameKeyPair(keyPairContainer: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, keyPairFile: FileStream)
        __new__(cls: type, keyPairArray: Array[Byte])
        __new__(cls: type, keyPairContainer: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    PublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublicKey(self: StrongNameKeyPair) -> Array[Byte]

"""



class TargetException(ApplicationException, ISerializable, _Exception):
    """
    TargetException()
    TargetException(message: str)
    TargetException(message: str, inner: Exception)
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


class TargetInvocationException(ApplicationException, ISerializable, _Exception):
    """
    TargetInvocationException(inner: Exception)
    TargetInvocationException(message: str, inner: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, inner: Exception)
        __new__(cls: type, message: str, inner: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class TargetParameterCountException(ApplicationException, ISerializable, _Exception):
    """
    TargetParameterCountException()
    TargetParameterCountException(message: str)
    TargetParameterCountException(message: str, inner: Exception)
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
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class TypeAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) TypeAttributes, values: Abstract (128), AnsiClass (0), AutoClass (131072), AutoLayout (0), BeforeFieldInit (1048576), Class (0), ClassSemanticsMask (32), CustomFormatClass (196608), CustomFormatMask (12582912), ExplicitLayout (16), HasSecurity (262144), Import (4096), Interface (32), LayoutMask (24), NestedAssembly (5), NestedFamANDAssem (6), NestedFamily (4), NestedFamORAssem (7), NestedPrivate (3), NestedPublic (2), NotPublic (0), Public (1), ReservedMask (264192), RTSpecialName (2048), Sealed (256), SequentialLayout (8), Serializable (8192), SpecialName (1024), StringFormatMask (196608), UnicodeClass (65536), VisibilityMask (7), WindowsRuntime (16384) """
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

    Abstract = None
    AnsiClass = None
    AutoClass = None
    AutoLayout = None
    BeforeFieldInit = None
    Class = None
    ClassSemanticsMask = None
    CustomFormatClass = None
    CustomFormatMask = None
    ExplicitLayout = None
    HasSecurity = None
    Import = None
    Interface = None
    LayoutMask = None
    NestedAssembly = None
    NestedFamANDAssem = None
    NestedFamily = None
    NestedFamORAssem = None
    NestedPrivate = None
    NestedPublic = None
    NotPublic = None
    Public = None
    ReservedMask = None
    RTSpecialName = None
    Sealed = None
    SequentialLayout = None
    Serializable = None
    SpecialName = None
    StringFormatMask = None
    UnicodeClass = None
    value__ = None
    VisibilityMask = None
    WindowsRuntime = None


class TypeInfo(Type, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    # no doc
    def AsType(self):
        """ AsType(self: TypeInfo) -> Type """
        pass

    def GetAttributeFlagsImpl(self, *args): #cannot find CLR method
        """ GetAttributeFlagsImpl(self: Type) -> TypeAttributes """
        pass

    def GetConstructorImpl(self, *args): #cannot find CLR method
        """ GetConstructorImpl(self: Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo """
        pass

    def GetDeclaredEvent(self, name):
        """ GetDeclaredEvent(self: TypeInfo, name: str) -> EventInfo """
        pass

    def GetDeclaredField(self, name):
        """ GetDeclaredField(self: TypeInfo, name: str) -> FieldInfo """
        pass

    def GetDeclaredMethod(self, name):
        """ GetDeclaredMethod(self: TypeInfo, name: str) -> MethodInfo """
        pass

    def GetDeclaredMethods(self, name):
        """ GetDeclaredMethods(self: TypeInfo, name: str) -> IEnumerable[MethodInfo] """
        pass

    def GetDeclaredNestedType(self, name):
        """ GetDeclaredNestedType(self: TypeInfo, name: str) -> TypeInfo """
        pass

    def GetDeclaredProperty(self, name):
        """ GetDeclaredProperty(self: TypeInfo, name: str) -> PropertyInfo """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo """
        pass

    def GetPropertyImpl(self, *args): #cannot find CLR method
        """ GetPropertyImpl(self: Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo """
        pass

    def GetTypeCodeImpl(self, *args): #cannot find CLR method
        """ GetTypeCodeImpl(self: Type) -> TypeCode """
        pass

    def HasElementTypeImpl(self, *args): #cannot find CLR method
        """ HasElementTypeImpl(self: Type) -> bool """
        pass

    def IsArrayImpl(self, *args): #cannot find CLR method
        """ IsArrayImpl(self: Type) -> bool """
        pass

    def IsAssignableFrom(self, *__args):
        """ IsAssignableFrom(self: TypeInfo, typeInfo: TypeInfo) -> bool """
        pass

    def IsByRefImpl(self, *args): #cannot find CLR method
        """ IsByRefImpl(self: Type) -> bool """
        pass

    def IsCOMObjectImpl(self, *args): #cannot find CLR method
        """ IsCOMObjectImpl(self: Type) -> bool """
        pass

    def IsContextfulImpl(self, *args): #cannot find CLR method
        """ IsContextfulImpl(self: Type) -> bool """
        pass

    def IsMarshalByRefImpl(self, *args): #cannot find CLR method
        """ IsMarshalByRefImpl(self: Type) -> bool """
        pass

    def IsPointerImpl(self, *args): #cannot find CLR method
        """ IsPointerImpl(self: Type) -> bool """
        pass

    def IsPrimitiveImpl(self, *args): #cannot find CLR method
        """ IsPrimitiveImpl(self: Type) -> bool """
        pass

    def IsValueTypeImpl(self, *args): #cannot find CLR method
        """ IsValueTypeImpl(self: Type) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    DeclaredConstructors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredConstructors(self: TypeInfo) -> IEnumerable[ConstructorInfo]

"""

    DeclaredEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredEvents(self: TypeInfo) -> IEnumerable[EventInfo]

"""

    DeclaredFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredFields(self: TypeInfo) -> IEnumerable[FieldInfo]

"""

    DeclaredMembers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredMembers(self: TypeInfo) -> IEnumerable[MemberInfo]

"""

    DeclaredMethods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredMethods(self: TypeInfo) -> IEnumerable[MethodInfo]

"""

    DeclaredNestedTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredNestedTypes(self: TypeInfo) -> IEnumerable[TypeInfo]

"""

    DeclaredProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclaredProperties(self: TypeInfo) -> IEnumerable[PropertyInfo]

"""

    GenericTypeParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenericTypeParameters(self: TypeInfo) -> Array[Type]

"""

    ImplementedInterfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImplementedInterfaces(self: TypeInfo) -> IEnumerable[Type]

"""



class TypeDelegator(TypeInfo, ICustomAttributeProvider, _MemberInfo, _Type, IReflect, IReflectableType):
    """ TypeDelegator(delegatingType: Type) """
    def GetAttributeFlagsImpl(self, *args): #cannot find CLR method
        """ GetAttributeFlagsImpl(self: TypeDelegator) -> TypeAttributes """
        pass

    def GetConstructorImpl(self, *args): #cannot find CLR method
        """ GetConstructorImpl(self: TypeDelegator, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo """
        pass

    def GetConstructors(self, bindingAttr=None):
        """ GetConstructors(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[ConstructorInfo] """
        pass

    def GetCustomAttributes(self, *__args):
        """
        GetCustomAttributes(self: TypeDelegator, inherit: bool) -> Array[object]
        GetCustomAttributes(self: TypeDelegator, attributeType: Type, inherit: bool) -> Array[object]
        """
        pass

    def GetElementType(self):
        """ GetElementType(self: TypeDelegator) -> Type """
        pass

    def GetEvent(self, name, bindingAttr=None):
        """ GetEvent(self: TypeDelegator, name: str, bindingAttr: BindingFlags) -> EventInfo """
        pass

    def GetEvents(self, bindingAttr=None):
        """
        GetEvents(self: TypeDelegator) -> Array[EventInfo]
        GetEvents(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[EventInfo]
        """
        pass

    def GetField(self, name, bindingAttr=None):
        """ GetField(self: TypeDelegator, name: str, bindingAttr: BindingFlags) -> FieldInfo """
        pass

    def GetFields(self, bindingAttr=None):
        """ GetFields(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[FieldInfo] """
        pass

    def GetInterface(self, name, ignoreCase=None):
        """ GetInterface(self: TypeDelegator, name: str, ignoreCase: bool) -> Type """
        pass

    def GetInterfaceMap(self, interfaceType):
        """ GetInterfaceMap(self: TypeDelegator, interfaceType: Type) -> InterfaceMapping """
        pass

    def GetInterfaces(self):
        """ GetInterfaces(self: TypeDelegator) -> Array[Type] """
        pass

    def GetMember(self, name, *__args):
        """ GetMember(self: TypeDelegator, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array[MemberInfo] """
        pass

    def GetMembers(self, bindingAttr=None):
        """ GetMembers(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[MemberInfo] """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: TypeDelegator, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo """
        pass

    def GetMethods(self, bindingAttr=None):
        """ GetMethods(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[MethodInfo] """
        pass

    def GetNestedType(self, name, bindingAttr=None):
        """ GetNestedType(self: TypeDelegator, name: str, bindingAttr: BindingFlags) -> Type """
        pass

    def GetNestedTypes(self, bindingAttr=None):
        """ GetNestedTypes(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[Type] """
        pass

    def GetProperties(self, bindingAttr=None):
        """ GetProperties(self: TypeDelegator, bindingAttr: BindingFlags) -> Array[PropertyInfo] """
        pass

    def GetPropertyImpl(self, *args): #cannot find CLR method
        """ GetPropertyImpl(self: TypeDelegator, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo """
        pass

    def GetTypeCodeImpl(self, *args): #cannot find CLR method
        """ GetTypeCodeImpl(self: Type) -> TypeCode """
        pass

    def HasElementTypeImpl(self, *args): #cannot find CLR method
        """ HasElementTypeImpl(self: TypeDelegator) -> bool """
        pass

    def InvokeMember(self, name, invokeAttr, binder, target, args, *__args):
        """ InvokeMember(self: TypeDelegator, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object """
        pass

    def IsArrayImpl(self, *args): #cannot find CLR method
        """ IsArrayImpl(self: TypeDelegator) -> bool """
        pass

    def IsAssignableFrom(self, *__args):
        """ IsAssignableFrom(self: TypeDelegator, typeInfo: TypeInfo) -> bool """
        pass

    def IsByRefImpl(self, *args): #cannot find CLR method
        """ IsByRefImpl(self: TypeDelegator) -> bool """
        pass

    def IsCOMObjectImpl(self, *args): #cannot find CLR method
        """ IsCOMObjectImpl(self: TypeDelegator) -> bool """
        pass

    def IsContextfulImpl(self, *args): #cannot find CLR method
        """ IsContextfulImpl(self: Type) -> bool """
        pass

    def IsDefined(self, attributeType, inherit):
        """ IsDefined(self: TypeDelegator, attributeType: Type, inherit: bool) -> bool """
        pass

    def IsMarshalByRefImpl(self, *args): #cannot find CLR method
        """ IsMarshalByRefImpl(self: Type) -> bool """
        pass

    def IsPointerImpl(self, *args): #cannot find CLR method
        """ IsPointerImpl(self: TypeDelegator) -> bool """
        pass

    def IsPrimitiveImpl(self, *args): #cannot find CLR method
        """ IsPrimitiveImpl(self: TypeDelegator) -> bool """
        pass

    def IsValueTypeImpl(self, *args): #cannot find CLR method
        """ IsValueTypeImpl(self: TypeDelegator) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, delegatingType):
        """
        __new__(cls: type)
        __new__(cls: type, delegatingType: Type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Assembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Assembly(self: TypeDelegator) -> Assembly

"""

    AssemblyQualifiedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyQualifiedName(self: TypeDelegator) -> str

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseType(self: TypeDelegator) -> Type

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: TypeDelegator) -> str

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: TypeDelegator) -> Guid

"""

    IsConstructedGenericType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConstructedGenericType(self: TypeDelegator) -> bool

"""

    MetadataToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataToken(self: TypeDelegator) -> int

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: TypeDelegator) -> Module

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: TypeDelegator) -> str

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Namespace(self: TypeDelegator) -> str

"""

    TypeHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeHandle(self: TypeDelegator) -> RuntimeTypeHandle

"""

    UnderlyingSystemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnderlyingSystemType(self: TypeDelegator) -> Type

"""


    typeImpl = None


class TypeFilter(MulticastDelegate, ICloneable, ISerializable):
    """ TypeFilter(object: object, method: IntPtr) """
    def BeginInvoke(self, m, filterCriteria, callback, object):
        """ BeginInvoke(self: TypeFilter, m: Type, filterCriteria: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TypeFilter, result: IAsyncResult) -> bool """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, m, filterCriteria):
        """ Invoke(self: TypeFilter, m: Type, filterCriteria: object) -> bool """
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


# variables with complex values

