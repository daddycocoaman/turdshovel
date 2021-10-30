# encoding: utf-8
# module Microsoft.Diagnostics.Runtime.DataReaders.Implementation calls itself Implementation
# from Microsoft.Diagnostics.Runtime, Version=2.0.5.1201, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IThreadReader:
    """
    This interface is implemented by all ClrMD provided implementations of Microsoft.Diagnostics.Runtime.IDataReader.
                This interface is not used by the ClrMD library itself, but is here to maintain functionality
                for previous uses of these functions in ClrMD 1.1's Microsoft.Diagnostics.Runtime.IDataReader.
                
                This inteface must always be requested and not assumed to be there:
                
                    IDataReader reader = ...;
                
                    if (reader is IThreadReader threadReader)
                        ...
    """
    def EnumerateOSThreadIds(self):
        """
        EnumerateOSThreadIds(self: IThreadReader) -> IEnumerable[UInt32]
        
            Enumerates the thread ids of all live threads in the target process.
        """
        pass

    def GetThreadTeb(self, osThreadId):
        """
        GetThreadTeb(self: IThreadReader, osThreadId: UInt32) -> UInt64
        
            Obtains the Windows specific Thread Execution Block.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


