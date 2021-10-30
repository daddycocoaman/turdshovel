# encoding: utf-8
# module System.Reflection.Metadata calls itself Metadata
# from System.Reflection.Metadata, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ArrayShape(object):
    """
    Represents the shape of an array type.
    
    ArrayShape(rank: int, sizes: ImmutableArray[int], lowerBounds: ImmutableArray[int])
    """
    @staticmethod # known case of __new__
    def __new__(self, rank, sizes, lowerBounds):
        """
        __new__(cls: type, rank: int, sizes: ImmutableArray[int], lowerBounds: ImmutableArray[int])
        __new__[ArrayShape]() -> ArrayShape
        """
        pass

    LowerBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower-bounds of all dimensions. Length may be smaller than rank, in which case the trailing dimensions have unspecified lower bounds.

Get: LowerBounds(self: ArrayShape) -> ImmutableArray[int]

"""

    Rank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of dimensions in the array.

Get: Rank(self: ArrayShape) -> int

"""

    Sizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the sizes of all dimensions.

Get: Sizes(self: ArrayShape) -> ImmutableArray[int]

"""



class AssemblyDefinition(object):
    # no doc
    def GetAssemblyName(self):
        """ GetAssemblyName(self: AssemblyDefinition) -> AssemblyName """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: AssemblyDefinition) -> CustomAttributeHandleCollection """
        pass

    def GetDeclarativeSecurityAttributes(self):
        """ GetDeclarativeSecurityAttributes(self: AssemblyDefinition) -> DeclarativeSecurityAttributeHandleCollection """
        pass

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Culture(self: AssemblyDefinition) -> StringHandle

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: AssemblyDefinition) -> AssemblyFlags

"""

    HashAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HashAlgorithm(self: AssemblyDefinition) -> AssemblyHashAlgorithm

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AssemblyDefinition) -> StringHandle

"""

    PublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublicKey(self: AssemblyDefinition) -> BlobHandle

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AssemblyDefinition) -> Version

"""



class AssemblyDefinitionHandle(object, IEquatable[AssemblyDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: AssemblyDefinitionHandle, obj: object) -> bool
        Equals(self: AssemblyDefinitionHandle, other: AssemblyDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: AssemblyDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: AssemblyDefinitionHandle) -> bool

"""



class AssemblyFile(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: AssemblyFile) -> CustomAttributeHandleCollection """
        pass

    ContainsMetadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the file contains metadata.

Get: ContainsMetadata(self: AssemblyFile) -> bool

"""

    HashValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hash value of the file content calculated using System.Reflection.Metadata.AssemblyDefinition.HashAlgorithm.

Get: HashValue(self: AssemblyFile) -> BlobHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the file name, including its extension.

Get: Name(self: AssemblyFile) -> StringHandle

"""



class AssemblyFileHandle(object, IEquatable[AssemblyFileHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: AssemblyFileHandle, obj: object) -> bool
        Equals(self: AssemblyFileHandle, other: AssemblyFileHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: AssemblyFileHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: AssemblyFileHandle) -> bool

"""



class AssemblyFileHandleCollection(object, IReadOnlyCollection[AssemblyFileHandle], IEnumerable[AssemblyFileHandle], IEnumerable):
    """ Represents a collection of System.Reflection.Metadata.AssemblyFileHandle. """
    def GetEnumerator(self):
        """ GetEnumerator(self: AssemblyFileHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AssemblyFileHandle](enumerable: IEnumerable[AssemblyFileHandle], value: AssemblyFileHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: AssemblyFileHandleCollection) -> int

"""


    Enumerator = None


class AssemblyReference(object):
    # no doc
    def GetAssemblyName(self):
        """ GetAssemblyName(self: AssemblyReference) -> AssemblyName """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: AssemblyReference) -> CustomAttributeHandleCollection """
        pass

    Culture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Culture(self: AssemblyReference) -> StringHandle

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: AssemblyReference) -> AssemblyFlags

"""

    HashValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HashValue(self: AssemblyReference) -> BlobHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AssemblyReference) -> StringHandle

"""

    PublicKeyOrToken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublicKeyOrToken(self: AssemblyReference) -> BlobHandle

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AssemblyReference) -> Version

"""



class AssemblyReferenceHandle(object, IEquatable[AssemblyReferenceHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: AssemblyReferenceHandle, obj: object) -> bool
        Equals(self: AssemblyReferenceHandle, other: AssemblyReferenceHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: AssemblyReferenceHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: AssemblyReferenceHandle) -> bool

"""



class AssemblyReferenceHandleCollection(object, IReadOnlyCollection[AssemblyReferenceHandle], IEnumerable[AssemblyReferenceHandle], IEnumerable):
    """ A collection of assembly references. """
    def GetEnumerator(self):
        """ GetEnumerator(self: AssemblyReferenceHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AssemblyReferenceHandle](enumerable: IEnumerable[AssemblyReferenceHandle], value: AssemblyReferenceHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: AssemblyReferenceHandleCollection) -> int

"""


    Enumerator = None


class Blob(object):
    # no doc
    def GetBytes(self):
        """ GetBytes(self: Blob) -> ArraySegment[Byte] """
        pass

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefault(self: Blob) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Blob) -> int

"""



class BlobBuilder(object):
    """ BlobBuilder(capacity: int) """
    def Align(self, alignment):
        """ Align(self: BlobBuilder, alignment: int) """
        pass

    def AllocateChunk(self, *args): #cannot find CLR method
        """ AllocateChunk(self: BlobBuilder, minimalSize: int) -> BlobBuilder """
        pass

    def Clear(self):
        """ Clear(self: BlobBuilder) """
        pass

    def ContentEquals(self, other):
        """
        ContentEquals(self: BlobBuilder, other: BlobBuilder) -> bool
        
            Compares the current content of this writer with another one.
        
            other: A System.Reflection.Metadata.BlobBuilder instance to compare with this one.
            Returns: ue if equal; otherwise, lse.
        """
        pass

    def Free(self, *args): #cannot find CLR method
        """ Free(self: BlobBuilder) """
        pass

    def FreeChunk(self, *args): #cannot find CLR method
        """ FreeChunk(self: BlobBuilder) """
        pass

    def GetBlobs(self):
        """
        GetBlobs(self: BlobBuilder) -> Blobs
        
            Returns a sequence of all blobs that represent the content of the builder.
            Returns: A sequence of blobs.
        """
        pass

    def LinkPrefix(self, prefix):
        """ LinkPrefix(self: BlobBuilder, prefix: BlobBuilder) """
        pass

    def LinkSuffix(self, suffix):
        """ LinkSuffix(self: BlobBuilder, suffix: BlobBuilder) """
        pass

    def PadTo(self, position):
        """ PadTo(self: BlobBuilder, position: int) """
        pass

    def ReserveBytes(self, byteCount):
        """
        ReserveBytes(self: BlobBuilder, byteCount: int) -> Blob
        
            Reserves a contiguous block of bytes.
        """
        pass

    def ToArray(self, start=None, byteCount=None):
        """
        ToArray(self: BlobBuilder) -> Array[Byte]
        ToArray(self: BlobBuilder, start: int, byteCount: int) -> Array[Byte]
        """
        pass

    def ToImmutableArray(self, start=None, byteCount=None):
        """
        ToImmutableArray(self: BlobBuilder) -> ImmutableArray[Byte]
        ToImmutableArray(self: BlobBuilder, start: int, byteCount: int) -> ImmutableArray[Byte]
        """
        pass

    def TryWriteBytes(self, source, byteCount):
        """
        TryWriteBytes(self: BlobBuilder, source: Stream, byteCount: int) -> int
        
            Attempts to write a sequence of bytes to the builder. A return value indicates the number of bytes successfully written.
            Returns: The number of bytes successfully written from source.
        """
        pass

    def WriteBoolean(self, value):
        """
        WriteBoolean(self: BlobBuilder, value: bool)
            Writes a System.Boolean value to the builder.
        
            value: The value to write.
        """
        pass

    def WriteByte(self, value):
        """
        WriteByte(self: BlobBuilder, value: Byte)
            Writes a System.Byte value to the builder.
        
            value: The value to write.
        """
        pass

    def WriteBytes(self, *__args):
        """
        WriteBytes(self: BlobBuilder, value: Byte, byteCount: int)
            Writes a specified number of occurrences of a byte value to the builder.
        
            byteCount: The number of occurences of value to write.
        WriteBytes(self: BlobBuilder, buffer: Byte*, byteCount: int)
            Writes a specified number of bytes from a buffer to the builder.
        
            byteCount: The number of bytes to write.
        WriteBytes(self: BlobBuilder, buffer: ImmutableArray[Byte])WriteBytes(self: BlobBuilder, buffer: ImmutableArray[Byte], start: int, byteCount: int)WriteBytes(self: BlobBuilder, buffer: Array[Byte])
            Writes the contents of a byte array to the builder.
        
            buffer: The byte array to write.
        WriteBytes(self: BlobBuilder, buffer: Array[Byte], start: int, byteCount: int)
            Writes a specified number of bytes starting at a specified index in a byte array to the builder.
        
            byteCount: The number of bytes to write.
        """
        pass

    def WriteCompressedInteger(self, value):
        """
        WriteCompressedInteger(self: BlobBuilder, value: int)
            Implements compressed unsigned integer encoding as defined by ECMA-335-II chapter 23.2: Blobs and signatures.
        
            value: The value to write.
        """
        pass

    def WriteCompressedSignedInteger(self, value):
        """
        WriteCompressedSignedInteger(self: BlobBuilder, value: int)
            Implements compressed signed integer encoding as defined by ECMA-335-II chapter 23.2: Blobs and signatures.
        
            value: The value to write.
        """
        pass

    def WriteConstant(self, value):
        """
        WriteConstant(self: BlobBuilder, value: object)
            Writes a constant value (see ECMA-335 Partition II section 22.9) at the current position.
        
            value: The constant value to write.
        """
        pass

    def WriteContentTo(self, destination):
        """
        WriteContentTo(self: BlobBuilder, destination: Stream)WriteContentTo(self: BlobBuilder, destination: BlobWriter) -> BlobWriter
        WriteContentTo(self: BlobBuilder, destination: BlobBuilder)
        """
        pass

    def WriteDateTime(self, value):
        """ WriteDateTime(self: BlobBuilder, value: DateTime) """
        pass

    def WriteDecimal(self, value):
        """ WriteDecimal(self: BlobBuilder, value: Decimal) """
        pass

    def WriteDouble(self, value):
        """ WriteDouble(self: BlobBuilder, value: float) """
        pass

    def WriteGuid(self, value):
        """ WriteGuid(self: BlobBuilder, value: Guid) """
        pass

    def WriteInt16(self, value):
        """ WriteInt16(self: BlobBuilder, value: Int16) """
        pass

    def WriteInt16BE(self, value):
        """ WriteInt16BE(self: BlobBuilder, value: Int16) """
        pass

    def WriteInt32(self, value):
        """ WriteInt32(self: BlobBuilder, value: int) """
        pass

    def WriteInt32BE(self, value):
        """ WriteInt32BE(self: BlobBuilder, value: int) """
        pass

    def WriteInt64(self, value):
        """ WriteInt64(self: BlobBuilder, value: Int64) """
        pass

    def WriteReference(self, reference, isSmall):
        """
        WriteReference(self: BlobBuilder, reference: int, isSmall: bool)
            Writes a reference to a heap (heap offset) or a table (row number).
        
            reference: Heap offset or table row number.
            isSmall: ue to encode the reference as a 16-bit integer; lse to encode it as a 32-bit integer.
        """
        pass

    def WriteSByte(self, value):
        """ WriteSByte(self: BlobBuilder, value: SByte) """
        pass

    def WriteSerializedString(self, value):
        """
        WriteSerializedString(self: BlobBuilder, value: str)
            Writes a string in SerString format (see ECMA-335-II 23.3 Custom attributes).
        """
        pass

    def WriteSingle(self, value):
        """ WriteSingle(self: BlobBuilder, value: Single) """
        pass

    def WriteUInt16(self, value):
        """ WriteUInt16(self: BlobBuilder, value: UInt16) """
        pass

    def WriteUInt16BE(self, value):
        """ WriteUInt16BE(self: BlobBuilder, value: UInt16) """
        pass

    def WriteUInt32(self, value):
        """ WriteUInt32(self: BlobBuilder, value: UInt32) """
        pass

    def WriteUInt32BE(self, value):
        """ WriteUInt32BE(self: BlobBuilder, value: UInt32) """
        pass

    def WriteUInt64(self, value):
        """ WriteUInt64(self: BlobBuilder, value: UInt64) """
        pass

    def WriteUserString(self, value):
        """
        WriteUserString(self: BlobBuilder, value: str)
            Writes a string in User String (#US) heap format (see ECMA-335-II 24.2.4 #US and #Blob heaps).
        """
        pass

    def WriteUTF16(self, value):
        """
        WriteUTF16(self: BlobBuilder, value: Array[Char])
            Writes a UTF16 (little-endian) encoded character array at the current position.
        WriteUTF16(self: BlobBuilder, value: str)
            Writes UTF16 (little-endian) encoded string at the current position.
        """
        pass

    def WriteUTF8(self, value, allowUnpairedSurrogates):
        """
        WriteUTF8(self: BlobBuilder, value: str, allowUnpairedSurrogates: bool)
            Writes a UTF8 encoded string at the current position.
        
            value: Constant value.
            allowUnpairedSurrogates: ue to encode unpaired surrogates as specified; lse to replace them with a U+FFFD character.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, capacity):
        """ __new__(cls: type, capacity: int) """
        pass

    ChunkCapacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BlobBuilder) -> int

"""

    FreeBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Blobs = None


class BlobContentId(object, IEquatable[BlobContentId]):
    """
    BlobContentId(guid: Guid, stamp: UInt32)
    BlobContentId(id: ImmutableArray[Byte])
    BlobContentId(id: Array[Byte])
    """
    def Equals(self, *__args):
        """
        Equals(self: BlobContentId, other: BlobContentId) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        Equals(self: BlobContentId, obj: object) -> bool
        """
        pass

    @staticmethod
    def FromHash(hashCode):
        """
        FromHash(hashCode: ImmutableArray[Byte]) -> BlobContentId
        FromHash(hashCode: Array[Byte]) -> BlobContentId
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: BlobContentId) -> int """
        pass

    @staticmethod
    def GetTimeBasedProvider():
        """ GetTimeBasedProvider() -> Func[IEnumerable[Blob], BlobContentId] """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, guid: Guid, stamp: UInt32)
        __new__(cls: type, id: ImmutableArray[Byte])
        __new__(cls: type, id: Array[Byte])
        __new__[BlobContentId]() -> BlobContentId
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: BlobContentId) -> Guid

"""

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefault(self: BlobContentId) -> bool

"""

    Stamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stamp(self: BlobContentId) -> UInt32

"""



class BlobHandle(object, IEquatable[BlobHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: BlobHandle, obj: object) -> bool
        Equals(self: BlobHandle, other: BlobHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: BlobHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: BlobHandle) -> bool

"""



