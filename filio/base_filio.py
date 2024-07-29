from typing import List
from utils.path import Path
from utils.str_helpers import str_to_list
from utils.file_helpers import get_file_extension
from os import rename,remove
from shutil import copy as cp
from typing import Optional


"""
a filio can be described as a program watching for changes
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



class BaseFilio:
    def __init__(
            self,
            input : Path,
            output : Path,
            action : str,
            names : str,
            prefix : Optional[str] = None,
            extension : Optional[str] = None,
            ) -> None:
        """
            input -> the input directory to be watched
            output -> the output directory to be watched
            action -> the action to be preformed on the file (mov,cop,del)
            names -> the name of the files to invoke the action with
            extension -> if the name matches than should we filter by extension [Optional]
            prefix -> whether the given file should or should not be moved or copied with a prefix [Optional]
        """
        self.input : Path = input
        self.output : Path = output
        self.action : str = action
        self.names : List[str] = str_to_list(names)
        self.prefix : Optional[str] = prefix
        if extension:
            self.extension : Optional[List[str]] = str_to_list(extension)
        else:
            self.extension = None



    def check_extension_and_name_exists(self,file_name : str) -> bool:
        name_exists : bool = False
        extension_exists : bool = False

        extension = get_file_extension(file_name)

        for ext in self.extension:
            if ext == extension:
                extension_exists = True
                break

        for name in self.names:
            ...

        return name_exists and extension_exists



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


    def listen(self) -> None:
        pass
    
    def __str__(self) -> str:
        return f"{self.input}-{self.output}"
    
