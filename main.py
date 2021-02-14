import pathlib
import argparse


def tree_maker(
        input_path: str, exclude_ext: str = "", write_md: bool = False) -> str:
    """
    docstring
    """

    INDENTCHAR = "    "  # 4 spaces
    INDENT_SYM = "├── "
    INDENT_SYM_LAST_LEVEL = "└──"
    BACKTICKS = "```"  # used when output written into .md

    input_path = pathlib.Path("testdir").resolve()

    # initialize list to contain tree as str
    res_list = []

    for path in sorted(input_path.rglob('*')):

        # check depth of path
        depth = len(path.relative_to(input_path).parts)

        # get list of children
        path_children = [path_child for path_child in path.glob('*')]

        # check whether to exclude
        include_file = True
        if path.is_file():
            path_suffix = path.suffix

            if path_suffix == exclude_ext:
                include_file = False

        if len(path_children) > 0 and include_file:

            spacer = INDENTCHAR * (depth - 1)
            path_str = f'{spacer}{INDENT_SYM} {path.name}'
            res_list.append(path_str)
            print(path_str)

        elif include_file:
            spacer = INDENTCHAR * (depth - 1)
            path_str = f'{spacer}{INDENT_SYM_LAST_LEVEL} {path.name}'
            res_list.append(path_str)
            print(path_str)

    if not write_md:
        print("not write")
        # build result string
        tree_str = " \n".join(res_list)
        return tree_str

    else:
        print("write")
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


def main():

    # Parse arguments
    parser = argparse.ArgumentParser(description="Get directory tree")
    parser.add_argument("--path", type=str, default="",
                        help="the path to directory of which tree you want"
                        "to have",
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
        input_path = pathlib.path().cwd()

    tree_maker(
        input_path=input_path,
        exclude_ext=exclude_ext,
        write_md=write_md)


if __name__ == '__main__':

    main()
