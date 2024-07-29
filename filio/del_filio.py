from filio.base_filio import BaseFilio
from utils.path import DirPath,UserPath
from typing import Optional
from watchdog.events import FileSystemEventHandler
import os


class DelFilioHandler(FileSystemEventHandler):
    def __init__(self,del_filio : "DelFilio") -> None:
        super().__init__()
        self.filio : DelFilio = del_filio


    def on_any_event(self,event):
        if event.is_directory:
            return None


        elif event.event_type == 'created':
            path : UserPath = UserPath(event.src_path)

            if self.filio.check_extension_and_name_exists(path):
                self.filio.perform(
                    path.full_file_name
                )

class DelFilio(BaseFilio):
    def __init__(self, input: DirPath, output: Optional[DirPath], action: str, names: str, prefix: Optional[str] = None, extension: Optional[str] = None) -> None:
        super().__init__(input, output, action, names, prefix, extension)
        self.handler = DelFilioHandler(self)


    def perform(self,file_name : str) -> None:
        os.remove(
            f"{self.input.abs_path}/{file_name}"
        )

    def __str__(self) -> str:
        return f"{self.input}-{self.output}"