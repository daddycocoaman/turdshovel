# encoding: utf-8
# module System.Runtime.CompilerServices calls itself CompilerServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, Microsoft.Bcl.AsyncInterfaces, Version=1.0.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51, System.Runtime.CompilerServices.Unsafe, Version=4.0.4.1, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Threading.Tasks.Extensions, Version=4.2.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# functions

def AsyncTaskMethodBuilder(*args, **kwargs): # real signature unknown
    """  """
    pass

def AsyncValueTaskMethodBuilder(*args, **kwargs): # real signature unknown
    """  """
    pass

def ConfiguredTaskAwaitable(*args, **kwargs): # real signature unknown
    """  """
    pass

def ConfiguredValueTaskAwaitable(*args, **kwargs): # real signature unknown
    """  """
    pass

def TaskAwaiter(*args, **kwargs): # real signature unknown
    """  """
    pass

def ValueTaskAwaiter(*args, **kwargs): # real signature unknown
    """  """
    pass

# classes

class AccessedThroughPropertyAttribute(Attribute, _Attribute):
    """ AccessedThroughPropertyAttribute(propertyName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, propertyName):
        """ __new__(cls: type, propertyName: str) """
        pass

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: AccessedThroughPropertyAttribute) -> str

"""



class AsyncIteratorMethodBuilder(object):
    """ Represents a builder for asynchronous iterators. """
    def AwaitOnCompleted(self, awaiter, stateMachine):
# Error generating skeleton for function AwaitOnCompleted: Method must be called on a Type for which Type.IsGenericParameter is false.

    def AwaitUnsafeOnCompleted(self, awaiter, stateMachine):
# Error generating skeleton for function AwaitUnsafeOnCompleted: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Complete(self):
        """
        Complete(self: AsyncIteratorMethodBuilder)
            Marks iteration as being completed, whether successfully or otherwise.
        """
        pass

    @staticmethod
    def Create():
        """
        Create() -> AsyncIteratorMethodBuilder
        
            Creates an instance of the System.Runtime.CompilerServices.AsyncIteratorMethodBuilder struct.
            Returns: The initialized instance.
        """
        pass

    def MoveNext(self, stateMachine):
# Error generating skeleton for function MoveNext: Method must be called on a Type for which Type.IsGenericParameter is false.


class StateMachineAttribute(Attribute, _Attribute):
    """ StateMachineAttribute(stateMachineType: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stateMachineType):
        """ __new__(cls: type, stateMachineType: Type) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    StateMachineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateMachineType(self: StateMachineAttribute) -> Type

"""



class AsyncIteratorStateMachineAttribute(StateMachineAttribute, _Attribute):
    """
    Indicates whether a method is an asynchronous iterator.
    
    AsyncIteratorStateMachineAttribute(stateMachineType: Type)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stateMachineType):
        """ __new__(cls: type, stateMachineType: Type) """
        pass


class AsyncMethodBuilderAttribute(Attribute, _Attribute):
    """ AsyncMethodBuilderAttribute(builderType: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, builderType):
        """ __new__(cls: type, builderType: Type) """
        pass

    BuilderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BuilderType(self: AsyncMethodBuilderAttribute) -> Type

"""



class AsyncStateMachineAttribute(StateMachineAttribute, _Attribute):
    """ AsyncStateMachineAttribute(stateMachineType: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stateMachineType):
        """ __new__(cls: type, stateMachineType: Type) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class AsyncVoidMethodBuilder(object):
    # no doc
    def AwaitOnCompleted(self, awaiter, stateMachine):
# Error generating skeleton for function AwaitOnCompleted: Method must be called on a Type for which Type.IsGenericParameter is false.

    def AwaitUnsafeOnCompleted(self, awaiter, stateMachine):
# Error generating skeleton for function AwaitUnsafeOnCompleted: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def Create():
        """ Create() -> AsyncVoidMethodBuilder """
        pass

    def SetException(self, exception):
        """ SetException(self: AsyncVoidMethodBuilder, exception: Exception) """
        pass

    def SetResult(self):
        """ SetResult(self: AsyncVoidMethodBuilder) """
        pass

    def SetStateMachine(self, stateMachine):
        """ SetStateMachine(self: AsyncVoidMethodBuilder, stateMachine: IAsyncStateMachine) """
        pass

    def Start(self, stateMachine):
