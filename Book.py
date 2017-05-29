import json
import sys
import os
from os import mkdir, listdir
from os.path import join, basename, realpath, dirname
import subprocess
from subprocess import call

from shutil import *

from utils import *


def write_data(data, file):
    with open(file, "w") as f:
        json.dump(data, f)


def create_new():
    title = raw_input("Title: ")
    if not title:
        die("Title cannot be empty", -1)

    confirmation = confirm("Create new book with title '%(title)s':" % locals())
    if not confirmation:
        die("OK!")

    directory = title.replace(" ", "-").lower()

    skeleton_folder = "skeleton"
    script_path = dirname(realpath(__file__))
    src = join(script_path, skeleton_folder)
    dest = join(os.getcwd(), directory)
    copytree(src, dest)

    use_vc = confirm("Use git?")
    data = {
            "title": title,
            "directory": directory,
            "use_vs": use_vc
            }
    config_path = join(directory, ".book")
    write_data(data, config_path)
    
    if use_vc:
        cmds = [
            "git init -q",
            "git add .book",
            "git commit -q -m \"Created book\""
        ]
        subprocess.Popen("; ".join(cmds), shell=True, cwd=directory)

    success("Success!")

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        die("Please specify an action!", -1)

    action = sys.argv[1]
    if action == "new":
        create_new()

