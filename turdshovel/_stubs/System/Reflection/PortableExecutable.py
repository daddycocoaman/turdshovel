# encoding: utf-8
# module System.Reflection.PortableExecutable calls itself PortableExecutable
# from System.Reflection.Metadata, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Characteristics(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) Characteristics, values: AggressiveWSTrim (16), Bit32Machine (256), BytesReversedHi (32768), BytesReversedLo (128), DebugStripped (512), Dll (8192), ExecutableImage (2), LargeAddressAware (32), LineNumsStripped (4), LocalSymsStripped (8), NetRunFromSwap (2048), RelocsStripped (1), RemovableRunFromSwap (1024), System (4096), UpSystemOnly (16384) """
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

    AggressiveWSTrim = None
    Bit32Machine = None
    BytesReversedHi = None
    BytesReversedLo = None
    DebugStripped = None
    Dll = None
    ExecutableImage = None
    LargeAddressAware = None
    LineNumsStripped = None
    LocalSymsStripped = None
    NetRunFromSwap = None
    RelocsStripped = None
    RemovableRunFromSwap = None
    System = None
    UpSystemOnly = None
    value__ = None


class CodeViewDebugDirectoryData(object):
    """ Provides information about a Program Debug Database (PDB) file. """
    Age = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The iteration of the PDB. The first iteration is 1. The iteration is incremented each time the PDB content is augmented.

Get: Age(self: CodeViewDebugDirectoryData) -> int

"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Globally Unique Identifier (GUID) of the associated PDB.

Get: Guid(self: CodeViewDebugDirectoryData) -> Guid

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The path to the .pdb file that contains debug information for the PE/COFF file.

Get: Path(self: CodeViewDebugDirectoryData) -> str

"""



class CoffHeader(object):
    """ Represents the header of a COFF file. """
    Characteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the flags that indicate the attributes of the file.

Get: Characteristics(self: CoffHeader) -> Characteristics

"""

    Machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the target machine.

Get: Machine(self: CoffHeader) -> Machine

"""

    NumberOfSections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of sections. This indicates the size of the section table, which immediately follows the headers.

Get: NumberOfSections(self: CoffHeader) -> Int16

"""

    NumberOfSymbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of entries in the symbol table. This data can be used to locate the string table, which immediately follows the symbol table. This value should be zero for a PE image.

Get: NumberOfSymbols(self: CoffHeader) -> int

"""

    PointerToSymbolTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file pointer to the COFF symbol table.

Get: PointerToSymbolTable(self: CoffHeader) -> int

"""

    SizeOfOptionalHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the optional header, which is required for executable files but not for object files. This value should be zero for an object file.

Get: SizeOfOptionalHeader(self: CoffHeader) -> Int16

"""

    TimeDateStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates when the file was created.

Get: TimeDateStamp(self: CoffHeader) -> int

"""



class CorFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    COR20Flags
    
    enum (flags) CorFlags, values: ILLibrary (4), ILOnly (1), NativeEntryPoint (16), Prefers32Bit (131072), Requires32Bit (2), StrongNameSigned (8), TrackDebugData (65536)
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

    ILLibrary = None
    ILOnly = None
    NativeEntryPoint = None
    Prefers32Bit = None
    Requires32Bit = None
    StrongNameSigned = None
    TrackDebugData = None
    value__ = None


class CorHeader(object):
    # no doc
    CodeManagerTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeManagerTableDirectory(self: CorHeader) -> DirectoryEntry

"""

    EntryPointTokenOrRelativeVirtualAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryPointTokenOrRelativeVirtualAddress(self: CorHeader) -> int

"""

    ExportAddressTableJumpsDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportAddressTableJumpsDirectory(self: CorHeader) -> DirectoryEntry

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: CorHeader) -> CorFlags

"""

    MajorRuntimeVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorRuntimeVersion(self: CorHeader) -> UInt16

"""

    ManagedNativeHeaderDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManagedNativeHeaderDirectory(self: CorHeader) -> DirectoryEntry

"""

    MetadataDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MetadataDirectory(self: CorHeader) -> DirectoryEntry

"""

    MinorRuntimeVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorRuntimeVersion(self: CorHeader) -> UInt16

"""

    ResourcesDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourcesDirectory(self: CorHeader) -> DirectoryEntry

"""

    StrongNameSignatureDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StrongNameSignatureDirectory(self: CorHeader) -> DirectoryEntry

"""

    VtableFixupsDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VtableFixupsDirectory(self: CorHeader) -> DirectoryEntry

"""