# Error generating skeleton for function Start: Method must be called on a Type for which Type.IsGenericParameter is false.


class CallConvCdecl(object):
    """ CallConvCdecl() """

class CallConvFastcall(object):
    """ CallConvFastcall() """

class CallConvStdcall(object):
    """ CallConvStdcall() """

class CallConvThiscall(object):
    """ CallConvThiscall() """

class CallerFilePathAttribute(Attribute, _Attribute):
    """ CallerFilePathAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CallerLineNumberAttribute(Attribute, _Attribute):
    """ CallerLineNumberAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CallerMemberNameAttribute(Attribute, _Attribute):
    """ CallerMemberNameAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class CompilationRelaxations(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) CompilationRelaxations, values: NoStringInterning (8) """
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

    NoStringInterning = None
    value__ = None


class CompilationRelaxationsAttribute(Attribute, _Attribute):
    """
    CompilationRelaxationsAttribute(relaxations: int)
    CompilationRelaxationsAttribute(relaxations: CompilationRelaxations)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, relaxations):
        """
        __new__(cls: type, relaxations: int)
        __new__(cls: type, relaxations: CompilationRelaxations)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    CompilationRelaxations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompilationRelaxations(self: CompilationRelaxationsAttribute) -> int

"""



class CompilerGeneratedAttribute(Attribute, _Attribute):
    """ CompilerGeneratedAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class CompilerGlobalScopeAttribute(Attribute, _Attribute):
    """ CompilerGlobalScopeAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class CompilerMarshalOverride(object):
    # no doc
    __all__ = []


class ConditionalWeakTable(object):
    """ ConditionalWeakTable[TKey, TValue]() """
    def Add(self, key, value):
        """ Add(self: ConditionalWeakTable[TKey, TValue], key: TKey, value: TValue) """
        pass

    def GetOrCreateValue(self, key):
        """ GetOrCreateValue(self: ConditionalWeakTable[TKey, TValue], key: TKey) -> TValue """
        pass

    def GetValue(self, key, createValueCallback):
        """ GetValue(self: ConditionalWeakTable[TKey, TValue], key: TKey, createValueCallback: CreateValueCallback) -> TValue """
        pass

    def Remove(self, key):
        """ Remove(self: ConditionalWeakTable[TKey, TValue], key: TKey) -> bool """
        pass

    def TryGetValue(self, key, value):
        """ TryGetValue(self: ConditionalWeakTable[TKey, TValue], key: TKey) -> (bool, TValue) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    CreateValueCallback = None


class ConfiguredAsyncDisposable(object):
    """ Provides a type that can be used to configure how awaits on an System.IAsyncDisposable are performed. """
    def DisposeAsync(self):
        """ DisposeAsync(self: ConfiguredAsyncDisposable) -> ConfiguredValueTaskAwaitable """
        pass


class ConfiguredCancelableAsyncEnumerable(object):
    # no doc
    def ConfigureAwait(self, continueOnCapturedContext):
        """
        ConfigureAwait(self: ConfiguredCancelableAsyncEnumerable[T], continueOnCapturedContext: bool) -> ConfiguredCancelableAsyncEnumerable[T]
        
            Configures how awaits on the tasks returned from an async iteration will be performed.
        
            continueOnCapturedContext: Whether to capture and marshal back to the current context.
            Returns: The configured enumerable.
        """
        pass

    def GetAsyncEnumerator(self):
        """ GetAsyncEnumerator(self: ConfiguredCancelableAsyncEnumerable[T]) -> Enumerator """
        pass

    def WithCancellation(self, cancellationToken):
        """
        WithCancellation(self: ConfiguredCancelableAsyncEnumerable[T], cancellationToken: CancellationToken) -> ConfiguredCancelableAsyncEnumerable[T]
        
            Sets the System.Threading.CancellationToken to be passed to System.Collections.Generic.IAsyncEnumerable when iterating.
        
            cancellationToken: The System.Threading.CancellationToken to use.
            Returns: The configured enumerable.
        """
        pass

    Enumerator = None


