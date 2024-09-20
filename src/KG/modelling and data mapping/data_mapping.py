# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:26:39 2024

@author: Deperias Kerre
"""
#importing a graph structure and other ontology URIs
from rdflib import Graph

#import other libraries
from rdflib import Graph, Literal, RDF, RDFS, URIRef, OWL

#loading th KG schema
myGraph=Graph()
myGraph.parse("C:/Users/USER/Documents/Projects/KG Scripts/scripts/KG_Schema.ttl")

