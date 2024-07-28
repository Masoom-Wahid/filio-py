from  typing import Optional
def get_file_extension(path : str) -> Optional[str]:
    """
    given a file this will return the extension
    for ex the path might be : ./usr/bin/smth/smth/fil.json
    this will first split it by "/" and then since "fil.json" 
    should be on the last which is the real file name

    after that we split by "." which hopefully should give us
    'json' , if the len(inputs) is  less than 1 then that means the
    input does not have any extension which is why we should return None
    """

    inputs : list[str] = path.split("/")[-1].split(".")
    if len(inputs) <= 1:
         return None
    else:
         return inputs[-1]