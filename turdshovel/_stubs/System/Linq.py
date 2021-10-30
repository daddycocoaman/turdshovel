# encoding: utf-8
# module System.Linq calls itself Linq
# from System.Collections.Immutable, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ImmutableArrayExtensions(object):
    """
    LINQ extension method overrides that offer greater efficiency for System.Collections.Immutable.ImmutableArray than the standard LINQ methods  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    @staticmethod
    def Aggregate(immutableArray, *__args):
        """
        Aggregate[T](immutableArray: ImmutableArray[T], func: Func[T, T, T]) -> T
        Aggregate[(TAccumulate, T)](immutableArray: ImmutableArray[T], seed: TAccumulate, func: Func[TAccumulate, T, TAccumulate]) -> TAccumulate
        Aggregate[(TAccumulate, TResult, T)](immutableArray: ImmutableArray[T], seed: TAccumulate, func: Func[TAccumulate, T, TAccumulate], resultSelector: Func[TAccumulate, TResult]) -> TResult
        """
        pass

    @staticmethod
    def All(immutableArray, predicate):
        """ All[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> bool """
        pass

    @staticmethod
    def Any(*__args):
        """
        Any[T](immutableArray: ImmutableArray[T]) -> bool
        Any[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> bool
        Any[T](builder: Builder) -> bool
        """
        pass

    @staticmethod
    def ElementAt(immutableArray, index):
        """ ElementAt[T](immutableArray: ImmutableArray[T], index: int) -> T """
        pass

    @staticmethod
    def ElementAtOrDefault(immutableArray, index):
        """ ElementAtOrDefault[T](immutableArray: ImmutableArray[T], index: int) -> T """
        pass

    @staticmethod
    def First(*__args):
        """
        First[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> T
        First[T](immutableArray: ImmutableArray[T]) -> T
        First[T](builder: Builder) -> T
        """
        pass

    @staticmethod
    def FirstOrDefault(*__args):
        """
        FirstOrDefault[T](immutableArray: ImmutableArray[T]) -> T
        FirstOrDefault[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> T
        FirstOrDefault[T](builder: Builder) -> T
        """
        pass

    @staticmethod
    def Last(*__args):
        """
        Last[T](immutableArray: ImmutableArray[T]) -> T
        Last[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> T
        Last[T](builder: Builder) -> T
        """
        pass

    @staticmethod
    def LastOrDefault(*__args):
        """
        LastOrDefault[T](immutableArray: ImmutableArray[T]) -> T
        LastOrDefault[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> T
        LastOrDefault[T](builder: Builder) -> T
        """
        pass

    @staticmethod
    def Select(immutableArray, selector):
        """ Select[(T, TResult)](immutableArray: ImmutableArray[T], selector: Func[T, TResult]) -> IEnumerable[TResult] """
        pass

    @staticmethod
    def SelectMany(immutableArray, collectionSelector, resultSelector):
        """ SelectMany[(TSource, TCollection, TResult)](immutableArray: ImmutableArray[TSource], collectionSelector: Func[TSource, IEnumerable[TCollection]], resultSelector: Func[TSource, TCollection, TResult]) -> IEnumerable[TResult] """
        pass

    @staticmethod
    def SequenceEqual(immutableArray, items, *__args):
        """
        SequenceEqual[(TDerived, TBase)](immutableArray: ImmutableArray[TBase], items: ImmutableArray[TDerived], comparer: IEqualityComparer[TBase]) -> bool
        SequenceEqual[(TDerived, TBase)](immutableArray: ImmutableArray[TBase], items: IEnumerable[TDerived], comparer: IEqualityComparer[TBase]) -> bool
        SequenceEqual[(TDerived, TBase)](immutableArray: ImmutableArray[TBase], items: ImmutableArray[TDerived], predicate: Func[TBase, TBase, bool]) -> bool
        """
        pass

    @staticmethod
    def Single(immutableArray, predicate=None):
        """
        Single[T](immutableArray: ImmutableArray[T]) -> T
        Single[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> T
        """
        pass

    @staticmethod
    def SingleOrDefault(immutableArray, predicate=None):
        """
        SingleOrDefault[T](immutableArray: ImmutableArray[T]) -> T
        SingleOrDefault[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> T
        """
        pass

    @staticmethod
    def ToArray(immutableArray):
        """ ToArray[T](immutableArray: ImmutableArray[T]) -> Array[T] """
        pass

    @staticmethod
    def ToDictionary(immutableArray, keySelector, *__args):
        """
        ToDictionary[(TKey, T)](immutableArray: ImmutableArray[T], keySelector: Func[T, TKey]) -> Dictionary[TKey, T]
        ToDictionary[(TKey, TElement, T)](immutableArray: ImmutableArray[T], keySelector: Func[T, TKey], elementSelector: Func[T, TElement]) -> Dictionary[TKey, TElement]
        ToDictionary[(TKey, T)](immutableArray: ImmutableArray[T], keySelector: Func[T, TKey], comparer: IEqualityComparer[TKey]) -> Dictionary[TKey, T]
        ToDictionary[(TKey, TElement, T)](immutableArray: ImmutableArray[T], keySelector: Func[T, TKey], elementSelector: Func[T, TElement], comparer: IEqualityComparer[TKey]) -> Dictionary[TKey, TElement]
        """
        pass

    @staticmethod
    def Where(immutableArray, predicate):
        """ Where[T](immutableArray: ImmutableArray[T], predicate: Func[T, bool]) -> IEnumerable[T] """
        pass

    __all__ = [
        'Aggregate',
        'All',
        'Any',
        'ElementAt',
        'ElementAtOrDefault',
        'First',
        'FirstOrDefault',
        'Last',
        'LastOrDefault',
        'Select',
        'SelectMany',
        'SequenceEqual',
        'Single',
        'SingleOrDefault',
        'ToArray',
        'ToDictionary',
        'Where',
    ]