class ContractHelper(object):
    # no doc
    @staticmethod
    def RaiseContractFailedEvent(failureKind, userMessage, conditionText, innerException):
        """ RaiseContractFailedEvent(failureKind: ContractFailureKind, userMessage: str, conditionText: str, innerException: Exception) -> str """
        pass

    @staticmethod
    def TriggerFailure(kind, displayMessage, userMessage, conditionText, innerException):
        """ TriggerFailure(kind: ContractFailureKind, displayMessage: str, userMessage: str, conditionText: str, innerException: Exception) """
        pass

    __all__ = [
        'RaiseContractFailedEvent',
        'TriggerFailure',
    ]


class CustomConstantAttribute(Attribute, _Attribute):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: CustomConstantAttribute) -> object

"""



class DateTimeConstantAttribute(CustomConstantAttribute, _Attribute):
    """ DateTimeConstantAttribute(ticks: Int64) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, ticks):
        """ __new__(cls: type, ticks: Int64) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DateTimeConstantAttribute) -> object

"""



class DecimalConstantAttribute(Attribute, _Attribute):
    """
    DecimalConstantAttribute(scale: Byte, sign: Byte, hi: UInt32, mid: UInt32, low: UInt32)
    DecimalConstantAttribute(scale: Byte, sign: Byte, hi: int, mid: int, low: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, scale, sign, hi, mid, low):
        """
        __new__(cls: type, scale: Byte, sign: Byte, hi: UInt32, mid: UInt32, low: UInt32)
        __new__(cls: type, scale: Byte, sign: Byte, hi: int, mid: int, low: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DecimalConstantAttribute) -> Decimal

"""



class DefaultDependencyAttribute(Attribute, _Attribute):
    """ DefaultDependencyAttribute(loadHintArgument: LoadHint) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, loadHintArgument):
        """ __new__(cls: type, loadHintArgument: LoadHint) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    LoadHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadHint(self: DefaultDependencyAttribute) -> LoadHint

"""



class DependencyAttribute(Attribute, _Attribute):
    """ DependencyAttribute(dependentAssemblyArgument: str, loadHintArgument: LoadHint) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dependentAssemblyArgument, loadHintArgument):
        """ __new__(cls: type, dependentAssemblyArgument: str, loadHintArgument: LoadHint) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    DependentAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DependentAssembly(self: DependencyAttribute) -> str

"""

    LoadHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadHint(self: DependencyAttribute) -> LoadHint

"""



class DisablePrivateReflectionAttribute(Attribute, _Attribute):
    """ DisablePrivateReflectionAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class DiscardableAttribute(Attribute, _Attribute):
    """ DiscardableAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class EnumeratorCancellationAttribute(Attribute, _Attribute):
    """ EnumeratorCancellationAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ExtensionAttribute(Attribute, _Attribute):
    """ ExtensionAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class FixedAddressValueTypeAttribute(Attribute, _Attribute):
    """ FixedAddressValueTypeAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class FixedBufferAttribute(Attribute, _Attribute):
    """ FixedBufferAttribute(elementType: Type, length: int) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, elementType, length):
        """ __new__(cls: type, elementType: Type, length: int) """
        pass

    ElementType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementType(self: FixedBufferAttribute) -> Type

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: FixedBufferAttribute) -> int

"""



class FormattableStringFactory(object):
    # no doc
    @staticmethod
    def Create(format, arguments):
        """ Create(format: str, *arguments: Array[object]) -> FormattableString """
        pass

    __all__ = [
        'Create',
    ]


class HasCopySemanticsAttribute(Attribute, _Attribute):
    """ HasCopySemanticsAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class IAsyncStateMachine:
    # no doc
    def MoveNext(self):
        """ MoveNext(self: IAsyncStateMachine) """
        pass

    def SetStateMachine(self, stateMachine):
        """ SetStateMachine(self: IAsyncStateMachine, stateMachine: IAsyncStateMachine) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class INotifyCompletion:
    # no doc
    def OnCompleted(self, continuation):
        """ OnCompleted(self: INotifyCompletion, continuation: Action) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ICriticalNotifyCompletion(INotifyCompletion):
    # no doc
    def UnsafeOnCompleted(self, continuation):
        """ UnsafeOnCompleted(self: ICriticalNotifyCompletion, continuation: Action) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDispatchConstantAttribute(CustomConstantAttribute, _Attribute):
    """ IDispatchConstantAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: IDispatchConstantAttribute) -> object

