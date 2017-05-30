import yaml
import json

import os.path
import string
import subprocess

import utils
from project import Project

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
