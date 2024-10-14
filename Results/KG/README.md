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
Query 5.1: What are the possible heterostructure material compositions for a QCL device with a working temperature less than 85 K in the contionous wave mode?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    SELECT DISTINCT ?material_composition
WHERE
{
 ?wt qudt_qv:hasQuantityValue ?tv;
 QpOnto:correspondsToWorkingMode QpOnto:ContinousWaveOperation;
 QpOnto:relatesToHeterostructure ?HS.
 ?tv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?HS QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?material_composition.
 FILTER(?unit=<https://qudt.org/vocab/unit/K>&&?value<85).
}
```
Query 5.2: What are the possible heterostructure material compositions for a QCL device with a lasing frequency greater than 1.5 THz?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    SELECT DISTINCT ?material_composition
WHERE
{
 ?lf qudt_qv:hasQuantityValue ?fv;
 QpOnto:relatesToHeterostructure ?HS.
 ?fv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
 ?HS QpOnto:hasMaterials ?HM.
 ?HM QpOnto:matFormula ?material_composition.
 FILTER(?unit=<https://qudt.org/vocab/unit/TeraHZ>&&?value>1.5).
}
```
Query 6.1: What are the DOIs and URLS of scientific articles documenting QCL laser devices with an optical power greater than 10mW?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?power prov:wasAttributedTo ?article;
qudt_qv:hasQuantityValue  ?pv.
?pv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/MilliW>&&?value>100).
}
```
Query 6.2: What are the DOIs and URLS of scientific articles documenting QCL laser devices with a working temperature greater than 100 K in pulse mode?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?wt prov:wasAttributedTo ?article;
qudt_qv:hasQuantityValue  ?tv;
QpOnto:correspondsToWorkingMode QpOnto:PulsedOperation.
?tv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/K>&&?value>100).
}
```
Query 6.3: What are the DOIs and URLs of scientific articles documenting a QCL laser with a material composition of GaAs/Al0.3Ga0.7As?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?HS prov:wasAttributedTo ?article;
QpOnto:hasMaterials ?HM.
?HM QpOnto:matFormula "GaAs/Al0.25Ga0.75As"^^xsd:string.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
}
```
Query 6.4: What are the DOIs and URLs of scientific articles documenting QCL lasers with bound to continuum design type?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?HS prov:wasAttributedTo ?article.
?HS QpOnto:hasDesignType QpOnto:BoundToContinum.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
}
```
Query 6.5: What are the DOIs and URLs of articles documenting QCL lasers with a heterostructure of material composition GaAs/Al0.15Ga0.85As, LO phonon design type and working temperatures greater than 70 K in pulse mode operation?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    SELECT ?doi ?url
WHERE
{
?HS prov:wasAttributedTo ?article;
QpOnto:hasDesignType QpOnto:LOPhononDepopulation;
QpOnto:hasMaterials ?HM.
?HM QpOnto:matFormula "GaAs/Al0.15Ga0.85As"^^xsd:string.
?wt QpOnto:relatesToHeterostructure ?HS;
qudt_qv:hasQuantityValue ?tv.
?tv qudt:numericValue ?value;
qudt:hasUnit ?unit.
?article QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/K>&&?value>70).
}
```
Query 7.1: What are the DOIs and URLs of the articles being referenced by a QCL device with a working temperature greater than 225 K in the continuous wave mode?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    PREFIX bibo:<https://dcmi.github.io/bibo/#:>
    SELECT ?doi ?url
WHERE
{
?wt prov:wasAttributedTo ?article1;
qudt_qv:hasQuantityValue  ?tv;
QpOnto:correspondsToWorkingMode QpOnto:ContinousWaveOperation.
?article1 bibo:cites ?article2.
?tv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
?article2 QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/K>&&?value>225).
}
```
Query 7.2: What are the DOIs and URLs of the articles being referenced by a QCL device with an optical power less than 1 mW?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    PREFIX bibo:<https://dcmi.github.io/bibo/#:>
    SELECT ?doi ?url
WHERE
{
?op prov:wasAttributedTo ?article1;
qudt_qv:hasQuantityValue  ?pv.
?article1 bibo:cites ?article2.
?pv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
?article2 QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/MilliW>&&?value<1).
}
```
Query 7.3: What are the DOIs and URLs of the articles being referenced by a QCL device with a lasing frequency greater than 2.5 THz and an LO Phonon design type?
```
PREFIX QpOnto:<https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#>
    PREFIX qudt:<https://qudt.org/schema/qudt/>
    PREFIX qudt_qv: <https://qudt.org/schema/qudt/#>
    PREFIX prov:<http://www.w3.org/ns/prov#>
    PREFIX bibo:<https://dcmi.github.io/bibo/#:>
    SELECT ?doi ?url
WHERE
{
?lf prov:wasAttributedTo ?article1;
QpOnto:relatesToHeterostructure ?HS;
qudt_qv:hasQuantityValue  ?fv.
?HS QpOnto:hasDesignType QpOnto:LOPhononDepopulation.
?article1 bibo:cites ?article2.
?fv qudt:numericValue ?value;
 qudt:hasUnit ?unit.
?article2 QpOnto:DOI ?doi;
QpOnto:URL ?url.
FILTER(?unit=<https://qudt.org/vocab/unit/TeraHZ>&&?value>2.5).
}
```
 

