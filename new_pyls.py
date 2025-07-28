import os
import argsparse
from typing import NamedTuple
from datetime import datetime

def main():
    options = get_command_line_args()
    list_files(options.dirname, options.longform, options.formatted) # writing
    #clean code is helpful not only for other people but also yourself

class Options(NamedTuple):
    dirname: str
    longform: bool
    formatted: bool

# Options === tuple(str, bool, bool) 

def get_command_line_args() -> Options:
    # ....argsparse .....
    return Options("file.txt, True, False")

class FileInfo(NamedTuple):
    name: str
    modtime: datetime
    size: int
    isdir: bool


def list_files(dirname: str, longform: bool, formatted: bool) -> None:
    validate_dir(dirname)
    contents: list[FileInfo] = find_contents_of_directory(dirname)
    presentation: list[str] = [present_file(fileinfo, longform, formatted) for fileinfo in contents]
    print_strings(presentation)

def print_strings(presentation: list[str]) -> None:
    for s in presentation:
        print(s)

def validate_dir(dirname: str):
    # Not valid
    if os.path.isdir(dirname):
        return True
    raise Exception("Invalid directory" + dirname)

def find_contents_of_directory(dirname: str) -> list[FileInfo]:
    path = os.path.listdir(dirname)
    return [get_fileinfo(os.path.join(dirname, filename) for filename in filenames]    

def get_fileinfo(dirname: str, filename: str) -> FileInfo:
    path = os.path.join(dirname, filename)
            isdir = os.path.isdir(path)
            stat = os.stat(path)
            modtime = stat.st_mtime
            size = stat.st_size
            return FileInfo(filename, datetime.fromtimestamp(modtime), size, isdir)

def present_file(fileinfo: FileInfo, longform: bool, formatted: bool) -> str:
            formatchar = "/" if fileinfo.isdire else ""
            if longform:
                if formatted:
                    return f{fileinfo.modtime.isoformat()} {fileinfo.size} {fileinfo.name}{formatchar}
                else:
                    return f{fileinfo.modtime.isoformat()} {fileinfo.size} {fileinfo.name}
            else:
                if formatted:
                    return f{fileinfo.name}{formatchar}
                else:
                     return f{fileinfo.name}
            
