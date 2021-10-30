# encoding: utf-8
# module Microsoft.Diagnostics.Runtime.Utilities calls itself Utilities
# from Microsoft.Diagnostics.Runtime, Version=2.0.5.1201, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class COMHelper(object):
    """ Base class for COM related objects in ClrMD. """
    @staticmethod
    def QueryInterface(pUnk, riid, result):
        """ QueryInterface(pUnk: IntPtr, riid: Guid) -> (HResult, Guid, IntPtr) """
        pass

    @staticmethod
    def Release(pUnk):
        """
        Release(pUnk: IntPtr) -> int
        
            Release an IUnknown pointer.
        
            pUnk: A pointer to the IUnknown interface to release.
            Returns: The result of pUnk->Release().
        """
        pass

    AddRefDelegate = None
    IUnknownGuid = None
    QueryInterfaceDelegate = None
    ReleaseDelegate = None


class CallableCOMWrapper(COMHelper, IDisposable):
    # no doc
    def AddRef(self):
        """ AddRef(self: CallableCOMWrapper) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: CallableCOMWrapper) """
        pass

    def QueryInterface(self, riid):
        """ QueryInterface(self: CallableCOMWrapper, riid: Guid) -> (IntPtr, Guid) """
        pass

    def Release(self):
        """ Release(self: CallableCOMWrapper) -> int """
        pass

    def SuppressRelease(self):
        """ SuppressRelease(self: CallableCOMWrapper) """
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
        """
        __new__(cls: type, toClone: CallableCOMWrapper)
        __new__(cls: type, library: RefCountedFreeLibrary, desiredInterface: Guid, pUnknown: IntPtr) -> Guid
        """
        pass

    Self = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vtable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class COMCallableIUnknown(COMHelper):
    """
    A class that allows you to build a custom IUnknown based interface to pass as a COM object.
                This class is public to allow others to use this code and not duplicate it, but it is not
                intended for general use.
    
    COMCallableIUnknown()
    """
    def AddInterface(self, guid, validate):
        """
        AddInterface(self: COMCallableIUnknown, guid: Guid, validate: bool) -> VTableBuilder
        
            Adds an IUnknown based interface to this COM object.
        
            guid: The GUID of this interface.
            validate: Whether or not to validate the delegates that
                    used to build this COM interface's methods.
            Returns: A VTableBuilder to construct this interface.  Note that until VTableBuilder.Complete
                    is called, the interface will not be registered.
        """
        pass

    def AddRef(self):
        """
        AddRef(self: COMCallableIUnknown) -> int
        
            AddRef.
            Returns: The new ref count.
        """
        pass

    def Destroy(self, *args): #cannot find CLR method
        """ Destroy(self: COMCallableIUnknown) """
        pass

    def Release(self):
        """
        Release(self: COMCallableIUnknown) -> int
        
            Release.
            Returns: The new RefCount.
        """
        pass

    IUnknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the IUnknown VTable for this object.

Get: IUnknown(self: COMCallableIUnknown) -> IUnknownVTable

"""

    IUnknownObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the IUnknown pointer to this object.

Get: IUnknownObject(self: COMCallableIUnknown) -> IntPtr

"""



class ElfAuxvType(Enum, IComparable, IFormattable, IConvertible):
    """ enum ElfAuxvType, values: Base (7), Null (0) """
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

    Base = None
    Null = None
    value__ = None


