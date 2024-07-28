from typing import List
from ..utils.str_helpers import str_to_list
from os import rename,remove
from shutil import copy as cp

"""
a filio can be described as an program watching for changes
in a directory
each program will be run in parallel using multiple threads
although using 'async' would save alot of memory consumption
and alot of cpu intensive tasks it would be hard to implement

Filio is the parent class for the Action Filio classes
such as:
    -> MovFilio
    -> CopyFilio
    -> DelFilio
"""



class Filio:
    def __init__(
            self,
            input : str,
            output : str,
            action : str,
            names : str,
            prefix : str | None = None,
            extension : str | None = None,
            ) -> None:
        """
            input -> the input directory to be watched
            output -> the output directory to be watched
            action -> the action to be preformed on the file (mov,cop,del)
            names -> the name of the files to invoke the action with
            extension -> if the name matches than should we filter by extension [Optional]
            prefix -> whether the given file should or should not be moved or copied with a prefix [Optional]
        """
        self.input : str = input
        self.output : str = output
        self.action : str = action
        self.names : List[str] = str_to_list(names)
        self.prefix : str | None = prefix
        self.extension : List[str] | None = str_to_list(extension)



    """
        bunch of helper function for file operations
    """
    def mov(self,file_name : str) -> None:
        rename(
            f"{self.input}/{file_name}",
            f"{self.output}/{self.prefix}{file_name}"
        )

    def copy(self,file_name : str) -> None:
        cp( 
            f"{self.input}/{file_name}",
            f"{self.output}/{self.prefix}{file_name}"  
        )

    
    def delete(self,file_name : str) -> None:
        remove(
            f"{self.input}/{file_name}"
        )