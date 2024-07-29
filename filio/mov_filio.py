from filio.base_filio import BaseFilio
from utils.path import DirPath,UserPath
from os import rename
from typing import Optional
from watchdog.events import FileSystemEventHandler

class MovFilioHandler(FileSystemEventHandler):
    def __init__(self,del_filio : "MovFilio") -> None:
        super().__init__()
        self.filio : MovFilio = del_filio


    def on_any_event(self,event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            path : UserPath = UserPath(event.src_path)
            if self.filio.check_extension_and_name_exists(path):
                self.filio.perform(
                        path.full_file_name
                    )

class MovFilio(BaseFilio):
    def __init__(self, input: DirPath, output: DirPath, action: str, names: str, prefix: Optional[str] = None, extension: Optional[str] = None) -> None:
        super().__init__(input, output, action, names, prefix, extension)
        self.handler = MovFilioHandler(self)

    def perform(self,file_name : str) -> None:
        rename(
            f"{self.input.abs_path}/{file_name}",
            f"{self.output.abs_path}/{self.prefix}{file_name}"
        )

    def __str__(self) -> str:
        return f"{self.input}-{self.output}"