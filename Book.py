import json
import sys
from os import mkdir
from os.path import join
import subprocess
from subprocess import call

def confirm(msg, enterConfirms=True):
    response = raw_input(msg + " ")
    return (enterConfirms and not response) or response.lower() == "y"


def printAndExit(msg, exitCode):
    print(msg)
    sys.exit(exitCode)


def success(msg):
    printAndExit(msg, exitCode=0)


def die(msg, exitCode=0):
    print(msg)
    sys.exit(exitCode)


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
    chapDir = join(directory, "chapters")
    charDir = join(directory, "characters")
    mkdir(directory)
    mkdir(chapDir)
    mkdir(charDir)

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