class DebugDirectoryBuilder(object):
    """ DebugDirectoryBuilder() """
    def AddCodeViewEntry(self, pdbPath, pdbContentId, portablePdbVersion):
        """
        AddCodeViewEntry(self: DebugDirectoryBuilder, pdbPath: str, pdbContentId: BlobContentId, portablePdbVersion: UInt16)
            Adds a CodeView entry.
        
            pdbPath: The path to the PDB. It should not be empty.
            pdbContentId: The unique id of the PDB content.
            portablePdbVersion: The version of Portable PDB format (e.g. 0x0100 for 1.0), or 0 if the PDB is not portable.
        """
        pass

    def AddEmbeddedPortablePdbEntry(self, debugMetadata, portablePdbVersion):
        """
        AddEmbeddedPortablePdbEntry(self: DebugDirectoryBuilder, debugMetadata: BlobBuilder, portablePdbVersion: UInt16)
            Adds an Embedded Portable PDB entry.
        
            debugMetadata: A Portable PDB metadata builder.
            portablePdbVersion: The version of Portable PDB format (e.g. 0x0100 for 1.0).
        """
        pass

    def AddEntry(self, type, version, stamp, data=None, dataSerializer=None):
        """
        AddEntry(self: DebugDirectoryBuilder, type: DebugDirectoryEntryType, version: UInt32, stamp: UInt32)
            Adds an entry of the specified type.
        
            type: The entry type.
            version: The entry version.
            stamp: The entry stamp.
        AddEntry[TData](self: DebugDirectoryBuilder, type: DebugDirectoryEntryType, version: UInt32, stamp: UInt32, data: TData, dataSerializer: Action[BlobBuilder, TData])
        """
        pass

    def AddPdbChecksumEntry(self, algorithmName, checksum):
        """ AddPdbChecksumEntry(self: DebugDirectoryBuilder, algorithmName: str, checksum: ImmutableArray[Byte]) """
        pass

    def AddReproducibleEntry(self):
        """
        AddReproducibleEntry(self: DebugDirectoryBuilder)
            Adds a reproducible entry.
        """
        pass


class DebugDirectoryEntry(object):
    """
    Identifies the location, size and format of a block of debug information.
    
    DebugDirectoryEntry(stamp: UInt32, majorVersion: UInt16, minorVersion: UInt16, type: DebugDirectoryEntryType, dataSize: int, dataRelativeVirtualAddress: int, dataPointer: int)
    """
    @staticmethod # known case of __new__
    def __new__(self, stamp, majorVersion, minorVersion, type, dataSize, dataRelativeVirtualAddress, dataPointer):
        """
        __new__(cls: type, stamp: UInt32, majorVersion: UInt16, minorVersion: UInt16, type: DebugDirectoryEntryType, dataSize: int, dataRelativeVirtualAddress: int, dataPointer: int)
        __new__[DebugDirectoryEntry]() -> DebugDirectoryEntry
        """
        pass

    DataPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file pointer to the debug data.

Get: DataPointer(self: DebugDirectoryEntry) -> int

"""

    DataRelativeVirtualAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address of the debug data when loaded, relative to the image base.

Get: DataRelativeVirtualAddress(self: DebugDirectoryEntry) -> int

"""

    DataSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the debug data (not including the debug directory itself).

Get: DataSize(self: DebugDirectoryEntry) -> int

"""

    IsPortableCodeView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the entry is a System.Reflection.PortableExecutable.DebugDirectoryEntryType.CodeView entry that points to a Portable PDB.

Get: IsPortableCodeView(self: DebugDirectoryEntry) -> bool

"""

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the debug data format.

Get: MajorVersion(self: DebugDirectoryEntry) -> UInt16

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the debug data format.

Get: MinorVersion(self: DebugDirectoryEntry) -> UInt16

"""

    Stamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the time and date that the debug data was created if the PE/COFF file is not deterministic; otherwise, gets a value based on the hash of the content.

Get: Stamp(self: DebugDirectoryEntry) -> UInt32

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the format of the debugging information.

Get: Type(self: DebugDirectoryEntry) -> DebugDirectoryEntryType

"""



class DebugDirectoryEntryType(Enum, IComparable, IFormattable, IConvertible):
    """
    An enumeration that describes the format of the debugging information of a System.Reflection.PortableExecutable.DebugDirectoryEntry.
    
    enum DebugDirectoryEntryType, values: CodeView (2), Coff (1), EmbeddedPortablePdb (17), PdbChecksum (19), Reproducible (16), Unknown (0)
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

    CodeView = None
    Coff = None
    EmbeddedPortablePdb = None
    PdbChecksum = None
    Reproducible = None
    Unknown = None
    value__ = None


class DirectoryEntry(object):
    """ DirectoryEntry(relativeVirtualAddress: int, size: int) """
    @staticmethod # known case of __new__
    def __new__(self, relativeVirtualAddress, size):
        """
        __new__(cls: type, relativeVirtualAddress: int, size: int)
        __new__[DirectoryEntry]() -> DirectoryEntry
        """
        pass

    RelativeVirtualAddress = None
    Size = None


class DllCharacteristics(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the characteristics of a dynamic link library.
    
    enum (flags) DllCharacteristics, values: AppContainer (4096), DynamicBase (64), HighEntropyVirtualAddressSpace (32), NoBind (2048), NoIsolation (512), NoSeh (1024), NxCompatible (256), ProcessInit (1), ProcessTerm (2), TerminalServerAware (32768), ThreadInit (4), ThreadTerm (8), WdmDriver (8192)
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

    AppContainer = None
    DynamicBase = None
    HighEntropyVirtualAddressSpace = None
    NoBind = None
    NoIsolation = None
    NoSeh = None
    NxCompatible = None
    ProcessInit = None
    ProcessTerm = None
    TerminalServerAware = None
    ThreadInit = None
    ThreadTerm = None
    value__ = None
    WdmDriver = None


class Machine(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the target machine's CPU architecture.
    
    enum Machine, values: Alpha (388), Alpha64 (644), AM33 (467), Amd64 (34404), Arm (448), Arm64 (43620), ArmThumb2 (452), Ebc (3772), I386 (332), IA64 (512), M32R (36929), MIPS16 (614), MipsFpu (870), MipsFpu16 (1126), PowerPC (496), PowerPCFP (497), SH3 (418), SH3Dsp (419), SH3E (420), SH4 (422), SH5 (424), Thumb (450), Tricore (1312), Unknown (0), WceMipsV2 (361)
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

    Alpha = None
    Alpha64 = None
    AM33 = None
    Amd64 = None
    Arm = None
    Arm64 = None
    ArmThumb2 = None
    Ebc = None
    I386 = None
    IA64 = None
    M32R = None
    MIPS16 = None
    MipsFpu = None
    MipsFpu16 = None
    PowerPC = None
    PowerPCFP = None
    SH3 = None
    SH3Dsp = None
    SH3E = None
    SH4 = None
    SH5 = None
    Thumb = None
    Tricore = None
    Unknown = None
    value__ = None
    WceMipsV2 = None


class PEBuilder(object):
    # no doc
    def CreateSections(self, *args): #cannot find CLR method
        """ CreateSections(self: PEBuilder) -> ImmutableArray[Section] """
        pass

    def GetDirectories(self, *args): #cannot find CLR method
        """ GetDirectories(self: PEBuilder) -> PEDirectoriesBuilder """
        pass

    def GetSections(self, *args): #cannot find CLR method
        """ GetSections(self: PEBuilder) -> ImmutableArray[Section] """
        pass

    def Serialize(self, builder):
        """ Serialize(self: PEBuilder, builder: BlobBuilder) -> BlobContentId """
        pass

    def SerializeSection(self, *args): #cannot find CLR method
        """ SerializeSection(self: PEBuilder, name: str, location: SectionLocation) -> BlobBuilder """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, header: PEHeaderBuilder, deterministicIdProvider: Func[IEnumerable[Blob], BlobContentId]) """
        pass

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Header(self: PEBuilder) -> PEHeaderBuilder