class ElfCoreFile(object, IDisposable):
    """
    A helper class to read linux coredumps.
    
    ElfCoreFile(coredump: str)
    ElfCoreFile(stream: Stream, leaveOpen: bool)
    """
    def Dispose(self):
        """ Dispose(self: ElfCoreFile) """
        pass

    def EnumeratePRStatus(self):
        """
        EnumeratePRStatus(self: ElfCoreFile) -> IEnumerable[IElfPRStatus]
        
            Enumerates all prstatus notes contained within this coredump.
        """
        pass

    def GetAuxvValue(self, type):
        """
        GetAuxvValue(self: ElfCoreFile, type: ElfAuxvType) -> UInt64
        
            Returns the Auxv value of the given type.
        """
        pass

    def ReadMemory(self, address, buffer):
        """ ReadMemory(self: ElfCoreFile, address: UInt64, buffer: Span[Byte]) -> int """
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
        __new__(cls: type, coredump: str)
        __new__(cls: type, stream: Stream, leaveOpen: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    ElfFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """All coredumps are themselves ELF files.  This property returns the ElfFile that represents this coredump.

Get: ElfFile(self: ElfCoreFile) -> ElfFile

"""

    LoadedImages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A mapping of all loaded images in the process.  The key is the base address that the module is loaded at.

Get: LoadedImages(self: ElfCoreFile) -> ImmutableDictionary[UInt64, ElfLoadedImage]

"""



class ElfFile(object, IDisposable):
    """
    A helper class to read ELF files.
    
    ElfFile(filename: str)
    ElfFile(stream: Stream, leaveOpen: bool)
    ElfFile(stream: Stream, position: UInt64, leaveOpen: bool, isVirtual: bool)
    """
    def Dispose(self):
        """ Dispose(self: ElfFile) """
        pass

    def TryGetExportSymbol(self, symbolName, offset):
        """
        TryGetExportSymbol(self: ElfFile, symbolName: str) -> (bool, UInt64)
        
            Returns the address of a module export symbol if found
        
            symbolName: symbol name (without the module name prepended)
            Returns: true if found
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
    def __new__(self, *__args):
        """
        __new__(cls: type, filename: str)
        __new__(cls: type, stream: Stream, leaveOpen: bool)
        __new__(cls: type, stream: Stream, position: UInt64, leaveOpen: bool, isVirtual: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    BuildId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the build id of this ELF module (or ImmutableArray.Default if it doesn't exist).

Get: BuildId(self: ElfFile) -> ImmutableArray[Byte]

"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ElfHeader of this file.

Get: Header(self: ElfFile) -> IElfHeader

"""

    Notes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of ElfNotes for this file.

Get: Notes(self: ElfFile) -> ImmutableArray[ElfNote]

"""

    ProgramHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of ProgramHeaders for this file.

Get: ProgramHeaders(self: ElfFile) -> ImmutableArray[ElfProgramHeader]

"""



class ElfHeaderType(Enum, IComparable, IFormattable, IConvertible):
    """
    The type of ELF file.
    
    enum ElfHeaderType, values: Core (4), Executable (2), Relocatable (1), Shared (3)
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

    Core = None
    Executable = None
    Relocatable = None
    Shared = None
    value__ = None


class ElfLoadedImage(object):
    """ A representation of an ELF loaded image section. """
    def AsStream(self):
        """
        AsStream(self: ElfLoadedImage) -> Stream
        
            Returns this ELF loaded image as a stream.
        """
        pass

    def Open(self):
        """
        Open(self: ElfLoadedImage) -> ElfFile
        
            Open the loaded image as an ELFFile.
            Returns: An ELFFile if this is a valid ELF image, null otherwise.
        """
        pass

    def ToString(self):
        """
        ToString(self: ElfLoadedImage) -> str
        
            Returns Microsoft.Diagnostics.Runtime.Utilities.ElfLoadedImage.FileName.
            Returns: Microsoft.Diagnostics.Runtime.Utilities.ElfLoadedImage.FileName
        """
        pass

    BaseAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The BaseAddress of this image

Get: BaseAddress(self: ElfLoadedImage) -> UInt64

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: ElfLoadedImage) -> str

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of this image in memory.

Get: Size(self: ElfLoadedImage) -> UInt64

"""



class ElfMachine(Enum, IComparable, IFormattable, IConvertible):
    """
    The ELF machine type
    
    enum ElfMachine, values: EM_386 (3), EM_AARCH64 (183), EM_ARM (40), EM_AVR32 (6317), EM_BLACKFIN (106), EM_CRIS (76), EM_FRV (21569), EM_H8_300 (46), EM_IA_64 (50), EM_M32R (88), EM_MN10300 (89), EM_NONE (0), EM_PARISC (15), EM_PPC (20), EM_PPC64 (21), EM_S390 (22), EM_SH (42), EM_SPARC32PLUS (18), EM_SPARCV9 (43), EM_SPU (23), EM_V850 (87), EM_X86_64 (62)
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

    EM_386 = None
    EM_AARCH64 = None
    EM_ARM = None
    EM_AVR32 = None
    EM_BLACKFIN = None
    EM_CRIS = None
    EM_FRV = None
    EM_H8_300 = None
    EM_IA_64 = None
    EM_M32R = None
    EM_MN10300 = None
    EM_NONE = None
    EM_PARISC = None
    EM_PPC = None
    EM_PPC64 = None
    EM_S390 = None
    EM_SH = None
    EM_SPARC32PLUS = None
    EM_SPARCV9 = None
    EM_SPU = None
    EM_V850 = None
    EM_X86_64 = None
    value__ = None


class ElfNote(object):
    """ A helper class to represent an ELF note section. """
    def ReadContents(self, position, buffer=None):
        """
        ReadContents(self: ElfNote, position: UInt64, buffer: Span[Byte]) -> int
        ReadContents[T](self: ElfNote, position: UInt64) -> T
        """
        pass

    ContentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The content size of the data stored within this note.

Get: ContentSize(self: ElfNote) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The note's name.

Get: Name(self: ElfNote) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of note this is.

Get: Type(self: ElfNote) -> ElfNoteType

"""



class ElfNoteType(Enum, IComparable, IFormattable, IConvertible):
    """
    The kind of ELF note.
    
    enum ElfNoteType, values: Aux (6), File (1179208773), PrpsFpreg (2), PrpsInfo (3), PrpsStatus (1), TASKSTRUCT (4)
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

    Aux = None
    File = None
    PrpsFpreg = None
    PrpsInfo = None
    PrpsStatus = None
    TASKSTRUCT = None
    value__ = None


class ElfProgramHeader(object):
    """ A helper class to represent ELF program headers. """
    FileOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of this header within the file.

Get: FileOffset(self: ElfProgramHeader) -> UInt64

"""

    FileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of this header within the file.

Get: FileSize(self: ElfProgramHeader) -> UInt64

"""

    IsExecutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this section of memory is executable.

Get: IsExecutable(self: ElfProgramHeader) -> bool

"""

    IsWritable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this section of memory is writable.

Get: IsWritable(self: ElfProgramHeader) -> bool

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of header this is.

Get: Type(self: ElfProgramHeader) -> ElfProgramHeaderType

"""

    VirtualAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The VirtualAddress of this header.

Get: VirtualAddress(self: ElfProgramHeader) -> UInt64

"""

    VirtualSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of this header.

Get: VirtualSize(self: ElfProgramHeader) -> UInt64

"""



class ElfProgramHeaderType(Enum, IComparable, IFormattable, IConvertible):
    """
    The type of program header.
    
    enum ElfProgramHeaderType, values: Dynamic (2), Interp (3), Load (1), Note (4), Null (0), Phdr (6), Shlib (5)
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

    Dynamic = None
    Interp = None
    Load = None
    Note = None
    Null = None
    Phdr = None
    Shlib = None
    value__ = None


class FileVersionInfo(object):
    """ FileVersionInfo represents the extended version formation that is optionally placed in the PE file resource area. """
    def ToString(self):
        """ ToString(self: FileVersionInfo) -> str """
        pass

    Comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets comments to supplement the file version

Get: Comments(self: FileVersionInfo) -> str

"""

    FileVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version string

Get: FileVersion(self: FileVersionInfo) -> str

"""

    VersionInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version of this module

Get: VersionInfo(self: FileVersionInfo) -> VersionInfo

"""



class HResult(object):
    """ HResult(hr: int) """
    def ToString(self):
        """ ToString(self: HResult) -> str """
        pass

    def __int__(self, *args): #cannot find CLR method
        """ __int__(hr: HResult) -> int """
        pass

    def __long__(self, *args): #cannot find CLR method
        """ __int__(hr: HResult) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hr):
        """
        __new__[HResult]() -> HResult
        
        __new__(cls: type, hr: int)
        """
        pass

    IsOK = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOK(self: HResult) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: HResult) -> int

