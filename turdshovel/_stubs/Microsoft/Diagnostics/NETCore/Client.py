# encoding: utf-8
# module Microsoft.Diagnostics.NETCore.Client calls itself Client
# from Microsoft.Diagnostics.NETCore.Client, Version=0.2.4.21401, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DiagnosticsClient(object):
    """
    This is a top-level class that contains methods to send various diagnostics command to the runtime.
    
    DiagnosticsClient(processId: int)
    """
    def AttachProfiler(self, attachTimeout, profilerGuid, profilerPath, additionalData):
        """
        AttachProfiler(self: DiagnosticsClient, attachTimeout: TimeSpan, profilerGuid: Guid, profilerPath: str, additionalData: Array[Byte])
            Attach a profiler.
        
            attachTimeout: Timeout for attaching the profiler
            profilerGuid: Guid for the profiler to be attached
            profilerPath: Path to the profiler to be attached
            additionalData: Additional data to be passed to the profiler
        """
        pass

    def GetProcessEnvironment(self):
        """ GetProcessEnvironment(self: DiagnosticsClient) -> Dictionary[str, str] """
        pass

    @staticmethod
    def GetPublishedProcesses():
        """
        GetPublishedProcesses() -> IEnumerable[int]
        
            Get all the active processes that can be attached to.
            Returns: IEnumerable of all the active process IDs.
        """
        pass

    def StartEventPipeSession(self, *__args):
        """
        StartEventPipeSession(self: DiagnosticsClient, providers: IEnumerable[EventPipeProvider], requestRundown: bool, circularBufferMB: int) -> EventPipeSession
        StartEventPipeSession(self: DiagnosticsClient, provider: EventPipeProvider, requestRundown: bool, circularBufferMB: int) -> EventPipeSession
        
            Start tracing the application and return an EventPipeSession object
        
            provider: An EventPipeProvider to turn on.
            requestRundown: If true, request rundown events from the runtime
            circularBufferMB: The size of the runtime's buffer for collecting events in MB
            Returns: An EventPipeSession object representing the EventPipe session that just started.
        """
        pass

    def WriteDump(self, dumpType, dumpPath, logDumpGeneration):
        """
        WriteDump(self: DiagnosticsClient, dumpType: DumpType, dumpPath: str, logDumpGeneration: bool)
            Trigger a core dump generation.
        
            dumpType: Type of the dump to be generated
            dumpPath: Full path to the dump to be generated. By default it is /tmp/coredump.{pid}
            logDumpGeneration: When set to true, display the dump generation debug log to the console.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, processId):
        """ __new__(cls: type, processId: int) """
        pass


class DiagnosticsClientException(Exception, ISerializable, _Exception):
    """ DiagnosticsClientException(msg: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, msg):
        """ __new__(cls: type, msg: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class DumpType(Enum, IComparable, IFormattable, IConvertible):
    """ enum DumpType, values: Full (4), Normal (1), Triage (3), WithHeap (2) """
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

    Full = None
    Normal = None
    Triage = None
    value__ = None
    WithHeap = None


class EventPipeProvider(object):
    """ EventPipeProvider(name: str, eventLevel: EventLevel, keywords: Int64, arguments: IDictionary[str, str]) """
    def Equals(self, obj):
        """ Equals(self: EventPipeProvider, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: EventPipeProvider) -> int """
        pass

    def ToString(self):
        """ ToString(self: EventPipeProvider) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, eventLevel, keywords, arguments):
        """ __new__(cls: type, name: str, eventLevel: EventLevel, keywords: Int64, arguments: IDictionary[str, str]) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Arguments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arguments(self: EventPipeProvider) -> IDictionary[str, str]

"""

    EventLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventLevel(self: EventPipeProvider) -> EventLevel

"""

    Keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keywords(self: EventPipeProvider) -> Int64

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EventPipeProvider) -> str

"""



class EventPipeSession(object, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: EventPipeSession) """
        pass

    def Stop(self):
        """
        Stop(self: EventPipeSession)
            Stops the given session
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

    EventStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventStream(self: EventPipeSession) -> Stream

"""



class ServerErrorException(DiagnosticsClientException, ISerializable, _Exception):
    """ ServerErrorException(msg: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, msg):
        """ __new__(cls: type, msg: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ProfilerAlreadyActiveException(ServerErrorException, ISerializable, _Exception):
    """ ProfilerAlreadyActiveException(msg: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, msg):
        """ __new__(cls: type, msg: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ServerNotAvailableException(DiagnosticsClientException, ISerializable, _Exception):
    """ ServerNotAvailableException(msg: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, msg):
        """ __new__(cls: type, msg: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class UnsupportedCommandException(ServerErrorException, ISerializable, _Exception):
    """ UnsupportedCommandException(msg: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, msg):
        """ __new__(cls: type, msg: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class UnsupportedProtocolException(DiagnosticsClientException, ISerializable, _Exception):
    """ UnsupportedProtocolException(msg: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, msg):
        """ __new__(cls: type, msg: str) """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