"""

    IdProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdProvider(self: PEBuilder) -> Func[IEnumerable[Blob], BlobContentId]

"""

    IsDeterministic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeterministic(self: PEBuilder) -> bool

"""


    Section = None


class ManagedPEBuilder(PEBuilder):
    """ ManagedPEBuilder(header: PEHeaderBuilder, metadataRootBuilder: MetadataRootBuilder, ilStream: BlobBuilder, mappedFieldData: BlobBuilder, managedResources: BlobBuilder, nativeResources: ResourceSectionBuilder, debugDirectoryBuilder: DebugDirectoryBuilder, strongNameSignatureSize: int, entryPoint: MethodDefinitionHandle, flags: CorFlags, deterministicIdProvider: Func[IEnumerable[Blob], BlobContentId]) """
    def Sign(self, peImage, signatureProvider):
        """ Sign(self: ManagedPEBuilder, peImage: BlobBuilder, signatureProvider: Func[IEnumerable[Blob], Array[Byte]]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, header, metadataRootBuilder, ilStream, mappedFieldData, managedResources, nativeResources, debugDirectoryBuilder, strongNameSignatureSize, entryPoint, flags, deterministicIdProvider):
        """ __new__(cls: type, header: PEHeaderBuilder, metadataRootBuilder: MetadataRootBuilder, ilStream: BlobBuilder, mappedFieldData: BlobBuilder, managedResources: BlobBuilder, nativeResources: ResourceSectionBuilder, debugDirectoryBuilder: DebugDirectoryBuilder, strongNameSignatureSize: int, entryPoint: MethodDefinitionHandle, flags: CorFlags, deterministicIdProvider: Func[IEnumerable[Blob], BlobContentId]) """
        pass

    ManagedResourcesDataAlignment = 8
    MappedFieldDataAlignment = 8


class PdbChecksumDebugDirectoryData(object):
    """ Represents a PDB Checksum debug directory entry. """
    AlgorithmName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the crypto hash algorithm used to calculate the checksum.

Get: AlgorithmName(self: PdbChecksumDebugDirectoryData) -> str

"""

    Checksum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The checksum of the PDB content.

Get: Checksum(self: PdbChecksumDebugDirectoryData) -> ImmutableArray[Byte]

"""



class PEDirectoriesBuilder(object):
    """
    Builds PE directories.
    
    PEDirectoriesBuilder()
    """
    AddressOfEntryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The address of the entry point relative to the image base when the PE file is loaded into memory.

Get: AddressOfEntryPoint(self: PEDirectoriesBuilder) -> int

Set: AddressOfEntryPoint(self: PEDirectoriesBuilder) = value
"""

    BaseRelocationTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base relocation table image directory entry.

Get: BaseRelocationTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: BaseRelocationTable(self: PEDirectoriesBuilder) = value
"""

    BoundImportTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bound import image directory entry.

Get: BoundImportTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: BoundImportTable(self: PEDirectoriesBuilder) = value
"""

    CopyrightTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The copyright/architecture image directory entry.

Get: CopyrightTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: CopyrightTable(self: PEDirectoriesBuilder) = value
"""

    CorHeaderTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The COM descriptortable image directory entry.

Get: CorHeaderTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: CorHeaderTable(self: PEDirectoriesBuilder) = value
"""

    DebugTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The debug table image directory entry.

Get: DebugTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: DebugTable(self: PEDirectoriesBuilder) = value
"""

    DelayImportTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The delay import table image directory entry.

Get: DelayImportTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: DelayImportTable(self: PEDirectoriesBuilder) = value
"""

    ExceptionTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The exception table image directory entry.

Get: ExceptionTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: ExceptionTable(self: PEDirectoriesBuilder) = value
"""

    ExportTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The export table image directory entry.

Get: ExportTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: ExportTable(self: PEDirectoriesBuilder) = value
"""

    GlobalPointerTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The global pointer table image directory entry.

Get: GlobalPointerTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: GlobalPointerTable(self: PEDirectoriesBuilder) = value
"""

    ImportAddressTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The import address table (IAT) image directory entry.

