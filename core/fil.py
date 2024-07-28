from .filio import filio

"""
    Fil is essentially just an abstraction over the ton of 
    functions which will be used to run filio
    it will do the jobs such as:
        read from json file
        sanitize the input
        start the prgoram
"""

class FilFileNotFoundExceptin(Exception):
    ...


class Fil:

    def __init__(self,path:str) -> None:
        self.filios : dict[str,filio] = self.__get_filios(path)

    

    def __get_filios(self,path:str) -> dict[str,filio]:
        ...
    
    def sanitize(self,filios : dict[str,filio]) -> None:
        ...

    def read_json_file(self,path : str) -> None:
        ...

    def run():
        ...

