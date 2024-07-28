#from .filio import filio

"""
    Fil is essentially just an abstraction over the ton of 
    functions which will be used to run filio
    it will do the jobs such as:
        read from json file
        sanitize the input
        start the prgoram
"""
import json
import  os

class FilFileNotFoundExceptin(Exception):
    def __init__(self, message):
        super().__init__(message)



class Fil:

    def __init__(self,path:str) -> None:
        """
            'watcher' : {
                'str' : 'str'
            }

        """
        self.filios : dict[str,dict[str,str]] = self.__get_filios(path)
        for key,value in self.filios.items():
            print(f"{key}: {value}")

    def __get_filios(self,path : str) -> dict[str,dict[str,str]]:
        if (path.endswith('.json')) and os.path.exists(path):
            with open(path,'r') as file:
                data = json.load(file)
            return data
        else:
            FilFileNotFoundExceptin("Invalid file, make sure it exists and has a .json extension")