"""



class IndexerNameAttribute(Attribute, _Attribute):
    """ IndexerNameAttribute(indexerName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, indexerName):
        """ __new__(cls: type, indexerName: str) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class InternalsVisibleToAttribute(Attribute, _Attribute):
    """ InternalsVisibleToAttribute(assemblyName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, assemblyName):
        """ __new__(cls: type, assemblyName: str) """
        pass

    AllInternalsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllInternalsVisible(self: InternalsVisibleToAttribute) -> bool

Set: AllInternalsVisible(self: InternalsVisibleToAttribute) = value
"""

    AssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyName(self: InternalsVisibleToAttribute) -> str

"""



class IsBoxed(object):
    # no doc
    __all__ = []


class IsByRefLikeAttribute(Attribute, _Attribute):
    """ IsByRefLikeAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IsByValue(object):
    # no doc
    __all__ = []


class IsConst(object):
    # no doc
    __all__ = []


class IsCopyConstructed(object):
    # no doc
    __all__ = []


class IsExplicitlyDereferenced(object):
    # no doc
    __all__ = []


class IsImplicitlyDereferenced(object):
    # no doc
    __all__ = []


class IsJitIntrinsic(object):
    # no doc
    __all__ = []


class IsLong(object):
    # no doc
    __all__ = []


class IsPinned(object):
    # no doc
    __all__ = []


class IsReadOnlyAttribute(Attribute, _Attribute):
    """ IsReadOnlyAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IsSignUnspecifiedByte(object):
    # no doc
    __all__ = []


class IsUdtReturn(object):
    # no doc
    __all__ = []


class IsVolatile(object):
    # no doc
    __all__ = []


class IteratorStateMachineAttribute(StateMachineAttribute, _Attribute):
    """ IteratorStateMachineAttribute(stateMachineType: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, stateMachineType):
        """ __new__(cls: type, stateMachineType: Type) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class ITuple:
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: ITuple) -> int

"""



class IUnknownConstantAttribute(CustomConstantAttribute, _Attribute):
    """ IUnknownConstantAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: IUnknownConstantAttribute) -> object

"""



class LoadHint(Enum, IComparable, IFormattable, IConvertible):
    """ enum LoadHint, values: Always (1), Default (0), Sometimes (2) """
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

    Always = None
    Default = None
    Sometimes = None
    value__ = None


class MethodCodeType(Enum, IComparable, IFormattable, IConvertible):
    """ enum MethodCodeType, values: IL (0), Native (1), OPTIL (2), Runtime (3) """
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

    IL = None
    Native = None
    OPTIL = None
    Runtime = None
    value__ = None


class MethodImplAttribute(Attribute, _Attribute):
    """
    MethodImplAttribute(methodImplOptions: MethodImplOptions)
    MethodImplAttribute(value: Int16)
    MethodImplAttribute()
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, methodImplOptions: MethodImplOptions)
        __new__(cls: type, value: Int16)
        __new__(cls: type)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MethodImplAttribute) -> MethodImplOptions

"""


    MethodCodeType = None


class MethodImplOptions(Enum, IComparable, IFormattable, IConvertible):
    """ enum (flags) MethodImplOptions, values: AggressiveInlining (256), ForwardRef (16), InternalCall (4096), NoInlining (8), NoOptimization (64), PreserveSig (128), SecurityMitigations (1024), Synchronized (32), Unmanaged (4) """
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
    ForwardRef = None
    InternalCall = None
    NoInlining = None
    NoOptimization = None
    PreserveSig = None
    SecurityMitigations = None
    Synchronized = None
    Unmanaged = None
    value__ = None


class NativeCppClassAttribute(Attribute, _Attribute):
    """ NativeCppClassAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class ReferenceAssemblyAttribute(Attribute, _Attribute):
    """
    ReferenceAssemblyAttribute()
    ReferenceAssemblyAttribute(description: str)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, description=None):
        """
        __new__(cls: type)
        __new__(cls: type, description: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ReferenceAssemblyAttribute) -> str

