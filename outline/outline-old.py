import yaml
import string

next_id = 1

def scene_id():
    global next_id

    id = next_id
    next_id += 1
    return "scene%(id)s" % locals()

def node(title):
    id = scene_id()
    return "\\node (%(id)s) {%(title)s};" % locals()

if __name__ == "__main__":
    out = ""
    with open("scene1.yaml", "r") as f:
        dat = yaml.load(f)
        for x in dat:
            out = out + node(x["scene"]) + "\n"
        print out
