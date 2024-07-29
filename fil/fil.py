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



class FilException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Fil:
    def __init__(self,path:JsonPath) -> None:
        self.filios : Dict[str,Union[MovFilio,CpFilio,DelFilio]] = self.__get_filios(path)
        for key,value in self.filios.items():
            print(f"{key}: {value}")



    def __santizie(self,value : Dict[str,str],action : Optional[str]) -> None:
        if action is None : raise FilException("Expected key 'action'")
        try:
            """
                input and names are mandatory in any case
                as for output , when we are deleting we dont need deletion so we dont want to 
                check for output when the action is 'del'
            """
            if not (value["input"] and value["name"]):
                raise FilException("Invalid Json file format")
            if action != "del" and not value["output"]:
                raise FilException("Invalid Json File Format")

        except KeyError:
            raise FilException("Invalid Json file format") 
        


    def __get_filios(self,path : JsonPath) -> Dict[str,Union[MovFilio,CpFilio,DelFilio]]:    
        result : Dict[str,Union[MovFilio,CpFilio,DelFilio]] = {}

        with open(path.abs_path,'r') as file:
            data = json.load(file)
 

            for key,value in data.items():
                action : str = value.get("action",None)
                self.__santizie(value,action)

                if action == "mov":
                    filio : MovFilio = MovFilio(
                        DirPath(value["input"]),
                        DirPath(value["output"]),
                        action,
                        value["name"],
                        prefix=data.get("prefix",None),
                        extension=data.get("extension",None)
                    )
                
                elif action == "del":
                    filio : MovFilio = DelFilio(
                        DirPath(value["input"]),
                        None,
                        action,
                        value["name"],
                        prefix=data.get("prefix",None),
                        extension=data.get("extension",None)
                    )

                elif action == "cp":
                    filio : MovFilio = DelFilio(
                        DirPath(value["input"]),
                        DirPath(value["output"]),
                        action,
                        value["name"],
                        prefix=data.get("prefix",None),
                        extension=data.get("extension",None)
                    )
                else:
                    raise FilException("Invalid 'action', chose from 'mov','cp','del'")
                


                result[key] = filio

        return result

    def run(self):
        """
            filios -> thread()
        """