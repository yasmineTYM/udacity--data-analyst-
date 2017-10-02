from pymongo import MongoClient
import csv
import json
import io
import re
import pprint


field_map = {
    "name" : "name",
    "bodyStyle_label" : "bodyStyle",
    "assembly_label" : "assembly",
    "class_label" : "class",
    "designer_label" : "designer",
    "engine_label" : "engine",
    "length" : "length",
    "height" : "height",
    "width" : "width",
    "weight" : "weight",
    "wheelbase" : "wheelbase",
    "layout_label" : "layout",
    "manufacturer_label" : "manufacturer",
    "modelEndYear" : "modelEndYear",
    "modelStartYear" : "modelStartYear",