Set: Value(self: HResult) = value
"""


    E_FAIL = -2147467259
    E_INVALIDARG = -2147024809
    E_NOINTERFACE = -2147467262
    E_NOTIMPL = -2147467263
    S_FALSE = 1
    S_OK = 0


class IElfHeader:
    """ An abstract version of 32 and 64 bit ELF headers. """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Architecture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The architecture of the ELF file.

Get: Architecture(self: IElfHeader) -> ElfMachine

"""

    Is64Bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this file is 64 bit or not.

Get: Is64Bit(self: IElfHeader) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether this file contains the magic header at the right offset or not.

Get: IsValid(self: IElfHeader) -> bool

"""

    ProgramHeaderCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The count of program headers.

Get: ProgramHeaderCount(self: IElfHeader) -> UInt16

"""

    ProgramHeaderEntrySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of program headers.

Get: ProgramHeaderEntrySize(self: IElfHeader) -> UInt16

"""

    ProgramHeaderOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of the program header.

Get: ProgramHeaderOffset(self: IElfHeader) -> UInt64

"""

    SectionHeaderCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The count of section headers.

Get: SectionHeaderCount(self: IElfHeader) -> UInt16

"""

    SectionHeaderEntrySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of section headers.

Get: SectionHeaderEntrySize(self: IElfHeader) -> UInt16

"""

    SectionHeaderOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset of the section header.