"""



class RequiredAttributeAttribute(Attribute, _Attribute):
    """ RequiredAttributeAttribute(requiredContract: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, requiredContract):
        """ __new__(cls: type, requiredContract: Type) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    RequiredContract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequiredContract(self: RequiredAttributeAttribute) -> Type

"""



class RuntimeCompatibilityAttribute(Attribute, _Attribute):
    """ RuntimeCompatibilityAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    WrapNonExceptionThrows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrapNonExceptionThrows(self: RuntimeCompatibilityAttribute) -> bool

Set: WrapNonExceptionThrows(self: RuntimeCompatibilityAttribute) = value
"""



class RuntimeFeature(object):
    # no doc
    @staticmethod
    def IsSupported(feature):
        """ IsSupported(feature: str) -> bool """
        pass

    PortablePdb = 'PortablePdb'
    __all__ = [
        'IsSupported',
        'PortablePdb',
    ]


class RuntimeHelpers(object):
    # no doc
    @staticmethod
    def EnsureSufficientExecutionStack():
        """ EnsureSufficientExecutionStack() """
        pass

    @staticmethod
    def Equals(*__args):
        """ Equals(o1: object, o2: object) -> bool """
        pass

    @staticmethod
    def ExecuteCodeWithGuaranteedCleanup(code, backoutCode, userData):
        """ ExecuteCodeWithGuaranteedCleanup(code: TryCode, backoutCode: CleanupCode, userData: object) """
        pass

    @staticmethod
    def GetHashCode(o=None):
        """ GetHashCode(o: object) -> int """
        pass

    @staticmethod
    def GetObjectValue(obj):
        """ GetObjectValue(obj: object) -> object """
        pass

    @staticmethod
    def InitializeArray(array, fldHandle):
        """ InitializeArray(array: Array, fldHandle: RuntimeFieldHandle) """
        pass

    @staticmethod
    def PrepareConstrainedRegions():
        """ PrepareConstrainedRegions() """
        pass

    @staticmethod
    def PrepareConstrainedRegionsNoOP():
        """ PrepareConstrainedRegionsNoOP() """
        pass

    @staticmethod
    def PrepareContractedDelegate(d):
        """ PrepareContractedDelegate(d: Delegate) """
        pass

    @staticmethod
    def PrepareDelegate(d):
        """ PrepareDelegate(d: Delegate) """
        pass

    @staticmethod
    def PrepareMethod(method, instantiation=None):
        """ PrepareMethod(method: RuntimeMethodHandle)PrepareMethod(method: RuntimeMethodHandle, instantiation: Array[RuntimeTypeHandle]) """
        pass

    @staticmethod
    def ProbeForSufficientStack():
        """ ProbeForSufficientStack() """
        pass

    @staticmethod
    def RunClassConstructor(type):
        """ RunClassConstructor(type: RuntimeTypeHandle) """
        pass

    @staticmethod
    def RunModuleConstructor(module):
        """ RunModuleConstructor(module: ModuleHandle) """
        pass

    CleanupCode = None
    OffsetToStringData = 12
    TryCode = None
    __all__ = [
        'CleanupCode',
        'EnsureSufficientExecutionStack',
        'Equals',
        'ExecuteCodeWithGuaranteedCleanup',
        'GetHashCode',
        'GetObjectValue',
        'InitializeArray',
        'PrepareConstrainedRegions',
        'PrepareConstrainedRegionsNoOP',
        'PrepareContractedDelegate',
        'PrepareDelegate',
        'PrepareMethod',
        'ProbeForSufficientStack',
        'RunClassConstructor',
        'RunModuleConstructor',
        'TryCode',
    ]


