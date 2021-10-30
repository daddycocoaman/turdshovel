# encoding: utf-8
# module System.Buffers.Text calls itself Text
# from System.Memory, Version=4.0.1.1, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Base64(object):
    # no doc
    @staticmethod
    def DecodeFromUtf8(utf8, bytes, bytesConsumed, bytesWritten, isFinalBlock):
        """ DecodeFromUtf8(utf8: ReadOnlySpan[Byte], bytes: Span[Byte], isFinalBlock: bool) -> (OperationStatus, int, int) """
        pass

    @staticmethod
    def DecodeFromUtf8InPlace(buffer, bytesWritten):
        """ DecodeFromUtf8InPlace(buffer: Span[Byte]) -> (OperationStatus, int) """
        pass

    @staticmethod
    def EncodeToUtf8(bytes, utf8, bytesConsumed, bytesWritten, isFinalBlock):
        """ EncodeToUtf8(bytes: ReadOnlySpan[Byte], utf8: Span[Byte], isFinalBlock: bool) -> (OperationStatus, int, int) """
        pass

    @staticmethod
    def EncodeToUtf8InPlace(buffer, dataLength, bytesWritten):
        """ EncodeToUtf8InPlace(buffer: Span[Byte], dataLength: int) -> (OperationStatus, int) """
        pass

    @staticmethod
    def GetMaxDecodedFromUtf8Length(length):
        """ GetMaxDecodedFromUtf8Length(length: int) -> int """
        pass

    @staticmethod
    def GetMaxEncodedToUtf8Length(length):
        """ GetMaxEncodedToUtf8Length(length: int) -> int """
        pass

    __all__ = [
        'DecodeFromUtf8',
        'DecodeFromUtf8InPlace',
        'EncodeToUtf8',
        'EncodeToUtf8InPlace',
        'GetMaxDecodedFromUtf8Length',
        'GetMaxEncodedToUtf8Length',
    ]


class Utf8Formatter(object):
    # no doc
    @staticmethod
    def TryFormat(value, destination, bytesWritten, format):
        """
        TryFormat(value: bool, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: DateTimeOffset, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: DateTime, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: Decimal, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: float, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: Single, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: Guid, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: Byte, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: SByte, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: UInt16, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: Int16, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: UInt32, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: int, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: UInt64, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: Int64, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        TryFormat(value: TimeSpan, destination: Span[Byte], format: StandardFormat) -> (bool, int)
        """
        pass

    __all__ = [
        'TryFormat',
    ]


class Utf8Parser(object):
    # no doc
    @staticmethod
    def TryParse(source, value, bytesConsumed, standardFormat):
        """
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, bool, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, DateTime, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, DateTimeOffset, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, Decimal, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, Single, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, float, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, Guid, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, SByte, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, Int16, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, int, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, Int64, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, Byte, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, UInt16, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, UInt32, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, UInt64, int)
        TryParse(source: ReadOnlySpan[Byte], standardFormat: Char) -> (bool, TimeSpan, int)
        """
        pass

    __all__ = [
        'TryParse',
    ]


