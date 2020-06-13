from ete3 import Tree, TreeStyle

file = open("gisaid_cov2020_sequences_filtered_8312_2.nw")
tree = file.read()
file.close()

t = Tree(tree)
t.populate(30)
ts = TreeStyle()
ts.show_leaf_name = True
ts.mode = "c"
ts.arc_start = -180
ts.arc_span = 180
t.show(tree_style=ts)
