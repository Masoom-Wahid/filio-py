import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from argparse import ArgumentParser
from fil.fil import Fil 
from utils.file_helpers import get_file_extension

"""

    -> core
        -> fil
            ->
        -> filio <-
            ->  mov_filio
            ->  copy_filio
            ->  del_filio


    -> test
    -> utils
    

"""



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S'
    )


    
    parser : ArgumentParser = ArgumentParser(
        prog="filio-py",
        description="https://github.com/Masoom-Wahid/filio written in python",
        epilog="Text at the bottom of help"
    ) 

    parser.add_argument("file_name")
    parser.add_argument("-c","--cwd")

    args = parser.parse_args()
    if not args.file_name:
        raise FileNotFoundError

    fil =  Fil(args.file_name)