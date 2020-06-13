### Directory tree
```
.
|-- src
|   |-- Preprocessing.ipynb
|   |-- Tree_Visualization.ipynb
|   |-- bubbleTree.py           
|   |-- circularTree.py         
|   |-- compareTree.py          
|   |-- nodeStyle.py            
|   |-- nodeStyleColored.py     
|   |-- plainTree.py            
|   |-- semi_tree.pdf           
|   |-- treeDrawingEngine.py    
|   `-- treeInTree.py           
|
`-- raw_data
    |-- gisaid_cov2020_sequences_filtered.fasta
    |-- gisaid_cov2020_sequences.fasta
    |-- metadata.tsv
    `-- ...
```
Notes: raw_data directory is git-ignored


### How to start
`pip3 install -r requirements.txt`

### Preprocessing
From Raw Data (GISAID fasta and nextstrain metadata), you can use `Preprocessing.ipynb` to filter out those useful data. In this case, we set it to `host: human` with known `age`, `gender`, `country`, and `submitted date`


---

### Raw Data:
Raw data from GISAID: https://www.epicov.org/epi3/frontend#61101

~~Nextstrain GISAID metadata: https://github.com/nextstrain/ncov~~

Nextstrain GISAID metadata is now avalable on GISAID: more instruction [here](https://github.com/nextstrain/ncov/blob/master/docs/running.md)


### More resources for tree visualization:
- http://www.randelshofer.ch/treeviz/
- https://biopython.org/wiki/Phylo
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2642634/
- http://tree.bio.ed.ac.uk/software/figtree/
- http://phylo.io/# 