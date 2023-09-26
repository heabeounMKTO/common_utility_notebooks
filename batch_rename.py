import argparse
from penis_utils import finding_shit as fs
import os
from pprint import pprint
from pathlib import Path


def batch_rename():
    folder_path, extension, new_name = opt.path, opt.ext, opt.newname
    all_files = fs.FilesFinder(folder_path).by_extension(tuple(extension))
    for idx, file in enumerate(all_files):
        splitf = os.path.splitext(file)
        renamed = folder_path + f"{new_name}_{idx}" + splitf[1]
        os.rename(file, renamed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True, help="folder path")
    parser.add_argument(
        "--ext",
        nargs="+",
        type=str,
        required=True,
        help='file extension(s) example: ".jpeg" ',
    )
    parser.add_argument(
        "--newname", default="rename", type=str, help="new name for rename"
    )
    opt = parser.parse_args()

batch_rename()
