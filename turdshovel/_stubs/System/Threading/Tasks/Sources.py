# encoding: utf-8
# module System.Threading.Tasks.Sources calls itself Sources
# from Microsoft.Bcl.AsyncInterfaces, Version=1.0.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51, System.Threading.Tasks.Extensions, Version=4.2.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# functions

def IValueTaskSource(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class ManualResetValueTaskSourceCore(object):
    # no doc
    def GetResult(self, token):
        """
        GetResult(self: ManualResetValueTaskSourceCore[TResult], token: Int16) -> TResult
        
            Gets the result of the operation.
        
            token: Opaque value that was provided to the System.Threading.Tasks.ValueTask's constructor.
        """
        pass

    def GetStatus(self, token):
        """
        GetStatus(self: ManualResetValueTaskSourceCore[TResult], token: Int16) -> ValueTaskSourceStatus
        
            Gets the status of the operation.
        
            token: Opaque value that was provided to the System.Threading.Tasks.ValueTask's constructor.
        """
        pass

    def OnCompleted(self, continuation, state, token, flags):
        """ OnCompleted(self: ManualResetValueTaskSourceCore[TResult], continuation: Action[object], state: object, token: Int16, flags: ValueTaskSourceOnCompletedFlags) """
        pass

    def Reset(self):
        """
        Reset(self: ManualResetValueTaskSourceCore[TResult])
            Resets to prepare for the next operation.
        """
        pass

    def SetException(self, error):
        """
        SetException(self: ManualResetValueTaskSourceCore[TResult], error: Exception)
            Complets with an error.
        """
        pass

    def SetResult(self, result):
        """
        SetResult(self: ManualResetValueTaskSourceCore[TResult], result: TResult)
            Completes with a successful result.
        
            result: The result.
        """
        pass

    RunContinuationsAsynchronously = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether to force continuations to run asynchronously.

Get: RunContinuationsAsynchronously(self: ManualResetValueTaskSourceCore[TResult]) -> bool

Set: RunContinuationsAsynchronously(self: ManualResetValueTaskSourceCore[TResult]) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the operation version.

Get: Version(self: ManualResetValueTaskSourceCore[TResult]) -> Int16

"""



class ValueTaskSourceOnCompletedFlags(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) ValueTaskSourceOnCompletedFlags, values: FlowExecutionContext (2), None (0), UseSchedulingContext (1) """
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

    FlowExecutionContext = None
    None = None
    UseSchedulingContext = None
    value__ = None


class ValueTaskSourceStatus(Enum, IComparable, IFormattable, IConvertible):
    """ enum ValueTaskSourceStatus, values: Canceled (3), Faulted (2), Pending (0), Succeeded (1) """
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

    Canceled = None
    Faulted = None
    Pending = None
    Succeeded = None
    value__ = None