class RuntimeWrappedException(Exception, ISerializable, _Exception):
    # no doc
    def GetObjectData(self, info, context):
        """ GetObjectData(self: RuntimeWrappedException, info: SerializationInfo, context: StreamingContext) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    WrappedException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedException(self: RuntimeWrappedException) -> object

"""


    SerializeObjectState = None


class ScopelessEnumAttribute(Attribute, _Attribute):
    """ ScopelessEnumAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SpecialNameAttribute(Attribute, _Attribute):
    """ SpecialNameAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class StringFreezingAttribute(Attribute, _Attribute):
    """ StringFreezingAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class SuppressIldasmAttribute(Attribute, _Attribute):
    """ SuppressIldasmAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class TupleElementNamesAttribute(Attribute, _Attribute):
    """ TupleElementNamesAttribute(transformNames: Array[str]) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, transformNames):
        """ __new__(cls: type, transformNames: Array[str]) """
        pass

    TransformNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformNames(self: TupleElementNamesAttribute) -> IList[str]

"""



class TypeForwardedFromAttribute(Attribute, _Attribute):
    """ TypeForwardedFromAttribute(assemblyFullName: str) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, assemblyFullName):
        """ __new__(cls: type, assemblyFullName: str) """
        pass

    AssemblyFullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyFullName(self: TypeForwardedFromAttribute) -> str

"""



class TypeForwardedToAttribute(Attribute, _Attribute):
    """ TypeForwardedToAttribute(destination: Type) """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, destination):
        """ __new__(cls: type, destination: Type) """
        pass

    Destination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Destination(self: TypeForwardedToAttribute) -> Type

