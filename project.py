from os import path
import yaml

class Project:
    __metadata_file = ".book"
    """The file containing the metadata for the book"""

    metadata = {}
    """The metadata for the book"""

    def __init__(self):
        if not path.isfile(self.__metadata_file):
            return

        with open(self.__metadata_file, "r") as f:
            self.metadata = yaml.load(f)

    def valid_project(self):
        """Determines if this is a valid book project"""
        return len(self.metadata) > 0

    def write_data(self, write_path=""):
        """
        Writes the metadata field to the file designated by __metadata_file.
        Accepts write_path to set the directory in which to write the data file.
        """
        write_path = path.join(write_path, self.__metadata_file)

        with open(write_path, "w") as f:
            yaml.dump(self.metadata, f, default_flow_style=False)
