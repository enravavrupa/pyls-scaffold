# Imports make the mentioned "modules" accessible to the code within
# this file, which is itself a "module".
import argparse
import os


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pyls", description="A baby version of ls.")

    # We now add descriptions for the expected arguments for our program.
    parser.add_argument(
        "dirname",
        # Indicates that either 0 or one directory name can be given.
        nargs="?",
        # Gives the default value to use when this argument is not given.
        default=".",
        # '.' means "current directory".
        help="The name of the directory whose contents are to be listed.",
    )
    parser.add_argument(
        "-l",
        "--longform",
        action="store_true",  # Indicates that the value is a boolean and no further
        # values need to be supplied on the command line.
        default=False,  # This is not really needed as False is the default already
        # when -l is not given on the command line. Including it
        # for illustration.
        help="Prints details about each file in the format -\n"
        "<timestamp> <filesize> <filename>",
    )
    parser.add_argument(
        "-F",
        "--formatted",
        action="store_true",
        default=False,
        help="Adds a character to tell you whether its a file or a directory.",
    )

    # Now we ask argparse to use the above information to interpret the
    # arguments and give us an object which will have `.dirname`,
    # `.longform` and `/.formatted` attributes we can access instead of
    # having to check for all the combinations ourselves.
    # Furthermore, if you call your program with either the `-h` or `--help``
    # flag, it will print out all of the specification above in a nice format
    # as help. This is a convention employed by most command line programs.
    args = parser.parse_args()
    os.chdir("/home/avrupaenrav/")
#    print(os.listdir("/home/avrupaenrav/"))


def pyls(dirname: str, longform: bool, formatted: bool) -> None:
    """
    DATA REPRESENTATION
    -------------------

    In this case, we're choosing a **representation** where we represent
    the directory name to list as a string and the choice of longform and
    formatted output as two boolean values.

    SIGNATURE
    ---------
    The "signature" of the procedure below can be written as
              str bool bool -> None

    PURPOSE
    -------

    - :param dirname: asks you for the name of the directory whose information
                      you want
    - :param longform: if true, then it lists all relevant data in longform
    - :param formatted: if true, then it uses '\' to indicate if a file is a
            directory

    EXAMPLES
    --------

    TODO: Below, give a few examples of what you expect the procedure to do when you
    give various inputs. This can help you think about what to implement.
    Consider various possible combinations.

    def(abc, True, True) -> returns elements of 'abc' in longform and formatted

    """
    for i in range(os.listdir(dirname)):
        if os.path.isfile(i):
            if longform and formatted:
                print(i, os.path.getmtime(i), os.path.getsize())
            elif longform:
                print(i, os.path.getmtime(i), os.path.getsize())
            elif formatted:
                print(i, os.path.getmtime(i), os.path.getsize())
            else:
                print(i)
        else:
            if longform and formatted:
                print(str(i)+ "/", os.path.getmtime(i), os.path.getsize())
            elif longform:
                print(i, os.path.getmtime(i), os.path.getsize())
            elif formatted:
                print(str(i)+ "/", os.path.getmtime(i), os.path.getsize())
            else:
                print(i)
# use os.path.isfile(path) to check if an object is file and then if it is
# a file then run pyls on it

# A python module may be loaded in one of two ways --
# 1. `python myfile.py`: In this case, the python file/module is considered to be
#    a "main program" and is named "__main__" within. So if you want to run code
#    only in this mode, you check whether __name__ is "__main__" and run that code.
# 2. `import myfile`: (within some other python file). In this mode, it is a pure
#    "module" that exposes functions and values via `myfile.` notation within the
#    importing python file. In this case, __name__ will be "myfile" and not "__main__".
 
if __name__ == "__main__":
    main()
