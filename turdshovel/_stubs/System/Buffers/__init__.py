# encoding: utf-8
# module System.Buffers calls itself Buffers
# from System.Buffers, Version=4.0.3.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ArrayPool(object):
    # no doc
    @staticmethod
    def Create(maxArrayLength=None, maxArraysPerBucket=None):
        """
        Create() -> ArrayPool[T]
        
            Creates a new instance of the System.Buffers.ArrayPool class.
            Returns: A new instance of the stem.Buffers.ArrayPool class.
        Create(maxArrayLength: int, maxArraysPerBucket: int) -> ArrayPool[T]
        
            Creates a new instance of the System.Buffers.ArrayPool class using the specifed configuration.
        
            maxArrayLength: The maximum length of an array instance that may be stored in the pool.
            maxArraysPerBucket: The maximum number of array instances that may be stored in each bucket in the pool. The pool groups arrays of similar lengths into buckets for faster access.
            Returns: A new instance of the stem.Buffers.ArrayPool class with the specified configuration.
        """
        pass

    def Rent(self, minimumLength):
        """
        Rent(self: ArrayPool[T], minimumLength: int) -> Array[T]
        
            Retrieves a buffer that is at least the requested length.
        
            minimumLength: The minimum length of the array.
            Returns: An array of type ] that is at least minimumLengthminimumLength in length.
        """
        pass

    def Return(self, array, clearArray):
        """ Return(self: ArrayPool[T], array: Array[T], clearArray: bool) """
        pass