class BlobReader(object):
    """ BlobReader(buffer: Byte*, length: int) """
    def Align(self, alignment):
        """
        Align(self: BlobReader, alignment: Byte)
            Repositions the reader forward by the number of bytes required to satisfy the given alignment.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: BlobReader, value: Byte) -> int
        
            Searches for a specified byte in the blob following the current position.
        
            value: The byte value to find.
            Returns: The index relative to the current position, or -1 if the byte is not found in the blob following the current position.
        """
        pass

    def ReadBlobHandle(self):
        """
        ReadBlobHandle(self: BlobReader) -> BlobHandle
        
            Reads a Blob heap handle encoded as a compressed integer.
        """
        pass

    def ReadBoolean(self):
        """ ReadBoolean(self: BlobReader) -> bool """
        pass

    def ReadByte(self):
        """ ReadByte(self: BlobReader) -> Byte """
        pass

    def ReadBytes(self, byteCount, buffer=None, bufferOffset=None):
        """
        ReadBytes(self: BlobReader, byteCount: int) -> Array[Byte]
        
            Reads bytes starting at the current position.
        
            byteCount: The number of bytes to read.
            Returns: The byte array.
        ReadBytes(self: BlobReader, byteCount: int, buffer: Array[Byte], bufferOffset: int)
            Reads bytes starting at the current position and writes them to the specified buffer starting at the specified offset.
        
            byteCount: The number of bytes to read.
            buffer: The destination buffer the bytes read will be written to.
            bufferOffset: The offset in the destination buffer where the bytes read will be written.
        """
        pass

    def ReadChar(self):
        """ ReadChar(self: BlobReader) -> Char """
        pass

    def ReadCompressedInteger(self):
        """
        ReadCompressedInteger(self: BlobReader) -> int
        
            Reads an unsigned compressed integer value. See Metadata Specification section II.23.2: Blobs and signatures.
            Returns: The value of the compressed integer that was read.
        """
        pass

    def ReadCompressedSignedInteger(self):
        """
        ReadCompressedSignedInteger(self: BlobReader) -> int
        
            Reads a signed compressed integer value. See Metadata Specification section II.23.2: Blobs and signatures.
            Returns: The value of the compressed integer that was read.
        """
        pass

    def ReadConstant(self, typeCode):
        """
        ReadConstant(self: BlobReader, typeCode: ConstantTypeCode) -> object
        
            Reads a constant value (see ECMA-335 Partition II section 22.9) from the current position.
            Returns: A boxed constant value. To avoid allocating the object use Read* methods directly.
        """
        pass

    def ReadDateTime(self):
        """ ReadDateTime(self: BlobReader) -> DateTime """
        pass

    def ReadDecimal(self):
        """
        ReadDecimal(self: BlobReader) -> Decimal
        
            Reads a System.Decimal number.
        """
        pass

    def ReadDouble(self):
        """ ReadDouble(self: BlobReader) -> float """
        pass

    def ReadGuid(self):
        """ ReadGuid(self: BlobReader) -> Guid """
        pass

    def ReadInt16(self):
        """ ReadInt16(self: BlobReader) -> Int16 """
        pass

    def ReadInt32(self):
        """ ReadInt32(self: BlobReader) -> int """
        pass

    def ReadInt64(self):
        """ ReadInt64(self: BlobReader) -> Int64 """
        pass

    def ReadSByte(self):
        """ ReadSByte(self: BlobReader) -> SByte """
        pass

    def ReadSerializationTypeCode(self):
        """
        ReadSerializationTypeCode(self: BlobReader) -> SerializationTypeCode
        
            Reads a type code encoded in a serialized custom attribute value.
            Returns: System.Reflection.Metadata.SerializationTypeCode.Invalid if the encoding is invalid.
        """
        pass

    def ReadSerializedString(self):
        """
        ReadSerializedString(self: BlobReader) -> str
        
            Reads a string encoded as a compressed integer containing its length followed by its contents in UTF8. Null strings are encoded as a single 0xFF byte.
            Returns: A string value, or ll.
        """
        pass

    def ReadSignatureHeader(self):
        """ ReadSignatureHeader(self: BlobReader) -> SignatureHeader """
        pass

    def ReadSignatureTypeCode(self):
        """
        ReadSignatureTypeCode(self: BlobReader) -> SignatureTypeCode
        
            Reads a type code encoded in a signature.
            Returns: The type code encoded in the serialized custom attribute value if the encoding is valid, or System.Reflection.Metadata.SignatureTypeCode.Invalid if the encoding is invalid.
        """
        pass

    def ReadSingle(self):
        """ ReadSingle(self: BlobReader) -> Single """
        pass

    def ReadTypeHandle(self):
        """
        ReadTypeHandle(self: BlobReader) -> EntityHandle
        
            Reads a type handle encoded in a signature as TypeDefOrRefOrSpecEncoded (see ECMA-335 II.23.2.8).
            Returns: The handle when the encoding is valid. Otherwise, a handle where the System.Reflection.Metadata.EntityHandle.IsNil property is ue.
        """
        pass

    def ReadUInt16(self):
        """ ReadUInt16(self: BlobReader) -> UInt16 """
        pass

    def ReadUInt32(self):
        """ ReadUInt32(self: BlobReader) -> UInt32 """
        pass

    def ReadUInt64(self):
        """ ReadUInt64(self: BlobReader) -> UInt64 """
        pass

    def ReadUTF16(self, byteCount):
        """
        ReadUTF16(self: BlobReader, byteCount: int) -> str
        
            Reads a UTF16 (little-endian) encoded string starting at the current position.
        
            byteCount: The number of bytes to read.
            Returns: The string.
        """
        pass

    def ReadUTF8(self, byteCount):
        """
        ReadUTF8(self: BlobReader, byteCount: int) -> str
        
            Reads a UTF8 encoded string starting at the current position.
        
            byteCount: The number of bytes to read.
            Returns: The string.
        """
        pass

    def Reset(self):
        """
        Reset(self: BlobReader)
            Repositions the reader to the start of the underlying memory block.
        """
        pass

    def TryReadCompressedInteger(self, value):
        """
        TryReadCompressedInteger(self: BlobReader) -> (bool, int)
        
            Reads an unsigned compressed integer value. See Metadata Specification section II.23.2: Blobs and signatures.
            Returns: ue if the value was read successfully. lse if the data at the current position was not a valid compressed integer.
        """
        pass

    def TryReadCompressedSignedInteger(self, value):
        """
        TryReadCompressedSignedInteger(self: BlobReader) -> (bool, int)
        
            Reads a signed compressed integer value. See Metadata Specification section II.23.2: Blobs and signatures.
            Returns: ue if the value was read successfully. lse if the data at the current position was not a valid compressed integer.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, buffer, length):
        """
        __new__(cls: type, buffer: Byte*, length: int)
        __new__[BlobReader]() -> BlobReader
        """
        pass

    CurrentPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the byte at the current position of the reader.

Get: CurrentPointer(self: BlobReader) -> Byte*

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the total length of the underlying memory block.

Get: Length(self: BlobReader) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset from the start of the blob to the current position.

Get: Offset(self: BlobReader) -> int

Set: Offset(self: BlobReader) = value
"""

    RemainingBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of bytes remaining from current position to the end of the underlying memory block.

Get: RemainingBytes(self: BlobReader) -> int

"""

    StartPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a pointer to the byte at the start of the underlying memory block.

Get: StartPointer(self: BlobReader) -> Byte*

"""



class BlobWriter(object):
    """
    BlobWriter(size: int)
    BlobWriter(buffer: Array[Byte])
    BlobWriter(blob: Blob)
    BlobWriter(buffer: Array[Byte], start: int, count: int)
    """
    def Align(self, alignment):
        """ Align(self: BlobWriter, alignment: int) """
        pass

    def Clear(self):
        """ Clear(self: BlobWriter) """
        pass

    def ContentEquals(self, other):
        """
        ContentEquals(self: BlobWriter, other: BlobWriter) -> bool
        
            Compares the current content of this writer with another one.
        """
        pass

    def PadTo(self, offset):
        """ PadTo(self: BlobWriter, offset: int) """
        pass

    def ToArray(self, start=None, byteCount=None):
        """
        ToArray(self: BlobWriter) -> Array[Byte]
        ToArray(self: BlobWriter, start: int, byteCount: int) -> Array[Byte]
        """
        pass

    def ToImmutableArray(self, start=None, byteCount=None):
        """
        ToImmutableArray(self: BlobWriter) -> ImmutableArray[Byte]
        ToImmutableArray(self: BlobWriter, start: int, byteCount: int) -> ImmutableArray[Byte]
        """
        pass

    def WriteBoolean(self, value):
        """ WriteBoolean(self: BlobWriter, value: bool) """
        pass

    def WriteByte(self, value):
        """ WriteByte(self: BlobWriter, value: Byte) """
        pass

    def WriteBytes(self, *__args):
        """
        WriteBytes(self: BlobWriter, value: Byte, byteCount: int)WriteBytes(self: BlobWriter, buffer: Byte*, byteCount: int)WriteBytes(self: BlobWriter, source: BlobBuilder)WriteBytes(self: BlobWriter, source: Stream, byteCount: int) -> int
        WriteBytes(self: BlobWriter, buffer: ImmutableArray[Byte])WriteBytes(self: BlobWriter, buffer: ImmutableArray[Byte], start: int, byteCount: int)WriteBytes(self: BlobWriter, buffer: Array[Byte])WriteBytes(self: BlobWriter, buffer: Array[Byte], start: int, byteCount: int)
        """
        pass

    def WriteCompressedInteger(self, value):
        """
        WriteCompressedInteger(self: BlobWriter, value: int)
            Implements compressed unsigned integer encoding as defined by ECMA-335-II chapter 23.2: Blobs and signatures.
        """
        pass

    def WriteCompressedSignedInteger(self, value):
        """
        WriteCompressedSignedInteger(self: BlobWriter, value: int)
            Implements compressed signed integer encoding as defined by ECMA-335-II chapter 23.2: Blobs and signatures.
        """
        pass

    def WriteConstant(self, value):
        """
        WriteConstant(self: BlobWriter, value: object)
            Writes a constant value (see ECMA-335 Partition II section 22.9) at the current position.
        """
        pass

    def WriteDateTime(self, value):
        """ WriteDateTime(self: BlobWriter, value: DateTime) """
        pass

    def WriteDecimal(self, value):
        """ WriteDecimal(self: BlobWriter, value: Decimal) """
        pass

    def WriteDouble(self, value):
        """ WriteDouble(self: BlobWriter, value: float) """
        pass

    def WriteGuid(self, value):
        """ WriteGuid(self: BlobWriter, value: Guid) """
        pass

    def WriteInt16(self, value):
        """ WriteInt16(self: BlobWriter, value: Int16) """
        pass

    def WriteInt16BE(self, value):
        """ WriteInt16BE(self: BlobWriter, value: Int16) """
        pass

    def WriteInt32(self, value):
        """ WriteInt32(self: BlobWriter, value: int) """
        pass

    def WriteInt32BE(self, value):
        """ WriteInt32BE(self: BlobWriter, value: int) """
        pass

    def WriteInt64(self, value):
        """ WriteInt64(self: BlobWriter, value: Int64) """
        pass

    def WriteReference(self, reference, isSmall):
        """
        WriteReference(self: BlobWriter, reference: int, isSmall: bool)
            Writes a reference to a heap (heap offset) or a table (row number).
        
            reference: Heap offset or table row number.
            isSmall: ue to encode the reference as 16-bit integer, lse to encode as 32-bit integer.
        """
        pass

    def WriteSByte(self, value):
        """ WriteSByte(self: BlobWriter, value: SByte) """
        pass

    def WriteSerializedString(self, str):
        """
        WriteSerializedString(self: BlobWriter, str: str)
            Writes a string in SerString format (see ECMA-335-II 23.3 Custom attributes).
        """
        pass

    def WriteSingle(self, value):
        """ WriteSingle(self: BlobWriter, value: Single) """
        pass

    def WriteUInt16(self, value):
        """ WriteUInt16(self: BlobWriter, value: UInt16) """
        pass

    def WriteUInt16BE(self, value):
        """ WriteUInt16BE(self: BlobWriter, value: UInt16) """
        pass

    def WriteUInt32(self, value):
        """ WriteUInt32(self: BlobWriter, value: UInt32) """
        pass

    def WriteUInt32BE(self, value):
        """ WriteUInt32BE(self: BlobWriter, value: UInt32) """
        pass

    def WriteUInt64(self, value):
        """ WriteUInt64(self: BlobWriter, value: UInt64) """
        pass

    def WriteUserString(self, value):
        """
        WriteUserString(self: BlobWriter, value: str)
            Writes a string in User String (#US) heap format (see ECMA-335-II 24.2.4 #US and #Blob heaps).
        """
        pass

    def WriteUTF16(self, value):
        """
        WriteUTF16(self: BlobWriter, value: Array[Char])
            Writes a UTF16 (little-endian) encoded string at the current position.
        WriteUTF16(self: BlobWriter, value: str)
            Writes a UTF16 (little-endian) encoded string at the current position.
        """
        pass

    def WriteUTF8(self, value, allowUnpairedSurrogates):
        """
        WriteUTF8(self: BlobWriter, value: str, allowUnpairedSurrogates: bool)
            Writes a UTF8 encoded string at the current position.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, size: int)
        __new__(cls: type, buffer: Array[Byte])
        __new__(cls: type, blob: Blob)
        __new__(cls: type, buffer: Array[Byte], start: int, count: int)
        __new__[BlobWriter]() -> BlobWriter
        """
        pass

    Blob = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blob(self: BlobWriter) -> Blob

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: BlobWriter) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: BlobWriter) -> int

Set: Offset(self: BlobWriter) = value
"""

    RemainingBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemainingBytes(self: BlobWriter) -> int

"""



class Constant(object):
    # no doc
    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent handle (System.Reflection.Metadata.ParameterHandle, System.Reflection.Metadata.FieldDefinitionHandle, or System.Reflection.Metadata.PropertyDefinitionHandle).

Get: Parent(self: Constant) -> EntityHandle

"""

    TypeCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a type code that identifies the type of the constant value.

Get: TypeCode(self: Constant) -> ConstantTypeCode

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the constant value.

Get: Value(self: Constant) -> BlobHandle

"""



