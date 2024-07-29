from filio.base_filio import BaseFilio
from utils.path import DirPath,UserPath
from shutil import copyfile
from typing import Optional
from watchdog.events import FileSystemEventHandler


class CpFilioHandler(FileSystemEventHandler):
    def __init__(self,cp_filio : "CpFilio") -> None:
        super().__init__()
        self.filio : CpFilio = cp_filio


    def on_any_event(self,event):
        if event.is_directory:
            return None


        elif event.event_type == 'created':
            path : UserPath = UserPath(event.src_path)
            self.filio.check_extension_and_name_exists(path)
            self.filio.perform(
                    path.full_file_name
                )


class CpFilio(BaseFilio):
    def __init__(self, input: DirPath, output: DirPath, action: str, names: str, prefix: Optional[str] = None, extension: Optional[str] = None) -> None:
        super().__init__(input, output, action, names, prefix, extension)
        self.handler : CpFilioHandler = CpFilioHandler(self)



    def perform(self,file_name : str) -> None:
        print( 
            f"{self.input.abs_path}/{file_name}",
            f"{self.output.abs_path}/{self.prefix}{file_name}"  
        )
        copyfile( 
            f"{self.input.abs_path}/{file_name}",
            f"{self.output.abs_path}/{self.prefix}{file_name}"  
        )

    def __str__(self) -> str:
        return f"{self.input}-{self.output}"