Get: ImportAddressTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: ImportAddressTable(self: PEDirectoriesBuilder) = value
"""

    ImportTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The import table image directory entry.

Get: ImportTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: ImportTable(self: PEDirectoriesBuilder) = value
"""

    LoadConfigTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The load configuration table image directory entry.

Get: LoadConfigTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: LoadConfigTable(self: PEDirectoriesBuilder) = value
"""

    ResourceTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The resource table image directory entry.

Get: ResourceTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: ResourceTable(self: PEDirectoriesBuilder) = value
"""

    ThreadLocalStorageTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The thread local storage (TLS) table image directory entry.

Get: ThreadLocalStorageTable(self: PEDirectoriesBuilder) -> DirectoryEntry

Set: ThreadLocalStorageTable(self: PEDirectoriesBuilder) = value
"""



class PEHeader(object):
    # no doc
    AddressOfEntryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address of the entry point relative to the image base when the PE file is loaded into memory.

Get: AddressOfEntryPoint(self: PEHeader) -> int

"""

    BaseOfCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address of the beginning-of-code section relative to the image base when the image is loaded into memory.

Get: BaseOfCode(self: PEHeader) -> int

"""

    BaseOfData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the address of the beginning-of-data section relative to the image base when the image is loaded into memory.

Get: BaseOfData(self: PEHeader) -> int

"""

    BaseRelocationTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseRelocationTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    BoundImportTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundImportTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    CertificateTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Certificate Table entry, which points to a table of attribute certificates.

Get: CertificateTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    CheckSum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the image file checksum.

Get: CheckSum(self: PEHeader) -> UInt32

"""

    CopyrightTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CopyrightTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    CorHeaderTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorHeaderTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    DebugTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DebugTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    DelayImportTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DelayImportTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    DllCharacteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DllCharacteristics(self: PEHeader) -> DllCharacteristics

"""

    ExceptionTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    ExportTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    FileAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alignment factor (in bytes) that is used to align the raw data of sections in the image file.

Get: FileAlignment(self: PEHeader) -> int

"""

    GlobalPointerTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalPointerTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    ImageBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the preferred address of the first byte of the image when it is loaded into memory.

Get: ImageBase(self: PEHeader) -> UInt64

"""

    ImportAddressTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportAddressTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    ImportTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    LoadConfigTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadConfigTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    Magic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that identifies the format of the image file.

Get: Magic(self: PEHeader) -> PEMagic

"""

    MajorImageVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the image.

Get: MajorImageVersion(self: PEHeader) -> UInt16

"""

    MajorLinkerVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the linker major version number.

Get: MajorLinkerVersion(self: PEHeader) -> Byte

"""

    MajorOperatingSystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the required operating system.

Get: MajorOperatingSystemVersion(self: PEHeader) -> UInt16

"""

    MajorSubsystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the subsystem.

Get: MajorSubsystemVersion(self: PEHeader) -> UInt16

"""

    MinorImageVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the image.

Get: MinorImageVersion(self: PEHeader) -> UInt16

"""

    MinorLinkerVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the linker minor version number.

Get: MinorLinkerVersion(self: PEHeader) -> Byte

"""

    MinorOperatingSystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the required operating system.

Get: MinorOperatingSystemVersion(self: PEHeader) -> UInt16

"""

    MinorSubsystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the subsystem.

Get: MinorSubsystemVersion(self: PEHeader) -> UInt16

"""

    NumberOfRvaAndSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of data-directory entries in the remainder of the System.Reflection.PortableExecutable.PEHeader. Each describes a location and size.

Get: NumberOfRvaAndSizes(self: PEHeader) -> int

"""

    ResourceTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourceTableDirectory(self: PEHeader) -> DirectoryEntry

"""

    SectionAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the alignment (in bytes) of sections when they are loaded into memory.

Get: SectionAlignment(self: PEHeader) -> int

"""

    SizeOfCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the code (text) section, or the sum of all code sections if there are multiple sections.

Get: SizeOfCode(self: PEHeader) -> int

"""

    SizeOfHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the combined size of an MS DOS stub, PE header, and section headers rounded up to a multiple of FileAlignment.

Get: SizeOfHeaders(self: PEHeader) -> int

"""

    SizeOfHeapCommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the local heap space to commit.

Get: SizeOfHeapCommit(self: PEHeader) -> UInt64

"""

    SizeOfHeapReserve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the local heap space to reserve. Only System.Reflection.PortableExecutable.PEHeader.SizeOfHeapCommit is committed; the rest is made available one page at a time until the reserve size is reached.

Get: SizeOfHeapReserve(self: PEHeader) -> UInt64

"""

    SizeOfImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size (in bytes) of the image, including all headers, as the image is loaded in memory.

Get: SizeOfImage(self: PEHeader) -> int

"""

    SizeOfInitializedData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the initialized data section, or the sum of all such sections if there are multiple data sections.

Get: SizeOfInitializedData(self: PEHeader) -> int

"""

    SizeOfStackCommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the stack to commit.

Get: SizeOfStackCommit(self: PEHeader) -> UInt64

"""

    SizeOfStackReserve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the stack to reserve. Only System.Reflection.PortableExecutable.PEHeader.SizeOfStackCommit is committed; the rest is made available one page at a time until the reserve size is reached.

Get: SizeOfStackReserve(self: PEHeader) -> UInt64

"""

    SizeOfUninitializedData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the uninitialized data section (BSS), or the sum of all such sections if there are multiple BSS sections.

