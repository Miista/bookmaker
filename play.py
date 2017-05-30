import yaml
import json

import os.path
import string
import subprocess

import utils

class Project:
    project_file = ".books"
    """The project file containing the meta data about the book."""

    chapter_file = "chapters.yaml"
    """A file containing the order of the chapters. Might not exist."""

    chapters = {}
    config = {}

    def __init__(self):
        self.chapters = self.read_config()["chapters"]
        self.config = self.read_project()

    def read_project(self):
        with open(self.project_file, "r") as f:
            return json.load(f)

    def read_config(self):
        with open(self.chapter_file, "r") as f:
            return yaml.load(f)

class Publisher:
    def publish(self):
        project = Project()

        if not os.path.isfile(project.chapter_file):
            utils.die("No problem", -1)

        chapters = string.join(map(lambda x: "chapters/%(x)s.md" % locals(), project.chapters))

        title = project.config["title"]

        this_path = os.getcwd()
        makefile_path = string.join(this_path, "Makefile")

        cmd = "pandoc --smart --standalone %(chapters)s -o %(title)s.pdf" % locals()
        subprocess.Popen(cmd, shell=True, cwd=this_path)

if __name__ == "__main__":
    pub = Publisher()
    pub.publish()
