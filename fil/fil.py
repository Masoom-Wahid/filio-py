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
from utils.path import JsonPath,DirPath
from filio.cp_filio import CpFilio
from filio.mov_filio import MovFilio
from filio.del_filio import DelFilio
from filio.base_filio import BaseFilio
from typing import Dict,Union

class FilFileNotFoundExceptin(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidJsonFormatException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Fil:
    def __init__(self,path:JsonPath) -> None:
        self.filios : Dict[str,Union[MovFilio,CpFilio,DelFilio]] = self.__get_filios(path)
        for key,value in self.filios.items():
            print(f"{key}: {value}")



    def __santizie(self,data : Dict[str,Dict[str,str]]) -> None:
        try:
            for value in data.values():
                if not (value["input"] and value["output"] and value["action"] and value["name"]):
                    raise InvalidJsonFormatException("Invalid Json file format")
        except KeyError:
            raise InvalidJsonFormatException("Invalid Json file format") 
        


    def __get_filios(self,path : JsonPath) -> Dict[str,Union[MovFilio,CpFilio,DelFilio]]:    
        result : Dict[str,Union[MovFilio,CpFilio,DelFilio]] = {}

        with open(path.abs_path,'r') as file:
            data = json.load(file)
            self.__santizie(data)

            # TODO: filter based on action which type of class will we push ?
            for key,value in data.items():
                result[key] = BaseFilio(
                    DirPath(value["input"]),
                    DirPath(value["output"]),
                    value["action"],
                    value["name"],
                    prefix=data.get("prefix",None),
                    extension=data.get("extension",None)
                )

        return result

    def run(self):
        """
            filios -> thread()
        """