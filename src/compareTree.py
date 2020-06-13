from ete3 import Tree

file = open("gisaid_cov2020_sequences_filtered_8312_2.nw")
tree1 = file.read()
file.close()
file = open("gisaid_cov2020_sequences_filtered_8312.RAxML_result.nw")
tree2 = file.read()
file.close()



t1 = Tree(tree1)
t2 = Tree(tree2)



rf, max_rf, common_leaves, parts_t1, parts_t2 = t1.robinson_foulds(t2, unrooted_trees=True)
#rf, rf_max, common_attrs, names, edges_t1, edges_t2, discarded_edges_t1, discarded_edges_t2 = t1.robinson_foulds(t2, unrooted_trees=True)
print t1, t2
print "RF distance is %s over a total of %s" %(rf, max_rf)
print "Partitions in tree2 that were not found in tree1:", parts_t1 - parts_t2
print "Partitions in tree1 that were not found in tree2:", parts_t2 - parts_t1

# We can also compare trees sharing only part of their labels

t1 = Tree('(((a,b),c), ((e, f), g));')
t2 = Tree('(((a,c),b), (g, H));')
rf, max_rf, common_leaves, parts_t1, parts_t2 = t1.robinson_foulds(t2, unrooted_trees=True)
#rf, rf_max, common_attrs, names, edges_t1, edges_t2, discarded_edges_t1, discarded_edges_t2 = t1.robinson_foulds(t2, unrooted_trees=True)

print t1, t2
print "Same distance holds even for partially overlapping trees"
print "RF distance is %s over a total of %s" %(rf, max_rf)
print "Partitions in tree2 that were not found in tree1:", parts_t1 - parts_t2
print "Partitions in tree1 that were not found in tree2:", parts_t2 - parts_t1
