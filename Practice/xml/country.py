#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:01:49 2018

@author: elishatam
"""

from xml.dom import minidom
xmldoc = minidom.parse('country.xml')
print(xmldoc.toxml())
country = xmldoc.getElementsByTagName("country")
firstchild = country[0]
print(firstchild.attributes["name"].value)
#simple string mathod to replace
#print(firstchild.attributes["name"].value.replace("Liechtenstein", "Germany"))
firstchild.attributes["name"].value = "Germany"
print(xmldoc.toxml())