class ConstantHandle(object, IEquatable[ConstantHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ConstantHandle, obj: object) -> bool
        Equals(self: ConstantHandle, other: ConstantHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ConstantHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ConstantHandle) -> bool

"""



class ConstantTypeCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies values that represent types of metadata constants.
    
    enum ConstantTypeCode, values: Boolean (2), Byte (5), Char (3), Double (13), Int16 (6), Int32 (8), Int64 (10), Invalid (0), NullReference (18), SByte (4), Single (12), String (14), UInt16 (7), UInt32 (9), UInt64 (11)
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

    Boolean = None
    Byte = None
    Char = None
    Double = None
    Int16 = None
    Int32 = None
    Int64 = None
    Invalid = None
    NullReference = None
    SByte = None
    Single = None
    String = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    value__ = None


class CustomAttribute(object):
    # no doc
    def DecodeValue(self, provider):
        """ DecodeValue[TType](self: CustomAttribute, provider: ICustomAttributeTypeProvider[TType]) -> CustomAttributeValue[TType] """
        pass

    Constructor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the constructor (the System.Reflection.Metadata.MethodDefinitionHandle or System.Reflection.Metadata.MemberReferenceHandle) of the custom attribute type.

Get: Constructor(self: CustomAttribute) -> EntityHandle

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the handle of the metadata entity the attribute is applied to.

Get: Parent(self: CustomAttribute) -> EntityHandle

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the attribute.

Get: Value(self: CustomAttribute) -> BlobHandle

"""



class CustomAttributeHandle(object, IEquatable[CustomAttributeHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: CustomAttributeHandle, obj: object) -> bool
        Equals(self: CustomAttributeHandle, other: CustomAttributeHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CustomAttributeHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: CustomAttributeHandle) -> bool

"""



class CustomAttributeHandleCollection(object, IReadOnlyCollection[CustomAttributeHandle], IEnumerable[CustomAttributeHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: CustomAttributeHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CustomAttributeHandle](enumerable: IEnumerable[CustomAttributeHandle], value: CustomAttributeHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: CustomAttributeHandleCollection) -> int

"""


    Enumerator = None


class CustomAttributeNamedArgument(object):
    """ CustomAttributeNamedArgument[TType](name: str, kind: CustomAttributeNamedArgumentKind, type: TType, value: object) """
    @staticmethod # known case of __new__
    def __new__(self, name, kind, type, value):
        """
        __new__(cls: type, name: str, kind: CustomAttributeNamedArgumentKind, type: TType, value: object)
        __new__[CustomAttributeNamedArgument`1]() -> CustomAttributeNamedArgument[TType]
        """
        pass

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the kind of argument.

Get: Kind(self: CustomAttributeNamedArgument[TType]) -> CustomAttributeNamedArgumentKind

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the argument.

Get: Name(self: CustomAttributeNamedArgument[TType]) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the argument.

Get: Type(self: CustomAttributeNamedArgument[TType]) -> TType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the argument.

Get: Value(self: CustomAttributeNamedArgument[TType]) -> object

"""



class CustomAttributeNamedArgumentKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define the kinds of arguments in a custom attribute signature.
    
    enum CustomAttributeNamedArgumentKind, values: Field (83), Property (84)
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

    Field = None
    Property = None
    value__ = None


class CustomAttributeTypedArgument(object):
    """ CustomAttributeTypedArgument[TType](type: TType, value: object) """
    @staticmethod # known case of __new__
    def __new__(self, type, value):
        """
        __new__(cls: type, type: TType, value: object)
        __new__[CustomAttributeTypedArgument`1]() -> CustomAttributeTypedArgument[TType]
        """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the argument.

Get: Type(self: CustomAttributeTypedArgument[TType]) -> TType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of the argument.

Get: Value(self: CustomAttributeTypedArgument[TType]) -> object

"""



class CustomAttributeValue(object):
    """ CustomAttributeValue[TType](fixedArguments: ImmutableArray[CustomAttributeTypedArgument[TType]], namedArguments: ImmutableArray[CustomAttributeNamedArgument[TType]]) """
    @staticmethod # known case of __new__
    def __new__(self, fixedArguments, namedArguments):
        """
        __new__(cls: type, fixedArguments: ImmutableArray[CustomAttributeTypedArgument[TType]], namedArguments: ImmutableArray[CustomAttributeNamedArgument[TType]])
        __new__[CustomAttributeValue`1]() -> CustomAttributeValue[TType]
        """
        pass

    FixedArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the fixed arguments for the custom attribute.

Get: FixedArguments(self: CustomAttributeValue[TType]) -> ImmutableArray[CustomAttributeTypedArgument[TType]]

"""

    NamedArguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the named arguments for the custom attribute value.

Get: NamedArguments(self: CustomAttributeValue[TType]) -> ImmutableArray[CustomAttributeNamedArgument[TType]]

"""



class CustomDebugInformation(object):
    # no doc
    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: CustomDebugInformation) -> GuidHandle

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: CustomDebugInformation) -> EntityHandle

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: CustomDebugInformation) -> BlobHandle

"""



class CustomDebugInformationHandle(object, IEquatable[CustomDebugInformationHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: CustomDebugInformationHandle, obj: object) -> bool
        Equals(self: CustomDebugInformationHandle, other: CustomDebugInformationHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CustomDebugInformationHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: CustomDebugInformationHandle) -> bool

"""



class CustomDebugInformationHandleCollection(object, IReadOnlyCollection[CustomDebugInformationHandle], IEnumerable[CustomDebugInformationHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: CustomDebugInformationHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CustomDebugInformationHandle](enumerable: IEnumerable[CustomDebugInformationHandle], value: CustomDebugInformationHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: CustomDebugInformationHandleCollection) -> int

"""


    Enumerator = None


class DebugMetadataHeader(object):
    # no doc
    EntryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryPoint(self: DebugMetadataHeader) -> MethodDefinitionHandle

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: DebugMetadataHeader) -> ImmutableArray[Byte]

"""

    IdStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the offset (in bytes) from the start of the metadata blob to the start of the System.Reflection.Metadata.DebugMetadataHeader.Id blob.

Get: IdStartOffset(self: DebugMetadataHeader) -> int

"""



class DeclarativeSecurityAttribute(object):
    # no doc
    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: DeclarativeSecurityAttribute) -> DeclarativeSecurityAction

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: DeclarativeSecurityAttribute) -> EntityHandle

"""

    PermissionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PermissionSet(self: DeclarativeSecurityAttribute) -> BlobHandle

"""



