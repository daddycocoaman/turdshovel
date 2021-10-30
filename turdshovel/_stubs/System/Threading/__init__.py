# encoding: utf-8
# module System.Threading calls itself Threading
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, Microsoft.Bcl.AsyncInterfaces, Version=1.0.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AbandonedMutexException(SystemException, ISerializable, _Exception):
    """
    AbandonedMutexException()
    AbandonedMutexException(message: str)
    AbandonedMutexException(message: str, inner: Exception)
    AbandonedMutexException(location: int, handle: WaitHandle)
    AbandonedMutexException(message: str, location: int, handle: WaitHandle)
    AbandonedMutexException(message: str, inner: Exception, location: int, handle: WaitHandle)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, inner: Exception)
        __new__(cls: type, location: int, handle: WaitHandle)
        __new__(cls: type, message: str, location: int, handle: WaitHandle)
        __new__(cls: type, message: str, inner: Exception, location: int, handle: WaitHandle)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Mutex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mutex(self: AbandonedMutexException) -> Mutex

"""

    MutexIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MutexIndex(self: AbandonedMutexException) -> int

"""


    SerializeObjectState = None


class ApartmentState(Enum, IComparable, IFormattable, IConvertible):
    """ enum ApartmentState, values: MTA (1), STA (0), Unknown (2) """
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

    MTA = None
    STA = None
    Unknown = None
    value__ = None


class AsyncFlowControl(object, IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: AsyncFlowControl) """
        pass

    def Equals(self, obj):
        """
        Equals(self: AsyncFlowControl, obj: object) -> bool
        Equals(self: AsyncFlowControl, obj: AsyncFlowControl) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: AsyncFlowControl) -> int """
        pass

    def Undo(self):
        """ Undo(self: AsyncFlowControl) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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


class AsyncLocal(object, IAsyncLocal):
    """
    AsyncLocal[T]()
    AsyncLocal[T](valueChangedHandler: Action[AsyncLocalValueChangedArgs[T]])
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, valueChangedHandler=None):
        """
        __new__(cls: type)
        __new__(cls: type, valueChangedHandler: Action[AsyncLocalValueChangedArgs[T]])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: AsyncLocal[T]) -> T

Set: Value(self: AsyncLocal[T]) = value
"""



class AsyncLocalValueChangedArgs(object):
    # no doc
    CurrentValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentValue(self: AsyncLocalValueChangedArgs[T]) -> T

"""

    PreviousValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviousValue(self: AsyncLocalValueChangedArgs[T]) -> T

"""

    ThreadContextChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThreadContextChanged(self: AsyncLocalValueChangedArgs[T]) -> bool