"""



class Unsafe(object):
    """ Contains generic, low-level functionality for manipulating pointers. """
    @staticmethod
    def Add(source, elementOffset):
        """
        Add[T](source: T, elementOffset: int) -> (T, T)
        Add[T](source: Void*, elementOffset: int) -> Void*
        Add[T](source: T, elementOffset: IntPtr) -> (T, T)
        """
        pass

    @staticmethod
    def AddByteOffset(source, byteOffset):
        """ AddByteOffset[T](source: T, byteOffset: IntPtr) -> (T, T) """
        pass

    @staticmethod
    def AreSame(left, right):
        """ AreSame[T](left: T, right: T) -> (bool, T, T) """
        pass

    @staticmethod
    def As(*__args):
        """
        As[T](o: object) -> T
        As[(TFrom, TTo)](source: TFrom) -> (TTo, TFrom)
        """
        pass

    @staticmethod
    def AsPointer(value):
        """ AsPointer[T](value: T) -> (Void*, T) """
        pass

    @staticmethod
    def AsRef(source):
        """
        AsRef[T](source: Void*) -> T
        AsRef[T](source: T) -> (T, T)
        """
        pass

    @staticmethod
    def ByteOffset(origin, target):
        """ ByteOffset[T](origin: T, target: T) -> (IntPtr, T, T) """
        pass

    @staticmethod
    def Copy(destination, source):
        """
        Copy[T](destination: Void*, source: T) -> T
        Copy[T](destination: T, source: Void*) -> T
        """
        pass

    @staticmethod
    def CopyBlock(destination, source, byteCount):
        """
        CopyBlock(destination: Void*, source: Void*, byteCount: UInt32)
            Copies bytes from the source address to the destination address.
        
            destination: The destination address to copy to.
            source: The source address to copy from.
            byteCount: The number of bytes to copy.
        CopyBlock(destination: Byte, source: Byte, byteCount: UInt32) -> (Byte, Byte)
        
            Copies bytes from the source address to the destination address.
        
            destination: The destination address to copy to.
            source: The source address to copy from.
            byteCount: The number of bytes to copy.
        """
        pass

    @staticmethod
    def CopyBlockUnaligned(destination, source, byteCount):
        """
        CopyBlockUnaligned(destination: Void*, source: Void*, byteCount: UInt32)
            Copies bytes from the source address to the destination address 
        without assuming architecture dependent alignment of the addresses.
        
            destination: The destination address to copy to.
            source: The source address to copy from.
            byteCount: The number of bytes to copy.
        CopyBlockUnaligned(destination: Byte, source: Byte, byteCount: UInt32) -> (Byte, Byte)
        
            Copies bytes from the source address to the destination address 
        without assuming architecture dependent alignment of the addresses.
        
            destination: The destination address to copy to.
            source: The source address to copy from.
            byteCount: The number of bytes to copy.
        """
        pass

    @staticmethod
    def InitBlock(startAddress, value, byteCount):
        """
        InitBlock(startAddress: Void*, value: Byte, byteCount: UInt32)
            Initializes a block of memory at the given location with a given initial value.
        
            startAddress: The address of the start of the memory block to initialize.
            value: The value to initialize the block to.
            byteCount: The number of bytes to initialize.
        InitBlock(startAddress: Byte, value: Byte, byteCount: UInt32) -> Byte
        
            Initializes a block of memory at the given location with a given initial value.
        
            startAddress: The address of the start of the memory block to initialize.
            value: The value to initialize the block to.
            byteCount: The number of bytes to initialize.
        """
        pass

    @staticmethod
    def InitBlockUnaligned(startAddress, value, byteCount):
        """
        InitBlockUnaligned(startAddress: Void*, value: Byte, byteCount: UInt32)
            Initializes a block of memory at the given location with a given initial value 
        without assuming architecture dependent alignment of the address.
        
            startAddress: The address of the start of the memory block to initialize.
            value: The value to initialize the block to.
            byteCount: The number of bytes to initialize.
        InitBlockUnaligned(startAddress: Byte, value: Byte, byteCount: UInt32) -> Byte
        
            Initializes a block of memory at the given location with a given initial value 
        without assuming architecture dependent alignment of the address.
        
            startAddress: The address of the start of the memory block to initialize.
            value: The value to initialize the block to.
            byteCount: The number of bytes to initialize.
        """
        pass

    @staticmethod
    def IsAddressGreaterThan(left, right):
        """ IsAddressGreaterThan[T](left: T, right: T) -> (bool, T, T) """
        pass

    @staticmethod
    def IsAddressLessThan(left, right):
        """ IsAddressLessThan[T](left: T, right: T) -> (bool, T, T) """
        pass

    @staticmethod
    def Read(source):
        """ Read[T](source: Void*) -> T """
        pass

    @staticmethod
    def ReadUnaligned(source):
        """
        ReadUnaligned[T](source: Void*) -> T
        ReadUnaligned[T](source: Byte) -> (T, Byte)
        """
        pass

    @staticmethod
    def SizeOf():
        """ SizeOf[T]() -> int """
        pass

    @staticmethod
    def Subtract(source, elementOffset):
        """
        Subtract[T](source: T, elementOffset: int) -> (T, T)
        Subtract[T](source: Void*, elementOffset: int) -> Void*
        Subtract[T](source: T, elementOffset: IntPtr) -> (T, T)
        """
        pass

    @staticmethod
    def SubtractByteOffset(source, byteOffset):
        """ SubtractByteOffset[T](source: T, byteOffset: IntPtr) -> (T, T) """
        pass

    @staticmethod
    def Write(destination, value):
        """ Write[T](destination: Void*, value: T) """
        pass

    @staticmethod
    def WriteUnaligned(destination, value):
        """ WriteUnaligned[T](destination: Void*, value: T)WriteUnaligned[T](destination: Byte, value: T) -> Byte """
        pass

    __all__ = [
        'Add',
        'AddByteOffset',
        'AreSame',
        'As',
        'AsPointer',
        'AsRef',
        'ByteOffset',
        'Copy',
        'CopyBlock',
        'CopyBlockUnaligned',
        'InitBlock',
        'InitBlockUnaligned',
        'IsAddressGreaterThan',
        'IsAddressLessThan',
        'Read',
        'ReadUnaligned',
        'SizeOf',
        'Subtract',
        'SubtractByteOffset',
        'Write',
        'WriteUnaligned',
    ]


class UnsafeValueTypeAttribute(Attribute, _Attribute):
    """ UnsafeValueTypeAttribute() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class YieldAwaitable(object):
    # no doc
    def GetAwaiter(self):
        """ GetAwaiter(self: YieldAwaitable) -> YieldAwaiter """
        pass

    YieldAwaiter = None