class DeclarativeSecurityAttributeHandle(object, IEquatable[DeclarativeSecurityAttributeHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: DeclarativeSecurityAttributeHandle, obj: object) -> bool
        Equals(self: DeclarativeSecurityAttributeHandle, other: DeclarativeSecurityAttributeHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DeclarativeSecurityAttributeHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: DeclarativeSecurityAttributeHandle) -> bool

"""



class DeclarativeSecurityAttributeHandleCollection(object, IReadOnlyCollection[DeclarativeSecurityAttributeHandle], IEnumerable[DeclarativeSecurityAttributeHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: DeclarativeSecurityAttributeHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DeclarativeSecurityAttributeHandle](enumerable: IEnumerable[DeclarativeSecurityAttributeHandle], value: DeclarativeSecurityAttributeHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: DeclarativeSecurityAttributeHandleCollection) -> int

"""


    Enumerator = None


class Document(object):
    """ The source document in the debug metadata. """
    Hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document content hash.

Get: Hash(self: Document) -> BlobHandle

"""

    HashAlgorithm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the hash algorithm used to calculate the System.Reflection.Metadata.Document.Hash (SHA1, SHA256, etc.).

Get: HashAlgorithm(self: Document) -> GuidHandle

"""

    Language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the source code language (C#, VB, F#, etc.).

Get: Language(self: Document) -> GuidHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the document name blob.

Get: Name(self: Document) -> DocumentNameBlobHandle

"""



class DocumentHandle(object, IEquatable[DocumentHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: DocumentHandle, obj: object) -> bool
        Equals(self: DocumentHandle, other: DocumentHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DocumentHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: DocumentHandle) -> bool

"""



class DocumentHandleCollection(object, IReadOnlyCollection[DocumentHandle], IEnumerable[DocumentHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: DocumentHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DocumentHandle](enumerable: IEnumerable[DocumentHandle], value: DocumentHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: DocumentHandleCollection) -> int

"""


    Enumerator = None


class DocumentNameBlobHandle(object, IEquatable[DocumentNameBlobHandle]):
    """ A System.Reflection.Metadata.BlobHandle representing a blob on #Blob heap in Portable PDB structured as Document Name. """
    def Equals(self, *__args):
        """
        Equals(self: DocumentNameBlobHandle, obj: object) -> bool
        Equals(self: DocumentNameBlobHandle, other: DocumentNameBlobHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DocumentNameBlobHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: DocumentNameBlobHandle) -> bool

"""



class EntityHandle(object, IEquatable[EntityHandle]):
    """ Represents a metadata entity (such as a type reference, type definition, type specification, method definition, or custom attribute). """
    def Equals(self, *__args):
        """
        Equals(self: EntityHandle, obj: object) -> bool
        
            Returns a value that indicates whether the current instance and the specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: ue if obj is an System.Reflection.Metadata.EntityHandle and is equal to the current instance; otherwise, lse.
        Equals(self: EntityHandle, other: EntityHandle) -> bool
        
            Returns a value that indicates whether the current instance and the specified System.Reflection.Metadata.EntityHandle are equal.
        
            other: The value to compare with the current instance.
            Returns: ue if the current instance and other are equal; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: EntityHandle) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code for this instance.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: EntityHandle) -> bool

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: EntityHandle) -> HandleKind

"""


    AssemblyDefinition = None
    ModuleDefinition = None


class EventAccessors(object):
    # no doc
    Adder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Adder(self: EventAccessors) -> MethodDefinitionHandle

"""

    Others = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Others(self: EventAccessors) -> ImmutableArray[MethodDefinitionHandle]

"""

    Raiser = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Raiser(self: EventAccessors) -> MethodDefinitionHandle

"""

    Remover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Remover(self: EventAccessors) -> MethodDefinitionHandle

"""



class EventDefinition(object):
    # no doc
    def GetAccessors(self):
        """ GetAccessors(self: EventDefinition) -> EventAccessors """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: EventDefinition) -> CustomAttributeHandleCollection """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: EventDefinition) -> EventAttributes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EventDefinition) -> StringHandle

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: EventDefinition) -> EntityHandle

"""



class EventDefinitionHandle(object, IEquatable[EventDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: EventDefinitionHandle, obj: object) -> bool
        Equals(self: EventDefinitionHandle, other: EventDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EventDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: EventDefinitionHandle) -> bool

"""



class EventDefinitionHandleCollection(object, IReadOnlyCollection[EventDefinitionHandle], IEnumerable[EventDefinitionHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: EventDefinitionHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[EventDefinitionHandle](enumerable: IEnumerable[EventDefinitionHandle], value: EventDefinitionHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: EventDefinitionHandleCollection) -> int

"""


    Enumerator = None


class ExceptionRegion(object):
    # no doc
    CatchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a TypeRef, TypeDef, or TypeSpec handle if the region represents a catch, or a nil token otherwise (fault(System.Reflection.Metadata.EntityHandle)).

Get: CatchType(self: ExceptionRegion) -> EntityHandle

"""

    FilterOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the IL offset of the start of the filter block, or -1 if the region is not a filter.

Get: FilterOffset(self: ExceptionRegion) -> int

"""

    HandlerLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length in bytes of the exception handler.

Get: HandlerLength(self: ExceptionRegion) -> int

"""

    HandlerOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the starting IL offset of the exception handler.

Get: HandlerOffset(self: ExceptionRegion) -> int

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: ExceptionRegion) -> ExceptionRegionKind

"""

    TryLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length in bytes of the try block.

Get: TryLength(self: ExceptionRegion) -> int

"""

    TryOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the starting IL offset of the try block.

Get: TryOffset(self: ExceptionRegion) -> int

"""



class ExceptionRegionKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum ExceptionRegionKind, values: Catch (0), Fault (4), Filter (1), Finally (2) """
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

    Catch = None
    Fault = None
    Filter = None
    Finally = None
    value__ = None


class ExportedType(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: ExportedType) -> CustomAttributeHandleCollection """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: ExportedType) -> TypeAttributes

"""

    Implementation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle to resolve the implementation of the target type.

Get: Implementation(self: ExportedType) -> EntityHandle

"""

    IsForwarder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsForwarder(self: ExportedType) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the target type, or fault if the type is nested or defined in a root namespace.

Get: Name(self: ExportedType) -> StringHandle

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full name of the namespace that contains the target type, or fault if the type is nested or defined in a root namespace.

Get: Namespace(self: ExportedType) -> StringHandle

"""

    NamespaceDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the definition handle of the namespace where the target type is defined, or fault if the type is nested or defined in a root namespace.

Get: NamespaceDefinition(self: ExportedType) -> NamespaceDefinitionHandle

"""



class ExportedTypeHandle(object, IEquatable[ExportedTypeHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ExportedTypeHandle, obj: object) -> bool
        Equals(self: ExportedTypeHandle, other: ExportedTypeHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ExportedTypeHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ExportedTypeHandle) -> bool

"""



class ExportedTypeHandleCollection(object, IReadOnlyCollection[ExportedTypeHandle], IEnumerable[ExportedTypeHandle], IEnumerable):
    """ Represents a collection of System.Reflection.Metadata.TypeReferenceHandle instances. """
    def GetEnumerator(self):
        """ GetEnumerator(self: ExportedTypeHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ExportedTypeHandle](enumerable: IEnumerable[ExportedTypeHandle], value: ExportedTypeHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: ExportedTypeHandleCollection) -> int

"""


    Enumerator = None


class FieldDefinition(object):
    # no doc
    def DecodeSignature(self, provider, genericContext):
        """ DecodeSignature[(TType, TGenericContext)](self: FieldDefinition, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> TType """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: FieldDefinition) -> CustomAttributeHandleCollection """
        pass

    def GetDeclaringType(self):
        """ GetDeclaringType(self: FieldDefinition) -> TypeDefinitionHandle """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: FieldDefinition) -> ConstantHandle """
        pass

    def GetMarshallingDescriptor(self):
        """ GetMarshallingDescriptor(self: FieldDefinition) -> BlobHandle """
        pass

    def GetOffset(self):
        """
        GetOffset(self: FieldDefinition) -> int
        
            Returns the field layout offset, or -1 if it is not available.
            Returns: The field definition offset, or -1 if it is not available.
        """
        pass

    def GetRelativeVirtualAddress(self):
        """ GetRelativeVirtualAddress(self: FieldDefinition) -> int """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: FieldDefinition) -> FieldAttributes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: FieldDefinition) -> StringHandle

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Signature(self: FieldDefinition) -> BlobHandle

"""



class FieldDefinitionHandle(object, IEquatable[FieldDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: FieldDefinitionHandle, obj: object) -> bool
        Equals(self: FieldDefinitionHandle, other: FieldDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: FieldDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: FieldDefinitionHandle) -> bool

"""



class FieldDefinitionHandleCollection(object, IReadOnlyCollection[FieldDefinitionHandle], IEnumerable[FieldDefinitionHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: FieldDefinitionHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FieldDefinitionHandle](enumerable: IEnumerable[FieldDefinitionHandle], value: FieldDefinitionHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: FieldDefinitionHandleCollection) -> int

"""


    Enumerator = None


class GenericParameter(object):
    # no doc
    def GetConstraints(self):
        """ GetConstraints(self: GenericParameter) -> GenericParameterConstraintHandleCollection """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: GenericParameter) -> CustomAttributeHandleCollection """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the attributes specifying variance and constraints.

Get: Attributes(self: GenericParameter) -> GenericParameterAttributes

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the zero-based index of the parameter within the declaring generic type or method declaration.

Get: Index(self: GenericParameter) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the generic parameter.

Get: Name(self: GenericParameter) -> StringHandle

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Reflection.Metadata.TypeDefinitionHandle or System.Reflection.Metadata.MethodDefinitionHandle that represents the parent of this generic parameter.

Get: Parent(self: GenericParameter) -> EntityHandle

"""



class GenericParameterConstraint(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: GenericParameterConstraint) -> CustomAttributeHandleCollection """
        pass

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the constrained System.Reflection.Metadata.GenericParameterHandle.

Get: Parameter(self: GenericParameterConstraint) -> GenericParameterHandle

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle (System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, or System.Reflection.Metadata.TypeSpecificationHandle) 
            specifying from which type this generic parameter is constrained to derive,
            or which interface this generic parameter is constrained to implement.

Get: Type(self: GenericParameterConstraint) -> EntityHandle

"""



class GenericParameterConstraintHandle(object, IEquatable[GenericParameterConstraintHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: GenericParameterConstraintHandle, obj: object) -> bool
        Equals(self: GenericParameterConstraintHandle, other: GenericParameterConstraintHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GenericParameterConstraintHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: GenericParameterConstraintHandle) -> bool

"""



class GenericParameterConstraintHandleCollection(object, IReadOnlyList[GenericParameterConstraintHandle], IReadOnlyCollection[GenericParameterConstraintHandle], IEnumerable[GenericParameterConstraintHandle], IEnumerable):
    """ Represents a collection of constraints of a generic type parameter. """
    def GetEnumerator(self):
        """ GetEnumerator(self: GenericParameterConstraintHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GenericParameterConstraintHandle](enumerable: IEnumerable[GenericParameterConstraintHandle], value: GenericParameterConstraintHandle) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: GenericParameterConstraintHandleCollection) -> int

"""


    Enumerator = None


class GenericParameterHandle(object, IEquatable[GenericParameterHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: GenericParameterHandle, obj: object) -> bool
        Equals(self: GenericParameterHandle, other: GenericParameterHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GenericParameterHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: GenericParameterHandle) -> bool

"""



class GenericParameterHandleCollection(object, IReadOnlyList[GenericParameterHandle], IReadOnlyCollection[GenericParameterHandle], IEnumerable[GenericParameterHandle], IEnumerable):
    """ Represents a collection of generic type parameters of a method or type. """
    def GetEnumerator(self):
        """ GetEnumerator(self: GenericParameterHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GenericParameterHandle](enumerable: IEnumerable[GenericParameterHandle], value: GenericParameterHandle) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: GenericParameterHandleCollection) -> int

"""


    Enumerator = None


class GuidHandle(object, IEquatable[GuidHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: GuidHandle, obj: object) -> bool
        Equals(self: GuidHandle, other: GuidHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GuidHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: GuidHandle) -> bool

"""



class Handle(object, IEquatable[Handle]):
    """ Represents any metadata entity (such as a type reference, a type definition, a type specification, a method definition, or a custom attribute) or value (a string, blob, guid, or user string). """
    def Equals(self, *__args):
        """
        Equals(self: Handle, obj: object) -> bool
        Equals(self: Handle, other: Handle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Handle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: Handle) -> bool

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: Handle) -> HandleKind

"""


    AssemblyDefinition = None
    ModuleDefinition = None


class HandleComparer(object, IEqualityComparer[Handle], IComparer[Handle], IEqualityComparer[EntityHandle], IComparer[EntityHandle]):
    # no doc
    def Compare(self, x, y):
        """
        Compare(self: HandleComparer, x: Handle, y: Handle) -> int
        
            Compares two handles.
        
            x: The first handle to compare.
            y: The second handle to compare.
            Returns: Zero if the two handles are equal, and a non-zero value if they are not.
        Compare(self: HandleComparer, x: EntityHandle, y: EntityHandle) -> int
        
            Compares two entity handles.
        
            x: The first entity handle to compare.
            y: The second entity handle to compare.
            Returns: Zero if the two entity handles are equal, and a non-zero value of they are not.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: HandleComparer, x: Handle, y: Handle) -> bool
        
            Determines whether the specified objects are equal.
        
            x: The first object of type T to compare.
            y: The second object of type T to compare.
            Returns: ue if the specified objects are equal; otherwise, lse.
        Equals(self: HandleComparer, x: EntityHandle, y: EntityHandle) -> bool
        
            Determines whether the specified objects are equal.
        
            x: The first object of type T to compare.
            y: The second object of type T to compare.
            Returns: ue if the specified objects are equal; otherwise, lse.
        """
        pass

    def GetHashCode(self, obj=None):
        """
        GetHashCode(self: HandleComparer, obj: Handle) -> int
        
            Returns a hash code for the specified object.
        
            obj: The System.Object for which a hash code is to be returned.
            Returns: A hash code for the specified object.
        GetHashCode(self: HandleComparer, obj: EntityHandle) -> int
        
            Returns a hash code for the specified object.
        
            obj: The System.Object for which a hash code is to be returned.
            Returns: A hash code for the specified object.
        """
        pass

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Default = None


class HandleKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum HandleKind, values: AssemblyDefinition (32), AssemblyFile (38), AssemblyReference (35), Blob (113), Constant (11), CustomAttribute (12), CustomDebugInformation (55), DeclarativeSecurityAttribute (14), Document (48), EventDefinition (20), ExportedType (39), FieldDefinition (4), GenericParameter (42), GenericParameterConstraint (44), Guid (114), ImportScope (53), InterfaceImplementation (9), LocalConstant (52), LocalScope (50), LocalVariable (51), ManifestResource (40), MemberReference (10), MethodDebugInformation (49), MethodDefinition (6), MethodImplementation (25), MethodSpecification (43), ModuleDefinition (0), ModuleReference (26), NamespaceDefinition (124), Parameter (8), PropertyDefinition (23), StandaloneSignature (17), String (120), TypeDefinition (2), TypeReference (1), TypeSpecification (27), UserString (112) """
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

    AssemblyDefinition = None
    AssemblyFile = None
    AssemblyReference = None
    Blob = None
    Constant = None
    CustomAttribute = None
    CustomDebugInformation = None
    DeclarativeSecurityAttribute = None
    Document = None
    EventDefinition = None
    ExportedType = None
    FieldDefinition = None
    GenericParameter = None
    GenericParameterConstraint = None
    Guid = None
    ImportScope = None
    InterfaceImplementation = None
    LocalConstant = None
    LocalScope = None
    LocalVariable = None
    ManifestResource = None
    MemberReference = None
    MethodDebugInformation = None
    MethodDefinition = None
    MethodImplementation = None
    MethodSpecification = None
    ModuleDefinition = None
    ModuleReference = None
    NamespaceDefinition = None
    Parameter = None
    PropertyDefinition = None
    StandaloneSignature = None
    String = None
    TypeDefinition = None
    TypeReference = None
    TypeSpecification = None
    UserString = None
    value__ = None


class IConstructedTypeProvider(ISZArrayTypeProvider[TType]):
    # no doc
    def GetArrayType(self, elementType, shape):
        """
        GetArrayType(self: IConstructedTypeProvider[TType], elementType: TType, shape: ArrayShape) -> TType
        
            Gets the type symbol for a generalized array of the given element type and shape.
        
            elementType: The type of the elements in the array.
            shape: The shape (rank, sizes, and lower bounds) of the array.
        """
        pass

    def GetByReferenceType(self, elementType):
        """
        GetByReferenceType(self: IConstructedTypeProvider[TType], elementType: TType) -> TType
        
            Gets the type symbol for a managed pointer to the given element type.
        """
        pass

    def GetGenericInstantiation(self, genericType, typeArguments):
        """
        GetGenericInstantiation(self: IConstructedTypeProvider[TType], genericType: TType, typeArguments: ImmutableArray[TType]) -> TType
        
            Gets the type symbol for a generic instantiation of the given generic type with the given type arguments.
        """
        pass

    def GetPointerType(self, elementType):
        """
        GetPointerType(self: IConstructedTypeProvider[TType], elementType: TType) -> TType
        
            Gets the type symbol for an unmanaged pointer to the given element type.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICustomAttributeTypeProvider(ISimpleTypeProvider[TType], ISZArrayTypeProvider[TType]):
    # no doc
    def GetSystemType(self):
        """
        GetSystemType(self: ICustomAttributeTypeProvider[TType]) -> TType
        
            Gets the  representation for System.Type.
        """
        pass

    def GetTypeFromSerializedName(self, name):
        """
        GetTypeFromSerializedName(self: ICustomAttributeTypeProvider[TType], name: str) -> TType
        
            Gets the type symbol for the given serialized type name.
        
            name: The serialized type name in so-called "reflection notation" format (as understood by the System.Type.GetType(System.String) method.)
            Returns: A  instance.
        """
        pass

    def GetUnderlyingEnumType(self, type):
        """
        GetUnderlyingEnumType(self: ICustomAttributeTypeProvider[TType], type: TType) -> PrimitiveTypeCode
        
            Gets the underlying type of the given enum type symbol.
        
            type: An enum type.
            Returns: A type code that indicates the underlying type of the enumeration.
        """
        pass

    def IsSystemType(self, type):
        """
        IsSystemType(self: ICustomAttributeTypeProvider[TType], type: TType) -> bool
        
            Verifies if the given type represents System.Type.
        
            type: The type to verify.
            Returns: ue if the given type is a System.Type, lse otherwise.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ILOpCode(Enum, IComparable, IFormattable, IConvertible):
    """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
    def Add(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Add_ovf(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Add_ovf_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def And(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Arglist(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Beq(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Beq_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bge(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bge_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bge_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bge_un_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bgt(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bgt_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bgt_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bgt_un_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ble(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ble_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ble_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ble_un_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Blt(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Blt_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Blt_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Blt_un_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bne_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Bne_un_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Box(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Br(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Break(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Brfalse(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Brfalse_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Brtrue(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Brtrue_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Br_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Call(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Calli(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Callvirt(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Castclass(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ceq(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Cgt(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Cgt_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ckfinite(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Clt(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Clt_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Constrained(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_i(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_i1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_i2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i1_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i2_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i4_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i8_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_i_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u1_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u2_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u4_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u8_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_ovf_u_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_r4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_r8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_r_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_u(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_u1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_u2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_u4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Conv_u8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Cpblk(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Cpobj(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Div(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Div_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Dup(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Endfilter(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Endfinally(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Initblk(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Initobj(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Isinst(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Jmp(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarg(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarga(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarga_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarg_0(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarg_1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarg_2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarg_3(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldarg_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_0(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_3(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_5(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_6(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_7(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_m1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i4_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_r4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldc_r8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelema(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_i(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_i1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_i2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_r4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_r8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_ref(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_u1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_u2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldelem_u4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldfld(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldflda(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldftn(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_i(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_i1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_i2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_r4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_r8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_ref(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_u1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_u2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldind_u4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldlen(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloc(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloca(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloca_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloc_0(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloc_1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloc_2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloc_3(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldloc_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldnull(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldobj(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldsfld(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldsflda(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldstr(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldtoken(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ldvirtftn(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Leave(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Leave_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Localloc(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Mkrefany(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Mul(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Mul_ovf(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Mul_ovf_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Neg(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Newarr(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Newobj(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Nop(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Not(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Or(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Pop(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Readonly(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Refanytype(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Refanyval(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Rem(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Rem_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Ret(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Rethrow(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Shl(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Shr(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Shr_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Sizeof(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Starg(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Starg_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_i(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_i1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_i2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_r4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_r8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stelem_ref(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stfld(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_i(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_i1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_i2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_i4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_i8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_r4(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_r8(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stind_ref(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stloc(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stloc_0(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stloc_1(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stloc_2(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stloc_3(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stloc_s(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stobj(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Stsfld(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Sub(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Sub_ovf(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Sub_ovf_un(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Switch(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Tail(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Throw(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Unaligned(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Unbox(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Unbox_any(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Volatile(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def Xor(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

    def __call__(self, *args): #cannot find CLR method
        """ enum ILOpCode, values: Add (88), Add_ovf (214), Add_ovf_un (215), And (95), Arglist (65024), Beq (59), Beq_s (46), Bge (60), Bge_s (47), Bge_un (65), Bge_un_s (52), Bgt (61), Bgt_s (48), Bgt_un (66), Bgt_un_s (53), Ble (62), Ble_s (49), Ble_un (67), Ble_un_s (54), Blt (63), Blt_s (50), Blt_un (68), Blt_un_s (55), Bne_un (64), Bne_un_s (51), Box (140), Br (56), Br_s (43), Break (1), Brfalse (57), Brfalse_s (44), Brtrue (58), Brtrue_s (45), Call (40), Calli (41), Callvirt (111), Castclass (116), Ceq (65025), Cgt (65026), Cgt_un (65027), Ckfinite (195), Clt (65028), Clt_un (65029), Constrained (65046), Conv_i (211), Conv_i1 (103), Conv_i2 (104), Conv_i4 (105), Conv_i8 (106), Conv_ovf_i (212), Conv_ovf_i_un (138), Conv_ovf_i1 (179), Conv_ovf_i1_un (130), Conv_ovf_i2 (181), Conv_ovf_i2_un (131), Conv_ovf_i4 (183), Conv_ovf_i4_un (132), Conv_ovf_i8 (185), Conv_ovf_i8_un (133), Conv_ovf_u (213), Conv_ovf_u_un (139), Conv_ovf_u1 (180), Conv_ovf_u1_un (134), Conv_ovf_u2 (182), Conv_ovf_u2_un (135), Conv_ovf_u4 (184), Conv_ovf_u4_un (136), Conv_ovf_u8 (186), Conv_ovf_u8_un (137), Conv_r_un (118), Conv_r4 (107), Conv_r8 (108), Conv_u (224), Conv_u1 (210), Conv_u2 (209), Conv_u4 (109), Conv_u8 (110), Cpblk (65047), Cpobj (112), Div (91), Div_un (92), Dup (37), Endfilter (65041), Endfinally (220), Initblk (65048), Initobj (65045), Isinst (117), Jmp (39), Ldarg (65033), Ldarg_0 (2), Ldarg_1 (3), Ldarg_2 (4), Ldarg_3 (5), Ldarg_s (14), Ldarga (65034), Ldarga_s (15), Ldc_i4 (32), Ldc_i4_0 (22), Ldc_i4_1 (23), Ldc_i4_2 (24), Ldc_i4_3 (25), Ldc_i4_4 (26), Ldc_i4_5 (27), Ldc_i4_6 (28), Ldc_i4_7 (29), Ldc_i4_8 (30), Ldc_i4_m1 (21), Ldc_i4_s (31), Ldc_i8 (33), Ldc_r4 (34), Ldc_r8 (35), Ldelem (163), Ldelem_i (151), Ldelem_i1 (144), Ldelem_i2 (146), Ldelem_i4 (148), Ldelem_i8 (150), Ldelem_r4 (152), Ldelem_r8 (153), Ldelem_ref (154), Ldelem_u1 (145), Ldelem_u2 (147), Ldelem_u4 (149), Ldelema (143), Ldfld (123), Ldflda (124), Ldftn (65030), Ldind_i (77), Ldind_i1 (70), Ldind_i2 (72), Ldind_i4 (74), Ldind_i8 (76), Ldind_r4 (78), Ldind_r8 (79), Ldind_ref (80), Ldind_u1 (71), Ldind_u2 (73), Ldind_u4 (75), Ldlen (142), Ldloc (65036), Ldloc_0 (6), Ldloc_1 (7), Ldloc_2 (8), Ldloc_3 (9), Ldloc_s (17), Ldloca (65037), Ldloca_s (18), Ldnull (20), Ldobj (113), Ldsfld (126), Ldsflda (127), Ldstr (114), Ldtoken (208), Ldvirtftn (65031), Leave (221), Leave_s (222), Localloc (65039), Mkrefany (198), Mul (90), Mul_ovf (216), Mul_ovf_un (217), Neg (101), Newarr (141), Newobj (115), Nop (0), Not (102), Or (96), Pop (38), Readonly (65054), Refanytype (65053), Refanyval (194), Rem (93), Rem_un (94), Ret (42), Rethrow (65050), Shl (98), Shr (99), Shr_un (100), Sizeof (65052), Starg (65035), Starg_s (16), Stelem (164), Stelem_i (155), Stelem_i1 (156), Stelem_i2 (157), Stelem_i4 (158), Stelem_i8 (159), Stelem_r4 (160), Stelem_r8 (161), Stelem_ref (162), Stfld (125), Stind_i (223), Stind_i1 (82), Stind_i2 (83), Stind_i4 (84), Stind_i8 (85), Stind_r4 (86), Stind_r8 (87), Stind_ref (81), Stloc (65038), Stloc_0 (10), Stloc_1 (11), Stloc_2 (12), Stloc_3 (13), Stloc_s (19), Stobj (129), Stsfld (128), Sub (89), Sub_ovf (218), Sub_ovf_un (219), Switch (69), Tail (65044), Throw (122), Unaligned (65042), Unbox (121), Unbox_any (165), Volatile (65043), Xor (97) """
        pass

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


class ILOpCodeExtensions(object):
    # no doc
    @staticmethod
    def GetBranchOperandSize(opCode):
        """
        GetBranchOperandSize(opCode: ILOpCode) -> int
        
            Calculates the size of the specified branch instruction operand.
        
            opCode: The branch op-code.
            Returns: 1 if opCode is a short branch, or 4 if it is a long branch.
        """
        pass

    @staticmethod
    def GetLongBranch(opCode):
        """
        GetLongBranch(opCode: ILOpCode) -> ILOpCode
        
            Gets a long form of the specified branch op-code.
        
            opCode: The branch op-code.
            Returns: The long form of the branch op-code.
        """
        pass

    @staticmethod
    def GetShortBranch(opCode):
        """
        GetShortBranch(opCode: ILOpCode) -> ILOpCode
        
            Gets a short form of the specified branch op-code.
        
            opCode: The branch op-code.
            Returns: The short form of the branch op-code.
        """
        pass

    @staticmethod
    def IsBranch(opCode):
        """
        IsBranch(opCode: ILOpCode) -> bool
        
            Verifies if the specified op-code is a branch to a label.
            Returns: ue if the specified op-code is a branch to a label, lse otherwise.
        """
        pass

    __all__ = [
        'GetBranchOperandSize',
        'GetLongBranch',
        'GetShortBranch',
        'IsBranch',
    ]


class ImageFormatLimitationException(Exception, ISerializable, _Exception):
    """
    The exception that is thrown when an attempt to write metadata exceeds a limit given by the format specification. For example, when the heap size limit is exceeded.
    
    ImageFormatLimitationException()
    ImageFormatLimitationException(message: str)
    ImageFormatLimitationException(message: str, innerException: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ImportDefinition(object):
    # no doc
    Alias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alias(self: ImportDefinition) -> BlobHandle

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: ImportDefinition) -> ImportDefinitionKind

"""

    TargetAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetAssembly(self: ImportDefinition) -> AssemblyReferenceHandle

"""

    TargetNamespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetNamespace(self: ImportDefinition) -> BlobHandle

"""

    TargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetType(self: ImportDefinition) -> EntityHandle

"""



class ImportDefinitionCollection(object, IEnumerable[ImportDefinition], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ImportDefinitionCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ImportDefinition](enumerable: IEnumerable[ImportDefinition], value: ImportDefinition) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Enumerator = None


class ImportDefinitionKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum ImportDefinitionKind, values: AliasAssemblyNamespace (8), AliasAssemblyReference (6), AliasNamespace (7), AliasType (9), ImportAssemblyNamespace (2), ImportAssemblyReferenceAlias (5), ImportNamespace (1), ImportType (3), ImportXmlNamespace (4) """
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

    AliasAssemblyNamespace = None
    AliasAssemblyReference = None
    AliasNamespace = None
    AliasType = None
    ImportAssemblyNamespace = None
    ImportAssemblyReferenceAlias = None
    ImportNamespace = None
    ImportType = None
    ImportXmlNamespace = None
    value__ = None


class ImportScope(object):
    """ Provides information about the lexical scope within which a group of imports are available. This information is stored in debug metadata. """
    def GetImports(self):
        """ GetImports(self: ImportScope) -> ImportDefinitionCollection """
        pass

    ImportsBlob = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportsBlob(self: ImportScope) -> BlobHandle

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: ImportScope) -> ImportScopeHandle

"""



class ImportScopeCollection(object, IReadOnlyCollection[ImportScopeHandle], IEnumerable[ImportScopeHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ImportScopeCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ImportScopeHandle](enumerable: IEnumerable[ImportScopeHandle], value: ImportScopeHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: ImportScopeCollection) -> int

"""


    Enumerator = None


class ImportScopeHandle(object, IEquatable[ImportScopeHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ImportScopeHandle, obj: object) -> bool
        Equals(self: ImportScopeHandle, other: ImportScopeHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ImportScopeHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ImportScopeHandle) -> bool

"""



class InterfaceImplementation(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: InterfaceImplementation) -> CustomAttributeHandleCollection """
        pass

    Interface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the interface that is implemented (System.Reflection.Metadata.TypeDefinitionHandle, System.Reflection.Metadata.TypeReferenceHandle, or System.Reflection.Metadata.TypeSpecificationHandle).

Get: Interface(self: InterfaceImplementation) -> EntityHandle

"""



class InterfaceImplementationHandle(object, IEquatable[InterfaceImplementationHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: InterfaceImplementationHandle, obj: object) -> bool
        Equals(self: InterfaceImplementationHandle, other: InterfaceImplementationHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: InterfaceImplementationHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: InterfaceImplementationHandle) -> bool

"""



class InterfaceImplementationHandleCollection(object, IReadOnlyCollection[InterfaceImplementationHandle], IEnumerable[InterfaceImplementationHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: InterfaceImplementationHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[InterfaceImplementationHandle](enumerable: IEnumerable[InterfaceImplementationHandle], value: InterfaceImplementationHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: InterfaceImplementationHandleCollection) -> int

"""


    Enumerator = None


class ISignatureTypeProvider(ISimpleTypeProvider[TType], IConstructedTypeProvider[TType], ISZArrayTypeProvider[TType]):
    # no doc
    def GetFunctionPointerType(self, signature):
        """
        GetFunctionPointerType(self: ISignatureTypeProvider[TType, TGenericContext], signature: MethodSignature[TType]) -> TType
        
            Gets the type symbol for the function pointer type of the given method signature.
            Returns: The type symbol for the function pointer type.
        """
        pass

    def GetGenericMethodParameter(self, genericContext, index):
        """
        GetGenericMethodParameter(self: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext, index: int) -> TType
        
            Gets the type symbol for the generic method parameter at the given zero-based index.
            Returns: The type symbol for the generic method parameter at index.
        """
        pass

    def GetGenericTypeParameter(self, genericContext, index):
        """
        GetGenericTypeParameter(self: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext, index: int) -> TType
        
            Gets the type symbol for the generic type parameter at the given zero-based index.
            Returns: The type symbol for the generic type parameter at the given zero-based index.
        """
        pass

    def GetModifiedType(self, modifier, unmodifiedType, isRequired):
        """
        GetModifiedType(self: ISignatureTypeProvider[TType, TGenericContext], modifier: TType, unmodifiedType: TType, isRequired: bool) -> TType
        
            Gets the type symbol for a type with a custom modifier applied.
        
            modifier: The modifier type applied.
            unmodifiedType: The type symbol of the underlying type without modifiers applied.
            isRequired: ue if the modifier is required, lse if it's optional.
            Returns: The type symbol.
        """
        pass

    def GetPinnedType(self, elementType):
        """
        GetPinnedType(self: ISignatureTypeProvider[TType, TGenericContext], elementType: TType) -> TType
        
            Gets the type symbol for a local variable type that is marked as pinned.
            Returns: The type symbol for the local variable type.
        """
        pass

    def GetTypeFromSpecification(self, reader, genericContext, handle, rawTypeKind):
        """
        GetTypeFromSpecification(self: ISignatureTypeProvider[TType, TGenericContext], reader: MetadataReader, genericContext: TGenericContext, handle: TypeSpecificationHandle, rawTypeKind: Byte) -> TType
        
            Gets the type symbol for a type specification.
        
            reader: The metadata reader that was passed to the signature decoder. It may be ll.
            genericContext: The context that was passed to the signature decoder.
            handle: The type specification handle.
            rawTypeKind: The kind of the type, as specified in the signature. To interpret this value, use 
             System.Reflection.Metadata.Ecma335.MetadataReaderExtensions.ResolveSignatureTypeKind(System.Reflection.Metadata.MetadataReader,System.Reflection.Metadata.EntityHandle,System.Byte).
        
            Returns: The type symbol for the type specification.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISimpleTypeProvider:
    # no doc
    def GetPrimitiveType(self, typeCode):
        """
        GetPrimitiveType(self: ISimpleTypeProvider[TType], typeCode: PrimitiveTypeCode) -> TType
        
            Gets the type symbol for a primitive type.
            Returns: The type symbol for .
        """
        pass

    def GetTypeFromDefinition(self, reader, handle, rawTypeKind):
        """
        GetTypeFromDefinition(self: ISimpleTypeProvider[TType], reader: MetadataReader, handle: TypeDefinitionHandle, rawTypeKind: Byte) -> TType
        
            Gets the type symbol for a type definition.
        
            reader: The metadata reader that was passed to the signature decoder. It may be ll.
            handle: The type definition handle.
            rawTypeKind: The kind of the type, as specified in the signature. To interpret this value use 
             System.Reflection.Metadata.Ecma335.MetadataReaderExtensions.ResolveSignatureTypeKind(System.Reflection.Metadata.MetadataReader,System.Reflection.Metadata.EntityHandle,System.Byte).
        
            Returns: The type symbol.
        """
        pass

    def GetTypeFromReference(self, reader, handle, rawTypeKind):
        """
        GetTypeFromReference(self: ISimpleTypeProvider[TType], reader: MetadataReader, handle: TypeReferenceHandle, rawTypeKind: Byte) -> TType
        
            Gets the type symbol for a type reference.
        
            reader: The metadata reader that was passed to the signature decoder. It may be ll.
            handle: The type definition handle.
            rawTypeKind: The kind of the type as specified in the signature. To interpret this value, use 
             System.Reflection.Metadata.Ecma335.MetadataReaderExtensions.ResolveSignatureTypeKind(System.Reflection.Metadata.MetadataReader,System.Reflection.Metadata.EntityHandle,System.Byte).
        
            Returns: The type symbol.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ISZArrayTypeProvider:
    # no doc
    def GetSZArrayType(self, elementType):
        """
        GetSZArrayType(self: ISZArrayTypeProvider[TType], elementType: TType) -> TType
        
            Gets the type symbol for a single-dimensional array of the given element type with a lower bounds of zero.
            Returns: A  instance.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LocalConstant(object):
    """ Provides information about local constants. This information is stored in debug metadata. """
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LocalConstant) -> StringHandle

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the constant signature.

Get: Signature(self: LocalConstant) -> BlobHandle

"""



class LocalConstantHandle(object, IEquatable[LocalConstantHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: LocalConstantHandle, obj: object) -> bool
        Equals(self: LocalConstantHandle, other: LocalConstantHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: LocalConstantHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: LocalConstantHandle) -> bool

"""



class LocalConstantHandleCollection(object, IReadOnlyCollection[LocalConstantHandle], IEnumerable[LocalConstantHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: LocalConstantHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LocalConstantHandle](enumerable: IEnumerable[LocalConstantHandle], value: LocalConstantHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: LocalConstantHandleCollection) -> int

"""


    Enumerator = None


class LocalScope(object):
    """ Provides information about the scope of local variables and constants. This information is stored in debug metadata. """
    def GetChildren(self):
        """ GetChildren(self: LocalScope) -> ChildrenEnumerator """
        pass

    def GetLocalConstants(self):
        """ GetLocalConstants(self: LocalScope) -> LocalConstantHandleCollection """
        pass

    def GetLocalVariables(self):
        """ GetLocalVariables(self: LocalScope) -> LocalVariableHandleCollection """
        pass

    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: LocalScope) -> int

"""

    ImportScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportScope(self: LocalScope) -> ImportScopeHandle

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: LocalScope) -> int

"""

    Method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Method(self: LocalScope) -> MethodDefinitionHandle

"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: LocalScope) -> int

"""



class LocalScopeHandle(object, IEquatable[LocalScopeHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: LocalScopeHandle, obj: object) -> bool
        Equals(self: LocalScopeHandle, other: LocalScopeHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: LocalScopeHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: LocalScopeHandle) -> bool

"""



class LocalScopeHandleCollection(object, IReadOnlyCollection[LocalScopeHandle], IEnumerable[LocalScopeHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: LocalScopeHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LocalScopeHandle](enumerable: IEnumerable[LocalScopeHandle], value: LocalScopeHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: LocalScopeHandleCollection) -> int

"""


    ChildrenEnumerator = None
    Enumerator = None


class LocalVariable(object):
    """ Provides information about local variables. This information is stored in debug metadata. """
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: LocalVariable) -> LocalVariableAttributes

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: LocalVariable) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LocalVariable) -> StringHandle

"""



class LocalVariableAttributes(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) LocalVariableAttributes, values: DebuggerHidden (1), None (0) """
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

    DebuggerHidden = None
    None = None
    value__ = None


class LocalVariableHandle(object, IEquatable[LocalVariableHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: LocalVariableHandle, obj: object) -> bool
        Equals(self: LocalVariableHandle, other: LocalVariableHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: LocalVariableHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: LocalVariableHandle) -> bool

"""



class LocalVariableHandleCollection(object, IReadOnlyCollection[LocalVariableHandle], IEnumerable[LocalVariableHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: LocalVariableHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LocalVariableHandle](enumerable: IEnumerable[LocalVariableHandle], value: LocalVariableHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: LocalVariableHandleCollection) -> int

"""


    Enumerator = None


class ManifestResource(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: ManifestResource) -> CustomAttributeHandleCollection """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the manifest resource attributes.

Get: Attributes(self: ManifestResource) -> ManifestResourceAttributes

"""

    Implementation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the implementation entity handle.

Get: Implementation(self: ManifestResource) -> EntityHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the resource name.

Get: Name(self: ManifestResource) -> StringHandle

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the byte offset within the referenced file at which this resource record begins.

Get: Offset(self: ManifestResource) -> Int64

"""



class ManifestResourceHandle(object, IEquatable[ManifestResourceHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ManifestResourceHandle, obj: object) -> bool
        Equals(self: ManifestResourceHandle, other: ManifestResourceHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ManifestResourceHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ManifestResourceHandle) -> bool

"""



class ManifestResourceHandleCollection(object, IReadOnlyCollection[ManifestResourceHandle], IEnumerable[ManifestResourceHandle], IEnumerable):
    """ Represents a collection of System.Reflection.Metadata.ManifestResourceHandle instances. """
    def GetEnumerator(self):
        """ GetEnumerator(self: ManifestResourceHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ManifestResourceHandle](enumerable: IEnumerable[ManifestResourceHandle], value: ManifestResourceHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: ManifestResourceHandleCollection) -> int

"""


    Enumerator = None


class MemberReference(object):
    # no doc
    def DecodeFieldSignature(self, provider, genericContext):
        """ DecodeFieldSignature[(TType, TGenericContext)](self: MemberReference, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> TType """
        pass

    def DecodeMethodSignature(self, provider, genericContext):
        """ DecodeMethodSignature[(TType, TGenericContext)](self: MemberReference, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> MethodSignature[TType] """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: MemberReference) -> CustomAttributeHandleCollection """
        pass

    def GetKind(self):
        """
        GetKind(self: MemberReference) -> MemberReferenceKind
        
            Determines if the member reference is to a method or field.
            Returns: One of the enumeration values that indicates the kind of member reference.
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MemberReference) -> StringHandle

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent entity handle.

Get: Parent(self: MemberReference) -> EntityHandle

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle to the signature blob.

Get: Signature(self: MemberReference) -> BlobHandle

"""



class MemberReferenceHandle(object, IEquatable[MemberReferenceHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: MemberReferenceHandle, obj: object) -> bool
        Equals(self: MemberReferenceHandle, other: MemberReferenceHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MemberReferenceHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: MemberReferenceHandle) -> bool

"""



class MemberReferenceHandleCollection(object, IReadOnlyCollection[MemberReferenceHandle], IEnumerable[MemberReferenceHandle], IEnumerable):
    """ Represents a collection of System.Reflection.Metadata.MemberReferenceHandle instances. """
    def GetEnumerator(self):
        """ GetEnumerator(self: MemberReferenceHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MemberReferenceHandle](enumerable: IEnumerable[MemberReferenceHandle], value: MemberReferenceHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: MemberReferenceHandleCollection) -> int

"""


    Enumerator = None


class MemberReferenceKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that indicate whether a System.Reflection.Metadata.MemberReference references a method or field.
    
    enum MemberReferenceKind, values: Field (1), Method (0)
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

    Field = None
    Method = None
    value__ = None


class MetadataKind(Enum, IComparable, IFormattable, IConvertible):
    """ enum MetadataKind, values: Ecma335 (0), ManagedWindowsMetadata (2), WindowsMetadata (1) """
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

    Ecma335 = None
    ManagedWindowsMetadata = None
    value__ = None
    WindowsMetadata = None


class MetadataReader(object):
    """
    Reads metadata as defined by the ECMA 335 CLI specification.
    
    MetadataReader(metadata: Byte*, length: int)
    MetadataReader(metadata: Byte*, length: int, options: MetadataReaderOptions)
    MetadataReader(metadata: Byte*, length: int, options: MetadataReaderOptions, utf8Decoder: MetadataStringDecoder)
    """
    def GetAssemblyDefinition(self):
        """ GetAssemblyDefinition(self: MetadataReader) -> AssemblyDefinition """
        pass

    def GetAssemblyFile(self, handle):
        """ GetAssemblyFile(self: MetadataReader, handle: AssemblyFileHandle) -> AssemblyFile """
        pass

    def GetAssemblyReference(self, handle):
        """ GetAssemblyReference(self: MetadataReader, handle: AssemblyReferenceHandle) -> AssemblyReference """
        pass

    def GetBlobBytes(self, handle):
        """ GetBlobBytes(self: MetadataReader, handle: BlobHandle) -> Array[Byte] """
        pass

    def GetBlobContent(self, handle):
        """ GetBlobContent(self: MetadataReader, handle: BlobHandle) -> ImmutableArray[Byte] """
        pass

    def GetBlobReader(self, handle):
        """
        GetBlobReader(self: MetadataReader, handle: BlobHandle) -> BlobReader
        GetBlobReader(self: MetadataReader, handle: StringHandle) -> BlobReader
        """
        pass

    def GetConstant(self, handle):
        """ GetConstant(self: MetadataReader, handle: ConstantHandle) -> Constant """
        pass

    def GetCustomAttribute(self, handle):
        """ GetCustomAttribute(self: MetadataReader, handle: CustomAttributeHandle) -> CustomAttribute """
        pass

    def GetCustomAttributes(self, handle):
        """ GetCustomAttributes(self: MetadataReader, handle: EntityHandle) -> CustomAttributeHandleCollection """
        pass

    def GetCustomDebugInformation(self, handle):
        """
        GetCustomDebugInformation(self: MetadataReader, handle: CustomDebugInformationHandle) -> CustomDebugInformation
        GetCustomDebugInformation(self: MetadataReader, handle: EntityHandle) -> CustomDebugInformationHandleCollection
        """
        pass

    def GetDeclarativeSecurityAttribute(self, handle):
        """ GetDeclarativeSecurityAttribute(self: MetadataReader, handle: DeclarativeSecurityAttributeHandle) -> DeclarativeSecurityAttribute """
        pass

    def GetDocument(self, handle):
        """ GetDocument(self: MetadataReader, handle: DocumentHandle) -> Document """
        pass

    def GetEventDefinition(self, handle):
        """ GetEventDefinition(self: MetadataReader, handle: EventDefinitionHandle) -> EventDefinition """
        pass

    def GetExportedType(self, handle):
        """ GetExportedType(self: MetadataReader, handle: ExportedTypeHandle) -> ExportedType """
        pass

    def GetFieldDefinition(self, handle):
        """ GetFieldDefinition(self: MetadataReader, handle: FieldDefinitionHandle) -> FieldDefinition """
        pass

    def GetGenericParameter(self, handle):
        """ GetGenericParameter(self: MetadataReader, handle: GenericParameterHandle) -> GenericParameter """
        pass

    def GetGenericParameterConstraint(self, handle):
        """ GetGenericParameterConstraint(self: MetadataReader, handle: GenericParameterConstraintHandle) -> GenericParameterConstraint """
        pass

    def GetGuid(self, handle):
        """ GetGuid(self: MetadataReader, handle: GuidHandle) -> Guid """
        pass

    def GetImportScope(self, handle):
        """ GetImportScope(self: MetadataReader, handle: ImportScopeHandle) -> ImportScope """
        pass

    def GetInterfaceImplementation(self, handle):
        """ GetInterfaceImplementation(self: MetadataReader, handle: InterfaceImplementationHandle) -> InterfaceImplementation """
        pass

    def GetLocalConstant(self, handle):
        """ GetLocalConstant(self: MetadataReader, handle: LocalConstantHandle) -> LocalConstant """
        pass

    def GetLocalScope(self, handle):
        """ GetLocalScope(self: MetadataReader, handle: LocalScopeHandle) -> LocalScope """
        pass

    def GetLocalScopes(self, handle):
        """
        GetLocalScopes(self: MetadataReader, handle: MethodDefinitionHandle) -> LocalScopeHandleCollection
        GetLocalScopes(self: MetadataReader, handle: MethodDebugInformationHandle) -> LocalScopeHandleCollection
        """
        pass

    def GetLocalVariable(self, handle):
        """ GetLocalVariable(self: MetadataReader, handle: LocalVariableHandle) -> LocalVariable """
        pass

    def GetManifestResource(self, handle):
        """ GetManifestResource(self: MetadataReader, handle: ManifestResourceHandle) -> ManifestResource """
        pass

    def GetMemberReference(self, handle):
        """ GetMemberReference(self: MetadataReader, handle: MemberReferenceHandle) -> MemberReference """
        pass

    def GetMethodDebugInformation(self, handle):
        """
        GetMethodDebugInformation(self: MetadataReader, handle: MethodDebugInformationHandle) -> MethodDebugInformation
        GetMethodDebugInformation(self: MetadataReader, handle: MethodDefinitionHandle) -> MethodDebugInformation
        """
        pass

    def GetMethodDefinition(self, handle):
        """ GetMethodDefinition(self: MetadataReader, handle: MethodDefinitionHandle) -> MethodDefinition """
        pass

    def GetMethodImplementation(self, handle):
        """ GetMethodImplementation(self: MetadataReader, handle: MethodImplementationHandle) -> MethodImplementation """
        pass

    def GetMethodSpecification(self, handle):
        """ GetMethodSpecification(self: MetadataReader, handle: MethodSpecificationHandle) -> MethodSpecification """
        pass

    def GetModuleDefinition(self):
        """ GetModuleDefinition(self: MetadataReader) -> ModuleDefinition """
        pass

    def GetModuleReference(self, handle):
        """ GetModuleReference(self: MetadataReader, handle: ModuleReferenceHandle) -> ModuleReference """
        pass

    def GetNamespaceDefinition(self, handle):
        """ GetNamespaceDefinition(self: MetadataReader, handle: NamespaceDefinitionHandle) -> NamespaceDefinition """
        pass

    def GetNamespaceDefinitionRoot(self):
        """ GetNamespaceDefinitionRoot(self: MetadataReader) -> NamespaceDefinition """
        pass

    def GetParameter(self, handle):
        """ GetParameter(self: MetadataReader, handle: ParameterHandle) -> Parameter """
        pass

    def GetPropertyDefinition(self, handle):
        """ GetPropertyDefinition(self: MetadataReader, handle: PropertyDefinitionHandle) -> PropertyDefinition """
        pass

    def GetStandaloneSignature(self, handle):
        """ GetStandaloneSignature(self: MetadataReader, handle: StandaloneSignatureHandle) -> StandaloneSignature """
        pass

    def GetString(self, handle):
        """
        GetString(self: MetadataReader, handle: StringHandle) -> str
        GetString(self: MetadataReader, handle: NamespaceDefinitionHandle) -> str
        GetString(self: MetadataReader, handle: DocumentNameBlobHandle) -> str
        """
        pass

    def GetTypeDefinition(self, handle):
        """ GetTypeDefinition(self: MetadataReader, handle: TypeDefinitionHandle) -> TypeDefinition """
        pass

    def GetTypeReference(self, handle):
        """ GetTypeReference(self: MetadataReader, handle: TypeReferenceHandle) -> TypeReference """
        pass

    def GetTypeSpecification(self, handle):
        """ GetTypeSpecification(self: MetadataReader, handle: TypeSpecificationHandle) -> TypeSpecification """
        pass

    def GetUserString(self, handle):
        """ GetUserString(self: MetadataReader, handle: UserStringHandle) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, metadata, length, options=None, utf8Decoder=None):
        """
        __new__(cls: type, metadata: Byte*, length: int)
        __new__(cls: type, metadata: Byte*, length: int, options: MetadataReaderOptions)
        __new__(cls: type, metadata: Byte*, length: int, options: MetadataReaderOptions, utf8Decoder: MetadataStringDecoder)
        """
        pass

    AssemblyFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyFiles(self: MetadataReader) -> AssemblyFileHandleCollection

"""

    AssemblyReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyReferences(self: MetadataReader) -> AssemblyReferenceHandleCollection

"""

    CustomAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomAttributes(self: MetadataReader) -> CustomAttributeHandleCollection

"""

    CustomDebugInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomDebugInformation(self: MetadataReader) -> CustomDebugInformationHandleCollection

"""

    DebugMetadataHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the information decoded from #Pdb stream, or ll if the stream is not present.

Get: DebugMetadataHeader(self: MetadataReader) -> DebugMetadataHeader

"""

    DeclarativeSecurityAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeclarativeSecurityAttributes(self: MetadataReader) -> DeclarativeSecurityAttributeHandleCollection

"""

    Documents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Documents(self: MetadataReader) -> DocumentHandleCollection

"""

    EventDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventDefinitions(self: MetadataReader) -> EventDefinitionHandleCollection

"""

    ExportedTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportedTypes(self: MetadataReader) -> ExportedTypeHandleCollection

"""

    FieldDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldDefinitions(self: MetadataReader) -> FieldDefinitionHandleCollection

"""

    ImportScopes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImportScopes(self: MetadataReader) -> ImportScopeCollection

"""

    IsAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the metadata represents an assembly.

Get: IsAssembly(self: MetadataReader) -> bool

"""

    LocalConstants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalConstants(self: MetadataReader) -> LocalConstantHandleCollection

"""

    LocalScopes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalScopes(self: MetadataReader) -> LocalScopeHandleCollection

"""

    LocalVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalVariables(self: MetadataReader) -> LocalVariableHandleCollection

"""

    ManifestResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManifestResources(self: MetadataReader) -> ManifestResourceHandleCollection

"""

    MemberReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberReferences(self: MetadataReader) -> MemberReferenceHandleCollection

"""

    MetadataKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the metadata kind.

Get: MetadataKind(self: MetadataReader) -> MetadataKind

"""

    MetadataLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the length of the underlying data.

Get: MetadataLength(self: MetadataReader) -> int

"""

    MetadataPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the pointer to the underlying data.

Get: MetadataPointer(self: MetadataReader) -> Byte*

"""

    MetadataVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version string read from metadata header.

Get: MetadataVersion(self: MetadataReader) -> str

"""

    MethodDebugInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodDebugInformation(self: MetadataReader) -> MethodDebugInformationHandleCollection

"""

    MethodDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodDefinitions(self: MetadataReader) -> MethodDefinitionHandleCollection

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Reflection.Metadata.MetadataReaderOptions passed to the constructor.

Get: Options(self: MetadataReader) -> MetadataReaderOptions

"""

    PropertyDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyDefinitions(self: MetadataReader) -> PropertyDefinitionHandleCollection

"""

    StringComparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the comparer used to compare strings stored in metadata.

Get: StringComparer(self: MetadataReader) -> MetadataStringComparer

"""

    TypeDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeDefinitions(self: MetadataReader) -> TypeDefinitionHandleCollection

"""

    TypeReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeReferences(self: MetadataReader) -> TypeReferenceHandleCollection

"""

    UTF8Decoder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the decoder used by the reader to produce string instances from UTF8-encoded byte sequences.

Get: UTF8Decoder(self: MetadataReader) -> MetadataStringDecoder

"""



class MetadataReaderOptions(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MetadataReaderOptions, values: ApplyWindowsRuntimeProjections (1), Default (1), None (0) """
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

    ApplyWindowsRuntimeProjections = None
    Default = None
    None = None
    value__ = None


class MetadataReaderProvider(object, IDisposable):
    """ Provides a System.Reflection.Metadata.MetadataReader for metadata stored in an array of bytes, a memory block, or a stream. """
    def Dispose(self):
        """
        Dispose(self: MetadataReaderProvider)
            Disposes all memory allocated by the reader.
        """
        pass

    @staticmethod
    def FromMetadataImage(*__args):
        """
        FromMetadataImage(start: Byte*, size: int) -> MetadataReaderProvider
        
            Creates a metadata provider over an image stored in memory.
        
            start: Pointer to the start of the metadata blob.
            size: The size of the metadata blob.
            Returns: The new metadata provider.
        FromMetadataImage(image: ImmutableArray[Byte]) -> MetadataReaderProvider
        """
        pass

    @staticmethod
    def FromMetadataStream(stream, options, size):
        """
        FromMetadataStream(stream: Stream, options: MetadataStreamOptions, size: int) -> MetadataReaderProvider
        
            Creates a provider for a stream of the specified size beginning at its current position.
        
            stream: A System.IO.Stream instance.
            options: Options specifying how sections of the image are read from the stream.
            size: Size of the metadata blob in the stream. If not specified, the metadata blob is assumed to span to the end of the stream.
            Returns: The new provider.
        """
        pass

    @staticmethod
    def FromPortablePdbImage(*__args):
        """
        FromPortablePdbImage(start: Byte*, size: int) -> MetadataReaderProvider
        
            Creates a portable PDB metadata provider over a blob stored in memory.
        
            start: Pointer to the start of the portable PDB blob.
            size: The size of the portable PDB blob.
            Returns: The new portable PDB metadata provider.
        FromPortablePdbImage(image: ImmutableArray[Byte]) -> MetadataReaderProvider
        """
        pass

    @staticmethod
    def FromPortablePdbStream(stream, options, size):
        """
        FromPortablePdbStream(stream: Stream, options: MetadataStreamOptions, size: int) -> MetadataReaderProvider
        
            Creates a provider for a stream of the specified size beginning at its current position.
        
            stream: The stream.
            options: Options specifying how sections of the image are read from the stream.
            size: Size of the metadata blob in the stream. If not specified, the metadata blob is assumed to span to the end of the stream.
            Returns: A System.Reflection.Metadata.MetadataReaderProvider instance.
        """
        pass

    def GetMetadataReader(self, options, utf8Decoder):
        """
        GetMetadataReader(self: MetadataReaderProvider, options: MetadataReaderOptions, utf8Decoder: MetadataStringDecoder) -> MetadataReader
        
            Gets a System.Reflection.Metadata.MetadataReader from a System.Reflection.Metadata.MetadataReaderProvider.
        
            options: A bitwise combination of the enumeration values that represent the configuration when reading the metadata.
            utf8Decoder: The encoding to use.
            Returns: A System.Reflection.Metadata.MetadataReader instance..
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class MetadataStreamOptions(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MetadataStreamOptions, values: Default (0), LeaveOpen (1), PrefetchMetadata (2) """
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
    LeaveOpen = None
    PrefetchMetadata = None
    value__ = None


class MetadataStringComparer(object):
    """ Provides string comparison helpers to query strings in metadata while avoiding allocation if possible. """
    def Equals(self, *__args):
        """
        Equals(self: MetadataStringComparer, handle: StringHandle, value: str) -> bool
        Equals(self: MetadataStringComparer, handle: StringHandle, value: str, ignoreCase: bool) -> bool
        Equals(self: MetadataStringComparer, handle: NamespaceDefinitionHandle, value: str) -> bool
        Equals(self: MetadataStringComparer, handle: NamespaceDefinitionHandle, value: str, ignoreCase: bool) -> bool
        Equals(self: MetadataStringComparer, handle: DocumentNameBlobHandle, value: str) -> bool
        Equals(self: MetadataStringComparer, handle: DocumentNameBlobHandle, value: str, ignoreCase: bool) -> bool
        """
        pass

    def StartsWith(self, handle, value, ignoreCase=None):
        """
        StartsWith(self: MetadataStringComparer, handle: StringHandle, value: str) -> bool
        StartsWith(self: MetadataStringComparer, handle: StringHandle, value: str, ignoreCase: bool) -> bool
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass


class MetadataStringDecoder(object):
    """
    Provides the System.Reflection.Metadata.MetadataReader with a custom mechanism for decoding byte sequences in metadata that represent text.
    
    MetadataStringDecoder(encoding: Encoding)
    """
    def GetString(self, bytes, byteCount):
        """
        GetString(self: MetadataStringDecoder, bytes: Byte*, byteCount: int) -> str
        
            Obtains strings for byte sequences in metadata. Override this to cache strings if required. Otherwise, it is implemented by forwarding straight to 
             System.Reflection.Metadata.MetadataStringDecoder.Encoding and every call will allocate a new string.
        
        
            bytes: Pointer to bytes to decode.
            byteCount: Number of bytes to decode.
            Returns: The decoded string.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, encoding):
        """ __new__(cls: type, encoding: Encoding) """
        pass

    Encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the encoding used by this instance.

Get: Encoding(self: MetadataStringDecoder) -> Encoding

"""


    DefaultUTF8 = None


class MethodBodyBlock(object):
    # no doc
    @staticmethod
    def Create(reader):
        """ Create(reader: BlobReader) -> MethodBodyBlock """
        pass

    def GetILBytes(self):
        """ GetILBytes(self: MethodBodyBlock) -> Array[Byte] """
        pass

    def GetILContent(self):
        """ GetILContent(self: MethodBodyBlock) -> ImmutableArray[Byte] """
        pass

    def GetILReader(self):
        """ GetILReader(self: MethodBodyBlock) -> BlobReader """
        pass

    ExceptionRegions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionRegions(self: MethodBodyBlock) -> ImmutableArray[ExceptionRegion]

"""

    LocalSignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalSignature(self: MethodBodyBlock) -> StandaloneSignatureHandle

"""

    LocalVariablesInitialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalVariablesInitialized(self: MethodBodyBlock) -> bool

"""

    MaxStack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxStack(self: MethodBodyBlock) -> int

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size of the method body, including the header, IL, and exception regions.

Get: Size(self: MethodBodyBlock) -> int

"""



class MethodDebugInformation(object):
    """ Provides debug information associated with a method definition. This information is stored in debug metadata. """
    def GetSequencePoints(self):
        """
        GetSequencePoints(self: MethodDebugInformation) -> SequencePointCollection
        
            Returns a collection of sequence points decoded from System.Reflection.Metadata.MethodDebugInformation.SequencePointsBlob.
            Returns: A collection of sequence points.
        """
        pass

    def GetStateMachineKickoffMethod(self):
        """
        GetStateMachineKickoffMethod(self: MethodDebugInformation) -> MethodDefinitionHandle
        
            Returns the kickoff method of the state machine.
            Returns: The kickoff method of the state machine, if the method is a MoveNext method of a state machine. Otherwise, it returns a handle whose 
             System.Reflection.Metadata.MethodDefinitionHandle.IsNil property is ue..
        """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the handle of the single document containing all sequence points of the method.

Get: Document(self: MethodDebugInformation) -> DocumentHandle

"""

    LocalSignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a local signature handle.

Get: LocalSignature(self: MethodDebugInformation) -> StandaloneSignatureHandle

"""

    SequencePointsBlob = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns a blob encoding sequence points.

Get: SequencePointsBlob(self: MethodDebugInformation) -> BlobHandle

"""



class MethodDebugInformationHandle(object, IEquatable[MethodDebugInformationHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: MethodDebugInformationHandle, obj: object) -> bool
        Equals(self: MethodDebugInformationHandle, other: MethodDebugInformationHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MethodDebugInformationHandle) -> int """
        pass

    def ToDefinitionHandle(self):
        """
        ToDefinitionHandle(self: MethodDebugInformationHandle) -> MethodDefinitionHandle
        
            Returns a handle to a System.Reflection.Metadata.MethodDefinition that corresponds to this handle.
            Returns: A method definition handle that corresponds to this handle.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: MethodDebugInformationHandle) -> bool

"""



class MethodDebugInformationHandleCollection(object, IReadOnlyCollection[MethodDebugInformationHandle], IEnumerable[MethodDebugInformationHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: MethodDebugInformationHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MethodDebugInformationHandle](enumerable: IEnumerable[MethodDebugInformationHandle], value: MethodDebugInformationHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: MethodDebugInformationHandleCollection) -> int

"""


    Enumerator = None


class MethodDefinition(object):
    # no doc
    def DecodeSignature(self, provider, genericContext):
        """ DecodeSignature[(TType, TGenericContext)](self: MethodDefinition, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> MethodSignature[TType] """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: MethodDefinition) -> CustomAttributeHandleCollection """
        pass

    def GetDeclarativeSecurityAttributes(self):
        """ GetDeclarativeSecurityAttributes(self: MethodDefinition) -> DeclarativeSecurityAttributeHandleCollection """
        pass

    def GetDeclaringType(self):
        """ GetDeclaringType(self: MethodDefinition) -> TypeDefinitionHandle """
        pass

    def GetGenericParameters(self):
        """ GetGenericParameters(self: MethodDefinition) -> GenericParameterHandleCollection """
        pass

    def GetImport(self):
        """ GetImport(self: MethodDefinition) -> MethodImport """
        pass

    def GetParameters(self):
        """ GetParameters(self: MethodDefinition) -> ParameterHandleCollection """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: MethodDefinition) -> MethodAttributes

"""

    ImplAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImplAttributes(self: MethodDefinition) -> MethodImplAttributes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MethodDefinition) -> StringHandle

"""

    RelativeVirtualAddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeVirtualAddress(self: MethodDefinition) -> int

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Signature(self: MethodDefinition) -> BlobHandle

"""



class MethodDefinitionHandle(object, IEquatable[MethodDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: MethodDefinitionHandle, obj: object) -> bool
        Equals(self: MethodDefinitionHandle, other: MethodDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MethodDefinitionHandle) -> int """
        pass

    def ToDebugInformationHandle(self):
        """
        ToDebugInformationHandle(self: MethodDefinitionHandle) -> MethodDebugInformationHandle
        
            Returns a handle to a System.Reflection.Metadata.MethodDebugInformation that corresponds to this handle.
            Returns: A method debug information handle that corresponds to this handle.
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: MethodDefinitionHandle) -> bool

"""



class MethodDefinitionHandleCollection(object, IReadOnlyCollection[MethodDefinitionHandle], IEnumerable[MethodDefinitionHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: MethodDefinitionHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MethodDefinitionHandle](enumerable: IEnumerable[MethodDefinitionHandle], value: MethodDefinitionHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: MethodDefinitionHandleCollection) -> int

"""


    Enumerator = None


class MethodImplementation(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: MethodImplementation) -> CustomAttributeHandleCollection """
        pass

    MethodBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodBody(self: MethodImplementation) -> EntityHandle

"""

    MethodDeclaration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MethodDeclaration(self: MethodImplementation) -> EntityHandle

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: MethodImplementation) -> TypeDefinitionHandle

"""



class MethodImplementationHandle(object, IEquatable[MethodImplementationHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: MethodImplementationHandle, obj: object) -> bool
        Equals(self: MethodImplementationHandle, other: MethodImplementationHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MethodImplementationHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: MethodImplementationHandle) -> bool

"""



class MethodImplementationHandleCollection(object, IReadOnlyCollection[MethodImplementationHandle], IEnumerable[MethodImplementationHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: MethodImplementationHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MethodImplementationHandle](enumerable: IEnumerable[MethodImplementationHandle], value: MethodImplementationHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: MethodImplementationHandleCollection) -> int

"""


    Enumerator = None


class MethodImport(object):
    # no doc
    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: MethodImport) -> MethodImportAttributes

"""

    Module = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Module(self: MethodImport) -> ModuleReferenceHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MethodImport) -> StringHandle

"""



class MethodSignature(object):
    """ MethodSignature[TType](header: SignatureHeader, returnType: TType, requiredParameterCount: int, genericParameterCount: int, parameterTypes: ImmutableArray[TType]) """
    @staticmethod # known case of __new__
    def __new__(self, header, returnType, requiredParameterCount, genericParameterCount, parameterTypes):
        """
        __new__(cls: type, header: SignatureHeader, returnType: TType, requiredParameterCount: int, genericParameterCount: int, parameterTypes: ImmutableArray[TType])
        __new__[MethodSignature`1]() -> MethodSignature[TType]
        """
        pass

    GenericParameterCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of generic type parameters for the method.

Get: GenericParameterCount(self: MethodSignature[TType]) -> int

"""

    Header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the information in the leading byte of the signature (kind, calling convention, flags).

Get: Header(self: MethodSignature[TType]) -> SignatureHeader

"""

    ParameterTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the method's parameter types.

Get: ParameterTypes(self: MethodSignature[TType]) -> ImmutableArray[TType]

"""

    RequiredParameterCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of parameters that are required for the method.

Get: RequiredParameterCount(self: MethodSignature[TType]) -> int

"""

    ReturnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the return type of the method.

Get: ReturnType(self: MethodSignature[TType]) -> TType

"""



class MethodSpecification(object):
    # no doc
    def DecodeSignature(self, provider, genericContext):
        """ DecodeSignature[(TType, TGenericContext)](self: MethodSpecification, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> ImmutableArray[TType] """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: MethodSpecification) -> CustomAttributeHandleCollection """
        pass

    Method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a thodDef or mberRef handle specifying which generic method this instance refers to (that is, which generic method it is an instantiation of).

Get: Method(self: MethodSpecification) -> EntityHandle

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle to the signature blob.

Get: Signature(self: MethodSpecification) -> BlobHandle

"""



class MethodSpecificationHandle(object, IEquatable[MethodSpecificationHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: MethodSpecificationHandle, obj: object) -> bool
        Equals(self: MethodSpecificationHandle, other: MethodSpecificationHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MethodSpecificationHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: MethodSpecificationHandle) -> bool

"""



class ModuleDefinition(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: ModuleDefinition) -> CustomAttributeHandleCollection """
        pass

    BaseGenerationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseGenerationId(self: ModuleDefinition) -> GuidHandle

"""

    Generation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Generation(self: ModuleDefinition) -> int

"""

    GenerationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenerationId(self: ModuleDefinition) -> GuidHandle

"""

    Mvid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mvid(self: ModuleDefinition) -> GuidHandle

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ModuleDefinition) -> StringHandle

"""



class ModuleDefinitionHandle(object, IEquatable[ModuleDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ModuleDefinitionHandle, obj: object) -> bool
        Equals(self: ModuleDefinitionHandle, other: ModuleDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ModuleDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ModuleDefinitionHandle) -> bool

"""



class ModuleReference(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: ModuleReference) -> CustomAttributeHandleCollection """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ModuleReference) -> StringHandle

"""



class ModuleReferenceHandle(object, IEquatable[ModuleReferenceHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ModuleReferenceHandle, obj: object) -> bool
        Equals(self: ModuleReferenceHandle, other: ModuleReferenceHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ModuleReferenceHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ModuleReferenceHandle) -> bool

"""



class NamespaceDefinition(object):
    # no doc
    ExportedTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all exported types that reside directly in a namespace.

Get: ExportedTypes(self: NamespaceDefinition) -> ImmutableArray[ExportedTypeHandle]

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unqualified name of the namespace definition.

Get: Name(self: NamespaceDefinition) -> StringHandle

"""

    NamespaceDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the namespace definitions that are direct children of the current namespace definition.

Get: NamespaceDefinitions(self: NamespaceDefinition) -> ImmutableArray[NamespaceDefinitionHandle]

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent namespace.

Get: Parent(self: NamespaceDefinition) -> NamespaceDefinitionHandle

"""

    TypeDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets all type definitions that reside directly in a namespace.

Get: TypeDefinitions(self: NamespaceDefinition) -> ImmutableArray[TypeDefinitionHandle]

"""



class NamespaceDefinitionHandle(object, IEquatable[NamespaceDefinitionHandle]):
    """ Provides a handle to a namespace definition. """
    def Equals(self, *__args):
        """
        Equals(self: NamespaceDefinitionHandle, obj: object) -> bool
        Equals(self: NamespaceDefinitionHandle, other: NamespaceDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: NamespaceDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: NamespaceDefinitionHandle) -> bool

"""



class Parameter(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: Parameter) -> CustomAttributeHandleCollection """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: Parameter) -> ConstantHandle """
        pass

    def GetMarshallingDescriptor(self):
        """ GetMarshallingDescriptor(self: Parameter) -> BlobHandle """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: Parameter) -> ParameterAttributes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Parameter) -> StringHandle

"""

    SequenceNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SequenceNumber(self: Parameter) -> int

"""



class ParameterHandle(object, IEquatable[ParameterHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: ParameterHandle, obj: object) -> bool
        Equals(self: ParameterHandle, other: ParameterHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: ParameterHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: ParameterHandle) -> bool

"""



class ParameterHandleCollection(object, IReadOnlyCollection[ParameterHandle], IEnumerable[ParameterHandle], IEnumerable):
    """ Contains a collection of parameters of a specified method. """
    def GetEnumerator(self):
        """ GetEnumerator(self: ParameterHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParameterHandle](enumerable: IEnumerable[ParameterHandle], value: ParameterHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: ParameterHandleCollection) -> int

"""


    Enumerator = None


class PEReaderExtensions(object):
    # no doc
    @staticmethod
    def GetMetadataReader(peReader, options=None, utf8Decoder=None):
        """
        GetMetadataReader(peReader: PEReader) -> MetadataReader
        
            Gets a System.Reflection.Metadata.MetadataReader from a System.Reflection.PortableExecutable.PEReader.
        
            peReader: The current System.Reflection.PortableExecutable.PEReader instance.
            Returns: A metadata reader.
        GetMetadataReader(peReader: PEReader, options: MetadataReaderOptions) -> MetadataReader
        
            Gets a  metadata reader with the specified metadata reading configuration from a System.Reflection.PortableExecutable.PEReader.
        
            peReader: The current System.Reflection.PortableExecutable.PEReader instance.
            options: An  enumeration value indicating the metadata reading configuration.
            Returns: A  metadata reader with the specified metadata reading configuration.
        GetMetadataReader(peReader: PEReader, options: MetadataReaderOptions, utf8Decoder: MetadataStringDecoder) -> MetadataReader
        
            Gets a metadata reader with the specified metadata reading configuration and encoding configuration from a System.Reflection.PortableExecutable.PEReader.
        
            peReader: The current System.Reflection.PortableExecutable.PEReader instance.
            options: An enumeration value indicating the metadata reading configuration.
            utf8Decoder: A metadata string decoder with the encoding configuration.
            Returns: >A metadata reader with the specified metadata reading configuration and encoding configuration.
        """
        pass

    @staticmethod
    def GetMethodBody(peReader, relativeVirtualAddress):
        """
        GetMethodBody(peReader: PEReader, relativeVirtualAddress: int) -> MethodBodyBlock
        
            Returns a body block of a method with the specified Relative Virtual Address (RVA);
        
            peReader: The current System.Reflection.PortableExecutable.PEReader instance.
            relativeVirtualAddress: The Relative Virtual Address (RVA).
            Returns: A method block body instance.
        """
        pass

    __all__ = [
        'GetMetadataReader',
        'GetMethodBody',
    ]


class PrimitiveSerializationTypeCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define the type codes used to encode types of primitive values in a System.Reflection.Metadata.CustomAttribute value blob.
    
    enum PrimitiveSerializationTypeCode, values: Boolean (2), Byte (5), Char (3), Double (13), Int16 (6), Int32 (8), Int64 (10), SByte (4), Single (12), String (14), UInt16 (7), UInt32 (9), UInt64 (11)
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

    Boolean = None
    Byte = None
    Char = None
    Double = None
    Int16 = None
    Int32 = None
    Int64 = None
    SByte = None
    Single = None
    String = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    value__ = None


class PrimitiveTypeCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define primitive types found in metadata signatures.
    
    enum PrimitiveTypeCode, values: Boolean (2), Byte (5), Char (3), Double (13), Int16 (6), Int32 (8), Int64 (10), IntPtr (24), Object (28), SByte (4), Single (12), String (14), TypedReference (22), UInt16 (7), UInt32 (9), UInt64 (11), UIntPtr (25), Void (1)
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

    Boolean = None
    Byte = None
    Char = None
    Double = None
    Int16 = None
    Int32 = None
    Int64 = None
    IntPtr = None
    Object = None
    SByte = None
    Single = None
    String = None
    TypedReference = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    UIntPtr = None
    value__ = None
    Void = None


class PropertyAccessors(object):
    # no doc
    Getter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Getter(self: PropertyAccessors) -> MethodDefinitionHandle

"""

    Others = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Others(self: PropertyAccessors) -> ImmutableArray[MethodDefinitionHandle]

"""

    Setter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Setter(self: PropertyAccessors) -> MethodDefinitionHandle

"""



class PropertyDefinition(object):
    # no doc
    def DecodeSignature(self, provider, genericContext):
        """ DecodeSignature[(TType, TGenericContext)](self: PropertyDefinition, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> MethodSignature[TType] """
        pass

    def GetAccessors(self):
        """ GetAccessors(self: PropertyDefinition) -> PropertyAccessors """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: PropertyDefinition) -> CustomAttributeHandleCollection """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: PropertyDefinition) -> ConstantHandle """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: PropertyDefinition) -> PropertyAttributes

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PropertyDefinition) -> StringHandle

"""

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Signature(self: PropertyDefinition) -> BlobHandle

"""



class PropertyDefinitionHandle(object, IEquatable[PropertyDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: PropertyDefinitionHandle, obj: object) -> bool
        Equals(self: PropertyDefinitionHandle, other: PropertyDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PropertyDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: PropertyDefinitionHandle) -> bool

"""



class PropertyDefinitionHandleCollection(object, IReadOnlyCollection[PropertyDefinitionHandle], IEnumerable[PropertyDefinitionHandle], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: PropertyDefinitionHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PropertyDefinitionHandle](enumerable: IEnumerable[PropertyDefinitionHandle], value: PropertyDefinitionHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: PropertyDefinitionHandleCollection) -> int

"""


    Enumerator = None


class ReservedBlob(object):
    # no doc
    def CreateWriter(self):
        """
        CreateWriter(self: ReservedBlob[THandle]) -> BlobWriter
        
            Returns a System.Reflection.Metadata.BlobWriter to be used to update the content.
            Returns: A blob writer to be used to update the content.
        """
        pass

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: ReservedBlob[THandle]) -> Blob

"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the reserved blob handle.

Get: Handle(self: ReservedBlob[THandle]) -> THandle

"""



class SequencePoint(object, IEquatable[SequencePoint]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: SequencePoint, obj: object) -> bool
        Equals(self: SequencePoint, other: SequencePoint) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: SequencePoint) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
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

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: SequencePoint) -> DocumentHandle

"""

    EndColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndColumn(self: SequencePoint) -> int

"""

    EndLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndLine(self: SequencePoint) -> int

"""

    IsHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHidden(self: SequencePoint) -> bool

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: SequencePoint) -> int

"""

    StartColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartColumn(self: SequencePoint) -> int

"""

    StartLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartLine(self: SequencePoint) -> int

"""


    HiddenLine = 16707566


class SequencePointCollection(object, IEnumerable[SequencePoint], IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: SequencePointCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SequencePoint](enumerable: IEnumerable[SequencePoint], value: SequencePoint) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Enumerator = None


class SerializationTypeCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies type codes used to encode the types of values in a System.Reflection.Metadata.CustomAttributeValue blob.
    
    enum SerializationTypeCode, values: Boolean (2), Byte (5), Char (3), Double (13), Enum (85), Int16 (6), Int32 (8), Int64 (10), Invalid (0), SByte (4), Single (12), String (14), SZArray (29), TaggedObject (81), Type (80), UInt16 (7), UInt32 (9), UInt64 (11)
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

    Boolean = None
    Byte = None
    Char = None
    Double = None
    Enum = None
    Int16 = None
    Int32 = None
    Int64 = None
    Invalid = None
    SByte = None
    Single = None
    String = None
    SZArray = None
    TaggedObject = None
    Type = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    value__ = None


class SignatureAttributes(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies additional flags that can be applied to method signatures. The underlying values of the fields in this type correspond to the representation in the leading signature byte represented by a System.Reflection.Metadata.SignatureHeader structure.
    
    enum (flags) SignatureAttributes, values: ExplicitThis (64), Generic (16), Instance (32), None (0)
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

    ExplicitThis = None
    Generic = None
    Instance = None
    None = None
    value__ = None


class SignatureCallingConvention(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies how arguments in a given signature are passed from the caller to the callee. The underlying values of the fields in this type correspond to the representation in the leading signature byte represented by a System.Reflection.Metadata.SignatureHeader structure.
    
    enum SignatureCallingConvention, values: CDecl (1), Default (0), FastCall (4), StdCall (2), ThisCall (3), Unmanaged (9), VarArgs (5)
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

    CDecl = None
    Default = None
    FastCall = None
    StdCall = None
    ThisCall = None
    Unmanaged = None
    value__ = None
    VarArgs = None


class SignatureHeader(object, IEquatable[SignatureHeader]):
    """
    Represents the signature characteristics specified by the leading byte of signature blobs.
    
    SignatureHeader(rawValue: Byte)
    SignatureHeader(kind: SignatureKind, convention: SignatureCallingConvention, attributes: SignatureAttributes)
    """
    def Equals(self, *__args):
        """
        Equals(self: SignatureHeader, obj: object) -> bool
        
            Compares the specified object with this System.Reflection.Metadata.SignatureHeader for equality.
        
            obj: The object to compare.
            Returns: ue if the objects are equal; otherwise, lse.
        Equals(self: SignatureHeader, other: SignatureHeader) -> bool
        
            Compares two System.Reflection.Metadata.SignatureHeader values for equality.
        
            other: The value to compare.
            Returns: ue if the values are equal; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: SignatureHeader) -> int
        
            Gets a hash code for the current object.
            Returns: A hash code for the current object.
        """
        pass

    def ToString(self):
        """
        ToString(self: SignatureHeader) -> str
        
            Returns a string that represents the current object.
            Returns: A string that represents the current object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rawValue: Byte)
        __new__(cls: type, kind: SignatureKind, convention: SignatureCallingConvention, attributes: SignatureAttributes)
        __new__[SignatureHeader]() -> SignatureHeader
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the signature attributes.

Get: Attributes(self: SignatureHeader) -> SignatureAttributes

"""

    CallingConvention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the calling convention.

Get: CallingConvention(self: SignatureHeader) -> SignatureCallingConvention

"""

    HasExplicitThis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Reflection.Metadata.SignatureHeader structure has the System.Reflection.Metadata.SignatureAttributes.ExplicitThis signature attribute.

Get: HasExplicitThis(self: SignatureHeader) -> bool

"""

    IsGeneric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Reflection.Metadata.SignatureHeader structure has the System.Reflection.Metadata.SignatureAttributes.Generic signature attribute.

Get: IsGeneric(self: SignatureHeader) -> bool

"""

    IsInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this System.Reflection.Metadata.SignatureHeader structure has the System.Reflection.Metadata.SignatureAttributes.Instance signature attribute.

Get: IsInstance(self: SignatureHeader) -> bool

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the signature kind.

Get: Kind(self: SignatureHeader) -> SignatureKind

"""

    RawValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the raw value of the header byte.

Get: RawValue(self: SignatureHeader) -> Byte

"""


    CallingConventionOrKindMask = None


class SignatureKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the signature kind. The underlying values of the fields in this type correspond to the representation in the leading signature byte represented by a System.Reflection.Metadata.SignatureHeader structure.
    
    enum SignatureKind, values: Field (6), LocalVariables (7), Method (0), MethodSpecification (10), Property (8)
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

    Field = None
    LocalVariables = None
    Method = None
    MethodSpecification = None
    Property = None
    value__ = None


class SignatureTypeCode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies constants that define type codes used in signature encoding.
    
    enum SignatureTypeCode, values: Array (20), Boolean (2), ByReference (16), Byte (5), Char (3), Double (13), FunctionPointer (27), GenericMethodParameter (30), GenericTypeInstance (21), GenericTypeParameter (19), Int16 (6), Int32 (8), Int64 (10), IntPtr (24), Invalid (0), Object (28), OptionalModifier (32), Pinned (69), Pointer (15), RequiredModifier (31), SByte (4), Sentinel (65), Single (12), String (14), SZArray (29), TypedReference (22), TypeHandle (64), UInt16 (7), UInt32 (9), UInt64 (11), UIntPtr (25), Void (1)
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

    Array = None
    Boolean = None
    ByReference = None
    Byte = None
    Char = None
    Double = None
    FunctionPointer = None
    GenericMethodParameter = None
    GenericTypeInstance = None
    GenericTypeParameter = None
    Int16 = None
    Int32 = None
    Int64 = None
    IntPtr = None
    Invalid = None
    Object = None
    OptionalModifier = None
    Pinned = None
    Pointer = None
    RequiredModifier = None
    SByte = None
    Sentinel = None
    Single = None
    String = None
    SZArray = None
    TypedReference = None
    TypeHandle = None
    UInt16 = None
    UInt32 = None
    UInt64 = None
    UIntPtr = None
    value__ = None
    Void = None


class SignatureTypeKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates the type definition of the signature.
    
    enum SignatureTypeKind, values: Class (18), Unknown (0), ValueType (17)
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

    Class = None
    Unknown = None
    ValueType = None
    value__ = None


class StandaloneSignature(object):
    # no doc
    def DecodeLocalSignature(self, provider, genericContext):
        """ DecodeLocalSignature[(TType, TGenericContext)](self: StandaloneSignature, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> ImmutableArray[TType] """
        pass

    def DecodeMethodSignature(self, provider, genericContext):
        """ DecodeMethodSignature[(TType, TGenericContext)](self: StandaloneSignature, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> MethodSignature[TType] """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: StandaloneSignature) -> CustomAttributeHandleCollection """
        pass

    def GetKind(self):
        """
        GetKind(self: StandaloneSignature) -> StandaloneSignatureKind
        
            Determines the kind of signature, which can be System.Reflection.Metadata.SignatureKind.Method or System.Reflection.Metadata.SignatureKind.LocalVariables.
            Returns: An enumeration value that indicates the signature kind.
        """
        pass

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a handle to the signature blob.

Get: Signature(self: StandaloneSignature) -> BlobHandle

"""



class StandaloneSignatureHandle(object, IEquatable[StandaloneSignatureHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: StandaloneSignatureHandle, obj: object) -> bool
        Equals(self: StandaloneSignatureHandle, other: StandaloneSignatureHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: StandaloneSignatureHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: StandaloneSignatureHandle) -> bool

"""



class StandaloneSignatureKind(Enum, IComparable, IFormattable, IConvertible):
    """
    Indicates whether a System.Reflection.Metadata.StandaloneSignature represents a standalone method or local variable signature.
    
    enum StandaloneSignatureKind, values: LocalVariables (1), Method (0)
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

    LocalVariables = None
    Method = None
    value__ = None


class StringHandle(object, IEquatable[StringHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: StringHandle, obj: object) -> bool
        Equals(self: StringHandle, other: StringHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: StringHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: StringHandle) -> bool

"""



class TypeDefinition(object):
    # no doc
    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: TypeDefinition) -> CustomAttributeHandleCollection """
        pass

    def GetDeclarativeSecurityAttributes(self):
        """ GetDeclarativeSecurityAttributes(self: TypeDefinition) -> DeclarativeSecurityAttributeHandleCollection """
        pass

    def GetDeclaringType(self):
        """
        GetDeclaringType(self: TypeDefinition) -> TypeDefinitionHandle
        
            Returns the enclosing type of a specified nested type.
            Returns: The enclosing type of the specified nested type, or a handle a handle whose System.Reflection.Metadata.TypeDefinitionHandle.IsNil property is ue if the type is not nested.
        """
        pass

    def GetEvents(self):
        """ GetEvents(self: TypeDefinition) -> EventDefinitionHandleCollection """
        pass

    def GetFields(self):
        """ GetFields(self: TypeDefinition) -> FieldDefinitionHandleCollection """
        pass

    def GetGenericParameters(self):
        """ GetGenericParameters(self: TypeDefinition) -> GenericParameterHandleCollection """
        pass

    def GetInterfaceImplementations(self):
        """ GetInterfaceImplementations(self: TypeDefinition) -> InterfaceImplementationHandleCollection """
        pass

    def GetLayout(self):
        """ GetLayout(self: TypeDefinition) -> TypeLayout """
        pass

    def GetMethodImplementations(self):
        """ GetMethodImplementations(self: TypeDefinition) -> MethodImplementationHandleCollection """
        pass

    def GetMethods(self):
        """ GetMethods(self: TypeDefinition) -> MethodDefinitionHandleCollection """
        pass

    def GetNestedTypes(self):
        """
        GetNestedTypes(self: TypeDefinition) -> ImmutableArray[TypeDefinitionHandle]
        
            Returns an array of types nested in the specified type.
            Returns: An immutable array of type definition handles that represent types nested in the specified type.
        """
        pass

    def GetProperties(self):
        """ GetProperties(self: TypeDefinition) -> PropertyDefinitionHandleCollection """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: TypeDefinition) -> TypeAttributes

"""

    BaseType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base type of the type definition: either System.Reflection.Metadata.TypeSpecificationHandle, System.Reflection.Metadata.TypeReferenceHandle or System.Reflection.Metadata.TypeDefinitionHandle.

Get: BaseType(self: TypeDefinition) -> EntityHandle

"""

    IsNested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this is a nested type.

Get: IsNested(self: TypeDefinition) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the type.

Get: Name(self: TypeDefinition) -> StringHandle

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full name of the namespace where the type is defined.

Get: Namespace(self: TypeDefinition) -> StringHandle

"""

    NamespaceDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the definition handle of the namespace where the type is defined.

Get: NamespaceDefinition(self: TypeDefinition) -> NamespaceDefinitionHandle

"""



class TypeDefinitionHandle(object, IEquatable[TypeDefinitionHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: TypeDefinitionHandle, obj: object) -> bool
        Equals(self: TypeDefinitionHandle, other: TypeDefinitionHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TypeDefinitionHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: TypeDefinitionHandle) -> bool

"""



class TypeDefinitionHandleCollection(object, IReadOnlyCollection[TypeDefinitionHandle], IEnumerable[TypeDefinitionHandle], IEnumerable):
    """ Contains a collection of System.Reflection.Metadata.TypeDefinitionHandle instances. """
    def GetEnumerator(self):
        """ GetEnumerator(self: TypeDefinitionHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TypeDefinitionHandle](enumerable: IEnumerable[TypeDefinitionHandle], value: TypeDefinitionHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: TypeDefinitionHandleCollection) -> int

"""


    Enumerator = None


class TypeLayout(object):
    """ TypeLayout(size: int, packingSize: int) """
    @staticmethod # known case of __new__
    def __new__(self, size, packingSize):
        """
        __new__(cls: type, size: int, packingSize: int)
        __new__[TypeLayout]() -> TypeLayout
        """
        pass

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefault(self: TypeLayout) -> bool

"""

    PackingSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PackingSize(self: TypeLayout) -> int

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: TypeLayout) -> int

"""



class TypeReference(object):
    # no doc
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the target type.

Get: Name(self: TypeReference) -> StringHandle

"""

    Namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the full name of the namespace where the target type is defined.

Get: Namespace(self: TypeReference) -> StringHandle

"""

    ResolutionScope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the resolution scope in which the target type is defined and is uniquely identified by the specified System.Reflection.Metadata.TypeReference.Namespace and System.Reflection.Metadata.TypeReference.Name.

Get: ResolutionScope(self: TypeReference) -> EntityHandle

"""



class TypeReferenceHandle(object, IEquatable[TypeReferenceHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: TypeReferenceHandle, obj: object) -> bool
        Equals(self: TypeReferenceHandle, other: TypeReferenceHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TypeReferenceHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: TypeReferenceHandle) -> bool

"""



class TypeReferenceHandleCollection(object, IReadOnlyCollection[TypeReferenceHandle], IEnumerable[TypeReferenceHandle], IEnumerable):
    """ Contains a collection of System.Reflection.Metadata.TypeReferenceHandle instances. """
    def GetEnumerator(self):
        """ GetEnumerator(self: TypeReferenceHandleCollection) -> Enumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TypeReferenceHandle](enumerable: IEnumerable[TypeReferenceHandle], value: TypeReferenceHandle) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: TypeReferenceHandleCollection) -> int

"""


    Enumerator = None


class TypeSpecification(object):
    # no doc
    def DecodeSignature(self, provider, genericContext):
        """ DecodeSignature[(TType, TGenericContext)](self: TypeSpecification, provider: ISignatureTypeProvider[TType, TGenericContext], genericContext: TGenericContext) -> TType """
        pass

    def GetCustomAttributes(self):
        """ GetCustomAttributes(self: TypeSpecification) -> CustomAttributeHandleCollection """
        pass

    Signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Signature(self: TypeSpecification) -> BlobHandle

"""



class TypeSpecificationHandle(object, IEquatable[TypeSpecificationHandle]):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: TypeSpecificationHandle, obj: object) -> bool
        Equals(self: TypeSpecificationHandle, other: TypeSpecificationHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TypeSpecificationHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: TypeSpecificationHandle) -> bool

"""



class UserStringHandle(object, IEquatable[UserStringHandle]):
    """ Represents a handle to the user string heap. """
    def Equals(self, *__args):
        """
        Equals(self: UserStringHandle, obj: object) -> bool
        Equals(self: UserStringHandle, other: UserStringHandle) -> bool
        
            Indicates whether the current object is equal to another object of the same type.
        
            other: An object to compare with this object.
            Returns: ue if the current object is equal to the other parameter; otherwise, lse.
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: UserStringHandle) -> int """
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

    IsNil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNil(self: UserStringHandle) -> bool

"""



# variables with complex values
