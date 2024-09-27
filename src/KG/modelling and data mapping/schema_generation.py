# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 08:20:39 2024

@author: Deperias Kerre
"""

#libraries for the graph instance and namespaces
from rdflib import Graph, RDF, RDFS, URIRef, Namespace

#Creating a graph instance and adding all the defined properties
myGraph=Graph()

#binding Ontology prefixes to namespaces
namespace_qcl_onto = Namespace("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#")
myGraph.bind("QpOnto", namespace_qcl_onto)
#BIBO ontology
namespace_bibo=Namespace("https://dcmi.github.io/bibo/#:")
myGraph.bind("bibo", namespace_bibo)
#MDO ontology
namespace_mdo=Namespace("https://w3id.org/mdo/core/")
myGraph.bind("mdo", namespace_mdo)

#URIs

# 1.KG Schema Classes
##agent
agent=URIRef("https://www.w3.org/TR/prov-o/#Agent")

##academic article
academic_article=namespace_bibo["AcademicArticle"]

##property
Property=namespace_mdo["Property"]

##laser working mode
working_mode=namespace_qcl_onto["LaserWorkingMode"]

##optoelectronic characteristics
working_temperature=namespace_qcl_onto["WorkingTemperature"]
optical_power=namespace_qcl_onto["OpticalPower"]
lasing_frequency=namespace_qcl_onto["LasingFrequency"]

##laser heterostructure
heterostructure=namespace_qcl_onto["LaserHeterostructure"]

##heterostructure materials
materials=namespace_qcl_onto["HeterostructureMaterials"]

##design type
laser_design=namespace_qcl_onto["LaserDesignType"]

##unit
unit=URIRef("https://qudt.org/schema/qudt/Unit")

##quantity kind
quantity_kind=URIRef("https://qudt.org/schema/qudt/QuantityKind")

##quantity value
quantity_value= URIRef("http://qudt.org/schema/qudt/QuantityValue")

##quantity kind
qudt_quantitykind="https://qudt.org/vocab/quantitykind/"

# 2.URIs for Class Instances

##Laser Working Modes
continous_wave=namespace_qcl_onto["ContinousWaveOperation"]
pulsed_mode=namespace_qcl_onto["PulsedOperation"]

##Laser Design Types
lo_phonon=namespace_qcl_onto["LOPhononDepopulation"]
bound_continum=namespace_qcl_onto["BoundToContinum"]
double_resonant=namespace_qcl_onto["DoubleResonantPhonon"]

##Property Units
qudt_unit="https://qudt.org/vocab/unit/"
Kelvin=URIRef(qudt_unit+"K")
Milliwatt=URIRef(qudt_unit+"MilliW")
TeraHertz=URIRef(qudt_unit+"TeraHZ")

##URIs for Quantity Kinds
power=URIRef(qudt_quantitykind+"Power")
frequency=URIRef(qudt_quantitykind+"Frequency")
temperature=URIRef(qudt_quantitykind+"Temperature")

##URIs for quantity Values
frequency_value=namespace_qcl_onto["FrequencyValue"]
power_value= namespace_qcl_onto["PowerValue"]
temperature_value=namespace_qcl_onto["WorkingTempValue"]

#3.URIs for object properties 

#was attributed to
attributed_to=URIRef("http://www.w3.org/ns/prov#wasAttributedTo")
#has materials
has_materials=namespace_qcl_onto["hasMaterials"]
#has quantity kind
has_quantitykind=URIRef("https://qudt.org/schema/qudt/hasQuantityKind")
#has design type
has_designtype=namespace_qcl_onto["hasDesignType"]
#relates to heterostructure
relates_to_heterostructure=namespace_qcl_onto["relatesToHeterostructure"]
#corresponds to working mode
corresponds_to_working_mode=namespace_qcl_onto["correspondsToWorkingMode"]
#has unit
has_unit=URIRef("https://qudt.org/schema/qudt/hasUnit")
#cites
cites= URIRef("https://dcmi.github.io/bibo/#:cites")
#was attributed to
attributed_to=URIRef("http://www.w3.org/ns/prov#wasAttributedTo")
#has quantity value
has_quantity_value=URIRef("https://qudt.org/schema/qudt#hasQuantityValue")
#sub class of
#for the rdfs subclass, no need to define as its already included in the imported RDFS library

#4.URIs for data properties
doi_prop=namespace_qcl_onto["DOI"]
materials_prop=namespace_qcl_onto["matFormula"]
numerical_value=URIRef("https://qudt.org/schema/qudt/numericValue")
publication_url=namespace_qcl_onto["URL"]

#datatypes
string=URIRef("http://www.w3.org/2001/XMLSchema#string")
number=URIRef("https://schema.org/Number")
URL=URIRef("https://schema.org/URL")

##mapping subclasses
myGraph.add((academic_article, RDFS.subClassOf, agent))

##mapping class instances

#property instances
myGraph.add((working_temperature, RDF.type, Property))
myGraph.add((optical_power, RDF.type, Property))
myGraph.add((lasing_frequency, RDF.type, Property))

#working modes
myGraph.add((continous_wave, RDF.type, working_mode))
myGraph.add((pulsed_mode, RDF.type, working_mode))

#design types
myGraph.add((lo_phonon, RDF.type, laser_design))
myGraph.add((bound_continum, RDF.type, laser_design))
myGraph.add((double_resonant, RDF.type, laser_design))

#units
myGraph.add((Kelvin, RDF.type, unit))
myGraph.add((Milliwatt, RDF.type, unit))
myGraph.add((TeraHertz, RDF.type, unit))

#quantity values
myGraph.add((frequency_value, RDF.type, quantity_value))
myGraph.add((power_value, RDF.type, quantity_value))
myGraph.add((temperature_value, RDF.type, quantity_value))

#quantity kinds
myGraph.add((power, RDF.type, quantity_kind))
myGraph.add((frequency, RDF.type, quantity_kind))
myGraph.add((temperature, RDF.type, quantity_kind))

##Implementing the object properties

#cite property
myGraph.add((academic_article, cites, academic_article))

#was attributed to
myGraph.add((working_temperature, attributed_to, academic_article))
myGraph.add((optical_power, attributed_to, academic_article))
myGraph.add((lasing_frequency, attributed_to, academic_article))
myGraph.add((heterostructure, attributed_to, academic_article))
myGraph.add((working_mode, attributed_to, academic_article))

#correspons to working mode
myGraph.add((working_temperature, corresponds_to_working_mode, working_mode))

#has quantity kind
myGraph.add((working_temperature, has_quantitykind, temperature))
myGraph.add((optical_power, has_quantitykind, power))
myGraph.add((lasing_frequency, has_quantitykind, frequency))

#has Quantity Value
myGraph.add((working_temperature, has_quantity_value, temperature_value))
myGraph.add((optical_power, has_quantity_value, power_value))
myGraph.add((lasing_frequency, has_quantity_value, frequency_value))

#relates to heterostructure
myGraph.add((working_temperature, relates_to_heterostructure, heterostructure))
myGraph.add((optical_power, relates_to_heterostructure, heterostructure))
myGraph.add((lasing_frequency, relates_to_heterostructure, heterostructure))

#has materials
myGraph.add((heterostructure, has_materials, materials))

#has design type
myGraph.add((heterostructure, has_designtype, laser_design))

#has unit
myGraph.add((power_value, has_unit, Milliwatt))
myGraph.add((frequency_value, has_unit, TeraHertz))
myGraph.add((temperature_value, has_unit, Kelvin))

#Generating the KG Schema in turtle format
myGraph.serialize(destination="KG_Schema.ttl")