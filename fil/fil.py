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
from utils.file_helpers import *
from filio.filio import Filio
from typing import Dict

class FilFileNotFoundExceptin(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidJsonFormatException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Fil:
    def __init__(self,path:str) -> None:
        self.filios : Dict[str,Filio] = self.__get_filios(path)
        for key,value in self.filios.items():
            print(f"{key}: {value}")



    def __santizie(self,data : Dict[str,Dict[str,str]]) -> None:
        try:
            for value in data.values():
                if not (value["input"] and value["output"] and value["action"] and value["name"]):
                    raise InvalidJsonFormatException("Invalid Json file format")
        except KeyError:
            raise InvalidJsonFormatException("Invalid Json file format") 

    def __get_filios(self,path : str) -> Dict[str,Filio]:
        if (get_file_extension(path) == "json") and os.path.exists(path):
            
            result : Dict[str,Filio] = {}

            with open(path,'r') as file:
                data = json.load(file)
                self.__santizie(data)

                for key,value in data.items():
                    result[key] = Filio(
                        value["input"],
                        value["output"],
                        value["action"],
                        value["name"],
                        prefix=data.get("prefix",None),
                        extension=data.get("extension",None)
                    )

            return result
        else:
            raise FilFileNotFoundExceptin("Invalid file, make sure it exists and has a .json extension")
