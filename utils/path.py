from typing import Optional,Tuple
from os.path import exists,isdir

"""
since we are working alot with paths , it would be better to have Path object
for each instance of a path
it would store all the neccesary attr and also alot of helper functions and methods
with it
"""

class FilFileExceptin(Exception):
    def __init__(self, message):
        super().__init__(message)

class BasePath:
    def __init__(self,abs_path : str,sanitize_for_json=False,is_dir=True) -> None:
        self.abs_path : str = abs_path
        self.full_file_name,self.file_name,self.__extension = self.get_file_name_and_extension()
        self.__sanitize_for_json = sanitize_for_json
        self.__is_dir = is_dir
        self.__sanitize_paths()

    
    def get_extension(self) -> str:
        raise NotImplementedError("get extension is not implemented in BasePath class")


    
    def get_file_name_and_extension(self) -> Optional[Tuple[str,str,str]]:
        full_file_name : list[str] = self.abs_path.split("/")[-1]
        file_details : Tuple[str,str] = full_file_name.split(".")
        if len(file_details) <= 1:
            raise FilFileExceptin(f"Expected a file ending with a valid extension got {self.abs_path}")
        else:
            return full_file_name,".".join(file_details[0:-1]),file_details[-1]

    def __sanitize_paths(self):
        if self.__sanitize_for_json and  self.__extension != "json":
            raise FilFileExceptin("Expected a file ending with .json")

        if not exists(self.abs_path):
            raise FilFileExceptin("Make Sure the given file exists")
        
    
        if self.__is_dir and not isdir(self.abs_path):
            raise FilFileExceptin("Expected a directory instead of a file")    
    
    def __str__(self) -> str:
        return f"""
            {self.abs_path},
            {self.full_file_name},
            {self.file_name},
            {self.get_extension()},
        """
        

class DirPath(BasePath):
    def __init__(self, abs_path: str, sanitize_for_json=False, is_dir=True) -> None:
        super().__init__(abs_path, sanitize_for_json, is_dir)


    def get_extension(self) -> None:
        return None

    def get_file_name_and_extension(self) -> Optional[Tuple[str,str,str]]:
        """
            since when a dir is /home/Downloads
            we dont care about anything except that abslote path and the relative path
            and also the file_name itself
            so no need to worry about extension of the path
        """
        full_file_name : list[str] = self.abs_path.split("/")[-1]
        return full_file_name,full_file_name,""



class JsonPath(BasePath):
    def __init__(self, abs_path: str, sanitize_for_json=True, is_dir=False) -> None:
        super().__init__(abs_path, sanitize_for_json, is_dir)

    def get_extension(self) -> str:
        return self.__extension

        


class UserPath(BasePath):
    def __init__(self, abs_path: str, sanitize_for_json=False, is_dir=False) -> None:
        super().__init__(abs_path, sanitize_for_json, is_dir)

    
    def get_extension(self) -> str:
        return self.__extension
