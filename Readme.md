### Directory tree
```
.
|-- Preprocessing.ipynb
`-- raw_data
    |-- gisaid_cov2020_sequences_filtered.fasta
    |-- gisaid_cov2020_sequences.fasta
    |-- metadata.tsv
    `-- ...
```
Notes: raw_data directory is git-ignored

### Preprocessing
From Raw Data (GISAID fasta and nextstrain metadata), you can use `Preprocessing.ipynb` to filter out those useful data. In this case, we set it to `host: human` with known `age`, `gender`, `country`, and `submitted date`

### Raw Data:
Raw data from GISAID: https://www.epicov.org/epi3/frontend#61101

~~Nextstrain GISAID metadata: https://github.com/nextstrain/ncov~~

Nextstrain GISAID metadata is now avalable on GISAID: more instruction [here](https://github.com/nextstrain/ncov/blob/master/docs/running.md)






