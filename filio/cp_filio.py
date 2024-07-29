from filio.base_filio import BaseFilio
from utils.path import DirPath
from shutil import copy as cp
from typing import Optional


class CpFilio(BaseFilio):
    def __init__(self, input: DirPath, output: DirPath, action: str, names: str, prefix: Optional[str] = None, extension: Optional[str] = None) -> None:
        super().__init__(input, output, action, names, prefix, extension)


    def action(self,file_name : str) -> None:
        cp( 
            f"{self.input}/{file_name}",
            f"{self.output}/{self.prefix}{file_name}"  
        )

    def __str__(self) -> str:
        return f"{self.input}-{self.output}"