Get: SectionHeaderOffset(self: IElfHeader) -> UInt64

"""

    SectionHeaderStringIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The section header string index.

Get: SectionHeaderStringIndex(self: IElfHeader) -> UInt16

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of ELF file.

Get: Type(self: IElfHeader) -> ElfHeaderType

"""



class IElfPRStatus:
    """ An abstraction of the ELF PRStatus view. """
    def CopyRegistersAsContext(self, context):
        """ CopyRegistersAsContext(self: IElfPRStatus, context: Span[Byte]) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ProcessId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The process id associated with this prstatus

Get: ProcessId(self: IElfPRStatus) -> UInt32

"""

    ThreadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The thread id of this prstatus.

Get: ThreadId(self: IElfPRStatus) -> UInt32

"""



class IUnknownVTable(object):
    """ The basic VTable for an IUnknown interface. """
    AddRef = None
    QueryInterface = None
    Release = None


class PEImage(object, IDisposable):
    """
    A class to read information out of PE images (dll/exe).
    
    PEImage(stream: Stream, leaveOpen: bool)
    PEImage(stream: Stream, leaveOpen: bool, isVirtual: bool)
    """
    def Dispose(self):
        """ Dispose(self: PEImage) """
        pass

    def GetFileVersionInfo(self):
        """
        GetFileVersionInfo(self: PEImage) -> FileVersionInfo
        
            Gets the File Version Information that is stored as a resource in the PE file.  (This is what the
                    version tab a file's property page is populated with).
        """
        pass

    def Read(self, virtualAddress, dest):
        """ Read(self: PEImage, virtualAddress: int, dest: Span[Byte]) -> int """
        pass

    def RvaToOffset(self, virtualAddress):
        """
        RvaToOffset(self: PEImage, virtualAddress: int) -> int
        
            Allows you to convert between a virtual address to a stream offset for this module.
        
            virtualAddress: The address to translate.
            Returns: The position in the stream of the data, -1 if the virtual address doesn't map to any location of the PE image.
        """
        pass

    def TryGetExportSymbol(self, symbolName, offset):
        """
        TryGetExportSymbol(self: PEImage, symbolName: str) -> (bool, UInt64)
        
            Returns the address of a module export symbol if found
        
            symbolName: symbol name (without the module name prepended)
            Returns: true if found
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
    def __new__(self, stream, leaveOpen, isVirtual=None):
        """
        __new__(cls: type, stream: Stream, leaveOpen: bool)
        __new__(cls: type, stream: Stream, leaveOpen: bool, isVirtual: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CoffHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wrapper over this PE image's IMAGE_FILE_HEADER structure.  Undefined behavior if IsValid is lse.

Get: CoffHeader(self: PEImage) -> CoffHeader

"""

    CorHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the managed header information for this image.  Undefined behavior if IsValid is lse.

Get: CorHeader(self: PEImage) -> CorHeader

"""

    DefaultPdb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the PDB information for this module.  If this image does not contain PDB info (or that information
            wasn't included in Stream) this returns ll.  If multiple PDB streams are present, this method returns the
            last entry.

Get: DefaultPdb(self: PEImage) -> PdbInfo

"""

    IndexFileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file size that this PE image is indexed under.

Get: IndexFileSize(self: PEImage) -> int

"""

    IndexTimeStamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the timestamp that this PE image is indexed under.

Get: IndexTimeStamp(self: PEImage) -> int

"""

    IsManaged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this image is managed. (.NET image)

Get: IsManaged(self: PEImage) -> bool

"""

    IsPE64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this image is for a 64bit processor.

Get: IsPE64(self: PEImage) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether the given Stream contains a valid DOS header and PE signature.

Get: IsValid(self: PEImage) -> bool

"""

    Pdbs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a list of PDBs associated with this PE image.  PE images can contain multiple PDB entries,
            but by convention it's usually the last entry that is the most up to date.  Unless you need to enumerate
            all PDBs for some reason, you should use DefaultPdb instead.
            Undefined behavior if IsValid is lse.

Get: Pdbs(self: PEImage) -> ImmutableArray[PdbInfo]

"""

    PEHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a wrapper over this PE image's IMAGE_OPTIONAL_HEADER.  Undefined behavior if IsValid is lse.

Get: PEHeader(self: PEImage) -> PEHeader

"""

    Reader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reader(self: PEImage) -> PEReader

"""

    Resources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root resource node of this PEImage.

Get: Resources(self: PEImage) -> ResourceEntry

"""

    Sections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of IMAGE_SECTION_HEADERs in the PE image.  Undefined behavior if IsValid is lse.

Get: Sections(self: PEImage) -> ImmutableArray[SectionHeader]

"""



class ResourceEntry(object):
    """ An entry in the resource table. """
    def GetData(self, *__args):
        """
        GetData(self: ResourceEntry, span: Span[Byte]) -> int
        GetData[T](self: ResourceEntry, offset: int) -> T
        """
        pass

    def ToString(self):
        """ ToString(self: ResourceEntry) -> str """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    ChildCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of children this entry contains.  Note that ResourceEntry.Children is capped at
            MaxChildrenCount entries.  This property returns the total number of entries as defined by the
            IMAGE_RESOURCE_DIRECTORY.  That means this number may be larger than Children.Count.

Get: ChildCount(self: ResourceEntry) -> int

"""

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the children resources of this ResourceEntry.

Get: Children(self: ResourceEntry) -> ImmutableArray[ResourceEntry]

"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the PEImage containing this ResourceEntry.

Get: Image(self: ResourceEntry) -> PEImage

"""

    IsLeaf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value indicating whether this is a leaf, and contains data.

Get: IsLeaf(self: ResourceEntry) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets resource Name.  May be ll if this is the root node.

Get: Name(self: ResourceEntry) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent resource of this ResourceEntry.  Null if and only if this is the root node.

Get: Parent(self: ResourceEntry) -> ResourceEntry

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of data for this node.

Get: Size(self: ResourceEntry) -> int

"""


    MaxChildrenCount = 128
    MaxNameLength = 512


class SigParser(object):
    """
    SigParser(rhs: SigParser)
    SigParser(sig: IntPtr, len: int)
    """
    def GetCallingConvInfo(self, data):
        """ GetCallingConvInfo(self: SigParser) -> (bool, int) """
        pass

    def GetData(self, data):
        """ GetData(self: SigParser) -> (bool, int) """
        pass

    def GetElemType(self, etype):
        """
        GetElemType(self: SigParser) -> (bool, ClrElementType)
        GetElemType(self: SigParser) -> (bool, int)
        """
        pass

    def GetToken(self, token):
        """ GetToken(self: SigParser) -> (bool, int) """
        pass

    def IsNull(self):
        """ IsNull(self: SigParser) -> bool """
        pass

    def PeekCallingConvInfo(self, data):
        """ PeekCallingConvInfo(self: SigParser) -> (bool, int) """
        pass

    def PeekElemType(self, etype):
        """
        PeekElemType(self: SigParser) -> (bool, ClrElementType)
        PeekElemType(self: SigParser) -> (bool, int)
        """
        pass

    def SkipCustomModifiers(self):
        """ SkipCustomModifiers(self: SigParser) -> bool """
        pass

    def SkipExactlyOne(self):
        """ SkipExactlyOne(self: SigParser) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[SigParser]() -> SigParser
        
        __new__(cls: type, rhs: SigParser)
        __new__(cls: type, sig: IntPtr, len: int)
        """
        pass

    IMAGE_CEE_CS_CALLCONV_EXPLICITTHIS = 64
    IMAGE_CEE_CS_CALLCONV_FIELD = 6
    IMAGE_CEE_CS_CALLCONV_GENERIC = 16
    IMAGE_CEE_CS_CALLCONV_GENERICINST = 10
    IMAGE_CEE_CS_CALLCONV_HASTHIS = 32
    IMAGE_CEE_CS_CALLCONV_LOCAL_SIG = 7
    IMAGE_CEE_CS_CALLCONV_MASK = 15
    IMAGE_CEE_CS_CALLCONV_MAX = 12
    IMAGE_CEE_CS_CALLCONV_NATIVEVARARG = 11
    IMAGE_CEE_CS_CALLCONV_PROPERTY = 8
    IMAGE_CEE_CS_CALLCONV_UNMGD = 9
    IMAGE_CEE_CS_CALLCONV_VARARG = 5


class VTableBuilder(object):
    """ Builds an individual VTable for a COM object. """
    def AddMethod(self, func, validate):
        """
        AddMethod(self: VTableBuilder, func: Delegate, validate: bool)
            Adds a method to be the next function in the VTable.
        
            func: The function to add to the next slot of the VTable.
            validate: Whether to validate the delegate matches requirements.
        """
        pass

    def Complete(self):
        """
        Complete(self: VTableBuilder) -> IntPtr
        
            Completes the VTable, registering its GUID with the associated COMCallableIUnknown's QueryInterface
                    method.  Note that if this method is not called, then the COM 
             interface will NOT be registered.
        
            Returns: A pointer to the interface built.  This pointer has not been AddRef'ed.
        """
        pass


