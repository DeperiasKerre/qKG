# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:13:36 2024

@author: Deperias Kerre
"""
#importing a graph structure and other ontology URIs
from rdflib import Graph
#import other libraries
from rdflib import Graph, Literal, RDF, RDFS, URIRef, OWL, Namespace

#Generating the KG Schema
##Creating a graph instance and adding all the defined properties
myGraph=Graph()

#binding namespace prefixes
##QCL Ontology
namespace_qcl_onto = Namespace("https://github.com/DeperiasKerre/qcl_Onto/blob/main/qclontology/version-1.0/qclonto.owl#")
myGraph.bind("QpOnto", namespace_qcl_onto)
#BIBO ontology
namespace_bibo=Namespace("https://dcmi.github.io/bibo/#:")
myGraph.bind("bibo", namespace_bibo)
##MDO ontology
namespace_mdo=Namespace("https://w3id.org/mdo/core/")
myGraph.bind("mdo", namespace_mdo)
##QUDT-The QUDT ontology has several subdivisions of vocabularies
###Units
namespace_qudt_units = Namespace("https://qudt.org/vocab/unit/")
myGraph.bind("QUDT.units", namespace_qudt_units)
###Quantity Kinds
namespace_qudt_quantity_kind = Namespace("https://qudt.org/vocab/quantitykind/")
myGraph.bind("QUDT.quantity_kinds", namespace_qudt_quantity_kind)
###properties
namespace_qudt_properties = Namespace("https://qudt.org/schema/qudt/")
myGraph.bind("QUDT.properties", namespace_qudt_properties)

#URIS for KG Concepts

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

##URIs for quantity Values
frequency_value=namespace_qcl_onto["FrequencyValue"]
power_value= namespace_qcl_onto["PowerValue"]
temperature_value=namespace_qcl_onto["WorkingTempValue"]

##URIs for Quantity Kinds
power=namespace_qudt_quantity_kind["Power"]
frequency=namespace_qudt_quantity_kind["Frequency"]
temperature=namespace_qudt_quantity_kind["Temperature"]

##URIS for Units
Kelvin=namespace_qudt_units["K"]
Milliwatt=namespace_qudt_units["MilliW"]
TeraHertz=namespace_qudt_units["TeraHZ"]

##Laser Working Modes
continous_wave=namespace_qcl_onto["ContinousWaveOperation"]
pulsed_mode=namespace_qcl_onto["PulsedOperation"]

##Laser Design Types
lo_phonon=namespace_qcl_onto["LOPhononDepopulation"]
bound_continum=namespace_qcl_onto["BoundToContinum"]
double_resonant=namespace_qcl_onto["DoubleResonantPhonon"]

#URIS for properties
#URIS for object properties
#was attributed to
attributed_to=URIRef("http://www.w3.org/ns/prov#wasAttributedTo")
#has materials
has_materials=namespace_qcl_onto["hasMaterials"]
#has quantity kind
has_quantitykind=namespace_qudt_properties["hasQuantityKind"]
#has design type
has_designtype=namespace_qcl_onto["hasDesignType"]
#relates to heterostructure
relates_to_heterostructure=namespace_qcl_onto["relatesToHeterostructure"]
#corresponds to working mode
corresponds_to_working_mode=namespace_qcl_onto["correspondsToWorkingMode"]
#has unit
has_unit=namespace_qudt_properties["hasUnit"]
#cites
cites= namespace_bibo["cites"]
#was attributed to
attributed_to=URIRef("http://www.w3.org/ns/prov#wasAttributedTo")
#has quantity value
has_quantity_value=namespace_qudt_properties["hasQuantityValue"]

#URIs for data properties
doi_prop=namespace_qcl_onto["DOI"]
materials_prop=namespace_qcl_onto["matFormula"]
numerical_value=namespace_qudt_properties["numericValue"]
publication_url=namespace_qcl_onto["URL"]

#datatypes
string=URIRef("http://www.w3.org/2001/XMLSchema#string")
number=URIRef("https://schema.org/Number")
URL=URIRef("https://schema.org/URL")

##mapping subclasses and class instances
myGraph.add((academic_article, RDFS.subClassOf, agent))

#property class instances
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

#number of graph elements
print(f"Number of elements:{len(myGraph)}")

#Generating the KG Schema in turtle format
myGraph.serialize(destination="KG_Schema.ttl")
