from ete3 import Tree, TreeStyle

file = open("gisaid_cov2020_sequences_filtered_8312_2.nw")
tree = file.read()
file.close()


t = Tree(tree)
t.show(tree_style=ts)

#save as image
t.render("mytree.png", w=183, units="mm")