Get: SizeOfUninitializedData(self: PEHeader) -> int

"""

    Subsystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the subsystem that is required to run this image.

Get: Subsystem(self: PEHeader) -> Subsystem

"""

    ThreadLocalStorageTableDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThreadLocalStorageTableDirectory(self: PEHeader) -> DirectoryEntry

"""



class PEHeaderBuilder(object):
    """
    Defines the header for a portable executable (PE) file.
    
    PEHeaderBuilder(machine: Machine, sectionAlignment: int, fileAlignment: int, imageBase: UInt64, majorLinkerVersion: Byte, minorLinkerVersion: Byte, majorOperatingSystemVersion: UInt16, minorOperatingSystemVersion: UInt16, majorImageVersion: UInt16, minorImageVersion: UInt16, majorSubsystemVersion: UInt16, minorSubsystemVersion: UInt16, subsystem: Subsystem, dllCharacteristics: DllCharacteristics, imageCharacteristics: Characteristics, sizeOfStackReserve: UInt64, sizeOfStackCommit: UInt64, sizeOfHeapReserve: UInt64, sizeOfHeapCommit: UInt64)
    """
    @staticmethod
    def CreateExecutableHeader():
        """
        CreateExecutableHeader() -> PEHeaderBuilder
        
            Creates an executable header.
            Returns: A System.Reflection.PortableExecutable.PEHeaderBuilder instance representing the executable header.
        """
        pass

    @staticmethod
    def CreateLibraryHeader():
        """
        CreateLibraryHeader() -> PEHeaderBuilder
        
            Creates a library header.
            Returns: A System.Reflection.PortableExecutable.PEHeaderBuilder instance representing the library header.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, machine, sectionAlignment, fileAlignment, imageBase, majorLinkerVersion, minorLinkerVersion, majorOperatingSystemVersion, minorOperatingSystemVersion, majorImageVersion, minorImageVersion, majorSubsystemVersion, minorSubsystemVersion, subsystem, dllCharacteristics, imageCharacteristics, sizeOfStackReserve, sizeOfStackCommit, sizeOfHeapReserve, sizeOfHeapCommit):
        """ __new__(cls: type, machine: Machine, sectionAlignment: int, fileAlignment: int, imageBase: UInt64, majorLinkerVersion: Byte, minorLinkerVersion: Byte, majorOperatingSystemVersion: UInt16, minorOperatingSystemVersion: UInt16, majorImageVersion: UInt16, minorImageVersion: UInt16, majorSubsystemVersion: UInt16, minorSubsystemVersion: UInt16, subsystem: Subsystem, dllCharacteristics: DllCharacteristics, imageCharacteristics: Characteristics, sizeOfStackReserve: UInt64, sizeOfStackCommit: UInt64, sizeOfHeapReserve: UInt64, sizeOfHeapCommit: UInt64) """
        pass

    DllCharacteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the dynamic linker library characteristics.

Get: DllCharacteristics(self: PEHeaderBuilder) -> DllCharacteristics

"""

    FileAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The alignment factor (in bytes) that is used to align the raw data of sections in the image file. The value should be a power of 2 between 512 and 64K, inclusive. The default is 512. If the section alignment is less than the architecture's page size, then file alignment must match the section alignment.

Get: FileAlignment(self: PEHeaderBuilder) -> int

"""

    ImageBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The preferred address of the first byte of image when loaded into memory; must be a multiple of 64K.

Get: ImageBase(self: PEHeaderBuilder) -> UInt64

"""

    ImageCharacteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the image characteristics.

Get: ImageCharacteristics(self: PEHeaderBuilder) -> Characteristics

"""

    Machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The target machine's CPU architecture.

Get: Machine(self: PEHeaderBuilder) -> Machine

"""

    MajorImageVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The major version number of the image.

Get: MajorImageVersion(self: PEHeaderBuilder) -> UInt16

"""

    MajorLinkerVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The linker major version number.

Get: MajorLinkerVersion(self: PEHeaderBuilder) -> Byte

"""

    MajorOperatingSystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The major version number of the required operating system.

Get: MajorOperatingSystemVersion(self: PEHeaderBuilder) -> UInt16

"""

    MajorSubsystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The major version number of the subsystem.

Get: MajorSubsystemVersion(self: PEHeaderBuilder) -> UInt16

"""

    MinorImageVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minor version number of the image.

Get: MinorImageVersion(self: PEHeaderBuilder) -> UInt16

"""

    MinorLinkerVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The linker minor version number.

Get: MinorLinkerVersion(self: PEHeaderBuilder) -> Byte

"""

    MinorOperatingSystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minor version number of the required operating system.

Get: MinorOperatingSystemVersion(self: PEHeaderBuilder) -> UInt16

"""

    MinorSubsystemVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minor version number of the subsystem.

Get: MinorSubsystemVersion(self: PEHeaderBuilder) -> UInt16

"""

    SectionAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The alignment (in bytes) of sections when they are loaded into memory.

Get: SectionAlignment(self: PEHeaderBuilder) -> int

"""

    SizeOfHeapCommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the local heap space to commit.

Get: SizeOfHeapCommit(self: PEHeaderBuilder) -> UInt64

"""

    SizeOfHeapReserve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the local heap space to reserve. Only System.Reflection.PortableExecutable.PEHeaderBuilder.SizeOfHeapCommit is committed; the rest is made available one page at a time until the reserve size is reached.

Get: SizeOfHeapReserve(self: PEHeaderBuilder) -> UInt64

"""

    SizeOfStackCommit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the stack to commit.

