## Knowleddge Graph Evaluation

### Consistency
Logical Reasoners

### Domain Requirements Validation
#### SPARQL Queries
* The queries can be found in a csv file [here](https://github.com/DeperiasKerre/qKG/blob/main/Results/KG/Competency%20Questions.csv).
* The queries results can be found in this [notebook](https://github.com/DeperiasKerre/qKG/blob/main/Results/KG/Sparql_Queries.ipynb).
Query 1.1: What are the possible material compositions of a QCL laser heterostructure with an LO
Phonon Design Type ?
```
    PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    SELECT DISTINCT ?mat_composition
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:LOPhononDepopulation;
     QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
}
```
Query 1.2: What are the possible material compositions of a QCL laser heterostructure with a Resonant Phonon Design Type?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    SELECT DISTINCT ?mat_composition
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:DoubleResonantPhonon;
     QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
}
```
Query 1.3: What are the possible material compositions of a QCL laser heterostructure with a Bound to Continuum design type?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#> 
    SELECT DISTINCT ?mat_composition
WHERE
{
 ?HS QpOnto:hasDesignType QpOnto:BoundToContinum;
     QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?mat_composition.
}
```
 

