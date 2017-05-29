import json
import sys
import os
from os import mkdir, listdir
from os.path import join, basename, realpath, dirname, isfile
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

    use_vc = confirm("Use git?")
    directory = title.replace(" ", "-").lower()

    # Put data into dictionary
    data = {
            "title": title,
            "directory": directory,
            "use_vc": use_vc
            }


    # Path to the script folder (it contains the skeleton folder)
    script_path = dirname(realpath(__file__))
    src = join(script_path, "skeleton")
    dest = join(os.getcwd(), directory)
    copytree(src, dest)

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


def make_book(type):
    this_path = os.getcwd()
    makefile_path = join(this_path, "Makefile")

    # If the Makefile does not exist,
    # we will copy it in
    if not isfile(makefile_path):
        # Copy Makefile in
        script_path = dirname(realpath(__file__))
        src = join(script_path, "skeleton/Makefile")
        copyfile(src, makefile_path)

    cmd = "make %(type)s" % locals()
    subprocess.Popen(cmd, shell=True, cwd=this_path)


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        die("Please specify an action!", -1)

    action = sys.argv[1]
    if action == "new":
        create_new()
    elif action == "make":
        type = "pdf"
        if len(sys.argv) <= 2:
            print("No type given. Defaulting to PDF.")
        else:
            type = sys.argv[2]

        make_book(type)


