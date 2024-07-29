from typing import List
from utils.path import DirPath,UserPath
from utils.str_helpers import str_to_list
from os import rename,remove
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
            input : DirPath,
            output : DirPath,
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
        self.input : DirPath = input
        self.output : DirPath = output
        self.action : str = action
        self.names : List[str] = str_to_list(names)
        self.prefix : Optional[str] = prefix
        if extension:
            self.extension : Optional[List[str]] = str_to_list(extension)
        else:
            self.extension = None



    def check_extension_and_name_exists(self,file : UserPath) -> bool:
        """
        @param file -> it should be a UserPath meaning a file which user changed
        the diffrence is that these are not checked for having .json file or being a dir
        except they are sanitized and then splitted for their file_name,abs_path,extensions and etc...


        so when the funciton is called it checks whether the user files are in the area which this user chagned
        if so it should return True else False
        """
        name_exists : bool = False
        extension_exists : bool = False

        extension : str = file.get_extension()
        if not self.extension:
            extension_exists = True
        else:
            for ext in self.extension:
                if ext == extension:
                    extension_exists = True
                    break

        for name in self.names:
            if name in file.file_name:
                name_exists = True
                break
    

        return name_exists and extension_exists



    """
        bunch of helper function for file operations
    """

    def perform(self,file_name : str) -> None:
        raise NotImplementedError("action is not implemented for base class")
    
    def __str__(self) -> str:
        raise NotImplementedError("You cannot print BaseFilio class")
    