"""



class WaitHandle(MarshalByRefObject, IDisposable):
    # no doc
    def Close(self):
        """ Close(self: WaitHandle) """
        pass

    def Dispose(self):
        """ Dispose(self: WaitHandle) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
        """
        pass

    @staticmethod
    def SignalAndWait(toSignal, toWaitOn, *__args):
        """
        SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle) -> bool
        SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle, timeout: TimeSpan, exitContext: bool) -> bool
        SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle, millisecondsTimeout: int, exitContext: bool) -> bool
        """
        pass

    @staticmethod
    def WaitAll(waitHandles, *__args):
        """
        WaitAll(waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool) -> bool
        WaitAll(waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> bool
        WaitAll(waitHandles: Array[WaitHandle]) -> bool
        WaitAll(waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> bool
        WaitAll(waitHandles: Array[WaitHandle], timeout: TimeSpan) -> bool
        """
        pass

    @staticmethod
    def WaitAny(waitHandles, *__args):
        """
        WaitAny(waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool) -> int
        WaitAny(waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> int
        WaitAny(waitHandles: Array[WaitHandle], timeout: TimeSpan) -> int
        WaitAny(waitHandles: Array[WaitHandle]) -> int
        WaitAny(waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> int
        """
        pass

    def WaitOne(self, *__args):
        """
        WaitOne(self: WaitHandle, millisecondsTimeout: int, exitContext: bool) -> bool
        WaitOne(self: WaitHandle, timeout: TimeSpan, exitContext: bool) -> bool
        WaitOne(self: WaitHandle) -> bool
        WaitOne(self: WaitHandle, millisecondsTimeout: int) -> bool
        WaitOne(self: WaitHandle, timeout: TimeSpan) -> bool
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

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: WaitHandle) -> IntPtr

Set: Handle(self: WaitHandle) = value
"""

    SafeWaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SafeWaitHandle(self: WaitHandle) -> SafeWaitHandle

Set: SafeWaitHandle(self: WaitHandle) = value
"""


    InvalidHandle = None
    WaitTimeout = 258


class EventWaitHandle(WaitHandle, IDisposable):
    """
    EventWaitHandle(initialState: bool, mode: EventResetMode)
    EventWaitHandle(initialState: bool, mode: EventResetMode, name: str)
    EventWaitHandle(initialState: bool, mode: EventResetMode, name: str) -> bool
    
    EventWaitHandle(initialState: bool, mode: EventResetMode, name: str, eventSecurity: EventWaitHandleSecurity) -> bool
    """
    def Dispose(self):
        """ Dispose(self: WaitHandle, explicitDisposing: bool) """
        pass

    def GetAccessControl(self):
        """ GetAccessControl(self: EventWaitHandle) -> EventWaitHandleSecurity """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
        """
        pass

    @staticmethod
    def OpenExisting(name, rights=None):
        """
        OpenExisting(name: str) -> EventWaitHandle
        OpenExisting(name: str, rights: EventWaitHandleRights) -> EventWaitHandle
        """
        pass

    def Reset(self):
        """ Reset(self: EventWaitHandle) -> bool """
        pass

    def Set(self):
        """ Set(self: EventWaitHandle) -> bool """
        pass

    def SetAccessControl(self, eventSecurity):
        """ SetAccessControl(self: EventWaitHandle, eventSecurity: EventWaitHandleSecurity) """
        pass

    @staticmethod
    def TryOpenExisting(name, *__args):
        """
        TryOpenExisting(name: str) -> (bool, EventWaitHandle)
        TryOpenExisting(name: str, rights: EventWaitHandleRights) -> (bool, EventWaitHandle)
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
    def __new__(self, initialState, mode, name=None, createdNew=None, eventSecurity=None):
        """
        __new__(cls: type, initialState: bool, mode: EventResetMode)
        __new__(cls: type, initialState: bool, mode: EventResetMode, name: str)
        __new__(cls: type, initialState: bool, mode: EventResetMode, name: str) -> bool
        
        __new__(cls: type, initialState: bool, mode: EventResetMode, name: str, eventSecurity: EventWaitHandleSecurity) -> bool
        """
        pass


class AutoResetEvent(EventWaitHandle, IDisposable):
    """ AutoResetEvent(initialState: bool) """
    def Dispose(self):
        """ Dispose(self: WaitHandle, explicitDisposing: bool) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
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
    def __new__(self, initialState):
        """ __new__(cls: type, initialState: bool) """
        pass


class Barrier(object, IDisposable):
    """
    Barrier(participantCount: int)
    Barrier(participantCount: int, postPhaseAction: Action[Barrier])
    """
    def AddParticipant(self):
        """ AddParticipant(self: Barrier) -> Int64 """
        pass

    def AddParticipants(self, participantCount):
        """ AddParticipants(self: Barrier, participantCount: int) -> Int64 """
        pass

    def Dispose(self):
        """ Dispose(self: Barrier) """
        pass

    def RemoveParticipant(self):
        """ RemoveParticipant(self: Barrier) """
        pass

    def RemoveParticipants(self, participantCount):
        """ RemoveParticipants(self: Barrier, participantCount: int) """
        pass

    def SignalAndWait(self, *__args):
        """
        SignalAndWait(self: Barrier)SignalAndWait(self: Barrier, cancellationToken: CancellationToken)SignalAndWait(self: Barrier, timeout: TimeSpan) -> bool
        SignalAndWait(self: Barrier, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        SignalAndWait(self: Barrier, millisecondsTimeout: int) -> bool
        SignalAndWait(self: Barrier, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
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
    def __new__(self, participantCount, postPhaseAction=None):
        """
        __new__(cls: type, participantCount: int)
        __new__(cls: type, participantCount: int, postPhaseAction: Action[Barrier])
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentPhaseNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPhaseNumber(self: Barrier) -> Int64

"""

    ParticipantCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParticipantCount(self: Barrier) -> int

"""

    ParticipantsRemaining = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParticipantsRemaining(self: Barrier) -> int

"""



class BarrierPostPhaseException(Exception, ISerializable, _Exception):
    """
    BarrierPostPhaseException()
    BarrierPostPhaseException(innerException: Exception)
    BarrierPostPhaseException(message: str)
    BarrierPostPhaseException(message: str, innerException: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, innerException: Exception)
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


class CancellationToken(object):
    """ CancellationToken(canceled: bool) """
    def Equals(self, other):
        """
        Equals(self: CancellationToken, other: CancellationToken) -> bool
        Equals(self: CancellationToken, other: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CancellationToken) -> int """
        pass

    def Register(self, callback, *__args):
        """
        Register(self: CancellationToken, callback: Action) -> CancellationTokenRegistration
        Register(self: CancellationToken, callback: Action, useSynchronizationContext: bool) -> CancellationTokenRegistration
        Register(self: CancellationToken, callback: Action[object], state: object) -> CancellationTokenRegistration
        Register(self: CancellationToken, callback: Action[object], state: object, useSynchronizationContext: bool) -> CancellationTokenRegistration
        """
        pass

    def ThrowIfCancellationRequested(self):
        """ ThrowIfCancellationRequested(self: CancellationToken) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, canceled):
        """
        __new__[CancellationToken]() -> CancellationToken
        
        __new__(cls: type, canceled: bool)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    CanBeCanceled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanBeCanceled(self: CancellationToken) -> bool

"""

    IsCancellationRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancellationRequested(self: CancellationToken) -> bool

"""

    WaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaitHandle(self: CancellationToken) -> WaitHandle

"""


    None = None


class CancellationTokenRegistration(object, IEquatable[CancellationTokenRegistration], IDisposable):
    # no doc
    def Dispose(self):
        """ Dispose(self: CancellationTokenRegistration) """
        pass

    def Equals(self, *__args):
        """
        Equals(self: CancellationTokenRegistration, obj: object) -> bool
        Equals(self: CancellationTokenRegistration, other: CancellationTokenRegistration) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CancellationTokenRegistration) -> int """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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


class CancellationTokenSource(object, IDisposable):
    """
    CancellationTokenSource()
    CancellationTokenSource(delay: TimeSpan)
    CancellationTokenSource(millisecondsDelay: int)
    """
    def Cancel(self, throwOnFirstException=None):
        """ Cancel(self: CancellationTokenSource, throwOnFirstException: bool)Cancel(self: CancellationTokenSource) """
        pass

    def CancelAfter(self, *__args):
        """ CancelAfter(self: CancellationTokenSource, delay: TimeSpan)CancelAfter(self: CancellationTokenSource, millisecondsDelay: int) """
        pass

    @staticmethod
    def CreateLinkedTokenSource(*__args):
        """
        CreateLinkedTokenSource(token1: CancellationToken, token2: CancellationToken) -> CancellationTokenSource
        CreateLinkedTokenSource(*tokens: Array[CancellationToken]) -> CancellationTokenSource
        """
        pass

    def Dispose(self):
        """ Dispose(self: CancellationTokenSource) """
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
        __new__(cls: type)
        __new__(cls: type, delay: TimeSpan)
        __new__(cls: type, millisecondsDelay: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsCancellationRequested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancellationRequested(self: CancellationTokenSource) -> bool

"""

    Token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Token(self: CancellationTokenSource) -> CancellationToken

"""



class CompressedStack(object, ISerializable):
    # no doc
    @staticmethod
    def Capture():
        """ Capture() -> CompressedStack """
        pass

    def CreateCopy(self):
        """ CreateCopy(self: CompressedStack) -> CompressedStack """
        pass

    @staticmethod
    def GetCompressedStack():
        """ GetCompressedStack() -> CompressedStack """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: CompressedStack, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod
    def Run(compressedStack, callback, state):
        """ Run(compressedStack: CompressedStack, callback: ContextCallback, state: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ContextCallback(MulticastDelegate, ICloneable, ISerializable):
    """ ContextCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state, callback, object):
        """ BeginInvoke(self: ContextCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ContextCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, state):
        """ Invoke(self: ContextCallback, state: object) """
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


class CountdownEvent(object, IDisposable):
    """ CountdownEvent(initialCount: int) """
    def AddCount(self, signalCount=None):
        """ AddCount(self: CountdownEvent)AddCount(self: CountdownEvent, signalCount: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CountdownEvent) """
        pass

    def Reset(self, count=None):
        """ Reset(self: CountdownEvent)Reset(self: CountdownEvent, count: int) """
        pass

    def Signal(self, signalCount=None):
        """
        Signal(self: CountdownEvent) -> bool
        Signal(self: CountdownEvent, signalCount: int) -> bool
        """
        pass

    def TryAddCount(self, signalCount=None):
        """
        TryAddCount(self: CountdownEvent) -> bool
        TryAddCount(self: CountdownEvent, signalCount: int) -> bool
        """
        pass

    def Wait(self, *__args):
        """
        Wait(self: CountdownEvent)Wait(self: CountdownEvent, cancellationToken: CancellationToken)Wait(self: CountdownEvent, timeout: TimeSpan) -> bool
        Wait(self: CountdownEvent, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        Wait(self: CountdownEvent, millisecondsTimeout: int) -> bool
        Wait(self: CountdownEvent, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
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
    def __new__(self, initialCount):
        """ __new__(cls: type, initialCount: int) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    CurrentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCount(self: CountdownEvent) -> int

"""

    InitialCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialCount(self: CountdownEvent) -> int

"""

    IsSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSet(self: CountdownEvent) -> bool

"""

    WaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaitHandle(self: CountdownEvent) -> WaitHandle

"""



class EventResetMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum EventResetMode, values: AutoReset (0), ManualReset (1) """
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

    AutoReset = None
    ManualReset = None
    value__ = None


class ExecutionContext(object, IDisposable, ISerializable):
    # no doc
    @staticmethod
    def Capture():
        """ Capture() -> ExecutionContext """
        pass

    def CreateCopy(self):
        """ CreateCopy(self: ExecutionContext) -> ExecutionContext """
        pass

    def Dispose(self):
        """ Dispose(self: ExecutionContext) """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: ExecutionContext, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod
    def IsFlowSuppressed():
        """ IsFlowSuppressed() -> bool """
        pass

    @staticmethod
    def RestoreFlow():
        """ RestoreFlow() """
        pass

    @staticmethod
    def Run(executionContext, callback, state):
        """ Run(executionContext: ExecutionContext, callback: ContextCallback, state: object) """
        pass

    @staticmethod
    def SuppressFlow():
        """ SuppressFlow() -> AsyncFlowControl """
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

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class HostExecutionContext(object, IDisposable):
    """
    HostExecutionContext()
    HostExecutionContext(state: object)
    """
    def CreateCopy(self):
        """ CreateCopy(self: HostExecutionContext) -> HostExecutionContext """
        pass

    def Dispose(self, disposing=None):
        """ Dispose(self: HostExecutionContext)Dispose(self: HostExecutionContext, disposing: bool) """
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
    def __new__(self, state=None):
        """
        __new__(cls: type)
        __new__(cls: type, state: object)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class HostExecutionContextManager(object):
    """ HostExecutionContextManager() """
    def Capture(self):
        """ Capture(self: HostExecutionContextManager) -> HostExecutionContext """
        pass

    def Revert(self, previousState):
        """ Revert(self: HostExecutionContextManager, previousState: object) """
        pass

    def SetHostExecutionContext(self, hostExecutionContext):
        """ SetHostExecutionContext(self: HostExecutionContextManager, hostExecutionContext: HostExecutionContext) -> object """
        pass


class Interlocked(object):
    # no doc
    @staticmethod
    def Add(location1, value):
        """
        Add(location1: int, value: int) -> (int, int)
        Add(location1: Int64, value: Int64) -> (Int64, Int64)
        """
        pass

    @staticmethod
    def CompareExchange(location1, value, comparand):
        """
        CompareExchange(location1: Int64, value: Int64, comparand: Int64) -> (Int64, Int64)
        CompareExchange(location1: Single, value: Single, comparand: Single) -> (Single, Single)
        CompareExchange(location1: float, value: float, comparand: float) -> (float, float)
        CompareExchange[T](location1: T, value: T, comparand: T) -> (T, T)
        CompareExchange(location1: int, value: int, comparand: int) -> (int, int)
        CompareExchange(location1: object, value: object, comparand: object) -> (object, object)
        CompareExchange(location1: IntPtr, value: IntPtr, comparand: IntPtr) -> (IntPtr, IntPtr)
        """
        pass

    @staticmethod
    def Decrement(location):
        """
        Decrement(location: int) -> (int, int)
        Decrement(location: Int64) -> (Int64, Int64)
        """
        pass

    @staticmethod
    def Exchange(location1, value):
        """
        Exchange(location1: Int64, value: Int64) -> (Int64, Int64)
        Exchange(location1: Single, value: Single) -> (Single, Single)
        Exchange(location1: float, value: float) -> (float, float)
        Exchange[T](location1: T, value: T) -> (T, T)
        Exchange(location1: int, value: int) -> (int, int)
        Exchange(location1: object, value: object) -> (object, object)
        Exchange(location1: IntPtr, value: IntPtr) -> (IntPtr, IntPtr)
        """
        pass

    @staticmethod
    def Increment(location):
        """
        Increment(location: int) -> (int, int)
        Increment(location: Int64) -> (Int64, Int64)
        """
        pass

    @staticmethod
    def MemoryBarrier():
        """ MemoryBarrier() """
        pass

    @staticmethod
    def Read(location):
        """ Read(location: Int64) -> (Int64, Int64) """
        pass

    @staticmethod
    def SpeculationBarrier():
        """ SpeculationBarrier() """
        pass

    __all__ = [
        'Add',
        'CompareExchange',
        'Decrement',
        'Exchange',
        'Increment',
        'MemoryBarrier',
        'Read',
        'SpeculationBarrier',
    ]


class IOCompletionCallback(MulticastDelegate, ICloneable, ISerializable):
    """ IOCompletionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, errorCode, numBytes, pOVERLAP, callback, object):
        """ BeginInvoke(self: IOCompletionCallback, errorCode: UInt32, numBytes: UInt32, pOVERLAP: NativeOverlapped*, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: IOCompletionCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, errorCode, numBytes, pOVERLAP):
        """ Invoke(self: IOCompletionCallback, errorCode: UInt32, numBytes: UInt32, pOVERLAP: NativeOverlapped*) """
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


class LazyInitializer(object):
    # no doc
    @staticmethod
    def EnsureInitialized(target, *__args):
        """
        EnsureInitialized[T](target: T, valueFactory: Func[T]) -> (T, T)
        EnsureInitialized[T](target: T) -> (T, T)
        EnsureInitialized[T](target: T, initialized: bool, syncLock: object) -> (T, T, bool, object)
        EnsureInitialized[T](target: T, initialized: bool, syncLock: object, valueFactory: Func[T]) -> (T, T, bool, object)
        """
        pass

    __all__ = [
        'EnsureInitialized',
    ]


class LazyThreadSafetyMode(Enum, IComparable, IFormattable, IConvertible):
    """ enum LazyThreadSafetyMode, values: ExecutionAndPublication (2), None (0), PublicationOnly (1) """
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

    ExecutionAndPublication = None
    None = None
    PublicationOnly = None
    value__ = None


class LockCookie(object):
    # no doc
    def Equals(self, obj):
        """
        Equals(self: LockCookie, obj: object) -> bool
        Equals(self: LockCookie, obj: LockCookie) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: LockCookie) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass


class LockRecursionException(Exception, ISerializable, _Exception):
    """
    LockRecursionException()
    LockRecursionException(message: str)
    LockRecursionException(message: str, innerException: Exception)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, message=None, innerException=None):
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, message: str, innerException: Exception)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ManualResetEvent(EventWaitHandle, IDisposable):
    """ ManualResetEvent(initialState: bool) """
    def Dispose(self):
        """ Dispose(self: WaitHandle, explicitDisposing: bool) """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
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
    def __new__(self, initialState):
        """ __new__(cls: type, initialState: bool) """
        pass


class ManualResetEventSlim(object, IDisposable):
    """
    ManualResetEventSlim()
    ManualResetEventSlim(initialState: bool)
    ManualResetEventSlim(initialState: bool, spinCount: int)
    """
    def Dispose(self):
        """ Dispose(self: ManualResetEventSlim) """
        pass

    def Reset(self):
        """ Reset(self: ManualResetEventSlim) """
        pass

    def Set(self):
        """ Set(self: ManualResetEventSlim) """
        pass

    def Wait(self, *__args):
        """
        Wait(self: ManualResetEventSlim)Wait(self: ManualResetEventSlim, cancellationToken: CancellationToken)Wait(self: ManualResetEventSlim, timeout: TimeSpan) -> bool
        Wait(self: ManualResetEventSlim, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        Wait(self: ManualResetEventSlim, millisecondsTimeout: int) -> bool
        Wait(self: ManualResetEventSlim, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
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
    def __new__(self, initialState=None, spinCount=None):
        """
        __new__(cls: type)
        __new__(cls: type, initialState: bool)
        __new__(cls: type, initialState: bool, spinCount: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSet(self: ManualResetEventSlim) -> bool

"""

    SpinCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpinCount(self: ManualResetEventSlim) -> int

"""

    WaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WaitHandle(self: ManualResetEventSlim) -> WaitHandle

"""



class Monitor(object):
    # no doc
    @staticmethod
    def Enter(obj, lockTaken=None):
        """
        Enter(obj: object, lockTaken: bool) -> bool
        Enter(obj: object)
        """
        pass

    @staticmethod
    def Exit(obj):
        """ Exit(obj: object) """
        pass

    @staticmethod
    def IsEntered(obj):
        """ IsEntered(obj: object) -> bool """
        pass

    @staticmethod
    def Pulse(obj):
        """ Pulse(obj: object) """
        pass

    @staticmethod
    def PulseAll(obj):
        """ PulseAll(obj: object) """
        pass

    @staticmethod
    def TryEnter(obj, *__args):
        """
        TryEnter(obj: object) -> bool
        TryEnter(obj: object, lockTaken: bool) -> bool
        TryEnter(obj: object, millisecondsTimeout: int) -> bool
        TryEnter(obj: object, timeout: TimeSpan) -> bool
        TryEnter(obj: object, millisecondsTimeout: int, lockTaken: bool) -> bool
        TryEnter(obj: object, timeout: TimeSpan, lockTaken: bool) -> bool
        """
        pass

    @staticmethod
    def Wait(obj, *__args):
        """
        Wait(obj: object, millisecondsTimeout: int, exitContext: bool) -> bool
        Wait(obj: object, timeout: TimeSpan, exitContext: bool) -> bool
        Wait(obj: object, millisecondsTimeout: int) -> bool
        Wait(obj: object, timeout: TimeSpan) -> bool
        Wait(obj: object) -> bool
        """
        pass

    __all__ = [
        'Enter',
        'Exit',
        'IsEntered',
        'Pulse',
        'PulseAll',
        'TryEnter',
        'Wait',
    ]


class Mutex(WaitHandle, IDisposable):
    """
    Mutex(initiallyOwned: bool, name: str) -> bool
    
    Mutex(initiallyOwned: bool, name: str, mutexSecurity: MutexSecurity) -> bool
    
    Mutex(initiallyOwned: bool, name: str)
    Mutex(initiallyOwned: bool)
    Mutex()
    """
    def Dispose(self):
        """ Dispose(self: WaitHandle, explicitDisposing: bool) """
        pass

    def GetAccessControl(self):
        """ GetAccessControl(self: Mutex) -> MutexSecurity """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
        """
        pass

    @staticmethod
    def OpenExisting(name, rights=None):
        """
        OpenExisting(name: str) -> Mutex
        OpenExisting(name: str, rights: MutexRights) -> Mutex
        """
        pass

    def ReleaseMutex(self):
        """ ReleaseMutex(self: Mutex) """
        pass

    def SetAccessControl(self, mutexSecurity):
        """ SetAccessControl(self: Mutex, mutexSecurity: MutexSecurity) """
        pass

    @staticmethod
    def TryOpenExisting(name, *__args):
        """
        TryOpenExisting(name: str) -> (bool, Mutex)
        TryOpenExisting(name: str, rights: MutexRights) -> (bool, Mutex)
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
    def __new__(self, initiallyOwned=None, name=None, createdNew=None, mutexSecurity=None):
        """
        __new__(cls: type, initiallyOwned: bool, name: str) -> bool
        
        __new__(cls: type, initiallyOwned: bool, name: str, mutexSecurity: MutexSecurity) -> bool
        
        __new__(cls: type, initiallyOwned: bool, name: str)
        __new__(cls: type, initiallyOwned: bool)
        __new__(cls: type)
        """
        pass


class NativeOverlapped(object):
    # no doc
    EventHandle = None
    InternalHigh = None
    InternalLow = None
    OffsetHigh = None
    OffsetLow = None


class Overlapped(object):
    """
    Overlapped()
    Overlapped(offsetLo: int, offsetHi: int, hEvent: IntPtr, ar: IAsyncResult)
    Overlapped(offsetLo: int, offsetHi: int, hEvent: int, ar: IAsyncResult)
    """
    @staticmethod
    def Free(nativeOverlappedPtr):
        """ Free(nativeOverlappedPtr: NativeOverlapped*) """
        pass

    def Pack(self, iocb, userData=None):
        """
        Pack(self: Overlapped, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped*
        Pack(self: Overlapped, iocb: IOCompletionCallback) -> NativeOverlapped*
        """
        pass

    @staticmethod
    def Unpack(nativeOverlappedPtr):
        """ Unpack(nativeOverlappedPtr: NativeOverlapped*) -> Overlapped """
        pass

    def UnsafePack(self, iocb, userData=None):
        """
        UnsafePack(self: Overlapped, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped*
        UnsafePack(self: Overlapped, iocb: IOCompletionCallback) -> NativeOverlapped*
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, offsetLo=None, offsetHi=None, hEvent=None, ar=None):
        """
        __new__(cls: type)
        __new__(cls: type, offsetLo: int, offsetHi: int, hEvent: IntPtr, ar: IAsyncResult)
        __new__(cls: type, offsetLo: int, offsetHi: int, hEvent: int, ar: IAsyncResult)
        """
        pass

    AsyncResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AsyncResult(self: Overlapped) -> IAsyncResult

Set: AsyncResult(self: Overlapped) = value
"""

    EventHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventHandle(self: Overlapped) -> int

Set: EventHandle(self: Overlapped) = value
"""

    EventHandleIntPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EventHandleIntPtr(self: Overlapped) -> IntPtr

Set: EventHandleIntPtr(self: Overlapped) = value
"""

    OffsetHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetHigh(self: Overlapped) -> int

Set: OffsetHigh(self: Overlapped) = value
"""

    OffsetLow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetLow(self: Overlapped) -> int

Set: OffsetLow(self: Overlapped) = value
"""



class ParameterizedThreadStart(MulticastDelegate, ICloneable, ISerializable):
    """ ParameterizedThreadStart(object: object, method: IntPtr) """
    def BeginInvoke(self, obj, callback, object):
        """ BeginInvoke(self: ParameterizedThreadStart, obj: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ParameterizedThreadStart, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, obj):
        """ Invoke(self: ParameterizedThreadStart, obj: object) """
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


class PreAllocatedOverlapped(object, IDisposable, IDeferredDisposable):
    """ PreAllocatedOverlapped(callback: IOCompletionCallback, state: object, pinData: object) """
    def Dispose(self):
        """ Dispose(self: PreAllocatedOverlapped) """
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
    def __new__(self, callback, state, pinData):
        """ __new__(cls: type, callback: IOCompletionCallback, state: object, pinData: object) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ReaderWriterLock(CriticalFinalizerObject):
    """ ReaderWriterLock() """
    def AcquireReaderLock(self, *__args):
        """ AcquireReaderLock(self: ReaderWriterLock, millisecondsTimeout: int)AcquireReaderLock(self: ReaderWriterLock, timeout: TimeSpan) """
        pass

    def AcquireWriterLock(self, *__args):
        """ AcquireWriterLock(self: ReaderWriterLock, millisecondsTimeout: int)AcquireWriterLock(self: ReaderWriterLock, timeout: TimeSpan) """
        pass

    def AnyWritersSince(self, seqNum):
        """ AnyWritersSince(self: ReaderWriterLock, seqNum: int) -> bool """
        pass

    def DowngradeFromWriterLock(self, lockCookie):
        """ DowngradeFromWriterLock(self: ReaderWriterLock, lockCookie: LockCookie) -> LockCookie """
        pass

    def ReleaseLock(self):
        """ ReleaseLock(self: ReaderWriterLock) -> LockCookie """
        pass

    def ReleaseReaderLock(self):
        """ ReleaseReaderLock(self: ReaderWriterLock) """
        pass

    def ReleaseWriterLock(self):
        """ ReleaseWriterLock(self: ReaderWriterLock) """
        pass

    def RestoreLock(self, lockCookie):
        """ RestoreLock(self: ReaderWriterLock, lockCookie: LockCookie) -> LockCookie """
        pass

    def UpgradeToWriterLock(self, *__args):
        """
        UpgradeToWriterLock(self: ReaderWriterLock, millisecondsTimeout: int) -> LockCookie
        UpgradeToWriterLock(self: ReaderWriterLock, timeout: TimeSpan) -> LockCookie
        """
        pass

    IsReaderLockHeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReaderLockHeld(self: ReaderWriterLock) -> bool

"""

    IsWriterLockHeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWriterLockHeld(self: ReaderWriterLock) -> bool

"""

    WriterSeqNum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriterSeqNum(self: ReaderWriterLock) -> int

"""



class RegisteredWaitHandle(MarshalByRefObject):
    # no doc
    def Unregister(self, waitObject):
        """ Unregister(self: RegisteredWaitHandle, waitObject: WaitHandle) -> bool """
        pass


class Semaphore(WaitHandle, IDisposable):
    """
    Semaphore(initialCount: int, maximumCount: int)
    Semaphore(initialCount: int, maximumCount: int, name: str)
    Semaphore(initialCount: int, maximumCount: int, name: str) -> bool
    
    Semaphore(initialCount: int, maximumCount: int, name: str, semaphoreSecurity: SemaphoreSecurity) -> bool
    """
    def Dispose(self):
        """ Dispose(self: WaitHandle, explicitDisposing: bool) """
        pass

    def GetAccessControl(self):
        """ GetAccessControl(self: Semaphore) -> SemaphoreSecurity """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
        """
        pass

    @staticmethod
    def OpenExisting(name, rights=None):
        """
        OpenExisting(name: str) -> Semaphore
        OpenExisting(name: str, rights: SemaphoreRights) -> Semaphore
        """
        pass

    def Release(self, releaseCount=None):
        """
        Release(self: Semaphore) -> int
        Release(self: Semaphore, releaseCount: int) -> int
        """
        pass

    def SetAccessControl(self, semaphoreSecurity):
        """ SetAccessControl(self: Semaphore, semaphoreSecurity: SemaphoreSecurity) """
        pass

    @staticmethod
    def TryOpenExisting(name, *__args):
        """
        TryOpenExisting(name: str) -> (bool, Semaphore)
        TryOpenExisting(name: str, rights: SemaphoreRights) -> (bool, Semaphore)
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
    def __new__(self, initialCount, maximumCount, name=None, createdNew=None, semaphoreSecurity=None):
        """
        __new__(cls: type, initialCount: int, maximumCount: int)
        __new__(cls: type, initialCount: int, maximumCount: int, name: str)
        __new__(cls: type, initialCount: int, maximumCount: int, name: str) -> bool
        
        __new__(cls: type, initialCount: int, maximumCount: int, name: str, semaphoreSecurity: SemaphoreSecurity) -> bool
        """
        pass


class SemaphoreFullException(SystemException, ISerializable, _Exception):
    """
    SemaphoreFullException()
    SemaphoreFullException(message: str)
    SemaphoreFullException(message: str, innerException: Exception)
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


class SemaphoreSlim(object, IDisposable):
    """
    SemaphoreSlim(initialCount: int)
    SemaphoreSlim(initialCount: int, maxCount: int)
    """
    def Dispose(self):
        """ Dispose(self: SemaphoreSlim) """
        pass

    def Release(self, releaseCount=None):
        """
        Release(self: SemaphoreSlim) -> int
        Release(self: SemaphoreSlim, releaseCount: int) -> int
        """
        pass

    def Wait(self, *__args):
        """
        Wait(self: SemaphoreSlim)Wait(self: SemaphoreSlim, cancellationToken: CancellationToken)Wait(self: SemaphoreSlim, timeout: TimeSpan) -> bool
        Wait(self: SemaphoreSlim, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        Wait(self: SemaphoreSlim, millisecondsTimeout: int) -> bool
        Wait(self: SemaphoreSlim, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        pass

    def WaitAsync(self, *__args):
        """
        WaitAsync(self: SemaphoreSlim) -> Task
        WaitAsync(self: SemaphoreSlim, cancellationToken: CancellationToken) -> Task
        WaitAsync(self: SemaphoreSlim, millisecondsTimeout: int) -> Task[bool]
        WaitAsync(self: SemaphoreSlim, timeout: TimeSpan) -> Task[bool]
        WaitAsync(self: SemaphoreSlim, timeout: TimeSpan, cancellationToken: CancellationToken) -> Task[bool]
        WaitAsync(self: SemaphoreSlim, millisecondsTimeout: int, cancellationToken: CancellationToken) -> Task[bool]
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
    def __new__(self, initialCount, maxCount=None):
        """
        __new__(cls: type, initialCount: int)
        __new__(cls: type, initialCount: int, maxCount: int)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    AvailableWaitHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AvailableWaitHandle(self: SemaphoreSlim) -> WaitHandle

"""

    CurrentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCount(self: SemaphoreSlim) -> int

"""



class SendOrPostCallback(MulticastDelegate, ICloneable, ISerializable):
    """ SendOrPostCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state, callback, object):
        """ BeginInvoke(self: SendOrPostCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SendOrPostCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, state):
        """ Invoke(self: SendOrPostCallback, state: object) """
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


class SpinLock(object):
    """ SpinLock(enableThreadOwnerTracking: bool) """
    def Enter(self, lockTaken):
        """ Enter(self: SpinLock, lockTaken: bool) -> bool """
        pass

    def Exit(self, useMemoryBarrier=None):
        """ Exit(self: SpinLock)Exit(self: SpinLock, useMemoryBarrier: bool) """
        pass

    def TryEnter(self, *__args):
        """
        TryEnter(self: SpinLock, lockTaken: bool) -> bool
        TryEnter(self: SpinLock, timeout: TimeSpan, lockTaken: bool) -> bool
        TryEnter(self: SpinLock, millisecondsTimeout: int, lockTaken: bool) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, enableThreadOwnerTracking):
        """
        __new__[SpinLock]() -> SpinLock
        
        __new__(cls: type, enableThreadOwnerTracking: bool)
        """
        pass

    IsHeld = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHeld(self: SpinLock) -> bool

"""

    IsHeldByCurrentThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHeldByCurrentThread(self: SpinLock) -> bool

"""

    IsThreadOwnerTrackingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsThreadOwnerTrackingEnabled(self: SpinLock) -> bool

"""



class SpinWait(object):
    # no doc
    def Reset(self):
        """ Reset(self: SpinWait) """
        pass

    def SpinOnce(self):
        """ SpinOnce(self: SpinWait) """
        pass

    @staticmethod
    def SpinUntil(condition, *__args):
        """
        SpinUntil(condition: Func[bool])SpinUntil(condition: Func[bool], timeout: TimeSpan) -> bool
        SpinUntil(condition: Func[bool], millisecondsTimeout: int) -> bool
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SpinWait) -> int

"""

    NextSpinWillYield = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextSpinWillYield(self: SpinWait) -> bool

"""



class SynchronizationContext(object):
    """ SynchronizationContext() """
    def CreateCopy(self):
        """ CreateCopy(self: SynchronizationContext) -> SynchronizationContext """
        pass

    def IsWaitNotificationRequired(self):
        """ IsWaitNotificationRequired(self: SynchronizationContext) -> bool """
        pass

    def OperationCompleted(self):
        """ OperationCompleted(self: SynchronizationContext) """
        pass

    def OperationStarted(self):
        """ OperationStarted(self: SynchronizationContext) """
        pass

    def Post(self, d, state):
        """ Post(self: SynchronizationContext, d: SendOrPostCallback, state: object) """
        pass

    def Send(self, d, state):
        """ Send(self: SynchronizationContext, d: SendOrPostCallback, state: object) """
        pass

    @staticmethod
    def SetSynchronizationContext(syncContext):
        """ SetSynchronizationContext(syncContext: SynchronizationContext) """
        pass

    def SetWaitNotificationRequired(self, *args): #cannot find CLR method
        """ SetWaitNotificationRequired(self: SynchronizationContext) """
        pass

    def Wait(self, waitHandles, waitAll, millisecondsTimeout):
        """ Wait(self: SynchronizationContext, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int """
        pass

    def WaitHelper(self, *args): #cannot find CLR method
        """ WaitHelper(waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int """
        pass

    Current = None


class SynchronizationLockException(SystemException, ISerializable, _Exception):
    """
    SynchronizationLockException()
    SynchronizationLockException(message: str)
    SynchronizationLockException(message: str, innerException: Exception)
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


class Thread(CriticalFinalizerObject, _Thread):
    """
    Thread(start: ThreadStart)
    Thread(start: ThreadStart, maxStackSize: int)
    Thread(start: ParameterizedThreadStart)
    Thread(start: ParameterizedThreadStart, maxStackSize: int)
    """
    def Abort(self, stateInfo=None):
        """ Abort(self: Thread, stateInfo: object)Abort(self: Thread) """
        pass

    @staticmethod
    def AllocateDataSlot():
        """ AllocateDataSlot() -> LocalDataStoreSlot """
        pass

    @staticmethod
    def AllocateNamedDataSlot(name):
        """ AllocateNamedDataSlot(name: str) -> LocalDataStoreSlot """
        pass

    @staticmethod
    def BeginCriticalRegion():
        """ BeginCriticalRegion() """
        pass

    @staticmethod
    def BeginThreadAffinity():
        """ BeginThreadAffinity() """
        pass

    def DisableComObjectEagerCleanup(self):
        """ DisableComObjectEagerCleanup(self: Thread) """
        pass

    @staticmethod
    def EndCriticalRegion():
        """ EndCriticalRegion() """
        pass

    @staticmethod
    def EndThreadAffinity():
        """ EndThreadAffinity() """
        pass

    @staticmethod
    def FreeNamedDataSlot(name):
        """ FreeNamedDataSlot(name: str) """
        pass

    def GetApartmentState(self):
        """ GetApartmentState(self: Thread) -> ApartmentState """
        pass

    def GetCompressedStack(self):
        """ GetCompressedStack(self: Thread) -> CompressedStack """
        pass

    @staticmethod
    def GetData(slot):
        """ GetData(slot: LocalDataStoreSlot) -> object """
        pass

    @staticmethod
    def GetDomain():
        """ GetDomain() -> AppDomain """
        pass

    @staticmethod
    def GetDomainID():
        """ GetDomainID() -> int """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Thread) -> int """
        pass

    @staticmethod
    def GetNamedDataSlot(name):
        """ GetNamedDataSlot(name: str) -> LocalDataStoreSlot """
        pass

    def Interrupt(self):
        """ Interrupt(self: Thread) """
        pass

    def Join(self, *__args):
        """
        Join(self: Thread)Join(self: Thread, millisecondsTimeout: int) -> bool
        Join(self: Thread, timeout: TimeSpan) -> bool
        """
        pass

    @staticmethod
    def MemoryBarrier():
        """ MemoryBarrier() """
        pass

    @staticmethod
    def ResetAbort():
        """ ResetAbort() """
        pass

    def Resume(self):
        """ Resume(self: Thread) """
        pass

    def SetApartmentState(self, state):
        """ SetApartmentState(self: Thread, state: ApartmentState) """
        pass

    def SetCompressedStack(self, stack):
        """ SetCompressedStack(self: Thread, stack: CompressedStack) """
        pass

    @staticmethod
    def SetData(slot, data):
        """ SetData(slot: LocalDataStoreSlot, data: object) """
        pass

    @staticmethod
    def Sleep(*__args):
        """ Sleep(millisecondsTimeout: int)Sleep(timeout: TimeSpan) """
        pass

    @staticmethod
    def SpinWait(iterations):
        """ SpinWait(iterations: int) """
        pass

    def Start(self, parameter=None):
        """ Start(self: Thread)Start(self: Thread, parameter: object) """
        pass

    def Suspend(self):
        """ Suspend(self: Thread) """
        pass

    def TrySetApartmentState(self, state):
        """ TrySetApartmentState(self: Thread, state: ApartmentState) -> bool """
        pass

    @staticmethod
    def VolatileRead(address):
        """
        VolatileRead(address: Byte) -> (Byte, Byte)
        VolatileRead(address: Int16) -> (Int16, Int16)
        VolatileRead(address: int) -> (int, int)
        VolatileRead(address: Int64) -> (Int64, Int64)
        VolatileRead(address: SByte) -> (SByte, SByte)
        VolatileRead(address: UInt16) -> (UInt16, UInt16)
        VolatileRead(address: UInt32) -> (UInt32, UInt32)
        VolatileRead(address: IntPtr) -> (IntPtr, IntPtr)
        VolatileRead(address: UIntPtr) -> (UIntPtr, UIntPtr)
        VolatileRead(address: UInt64) -> (UInt64, UInt64)
        VolatileRead(address: Single) -> (Single, Single)
        VolatileRead(address: float) -> (float, float)
        VolatileRead(address: object) -> (object, object)
        """
        pass

    @staticmethod
    def VolatileWrite(address, value):
        """
        VolatileWrite(address: Byte, value: Byte) -> Byte
        VolatileWrite(address: Int16, value: Int16) -> Int16
        VolatileWrite(address: int, value: int) -> int
        VolatileWrite(address: Int64, value: Int64) -> Int64
        VolatileWrite(address: SByte, value: SByte) -> SByte
        VolatileWrite(address: UInt16, value: UInt16) -> UInt16
        VolatileWrite(address: UInt32, value: UInt32) -> UInt32
        VolatileWrite(address: IntPtr, value: IntPtr) -> IntPtr
        VolatileWrite(address: UIntPtr, value: UIntPtr) -> UIntPtr
        VolatileWrite(address: UInt64, value: UInt64) -> UInt64
        VolatileWrite(address: Single, value: Single) -> Single
        VolatileWrite(address: float, value: float) -> float
        VolatileWrite(address: object, value: object) -> object
        """
        pass

    @staticmethod
    def Yield():
        """ Yield() -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, start, maxStackSize=None):
        """
        __new__(cls: type, start: ThreadStart)
        __new__(cls: type, start: ThreadStart, maxStackSize: int)
        __new__(cls: type, start: ParameterizedThreadStart)
        __new__(cls: type, start: ParameterizedThreadStart, maxStackSize: int)
        """
        pass

    ApartmentState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApartmentState(self: Thread) -> ApartmentState

Set: ApartmentState(self: Thread) = value
"""

    CurrentCulture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCulture(self: Thread) -> CultureInfo

Set: CurrentCulture(self: Thread) = value
"""

    CurrentUICulture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentUICulture(self: Thread) -> CultureInfo

Set: CurrentUICulture(self: Thread) = value
"""

    ExecutionContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecutionContext(self: Thread) -> ExecutionContext

"""

    IsAlive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAlive(self: Thread) -> bool

"""

    IsBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBackground(self: Thread) -> bool

Set: IsBackground(self: Thread) = value
"""

    IsThreadPoolThread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsThreadPoolThread(self: Thread) -> bool

"""

    ManagedThreadId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManagedThreadId(self: Thread) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Thread) -> str

Set: Name(self: Thread) = value
"""

    Priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Priority(self: Thread) -> ThreadPriority

Set: Priority(self: Thread) = value
"""

    ThreadState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThreadState(self: Thread) -> ThreadState

"""


    CurrentContext = None
    CurrentPrincipal = None
    CurrentThread = None


class ThreadAbortException(SystemException, ISerializable, _Exception):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ExceptionState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceptionState(self: ThreadAbortException) -> object

"""


    SerializeObjectState = None


class ThreadExceptionEventArgs(EventArgs):
    """ ThreadExceptionEventArgs(t: Exception) """
    @staticmethod # known case of __new__
    def __new__(self, t):
        """ __new__(cls: type, t: Exception) """
        pass

    Exception = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exception(self: ThreadExceptionEventArgs) -> Exception

"""



class ThreadExceptionEventHandler(MulticastDelegate, ICloneable, ISerializable):
    """ ThreadExceptionEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, e, callback, object):
        """ BeginInvoke(self: ThreadExceptionEventHandler, sender: object, e: ThreadExceptionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ThreadExceptionEventHandler, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ThreadExceptionEventHandler, sender: object, e: ThreadExceptionEventArgs) """
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


class ThreadInterruptedException(SystemException, ISerializable, _Exception):
    """
    ThreadInterruptedException()
    ThreadInterruptedException(message: str)
    ThreadInterruptedException(message: str, innerException: Exception)
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


class ThreadLocal(object, IDisposable):
    """
    ThreadLocal[T]()
    ThreadLocal[T](trackAllValues: bool)
    ThreadLocal[T](valueFactory: Func[T])
    ThreadLocal[T](valueFactory: Func[T], trackAllValues: bool)
    """
    def Dispose(self):
        """ Dispose(self: ThreadLocal[T]) """
        pass

    def ToString(self):
        """ ToString(self: ThreadLocal[T]) -> str """
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
        __new__(cls: type)
        __new__(cls: type, trackAllValues: bool)
        __new__(cls: type, valueFactory: Func[T])
        __new__(cls: type, valueFactory: Func[T], trackAllValues: bool)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    IsValueCreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValueCreated(self: ThreadLocal[T]) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ThreadLocal[T]) -> T

Set: Value(self: ThreadLocal[T]) = value
"""

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Values(self: ThreadLocal[T]) -> IList[T]

"""



class ThreadPool(object):
    # no doc
    @staticmethod
    def BindHandle(osHandle):
        """
        BindHandle(osHandle: IntPtr) -> bool
        BindHandle(osHandle: SafeHandle) -> bool
        """
        pass

    @staticmethod
    def GetAvailableThreads(workerThreads, completionPortThreads):
        """ GetAvailableThreads() -> (int, int) """
        pass

    @staticmethod
    def GetMaxThreads(workerThreads, completionPortThreads):
        """ GetMaxThreads() -> (int, int) """
        pass

    @staticmethod
    def GetMinThreads(workerThreads, completionPortThreads):
        """ GetMinThreads() -> (int, int) """
        pass

    @staticmethod
    def QueueUserWorkItem(callBack, state=None):
        """
        QueueUserWorkItem(callBack: WaitCallback, state: object) -> bool
        QueueUserWorkItem(callBack: WaitCallback) -> bool
        """
        pass

    @staticmethod
    def RegisterWaitForSingleObject(waitObject, callBack, state, *__args):
        """
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: UInt32, executeOnlyOnce: bool) -> RegisteredWaitHandle
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> RegisteredWaitHandle
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: Int64, executeOnlyOnce: bool) -> RegisteredWaitHandle
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, timeout: TimeSpan, executeOnlyOnce: bool) -> RegisteredWaitHandle
        """
        pass

    @staticmethod
    def SetMaxThreads(workerThreads, completionPortThreads):
        """ SetMaxThreads(workerThreads: int, completionPortThreads: int) -> bool """
        pass

    @staticmethod
    def SetMinThreads(workerThreads, completionPortThreads):
        """ SetMinThreads(workerThreads: int, completionPortThreads: int) -> bool """
        pass

    @staticmethod
    def UnsafeQueueNativeOverlapped(overlapped):
        """ UnsafeQueueNativeOverlapped(overlapped: NativeOverlapped*) -> bool """
        pass

    @staticmethod
    def UnsafeQueueUserWorkItem(callBack, state):
        """ UnsafeQueueUserWorkItem(callBack: WaitCallback, state: object) -> bool """
        pass

    @staticmethod
    def UnsafeRegisterWaitForSingleObject(waitObject, callBack, state, *__args):
        """
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: UInt32, executeOnlyOnce: bool) -> RegisteredWaitHandle
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> RegisteredWaitHandle
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: Int64, executeOnlyOnce: bool) -> RegisteredWaitHandle
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, timeout: TimeSpan, executeOnlyOnce: bool) -> RegisteredWaitHandle
        """
        pass

    __all__ = [
        'BindHandle',
        'GetAvailableThreads',
        'GetMaxThreads',
        'GetMinThreads',
        'QueueUserWorkItem',
        'RegisterWaitForSingleObject',
        'SetMaxThreads',
        'SetMinThreads',
        'UnsafeQueueNativeOverlapped',
        'UnsafeQueueUserWorkItem',
        'UnsafeRegisterWaitForSingleObject',
    ]


class ThreadPoolBoundHandle(object, IDisposable):
    # no doc
    def AllocateNativeOverlapped(self, *__args):
        """
        AllocateNativeOverlapped(self: ThreadPoolBoundHandle, callback: IOCompletionCallback, state: object, pinData: object) -> NativeOverlapped*
        AllocateNativeOverlapped(self: ThreadPoolBoundHandle, preAllocated: PreAllocatedOverlapped) -> NativeOverlapped*
        """
        pass

    @staticmethod
    def BindHandle(handle):
        """ BindHandle(handle: SafeHandle) -> ThreadPoolBoundHandle """
        pass

    def Dispose(self):
        """ Dispose(self: ThreadPoolBoundHandle) """
        pass

    def FreeNativeOverlapped(self, overlapped):
        """ FreeNativeOverlapped(self: ThreadPoolBoundHandle, overlapped: NativeOverlapped*) """
        pass

    @staticmethod
    def GetNativeOverlappedState(overlapped):
        """ GetNativeOverlappedState(overlapped: NativeOverlapped*) -> object """
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

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: ThreadPoolBoundHandle) -> SafeHandle

"""



