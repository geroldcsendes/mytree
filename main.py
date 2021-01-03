import os
import sys
import argparse


def get_relative_depth(dir_path: str, level_offset: int) -> int:
    return dir_path.count(os.path.sep) - level_offset


def exclude_dir_and_subdirs(dir):
    pass


def tree_maker(
        input_path: str, exclude_ext: str = "", write_md: bool = False) -> str:
    """
    docstring
    """

    INDENTCHAR = "    "
    INDENT_SYMBOL = "├── "
    BACKTICKS = "```"  # used when output written into .md

    # FIXME there should be a builtin method to do this
    level_offset = input_path.count(os.path.sep) - 0

    # initialize list to contain tree as str
    res_list = []

    for root, subdirs, files in os.walk(input_path):

        level = get_relative_depth(root, level_offset)

        if level == 0:
            root_str = INDENTCHAR * level + root
            print(root_str)
            res_list.append(root_str)
            pass
        else:
            root_str = (INDENTCHAR * level + INDENT_SYMBOL +
                        os.path.basename(root) + "/")

            print(root_str) 
            res_list.append(root_str)
        level += 1

        for filename in files:

            file_str = INDENTCHAR * level + INDENT_SYMBOL + filename
            # check whether to exclude
            if filename.endswith(tuple(exclude_ext)):
                pass
            else:
                print(file_str)
                res_list.append(file_str)

    if not write_md:
        # build result string
        tree_str = " \n".join(res_list)
        return tree_str

    else:
        # build result string
        res_list.insert(0, BACKTICKS)
        res_list.append(BACKTICKS)
        tree_str = " \n".join(res_list)

        # create result string
        print("Printing result tree...")

        print(tree_str)
        with open("mytree.md", "w+", encoding='utf-8') as writer:
            writer.write(tree_str)

        return tree_str


if __name__ == '__main__':

    # Parse arguments
    parser = argparse.ArgumentParser(description="Get directory tree")
    parser.add_argument("--path", type=str, default="",
                        help="the path to directory of which tree you want to have",
                        required=True)
    parser.add_argument("--exclude_ext", type=str, nargs="*", default=[],
                        help="Files with extensions you don't want to include",
                        required=False)
    parser.add_argument("--write_md", type=bool, default=False, required=False,
                        help="Whether to write tree to an md. file")

    # parse arguments
    args = parser.parse_args()
    input_path = args.path
    exclude_ext = args.exclude_ext
    write_md = args.write_md

    if input_path == "":
        input_path = os.getcwd()

    if not os.path.isdir(input_path):
        print('The path specified does not exist')
        sys.exit()

    tree_maker(
        input_path=input_path,
        exclude_ext=exclude_ext,
        write_md=write_md)    

# example call: python main.py --path C:\Users\gerol\Desktop\python\mytree\testdir\test1
# ex call with excluding extensions
# python main.py --path C:\Users\gerol\Desktop\python\mytree\testdir\test1 --exclude_ext ".csv" ".txt" "__init__.py"
