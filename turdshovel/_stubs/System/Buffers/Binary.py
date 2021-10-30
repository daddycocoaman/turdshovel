# encoding: utf-8
# module System.Buffers.Binary calls itself Binary
# from System.Memory, Version=4.0.1.1, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BinaryPrimitives(object):
    # no doc
    @staticmethod
    def ReadInt16BigEndian(source):
        """ ReadInt16BigEndian(source: ReadOnlySpan[Byte]) -> Int16 """
        pass

    @staticmethod
    def ReadInt16LittleEndian(source):
        """ ReadInt16LittleEndian(source: ReadOnlySpan[Byte]) -> Int16 """
        pass

    @staticmethod
    def ReadInt32BigEndian(source):
        """ ReadInt32BigEndian(source: ReadOnlySpan[Byte]) -> int """
        pass

    @staticmethod
    def ReadInt32LittleEndian(source):
        """ ReadInt32LittleEndian(source: ReadOnlySpan[Byte]) -> int """
        pass

    @staticmethod
    def ReadInt64BigEndian(source):
        """ ReadInt64BigEndian(source: ReadOnlySpan[Byte]) -> Int64 """
        pass

    @staticmethod
    def ReadInt64LittleEndian(source):
        """ ReadInt64LittleEndian(source: ReadOnlySpan[Byte]) -> Int64 """
        pass

    @staticmethod
    def ReadUInt16BigEndian(source):
        """ ReadUInt16BigEndian(source: ReadOnlySpan[Byte]) -> UInt16 """
        pass

    @staticmethod
    def ReadUInt16LittleEndian(source):
        """ ReadUInt16LittleEndian(source: ReadOnlySpan[Byte]) -> UInt16 """
        pass

    @staticmethod
    def ReadUInt32BigEndian(source):
        """ ReadUInt32BigEndian(source: ReadOnlySpan[Byte]) -> UInt32 """
        pass

    @staticmethod
    def ReadUInt32LittleEndian(source):
        """ ReadUInt32LittleEndian(source: ReadOnlySpan[Byte]) -> UInt32 """
        pass

    @staticmethod
    def ReadUInt64BigEndian(source):
        """ ReadUInt64BigEndian(source: ReadOnlySpan[Byte]) -> UInt64 """
        pass

    @staticmethod
    def ReadUInt64LittleEndian(source):
        """ ReadUInt64LittleEndian(source: ReadOnlySpan[Byte]) -> UInt64 """
        pass

    @staticmethod
    def ReverseEndianness(value):
        """
        ReverseEndianness(value: SByte) -> SByte
        ReverseEndianness(value: Int16) -> Int16
        ReverseEndianness(value: int) -> int
        ReverseEndianness(value: Int64) -> Int64
        ReverseEndianness(value: Byte) -> Byte
        ReverseEndianness(value: UInt16) -> UInt16
        ReverseEndianness(value: UInt32) -> UInt32
        ReverseEndianness(value: UInt64) -> UInt64
        """
        pass

    @staticmethod
    def TryReadInt16BigEndian(source, value):
        """ TryReadInt16BigEndian(source: ReadOnlySpan[Byte]) -> (bool, Int16) """
        pass

    @staticmethod
    def TryReadInt16LittleEndian(source, value):
        """ TryReadInt16LittleEndian(source: ReadOnlySpan[Byte]) -> (bool, Int16) """
        pass

    @staticmethod
    def TryReadInt32BigEndian(source, value):
        """ TryReadInt32BigEndian(source: ReadOnlySpan[Byte]) -> (bool, int) """
        pass

    @staticmethod
    def TryReadInt32LittleEndian(source, value):
        """ TryReadInt32LittleEndian(source: ReadOnlySpan[Byte]) -> (bool, int) """
        pass

    @staticmethod
    def TryReadInt64BigEndian(source, value):
        """ TryReadInt64BigEndian(source: ReadOnlySpan[Byte]) -> (bool, Int64) """
        pass

    @staticmethod
    def TryReadInt64LittleEndian(source, value):
        """ TryReadInt64LittleEndian(source: ReadOnlySpan[Byte]) -> (bool, Int64) """
        pass

    @staticmethod
    def TryReadUInt16BigEndian(source, value):
        """ TryReadUInt16BigEndian(source: ReadOnlySpan[Byte]) -> (bool, UInt16) """
        pass

    @staticmethod
    def TryReadUInt16LittleEndian(source, value):
        """ TryReadUInt16LittleEndian(source: ReadOnlySpan[Byte]) -> (bool, UInt16) """
        pass

    @staticmethod
    def TryReadUInt32BigEndian(source, value):
        """ TryReadUInt32BigEndian(source: ReadOnlySpan[Byte]) -> (bool, UInt32) """
        pass

    @staticmethod
    def TryReadUInt32LittleEndian(source, value):
        """ TryReadUInt32LittleEndian(source: ReadOnlySpan[Byte]) -> (bool, UInt32) """
        pass

    @staticmethod
    def TryReadUInt64BigEndian(source, value):
        """ TryReadUInt64BigEndian(source: ReadOnlySpan[Byte]) -> (bool, UInt64) """
        pass

    @staticmethod
    def TryReadUInt64LittleEndian(source, value):
        """ TryReadUInt64LittleEndian(source: ReadOnlySpan[Byte]) -> (bool, UInt64) """
        pass

    @staticmethod
    def TryWriteInt16BigEndian(destination, value):
        """ TryWriteInt16BigEndian(destination: Span[Byte], value: Int16) -> bool """
        pass

    @staticmethod
    def TryWriteInt16LittleEndian(destination, value):
        """ TryWriteInt16LittleEndian(destination: Span[Byte], value: Int16) -> bool """
        pass

    @staticmethod
    def TryWriteInt32BigEndian(destination, value):
        """ TryWriteInt32BigEndian(destination: Span[Byte], value: int) -> bool """
        pass

    @staticmethod
    def TryWriteInt32LittleEndian(destination, value):
        """ TryWriteInt32LittleEndian(destination: Span[Byte], value: int) -> bool """
        pass

    @staticmethod
    def TryWriteInt64BigEndian(destination, value):
        """ TryWriteInt64BigEndian(destination: Span[Byte], value: Int64) -> bool """
        pass

    @staticmethod
    def TryWriteInt64LittleEndian(destination, value):
        """ TryWriteInt64LittleEndian(destination: Span[Byte], value: Int64) -> bool """
        pass

    @staticmethod
    def TryWriteUInt16BigEndian(destination, value):
        """ TryWriteUInt16BigEndian(destination: Span[Byte], value: UInt16) -> bool """
        pass

    @staticmethod
    def TryWriteUInt16LittleEndian(destination, value):
        """ TryWriteUInt16LittleEndian(destination: Span[Byte], value: UInt16) -> bool """
        pass

    @staticmethod
    def TryWriteUInt32BigEndian(destination, value):
        """ TryWriteUInt32BigEndian(destination: Span[Byte], value: UInt32) -> bool """
        pass

    @staticmethod
    def TryWriteUInt32LittleEndian(destination, value):
        """ TryWriteUInt32LittleEndian(destination: Span[Byte], value: UInt32) -> bool """
        pass

    @staticmethod
    def TryWriteUInt64BigEndian(destination, value):
        """ TryWriteUInt64BigEndian(destination: Span[Byte], value: UInt64) -> bool """
        pass

    @staticmethod
    def TryWriteUInt64LittleEndian(destination, value):
        """ TryWriteUInt64LittleEndian(destination: Span[Byte], value: UInt64) -> bool """
        pass

    @staticmethod
    def WriteInt16BigEndian(destination, value):
        """ WriteInt16BigEndian(destination: Span[Byte], value: Int16) """
        pass

    @staticmethod
    def WriteInt16LittleEndian(destination, value):
        """ WriteInt16LittleEndian(destination: Span[Byte], value: Int16) """
        pass

    @staticmethod
    def WriteInt32BigEndian(destination, value):
        """ WriteInt32BigEndian(destination: Span[Byte], value: int) """
        pass

    @staticmethod
    def WriteInt32LittleEndian(destination, value):
        """ WriteInt32LittleEndian(destination: Span[Byte], value: int) """
        pass

    @staticmethod
    def WriteInt64BigEndian(destination, value):
        """ WriteInt64BigEndian(destination: Span[Byte], value: Int64) """
        pass

    @staticmethod
    def WriteInt64LittleEndian(destination, value):
        """ WriteInt64LittleEndian(destination: Span[Byte], value: Int64) """
        pass

    @staticmethod
    def WriteUInt16BigEndian(destination, value):
        """ WriteUInt16BigEndian(destination: Span[Byte], value: UInt16) """
        pass

    @staticmethod
    def WriteUInt16LittleEndian(destination, value):
        """ WriteUInt16LittleEndian(destination: Span[Byte], value: UInt16) """
        pass

    @staticmethod
    def WriteUInt32BigEndian(destination, value):
        """ WriteUInt32BigEndian(destination: Span[Byte], value: UInt32) """
        pass

    @staticmethod
    def WriteUInt32LittleEndian(destination, value):
        """ WriteUInt32LittleEndian(destination: Span[Byte], value: UInt32) """
        pass

    @staticmethod
    def WriteUInt64BigEndian(destination, value):
        """ WriteUInt64BigEndian(destination: Span[Byte], value: UInt64) """
        pass

    @staticmethod
    def WriteUInt64LittleEndian(destination, value):
        """ WriteUInt64LittleEndian(destination: Span[Byte], value: UInt64) """
        pass

    __all__ = [
        'ReadInt16BigEndian',
        'ReadInt16LittleEndian',
        'ReadInt32BigEndian',
        'ReadInt32LittleEndian',
        'ReadInt64BigEndian',
        'ReadInt64LittleEndian',
        'ReadUInt16BigEndian',
        'ReadUInt16LittleEndian',
        'ReadUInt32BigEndian',
        'ReadUInt32LittleEndian',
        'ReadUInt64BigEndian',
        'ReadUInt64LittleEndian',
        'ReverseEndianness',
        'TryReadInt16BigEndian',
        'TryReadInt16LittleEndian',
        'TryReadInt32BigEndian',
        'TryReadInt32LittleEndian',
        'TryReadInt64BigEndian',
        'TryReadInt64LittleEndian',
        'TryReadUInt16BigEndian',
        'TryReadUInt16LittleEndian',
        'TryReadUInt32BigEndian',
        'TryReadUInt32LittleEndian',
        'TryReadUInt64BigEndian',
        'TryReadUInt64LittleEndian',
        'TryWriteInt16BigEndian',
        'TryWriteInt16LittleEndian',
        'TryWriteInt32BigEndian',
        'TryWriteInt32LittleEndian',
        'TryWriteInt64BigEndian',
        'TryWriteInt64LittleEndian',
        'TryWriteUInt16BigEndian',
        'TryWriteUInt16LittleEndian',
        'TryWriteUInt32BigEndian',
        'TryWriteUInt32LittleEndian',
        'TryWriteUInt64BigEndian',
        'TryWriteUInt64LittleEndian',
        'WriteInt16BigEndian',
        'WriteInt16LittleEndian',
        'WriteInt32BigEndian',
        'WriteInt32LittleEndian',
        'WriteInt64BigEndian',
        'WriteInt64LittleEndian',
        'WriteUInt16BigEndian',
        'WriteUInt16LittleEndian',
        'WriteUInt32BigEndian',
        'WriteUInt32LittleEndian',
        'WriteUInt64BigEndian',
        'WriteUInt64LittleEndian',
    ]