class ThreadPriority(Enum, IComparable, IFormattable, IConvertible):
    """ enum ThreadPriority, values: AboveNormal (3), BelowNormal (1), Highest (4), Lowest (0), Normal (2) """
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

    AboveNormal = None
    BelowNormal = None
    Highest = None
    Lowest = None
    Normal = None
    value__ = None


class ThreadStart(MulticastDelegate, ICloneable, ISerializable):
    """ ThreadStart(object: object, method: IntPtr) """
    def BeginInvoke(self, callback, object):
        """ BeginInvoke(self: ThreadStart, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ThreadStart, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self):
        """ Invoke(self: ThreadStart) """
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


class ThreadStartException(SystemException, ISerializable, _Exception):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    SerializeObjectState = None


class ThreadState(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ThreadState, values: Aborted (256), AbortRequested (128), Background (4), Running (0), Stopped (16), StopRequested (1), Suspended (64), SuspendRequested (2), Unstarted (8), WaitSleepJoin (32) """
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

    Aborted = None
    AbortRequested = None
    Background = None
    Running = None
    Stopped = None
    StopRequested = None
    Suspended = None
    SuspendRequested = None
    Unstarted = None
    value__ = None
    WaitSleepJoin = None


class ThreadStateException(SystemException, ISerializable, _Exception):
    """
    ThreadStateException()
    ThreadStateException(message: str)
    ThreadStateException(message: str, innerException: Exception)
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


class Timeout(object):
    # no doc
    Infinite = -1
    InfiniteTimeSpan = None
    __all__ = [
        'Infinite',
        'InfiniteTimeSpan',
    ]


class Timer(MarshalByRefObject, IDisposable):
    """
    Timer(callback: TimerCallback, state: object, dueTime: int, period: int)
    Timer(callback: TimerCallback, state: object, dueTime: TimeSpan, period: TimeSpan)
    Timer(callback: TimerCallback, state: object, dueTime: UInt32, period: UInt32)
    Timer(callback: TimerCallback, state: object, dueTime: Int64, period: Int64)
    Timer(callback: TimerCallback)
    """
    def Change(self, dueTime, period):
        """
        Change(self: Timer, dueTime: int, period: int) -> bool
        Change(self: Timer, dueTime: TimeSpan, period: TimeSpan) -> bool
        Change(self: Timer, dueTime: UInt32, period: UInt32) -> bool
        Change(self: Timer, dueTime: Int64, period: Int64) -> bool
        """
        pass

    def Dispose(self, notifyObject=None):
        """ Dispose(self: Timer)Dispose(self: Timer, notifyObject: WaitHandle) -> bool """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        MemberwiseClone(self: object) -> object
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
    def __new__(self, callback, state=None, dueTime=None, period=None):
        """
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: int, period: int)
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: TimeSpan, period: TimeSpan)
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: UInt32, period: UInt32)
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: Int64, period: Int64)
        __new__(cls: type, callback: TimerCallback)
        """
        pass


class TimerCallback(MulticastDelegate, ICloneable, ISerializable):
    """ TimerCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state, callback, object):
        """ BeginInvoke(self: TimerCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TimerCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, state):
        """ Invoke(self: TimerCallback, state: object) """
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


class Volatile(object):
    # no doc
    @staticmethod
    def Read(location):
        """
        Read(location: Int64) -> (Int64, Int64)
        Read[T](location: T) -> (T, T)
        Read(location: bool) -> (bool, bool)
        Read(location: SByte) -> (SByte, SByte)
        Read(location: Byte) -> (Byte, Byte)
        Read(location: Int16) -> (Int16, Int16)
        Read(location: UInt16) -> (UInt16, UInt16)
        Read(location: int) -> (int, int)
        Read(location: UInt32) -> (UInt32, UInt32)
        Read(location: UInt64) -> (UInt64, UInt64)
        Read(location: IntPtr) -> (IntPtr, IntPtr)
        Read(location: UIntPtr) -> (UIntPtr, UIntPtr)
        Read(location: Single) -> (Single, Single)
        Read(location: float) -> (float, float)
        """
        pass

    @staticmethod
    def Write(location, value):
        """
        Write(location: Int64, value: Int64) -> Int64
        Write[T](location: T, value: T) -> T
        Write(location: bool, value: bool) -> bool
        Write(location: SByte, value: SByte) -> SByte
        Write(location: Byte, value: Byte) -> Byte
        Write(location: Int16, value: Int16) -> Int16
        Write(location: UInt16, value: UInt16) -> UInt16
        Write(location: int, value: int) -> int
        Write(location: UInt32, value: UInt32) -> UInt32
        Write(location: UInt64, value: UInt64) -> UInt64
        Write(location: IntPtr, value: IntPtr) -> IntPtr
        Write(location: UIntPtr, value: UIntPtr) -> UIntPtr
        Write(location: Single, value: Single) -> Single
        Write(location: float, value: float) -> float
        """
        pass

    __all__ = [
        'Read',
        'Write',
    ]


class WaitCallback(MulticastDelegate, ICloneable, ISerializable):
    """ WaitCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state, callback, object):
        """ BeginInvoke(self: WaitCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: WaitCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, state):
        """ Invoke(self: WaitCallback, state: object) """
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


class WaitHandleCannotBeOpenedException(ApplicationException, ISerializable, _Exception):
    """
    WaitHandleCannotBeOpenedException()
    WaitHandleCannotBeOpenedException(message: str)
    WaitHandleCannotBeOpenedException(message: str, innerException: Exception)
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


class WaitHandleExtensions(object):
    # no doc
    @staticmethod
    def GetSafeWaitHandle(waitHandle):
        """ GetSafeWaitHandle(waitHandle: WaitHandle) -> SafeWaitHandle """
        pass

    @staticmethod
    def SetSafeWaitHandle(waitHandle, value):
        """ SetSafeWaitHandle(waitHandle: WaitHandle, value: SafeWaitHandle) """
        pass

    __all__ = [
        'GetSafeWaitHandle',
        'SetSafeWaitHandle',
    ]


class WaitOrTimerCallback(MulticastDelegate, ICloneable, ISerializable):
    """ WaitOrTimerCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state, timedOut, callback, object):
        """ BeginInvoke(self: WaitOrTimerCallback, state: object, timedOut: bool, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """ CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """ DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: WaitOrTimerCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: MulticastDelegate) -> MethodInfo """
        pass

    def Invoke(self, state, timedOut):
        """ Invoke(self: WaitOrTimerCallback, state: object, timedOut: bool) """
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