Get: SizeOfStackCommit(self: PEHeaderBuilder) -> UInt64

"""

    SizeOfStackReserve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the stack to reserve. Only System.Reflection.PortableExecutable.PEHeaderBuilder.SizeOfStackCommit is committed; the rest is made available one page at a time until the reserve size is reached.

Get: SizeOfStackReserve(self: PEHeaderBuilder) -> UInt64

"""

    Subsystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The subsystem that is required to run this image.

Get: Subsystem(self: PEHeaderBuilder) -> Subsystem

"""



class PEHeaders(object):
    """
    Defines a type that reads PE (Portable Executable) and COFF (Common Object File Format) headers from a stream.
    
    PEHeaders(peStream: Stream)
    PEHeaders(peStream: Stream, size: int)
    PEHeaders(peStream: Stream, size: int, isLoadedImage: bool)
    """
    def GetContainingSectionIndex(self, relativeVirtualAddress):
        """
        GetContainingSectionIndex(self: PEHeaders, relativeVirtualAddress: int) -> int
        
            Searches sections of the PE image for the section that contains the specified Relative Virtual Address.
        
            relativeVirtualAddress: The relative virtual address to search for.
            Returns: The index of the section that contains relativeVirtualAddress, or -1 if there the search is unsuccessful.
        """
        pass

    def TryGetDirectoryOffset(self, directory, offset):
        """
        TryGetDirectoryOffset(self: PEHeaders, directory: DirectoryEntry) -> (bool, int)
        
            Gets the offset (in bytes) from the start of the image to the given directory data.
        
            directory: The PE directory entry.
            Returns: ue if the directory data is found; lse otherwise.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, peStream, size=None, isLoadedImage=None):
        """
        __new__(cls: type, peStream: Stream)
        __new__(cls: type, peStream: Stream, size: int)
        __new__(cls: type, peStream: Stream, size: int, isLoadedImage: bool)
        """
        pass

    CoffHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the COFF header of the image.

Get: CoffHeader(self: PEHeaders) -> CoffHeader

"""

    CoffHeaderStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the byte offset from the start of the PE image to the start of the COFF header.

Get: CoffHeaderStartOffset(self: PEHeaders) -> int

"""

    CorHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the COR header.

Get: CorHeader(self: PEHeaders) -> CorHeader

"""

    CorHeaderStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the byte offset from the start of the image to the COR header.

Get: CorHeaderStartOffset(self: PEHeaders) -> int

"""

    IsCoffOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the image is Coff only.

Get: IsCoffOnly(self: PEHeaders) -> bool

"""

    IsConsoleApplication = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the image represents a Windows console application.

Get: IsConsoleApplication(self: PEHeaders) -> bool

"""

    IsDll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the image represents a dynamic link library.

Get: IsDll(self: PEHeaders) -> bool

"""

    IsExe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the image represents an executable.

Get: IsExe(self: PEHeaders) -> bool

"""

    MetadataSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the CLI metadata.

Get: MetadataSize(self: PEHeaders) -> int

"""

    MetadataStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the offset (in bytes) from the start of the PE image to the start of the CLI metadata.

Get: MetadataStartOffset(self: PEHeaders) -> int

"""

    PEHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the image's PE header.

Get: PEHeader(self: PEHeaders) -> PEHeader

"""

    PEHeaderStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the byte offset of the header from the start of the image.

Get: PEHeaderStartOffset(self: PEHeaders) -> int

"""

    SectionHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the PE section headers.

Get: SectionHeaders(self: PEHeaders) -> ImmutableArray[SectionHeader]

"""



class PEMagic(Enum, IComparable, IFormattable, IConvertible):
    """ enum PEMagic, values: PE32 (267), PE32Plus (523) """
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

    PE32 = None
    PE32Plus = None
    value__ = None


class PEMemoryBlock(object):
    # no doc
    def GetContent(self, start=None, length=None):
        """
        GetContent(self: PEMemoryBlock) -> ImmutableArray[Byte]
        
            Reads the contents of the entire block into an array.
            Returns: An immutable byte array.
        GetContent(self: PEMemoryBlock, start: int, length: int) -> ImmutableArray[Byte]
        
            Reads the contents of a part of the block into an array.
        
            start: The starting position in the block.
            length: The number of bytes to read.
            Returns: An immutable array of bytes.
        """
        pass

    def GetReader(self, start=None, length=None):
        """
        GetReader(self: PEMemoryBlock) -> BlobReader
        
            Creates a System.Reflection.Metadata.BlobReader for a blob spanning the entire block.
            Returns: A reader for a blob spanning the entire block.
        GetReader(self: PEMemoryBlock, start: int, length: int) -> BlobReader
        
            Creates a System.Reflection.Metadata.BlobReader for a blob spanning a part of the block.
        
            start: The starting position in the block.
            length: The number of bytes in the portion of the block.
            Returns: A reader for a blob spanning a portion of the block.
        """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the block.

Get: Length(self: PEMemoryBlock) -> int

"""

    Pointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the first byte of the block.

Get: Pointer(self: PEMemoryBlock) -> Byte*

