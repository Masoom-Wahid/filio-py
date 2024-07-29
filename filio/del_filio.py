from filio.base_filio import BaseFilio
from utils.path import DirPath
from os import remove
from typing import Optional

class DelFilio(BaseFilio):
    def __init__(self, input: DirPath, output: Optional[DirPath], action: str, names: str, prefix: Optional[str] = None, extension: Optional[str] = None) -> None:
        super().__init__(input, output, action, names, prefix, extension)


    
    def action(self,file_name : str) -> None:
        remove(
            f"{self.input}/{file_name}",
            f"{self.output}/{self.prefix}{file_name}"
        )

    def __str__(self) -> str:
        return f"{self.input}-{self.output}"