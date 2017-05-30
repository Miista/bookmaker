import string

template = """
\documentclass[tikz]{standalone}
\usetikzlibrary{positioning,backgrounds,arrows.meta}
\\begin{document}
\\tikzset{
  every node/.style={
    draw,
    circle,
    fill=white
  },
  main/.style={
    color=red
  },
  minor/.style={
    color=blue
  },
  line/.style={
    line width=0.3mm
  }
}
\\begin{tikzpicture}
%(content)s
\end{tikzpicture}
\end{document}
"""

scenes = {
  "main": [
    "start",
    "trouble",
    "rising",
    "the end"
  ],
  "line2": [
    "start",
    "trouble",
    "kissing",
    "rising",
    "the end"
  ],
  "line3": [
    "start",
    "rising"
  ],
  "line4": [
    "trouble",
    "the end"
  ]
}

def node(id, x, y, type="", text=""):
  return "\\node[%(type)s,label={%(text)s}] (%(id)s) at (%(x)s,%(y)s) {};\n" % locals()

def connect(start, end, color="black", group=0):
  return "\draw[-,line,color=%(color)s,transform canvas={yshift=-%(group)spt}] (%(start)s.center) to (%(end)s.center);\n" % locals()
def mkkey(s):
  return s.replace(" ", "-")

colors = ['orange', 'green', 'blue', 'gray']

if __name__ == "__main__":
  scene_nodes = {}
  row = 0
  content = ""
  main_scenes = scenes["main"]
  del scenes["main"]
  x = 0
  max_major_scene_count = len(main_scenes)
  rng = range(0, max_major_scene_count)
  final_scene = False
  for i in rng:
    sc = main_scenes[i]
    key = mkkey("main" + sc)
    scene_nodes.setdefault("main",[]).append(key)
    # Make the start node
    content += node(key, x, 0, type="main")
    if max_major_scene_count <= i+1:
      final_scene = True
      next_main = main_scenes[i]
    else:
      next_main = main_scenes[i+1]
    # Consult the other scenes
    y = 0
    ix = x+1
    highest_x = ix
    for lsc in scenes:
      y += 1
      items_added = 0
      for s in scenes[lsc]: # every scene in this line
        print s
        if s == next_main or s in main_scenes[i+1:]: # we don't wanna skip ahead of ourselves!
          print s +" is in " + string.join(main_scenes)
          key = mkkey("main" + s)
          scene_nodes.setdefault(lsc,[]).append(key)
          break
        key = mkkey(lsc + s)
        content += node(key, ix, y, text=str(s))
        scene_nodes.setdefault(lsc,[]).append(key)
        items_added += 1
        ix += 1
      del scenes[lsc][:items_added]
      highest_x = ix if ix > x else x
    x = highest_x
  
  print scene_nodes

  content += "\n"
  content += "\\begin{scope}[on background layer]\n"

  main = scene_nodes["main"][0]
  colorid = 0
  group = 0
  for l in scene_nodes:
    start = scene_nodes[l][0]
    content += connect(main, start, color=colors[colorid], group=group)
    for n in scene_nodes[l][1:]:
      end = n
      content += connect(start, end, color=colors[colorid], group=group)
      start = end
    colorid += 1
    group += 1

  content += "\end{scope}"

  print template % locals()
  with open("t.tex", "w") as f:
    f.write(template % locals())