"""



class PEReader(object, IDisposable):
    """
    Provides a reader for Portable Executable format (PE) files.
    
    PEReader(peImage: Byte*, size: int)
    PEReader(peImage: Byte*, size: int, isLoadedImage: bool)
    PEReader(peStream: Stream)
    PEReader(peStream: Stream, options: PEStreamOptions)
    PEReader(peStream: Stream, options: PEStreamOptions, size: int)
    PEReader(peImage: ImmutableArray[Byte])
    """
    def Dispose(self):
        """
        Dispose(self: PEReader)
            Disposes all memory allocated by the reader.
        """
        pass

    def GetEntireImage(self):
        """
        GetEntireImage(self: PEReader) -> PEMemoryBlock
        
            Gets a System.Reflection.PortableExecutable.PEMemoryBlock object containing the entire PE image.
            Returns: A memory block that contains the entire PE image.
        """
        pass

    def GetMetadata(self):
        """
        GetMetadata(self: PEReader) -> PEMemoryBlock
        
            Loads a PE section that contains CLI metadata.
            Returns: A memory block that contains the CLI metadata.
        """
        pass

    def GetSectionData(self, *__args):
        """
        GetSectionData(self: PEReader, relativeVirtualAddress: int) -> PEMemoryBlock
        
            Loads the PE section that contains the specified relative virtual address into memory and returns a memory block that starts at that address and ends at the end of the containing 
             section.
        
        
            relativeVirtualAddress: The Relative Virtual Address of the data to read.
            Returns: A memory block that starats at relativeVirtualAddress and ends at the end of the containing section, or an empty block if relativeVirtualAddress doesn't represent a location in any 
             of the PE sections of this PE image.
        
        GetSectionData(self: PEReader, sectionName: str) -> PEMemoryBlock
        
            Loads the PE section with the specified name into memory and returns a memory block that spans the section.
        
            sectionName: The name of the section.
            Returns: A memory block that spans the section, or an empty block if no section of the given sectionName exists in this PE image.
        """
        pass

    def ReadCodeViewDebugDirectoryData(self, entry):
        """
        ReadCodeViewDebugDirectoryData(self: PEReader, entry: DebugDirectoryEntry) -> CodeViewDebugDirectoryData
        
            Reads the data pointed to by the specified Debug Directory entry and interprets it as CodeView.
        
            entry: A Debug Directory entry instance.
            Returns: A code view debug directory data instance.
        """
        pass

    def ReadDebugDirectory(self):
        """
        ReadDebugDirectory(self: PEReader) -> ImmutableArray[DebugDirectoryEntry]
        
            Reads all Debug Directory table entries.
            Returns: An array of Debug Directory table entries.
        """
        pass

    def ReadEmbeddedPortablePdbDebugDirectoryData(self, entry):
        """
        ReadEmbeddedPortablePdbDebugDirectoryData(self: PEReader, entry: DebugDirectoryEntry) -> MetadataReaderProvider
        
            Reads the data pointed to by the specified Debug Directory entry and interprets it as an Embedded Portable PDB blob.
        
            entry: The Debug Directory entry whose data is to be read.
            Returns: The provider of a metadata reader for reading a Portable PDB image.
        """
        pass

    def ReadPdbChecksumDebugDirectoryData(self, entry):
        """
        ReadPdbChecksumDebugDirectoryData(self: PEReader, entry: DebugDirectoryEntry) -> PdbChecksumDebugDirectoryData
        
            Reads the data pointed to by the specified Debug Directory entry and interprets it as a PDB Checksum entry.
        
            entry: The Debug Directory entry whose data is to be read.
            Returns: The PDB Checksum entry.
        """
        pass

    def TryOpenAssociatedPortablePdb(self, peImagePath, pdbFileStreamProvider, pdbReaderProvider, pdbPath):
        """ TryOpenAssociatedPortablePdb(self: PEReader, peImagePath: str, pdbFileStreamProvider: Func[str, Stream]) -> (bool, MetadataReaderProvider, str) """
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
        __new__(cls: type, peImage: Byte*, size: int)
        __new__(cls: type, peImage: Byte*, size: int, isLoadedImage: bool)
        __new__(cls: type, peStream: Stream)
        __new__(cls: type, peStream: Stream, options: PEStreamOptions)
        __new__(cls: type, peStream: Stream, options: PEStreamOptions, size: int)
        __new__(cls: type, peImage: ImmutableArray[Byte])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    HasMetadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the PE image contains CLI metadata.

Get: HasMetadata(self: PEReader) -> bool

"""

    IsEntireImageAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the reader can access the entire PE image.

Get: IsEntireImageAvailable(self: PEReader) -> bool

"""

    IsLoadedImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates if the PE image has been loaded into memory by the OS loader.

Get: IsLoadedImage(self: PEReader) -> bool

"""

    PEHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the PE headers.

Get: PEHeaders(self: PEReader) -> PEHeaders

