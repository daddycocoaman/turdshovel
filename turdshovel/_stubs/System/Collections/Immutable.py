# encoding: utf-8
# module System.Collections.Immutable calls itself Immutable
# from System.Collections.Immutable, Version=5.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# functions

def ImmutableArray(*args, **kwargs): # real signature unknown
    """
    Provides methods for creating an array that is immutable; meaning it cannot be changed once it is created.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableDictionary(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableDictionary class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableHashSet(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableHashSet class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableList(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableList class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableQueue(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableQueue class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableSortedDictionary(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableSortedDictionary class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableSortedSet(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableSortedSet class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

def ImmutableStack(*args, **kwargs): # real signature unknown
    """
    Provides a set of initialization methods for instances of the System.Collections.Immutable.ImmutableStack class.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    pass

# classes

class IImmutableDictionary(IReadOnlyDictionary[TKey, TValue], IReadOnlyCollection[KeyValuePair[TKey, TValue]], IEnumerable[KeyValuePair[TKey, TValue]], IEnumerable):
    # no doc
    def Add(self, key, value):
        """
        Add(self: IImmutableDictionary[TKey, TValue], key: TKey, value: TValue) -> IImmutableDictionary[TKey, TValue]
        
            Adds an element with the specified key and value to the dictionary.
        
            key: The key of the element to add.
            value: The value of the element to add.
            Returns: A new immutable dictionary that contains the additional key/value pair.
        """
        pass

    def AddRange(self, pairs):
        """ AddRange(self: IImmutableDictionary[TKey, TValue], pairs: IEnumerable[KeyValuePair[TKey, TValue]]) -> IImmutableDictionary[TKey, TValue] """
        pass

    def Clear(self):
        """
        Clear(self: IImmutableDictionary[TKey, TValue]) -> IImmutableDictionary[TKey, TValue]
        
            Retrieves an empty dictionary that has the same ordering and key/value comparison rules as this dictionary instance.
            Returns: An empty dictionary with equivalent ordering and key/value comparison rules.
        """
        pass

    def Contains(self, pair):
        """
        Contains(self: IImmutableDictionary[TKey, TValue], pair: KeyValuePair[TKey, TValue]) -> bool
        
            Determines whether the immutable dictionary contains the specified key/value pair.
        
            pair: The key/value pair to locate.
            Returns: ue if the specified key/value pair is found in the dictionary; otherwise, lse.
        """
        pass

    def Remove(self, key):
        """
        Remove(self: IImmutableDictionary[TKey, TValue], key: TKey) -> IImmutableDictionary[TKey, TValue]
        
            Removes the element with the specified key from the immutable dictionary.
        
            key: The key of the element to remove.
            Returns: A new immutable dictionary with the specified element removed; or this instance if the specified key cannot be found in the dictionary.
        """
        pass

    def RemoveRange(self, keys):
        """
        RemoveRange(self: IImmutableDictionary[TKey, TValue], keys: IEnumerable[TKey]) -> IImmutableDictionary[TKey, TValue]
        
            Removes the elements with the specified keys from the immutable dictionary.
        
            keys: The keys of the elements to remove.
            Returns: A new immutable dictionary with the specified keys removed; or this instance if the specified keys cannot be found in the dictionary.
        """
        pass

    def SetItem(self, key, value):
        """
        SetItem(self: IImmutableDictionary[TKey, TValue], key: TKey, value: TValue) -> IImmutableDictionary[TKey, TValue]
        
            Sets the specified key and value in the immutable dictionary, possibly overwriting an existing value for the key.
        
            key: The key of the entry to add.
            value: The key value to set.
            Returns: A new immutable dictionary that contains the specified key/value pair.
        """
        pass

    def SetItems(self, items):
        """ SetItems(self: IImmutableDictionary[TKey, TValue], items: IEnumerable[KeyValuePair[TKey, TValue]]) -> IImmutableDictionary[TKey, TValue] """
        pass

    def TryGetKey(self, equalKey, actualKey):
        """ TryGetKey(self: IImmutableDictionary[TKey, TValue], equalKey: TKey) -> (bool, TKey) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair`2](enumerable: IEnumerable[KeyValuePair[TKey, TValue]], value: KeyValuePair[TKey, TValue]) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class IImmutableList(IReadOnlyList[T], IReadOnlyCollection[T], IEnumerable[T], IEnumerable):
    # no doc
    def Add(self, value):
        """
        Add(self: IImmutableList[T], value: T) -> IImmutableList[T]
        
            Makes a copy of the list, and adds the specified object to the end of the  copied list.
        
            value: The object to add to the list.
            Returns: A new list with the object added.
        """
        pass

    def AddRange(self, items):
        """
        AddRange(self: IImmutableList[T], items: IEnumerable[T]) -> IImmutableList[T]
        
            Makes a copy of the list and adds the specified objects to the end of the copied list.
        
            items: The objects to add to the list.
            Returns: A new list with the elements added.
        """
        pass

    def Clear(self):
        """
        Clear(self: IImmutableList[T]) -> IImmutableList[T]
        
            Creates  a list with all the items removed, but with the same sorting and ordering semantics as this list.
            Returns: An empty list that has the same sorting and ordering semantics as this instance.
        """
        pass

    def IndexOf(self, item, index, count, equalityComparer):
        """
        IndexOf(self: IImmutableList[T], item: T, index: int, count: int, equalityComparer: IEqualityComparer[T]) -> int
        
            Searches for the specified object and returns the zero-based index of the first occurrence within the range of elements in the System.Collections.Immutable.IImmutableList that starts 
             at the specified index and contains the specified number of elements.
        
        
            item: The object to locate in the System.Collections.Immutable.IImmutableList. This value can be null for reference types.
            index: The zero-based starting indexes of the search. 0 (zero) is valid in an empty list.
            count: The number of elements in the section to search.
            equalityComparer: The equality comparer to use to locate item.
            Returns: The zero-based index of the first occurrence of item within the range of elements in the System.Collections.Immutable.IImmutableList that starts at index and contains count number of 
             elements if found; otherwise -1.
        """
        pass

    def Insert(self, index, element):
        """
        Insert(self: IImmutableList[T], index: int, element: T) -> IImmutableList[T]
        
            Inserts the specified element at the specified index in the immutable list.
        
            index: The zero-based index at which to insert the value.
            element: The object to insert.
            Returns: A new immutable list that includes the specified element.
        """
        pass

    def InsertRange(self, index, items):
        """
        InsertRange(self: IImmutableList[T], index: int, items: IEnumerable[T]) -> IImmutableList[T]
        
            Inserts the specified elements at the specified index in the immutable list.
        
            index: The zero-based index at which the new elements should be inserted.
            items: The elements to insert.
            Returns: A new immutable list that includes the specified elements.
        """
        pass

    def LastIndexOf(self, item, index, count, equalityComparer):
        """
        LastIndexOf(self: IImmutableList[T], item: T, index: int, count: int, equalityComparer: IEqualityComparer[T]) -> int
        
            Searches for the specified object and returns the zero-based index of the last occurrence within the range of elements in the System.Collections.Immutable.IImmutableList that 
             contains the specified number of elements and ends at the specified index.
        
        
            item: The object to locate in the list. The value can be ll for reference types.
            index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            count: The number of elements in the section to search.
            equalityComparer: The equality comparer to match item.
            Returns: Returns System.Int32.
        """
        pass

    def Remove(self, value, equalityComparer):
        """
        Remove(self: IImmutableList[T], value: T, equalityComparer: IEqualityComparer[T]) -> IImmutableList[T]
        
            Removes the first occurrence of a specified object from this immutable list.
        
            value: The object to remove from the list.
            equalityComparer: The equality comparer to use to locate value.
            Returns: A new list with the specified object removed.
        """
        pass

    def RemoveAll(self, match):
        """
        RemoveAll(self: IImmutableList[T], match: Predicate[T]) -> IImmutableList[T]
        
            Removes all the elements that match the conditions defined by the specified predicate.
        
            match: The delegate that defines the conditions of the elements to remove.
            Returns: A new immutable list with the elements removed.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: IImmutableList[T], index: int) -> IImmutableList[T]
        
            Removes the element at the specified index of the immutable list.
        
            index: The index of the element to remove.
            Returns: A new list with the element removed.
        """
        pass

    def RemoveRange(self, *__args):
        """
        RemoveRange(self: IImmutableList[T], items: IEnumerable[T], equalityComparer: IEqualityComparer[T]) -> IImmutableList[T]
        
            Removes the specified object from the list.
        
            items: The objects to remove from the list.
            equalityComparer: The equality comparer to use to determine if items match any objects in the list.
            Returns: A new immutable list with the specified objects removed, if items matched objects in the list.
        RemoveRange(self: IImmutableList[T], index: int, count: int) -> IImmutableList[T]
        
            Removes a range of elements from the System.Collections.Immutable.IImmutableList.
        
            index: The zero-based starting index of the range of elements to remove.
            count: The number of elements to remove.
            Returns: A new immutable list with the elements removed.
        """
        pass

    def Replace(self, oldValue, newValue, equalityComparer):
        """
        Replace(self: IImmutableList[T], oldValue: T, newValue: T, equalityComparer: IEqualityComparer[T]) -> IImmutableList[T]
        
            Returns a new list with the first matching element in the list replaced with the specified element.
        
            oldValue: The element to be replaced.
            newValue: The element to replace the first occurrence of oldValue with
            equalityComparer: The equality comparer to use for matching oldValue.
            Returns: A new list that contains newValue, even if oldvalue is the same as newValue.
        """
        pass

    def SetItem(self, index, value):
        """
        SetItem(self: IImmutableList[T], index: int, value: T) -> IImmutableList[T]
        
            Replaces an element in the list at a given position with the specified element.
        
            index: The position in the list of the element to replace.
            value: The element to replace the old element with.
            Returns: A new list that contains the new element, even if the element at the specified location is the same as the new element.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass


class IImmutableQueue(IEnumerable[T], IEnumerable):
    # no doc
    def Clear(self):
        """
        Clear(self: IImmutableQueue[T]) -> IImmutableQueue[T]
        
            Returns a new queue with all the elements removed.
            Returns: An empty immutable queue.
        """
        pass

    def Dequeue(self):
        """
        Dequeue(self: IImmutableQueue[T]) -> IImmutableQueue[T]
        
            Removes the first element in the immutable queue, and returns the new queue.
            Returns: The new immutable queue with the first element removed. This value is never ll.
        """
        pass

    def Enqueue(self, value):
        """
        Enqueue(self: IImmutableQueue[T], value: T) -> IImmutableQueue[T]
        
            Adds an element to the end of the immutable queue, and returns the new queue.
        
            value: The element to add.
            Returns: The new immutable queue with the specified element added.
        """
        pass

    def Peek(self):
        """
        Peek(self: IImmutableQueue[T]) -> T
        
            Returns the element at the beginning of the immutable queue without removing it.
            Returns: The element at the beginning of the queue.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this immutable queue is empty.

Get: IsEmpty(self: IImmutableQueue[T]) -> bool

"""



class IImmutableSet(IReadOnlyCollection[T], IEnumerable[T], IEnumerable):
    # no doc
    def Add(self, value):
        """
        Add(self: IImmutableSet[T], value: T) -> IImmutableSet[T]
        
            Adds the specified element to this immutable set.
        
            value: The element to add.
            Returns: A new set with the element added, or this set if the element is already in the set.
        """
        pass

    def Clear(self):
        """
        Clear(self: IImmutableSet[T]) -> IImmutableSet[T]
        
            Retrieves an empty immutable set that has the same sorting and ordering semantics as this instance.
            Returns: An empty set that has the same sorting and ordering semantics as this instance.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: IImmutableSet[T], value: T) -> bool
        
            Determines whether this immutable set contains a specified element.
        
            value: The element to locate in the set.
            Returns: ue if the set contains the specified value; otherwise, lse.
        """
        pass

    def Except(self, other):
        """
        Except(self: IImmutableSet[T], other: IEnumerable[T]) -> IImmutableSet[T]
        
            Removes the elements in the specified collection from the current immutable set.
        
            other: The collection of items to remove from this set.
            Returns: A new set with the items removed; or the original set if none of the items were in the set.
        """
        pass

    def Intersect(self, other):
        """
        Intersect(self: IImmutableSet[T], other: IEnumerable[T]) -> IImmutableSet[T]
        
            Creates an immutable set that contains only elements that exist in this set and the specified set.
        
            other: The collection to compare to the current System.Collections.Immutable.IImmutableSet.
            Returns: A new immutable set that contains elements that exist in both sets.
        """
        pass

    def IsProperSubsetOf(self, other):
        """
        IsProperSubsetOf(self: IImmutableSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current immutable set is a proper (strict) subset of the specified collection.
        
            other: The collection to compare to the current set.
            Returns: ue if the current set is a proper subset of the specified collection; otherwise, lse.
        """
        pass

    def IsProperSupersetOf(self, other):
        """
        IsProperSupersetOf(self: IImmutableSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current immutable set is a proper (strict) superset of the specified collection.
        
            other: The collection to compare to the current set.
            Returns: ue if the current set is a proper superset of the specified collection; otherwise, lse.
        """
        pass

    def IsSubsetOf(self, other):
        """
        IsSubsetOf(self: IImmutableSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current immutable set is a subset of a specified collection.
        
            other: The collection to compare to the current set.
            Returns: ue if the current set is a subset of the specified collection; otherwise, lse.
        """
        pass

    def IsSupersetOf(self, other):
        """
        IsSupersetOf(self: IImmutableSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current immutable set is a superset of a specified collection.
        
            other: The collection to compare to the current set.
            Returns: ue if the current set is a superset of the specified collection; otherwise, lse.
        """
        pass

    def Overlaps(self, other):
        """
        Overlaps(self: IImmutableSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current immutable set overlaps with the specified collection.
        
            other: The collection to compare to the current set.
            Returns: ue if the current set and the specified collection share at least one common element; otherwise, lse.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: IImmutableSet[T], value: T) -> IImmutableSet[T]
        
            Removes the specified element from this immutable set.
        
            value: The element to remove.
            Returns: A new set with the specified element removed, or the current set if the element cannot be found in the set.
        """
        pass

    def SetEquals(self, other):
        """
        SetEquals(self: IImmutableSet[T], other: IEnumerable[T]) -> bool
        
            Determines whether the current immutable set and the specified collection contain the same elements.
        
            other: The collection to compare to the current set.
            Returns: ue if the sets are equal; otherwise, lse.
        """
        pass

    def SymmetricExcept(self, other):
        """
        SymmetricExcept(self: IImmutableSet[T], other: IEnumerable[T]) -> IImmutableSet[T]
        
            Creates an immutable set that contains only elements that are present either in the current set or in the specified collection, but not both.
        
            other: The collection to compare to the current set.
            Returns: A new set that contains the elements that are present only in the current set or in the specified collection, but not both.
        """
        pass

    def TryGetValue(self, equalValue, actualValue):
        """ TryGetValue(self: IImmutableSet[T], equalValue: T) -> (bool, T) """
        pass

    def Union(self, other):
        """
        Union(self: IImmutableSet[T], other: IEnumerable[T]) -> IImmutableSet[T]
        
            Creates a new immutable set that contains all elements that are present in either the current set or in the specified collection.
        
            other: The collection to add elements from.
            Returns: A new immutable set with the items added; or the original set if all the items were already in the set.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class IImmutableStack(IEnumerable[T], IEnumerable):
    # no doc
    def Clear(self):
        """
        Clear(self: IImmutableStack[T]) -> IImmutableStack[T]
        
            Removes all objects from the immutable stack.
            Returns: An empty immutable stack.
        """
        pass

    def Peek(self):
        """
        Peek(self: IImmutableStack[T]) -> T
        
            Returns the element at the top of the immutable stack without removing it.
            Returns: The element at the top of the stack.
        """
        pass

    def Pop(self):
        """
        Pop(self: IImmutableStack[T]) -> IImmutableStack[T]
        
            Removes the element at the top of the immutable stack and returns the new stack.
            Returns: The new stack; never ll
        """
        pass

    def Push(self, value):
        """
        Push(self: IImmutableStack[T], value: T) -> IImmutableStack[T]
        
            Inserts an element at the top of the immutable stack and returns the new stack.
        
            value: The element to push onto the stack.
            Returns: The new stack.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether this immutable stack is empty.

