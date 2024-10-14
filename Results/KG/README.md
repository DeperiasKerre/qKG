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
Query 2.1: What are the working temperatures for a QCL laser operating in the continuous wave mode?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#> 
    SELECT ?value ?label ?unit 
WHERE
{
 ?wt QpOnto:correspondsToWorkingMode QpOnto:ContinousWaveOperation;
 qudt_qv:hasQuantityValue ?tv.
 ?tv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?unit RDFS:label ?label. 
}
```
Query 2.2: What are the working temperatures for a QCL laser operating in the pulsed mode?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?value ?label ?unit 
WHERE
{
 ?wt QpOnto:correspondsToWorkingMode QpOnto:PulsedOperation;
 qudt_qv:hasQuantityValue ?tv.
 ?tv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?unit RDFS:label ?label.
}
```
Query 3.1: What are the possible power values for a QCL laser with a heterostructure with material composition GaAs/Al0.15Ga0.85As?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?value ?label ?unit
WHERE
{
?HS QpOnto:hasMaterials ?HM.
?HM QpOnto:matFormula   "GaAs/Al0.15Ga0.85As"^^xsd:string.
?op QpOnto:relatesToHeterostructure ?HS;
qudt_qv:hasQuantityValue ?pv.
 ?pv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?unit RDFS:label ?label.
 FILTER(?unit=<https://qudt.org/vocab/unit/MilliW>).
}
```
Query 3.2: What are the possible frequency values for a QCL laser with a heterostructure with material composition In0.53Ga0.47As/GaAs0.51Sb0.49?
```
 PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?value ?label ?unit
WHERE
{
?HS QpOnto:hasMaterials ?HM.
?HM QpOnto:matFormula   "In0.53Ga0.47As/GaAs0.51Sb0.49"^^xsd:string.
?lf QpOnto:relatesToHeterostructure ?HS;
qudt_qv:hasQuantityValue ?fv.
 ?fv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?unit RDFS:label ?label.
 FILTER(?unit=<https://qudt.org/vocab/unit/TeraHZ>).
}
```
Query 3.3: What are the possible working temperature values for a QCL laser with a heterostructure with material composition GaAs/Al0.3Ga0.7As?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?value ?label ?unit
WHERE
{
?HS QpOnto:hasMaterials ?HM.
?HM QpOnto:matFormula   "GaAs/Al0.3Ga0.7As"^^xsd:string.
?lf QpOnto:relatesToHeterostructure ?HS;
qudt_qv:hasQuantityValue ?qv.
 ?qv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?unit RDFS:label ?label.
 FILTER(?unit=<https://qudt.org/vocab/unit/K>).
}
```
Query 4.1: What are the possible heterostructure designs for a QCL device with a working temperature greater than 100 K in Pulsed Mode?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?design_type ?label
WHERE
{
 ?wt qudt_qv:hasQuantityValue ?tv;
 QpOnto:correspondsToWorkingMode QpOnto:PulsedOperation;
 QpOnto:relatesToHeterostructure ?HS.
 ?tv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?HS QpOnto:hasDesignType ?design_type.
 ?design_type RDFS:label ?label.
 FILTER(?unit=<https://qudt.org/vocab/unit/K>&&?value>100).
}
```
Query 4.2:  What are the possible heterostructure designs for a QCL device with an optical power less than 50 mW?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX RDFS: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?design_type ?label
WHERE
{
 ?op qudt_qv:hasQuantityValue ?pv;
 QpOnto:relatesToHeterostructure ?HS.
 ?pv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?HS QpOnto:hasDesignType ?design_type.
 ?design_type RDFS:label ?label.
 FILTER(?unit=<https://qudt.org/vocab/unit/MilliW>&&?value<50).
}
```
 