"""



class PEStreamOptions(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides options that specify how sections of a PE image are read from a stream.
    
    enum (flags) PEStreamOptions, values: Default (0), IsLoadedImage (8), LeaveOpen (1), PrefetchEntireImage (4), PrefetchMetadata (2)
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

    Default = None
    IsLoadedImage = None
    LeaveOpen = None
    PrefetchEntireImage = None
    PrefetchMetadata = None
    value__ = None


class ResourceSectionBuilder(object):
    """ Defines the base class for a PE resource section builder. Derive from System.Reflection.PortableExecutable.ResourceSectionBuilder to provide serialization logic for native resources. """
    def Serialize(self, *args): #cannot find CLR method
        """
        Serialize(self: ResourceSectionBuilder, builder: BlobBuilder, location: SectionLocation)
            Serializes the specified resource.
        
            builder: A blob that contains the data to serialize.
            location: The location to which to serialize builder.
        """
        pass


class SectionCharacteristics(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) SectionCharacteristics, values: Align1024Bytes (11534336), Align128Bytes (8388608), Align16Bytes (5242880), Align1Bytes (1048576), Align2048Bytes (12582912), Align256Bytes (9437184), Align2Bytes (2097152), Align32Bytes (6291456), Align4096Bytes (13631488), Align4Bytes (3145728), Align512Bytes (10485760), Align64Bytes (7340032), Align8192Bytes (14680064), Align8Bytes (4194304), AlignMask (15728640), ContainsCode (32), ContainsInitializedData (64), ContainsUninitializedData (128), GPRel (32768), LinkerComdat (4096), LinkerInfo (512), LinkerNRelocOvfl (16777216), LinkerOther (256), LinkerRemove (2048), Mem16Bit (131072), MemDiscardable (33554432), MemExecute (536870912), MemFardata (32768), MemLocked (262144), MemNotCached (67108864), MemNotPaged (134217728), MemPreload (524288), MemProtected (16384), MemPurgeable (131072), MemRead (1073741824), MemShared (268435456), MemSysheap (65536), MemWrite (2147483648), NoDeferSpecExc (16384), TypeCopy (16), TypeDSect (1), TypeGroup (4), TypeNoLoad (2), TypeNoPad (8), TypeOver (1024), TypeReg (0) """
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

    Align1024Bytes = None
    Align128Bytes = None
    Align16Bytes = None
    Align1Bytes = None
    Align2048Bytes = None
    Align256Bytes = None
    Align2Bytes = None
    Align32Bytes = None
    Align4096Bytes = None
    Align4Bytes = None
    Align512Bytes = None
    Align64Bytes = None
    Align8192Bytes = None
    Align8Bytes = None
    AlignMask = None
    ContainsCode = None
    ContainsInitializedData = None
    ContainsUninitializedData = None
    GPRel = None
    LinkerComdat = None
    LinkerInfo = None
    LinkerNRelocOvfl = None
    LinkerOther = None
    LinkerRemove = None
    Mem16Bit = None
    MemDiscardable = None
    MemExecute = None
    MemFardata = None
    MemLocked = None
    MemNotCached = None
    MemNotPaged = None
    MemPreload = None
    MemProtected = None
    MemPurgeable = None
    MemRead = None
    MemShared = None
    MemSysheap = None
    MemWrite = None
    NoDeferSpecExc = None
    TypeCopy = None
    TypeDSect = None
    TypeGroup = None
    TypeNoLoad = None
    TypeNoPad = None
    TypeOver = None
    TypeReg = None
    value__ = None


class SectionHeader(object):
    """ Provides information about the section header of a PE/COFF file. """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the section.

Get: Name(self: SectionHeader) -> str

"""

    NumberOfLineNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of line-number entries for the section.

Get: NumberOfLineNumbers(self: SectionHeader) -> UInt16

"""

    NumberOfRelocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of relocation entries for the section.

Get: NumberOfRelocations(self: SectionHeader) -> UInt16

"""

    PointerToLineNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file pointer to the beginning of line-number entries for the section.

Get: PointerToLineNumbers(self: SectionHeader) -> int

"""

    PointerToRawData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file pointer to the first page of the section within the COFF file.

Get: PointerToRawData(self: SectionHeader) -> int

"""

    PointerToRelocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file pointer to the beginning of relocation entries for the section.

Get: PointerToRelocations(self: SectionHeader) -> int

"""

    SectionCharacteristics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the flags that describe the characteristics of the section.

Get: SectionCharacteristics(self: SectionHeader) -> SectionCharacteristics

"""

    SizeOfRawData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the section (for object files) or the size of the initialized data on disk (for image files).

Get: SizeOfRawData(self: SectionHeader) -> int

"""

    VirtualAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the virtual addess of the section.

Get: VirtualAddress(self: SectionHeader) -> int

"""

    VirtualSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total size of the section when loaded into memory.

Get: VirtualSize(self: SectionHeader) -> int

"""



class SectionLocation(object):
    """ SectionLocation(relativeVirtualAddress: int, pointerToRawData: int) """
    @staticmethod # known case of __new__
    def __new__(self, relativeVirtualAddress, pointerToRawData):
        """
        __new__(cls: type, relativeVirtualAddress: int, pointerToRawData: int)
        __new__[SectionLocation]() -> SectionLocation
        """
        pass

    PointerToRawData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointerToRawData(self: SectionLocation) -> int

"""

    RelativeVirtualAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeVirtualAddress(self: SectionLocation) -> int

"""



class Subsystem(Enum, IComparable, IFormattable, IConvertible):
    """
    Describes the subsystem requirement for the image.
    
    enum Subsystem, values: EfiApplication (10), EfiBootServiceDriver (11), EfiRom (13), EfiRuntimeDriver (12), Native (1), NativeWindows (8), OS2Cui (5), PosixCui (7), Unknown (0), WindowsBootApplication (16), WindowsCEGui (9), WindowsCui (3), WindowsGui (2), Xbox (14)
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

    EfiApplication = None
    EfiBootServiceDriver = None
    EfiRom = None
    EfiRuntimeDriver = None
    Native = None
    NativeWindows = None
    OS2Cui = None
    PosixCui = None
    Unknown = None
    value__ = None
    WindowsBootApplication = None
    WindowsCEGui = None
    WindowsCui = None
    WindowsGui = None
    Xbox = None


