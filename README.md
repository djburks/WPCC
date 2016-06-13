# WPCC
## Weighted Pearson Correlation Coefficient Calculator for Python

- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [OPTIONS](#options)
- [INPUT](#input)

### INSTALLATION

For now, simply download the wpcc.py file and make sure it is in the same directory as your own program.

### DESCRIPTION

WPCC contains a single function (wpearson), that allows users to calculate a weighted Pearson Correlation Coefficient for two vectors.  This was primarily written to find gene co-expression patterns when given a list of genes with accompanying vectors of normalized expression data.  The weights are based on the redundancy of samples from which the expression values were taken.

For more information concerning weighted PCC calculation and gene-coexpression, please see the following journal:

[Rank of Correlation Coefficient...Obayashi and Kinoshita, 2009 (NCBI)](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2762411/)

### OPTIONS

To calculate weighted PCC, supply the wpearson function with three equal-length vectors.  The first two vectors should be those for which correlation is being calculated.  The third should contain the weights. The order of all vectors matters.  

```
>>> import wpcc

>>> dal = [8,22,88,84,21]
>>> san = [8,32,80,82,35]
>>> wts = [0.9,0.7,0.5,0.3,0.2]

>>> wpcc.wpearson(dal,san,wts)

0.9819
```
An optional rounding parameter can be supplied as a fourth option for the number of decimal places desired.  The default is 4.

```
>>> wpcc.wpearson(dal,san,wts,8)
0.98193095

```
### INPUT

Each of the three vectors should be entirely numerical and ordered.  Using the above example, a weight of 0.5 corresponds to values 88 and 80 for the dal and san vectors, respectively.  

Assigining an equal-length vector of identicial weights (i.e. [1,1,1,1,1]) will allow you to calculate an unweighted PCC.