Get: IsEmpty(self: IImmutableStack[T]) -> bool

"""



class ImmutableInterlocked(object):
    """
    Contains interlocked exchange mechanisms for immutable collections.  
      
     NuGet package: System.Collections.Immutable (about immutable collections and how to install)
    """
    @staticmethod
    def AddOrUpdate(location, key, *__args):
        """
        AddOrUpdate[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey, addValueFactory: Func[TKey, TValue], updateValueFactory: Func[TKey, TValue, TValue]) -> (TValue, ImmutableDictionary[TKey, TValue])
        AddOrUpdate[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey, addValue: TValue, updateValueFactory: Func[TKey, TValue, TValue]) -> (TValue, ImmutableDictionary[TKey, TValue])
        """
        pass

    @staticmethod
    def Enqueue(location, value):
        """ Enqueue[T](location: ImmutableQueue[T], value: T) -> ImmutableQueue[T] """
        pass

    @staticmethod
    def GetOrAdd(location, key, *__args):
        """
        GetOrAdd[(TKey, TValue, TArg)](location: ImmutableDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TArg, TValue], factoryArgument: TArg) -> (TValue, ImmutableDictionary[TKey, TValue])
        GetOrAdd[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey, valueFactory: Func[TKey, TValue]) -> (TValue, ImmutableDictionary[TKey, TValue])
        GetOrAdd[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey, value: TValue) -> (TValue, ImmutableDictionary[TKey, TValue])
        """
        pass

    @staticmethod
    def InterlockedCompareExchange(location, value, comparand):
        """ InterlockedCompareExchange[T](location: ImmutableArray[T], value: ImmutableArray[T], comparand: ImmutableArray[T]) -> (ImmutableArray[T], ImmutableArray[T]) """
        pass

    @staticmethod
    def InterlockedExchange(location, value):
        """ InterlockedExchange[T](location: ImmutableArray[T], value: ImmutableArray[T]) -> (ImmutableArray[T], ImmutableArray[T]) """
        pass

    @staticmethod
    def InterlockedInitialize(location, value):
        """ InterlockedInitialize[T](location: ImmutableArray[T], value: ImmutableArray[T]) -> (bool, ImmutableArray[T]) """
        pass

    @staticmethod
    def Push(location, value):
        """ Push[T](location: ImmutableStack[T], value: T) -> ImmutableStack[T] """
        pass

    @staticmethod
    def TryAdd(location, key, value):
        """ TryAdd[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey, value: TValue) -> (bool, ImmutableDictionary[TKey, TValue]) """
        pass

    @staticmethod
    def TryDequeue(location, value):
        """ TryDequeue[T](location: ImmutableQueue[T]) -> (bool, ImmutableQueue[T], T) """
        pass

    @staticmethod
    def TryPop(location, value):
        """ TryPop[T](location: ImmutableStack[T]) -> (bool, ImmutableStack[T], T) """
        pass

    @staticmethod
    def TryRemove(location, key, value):
        """ TryRemove[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey) -> (bool, ImmutableDictionary[TKey, TValue], TValue) """
        pass

    @staticmethod
    def TryUpdate(location, key, newValue, comparisonValue):
        """ TryUpdate[(TKey, TValue)](location: ImmutableDictionary[TKey, TValue], key: TKey, newValue: TValue, comparisonValue: TValue) -> (bool, ImmutableDictionary[TKey, TValue]) """
        pass

    @staticmethod
    def Update(location, transformer, transformerArgument=None):
        """
        Update[T](location: T, transformer: Func[T, T]) -> (bool, T)
        Update[(T, TArg)](location: T, transformer: Func[T, TArg, T], transformerArgument: TArg) -> (bool, T)
        Update[T](location: ImmutableArray[T], transformer: Func[ImmutableArray[T], ImmutableArray[T]]) -> (bool, ImmutableArray[T])
        Update[(T, TArg)](location: ImmutableArray[T], transformer: Func[ImmutableArray[T], TArg, ImmutableArray[T]], transformerArgument: TArg) -> (bool, ImmutableArray[T])
        """
        pass

    __all__ = [
        'AddOrUpdate',
        'Enqueue',
        'GetOrAdd',
        'InterlockedCompareExchange',
        'InterlockedExchange',
        'InterlockedInitialize',
        'Push',
        'TryAdd',
        'TryDequeue',
        'TryPop',
        'TryRemove',
        'TryUpdate',
        'Update',
    ]


