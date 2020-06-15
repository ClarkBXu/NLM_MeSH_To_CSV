# NLM_MeSH_To_CSV
Script for converting National Library of Medicine MeSH Files from XML to CSV for medical concept searching.

## Author
Clark Xu - June 15, 2020

## Purpose
The script converts descriptors in the 2020 National Library of Medicine (NLM) MeSH Data from XML to CSV File Format for ease of medical concept searching on the NLM website. Contribution to the PAGER-COV Project.

NLM Files documented at: https://www.nlm.nih.gov/databases/download/mesh.html <br>
PAGER-COV documented at: http://discovery.informatics.uab.edu/PAGERCOV/

## Specifications and Dependencies
### Specifications:
Python 3
### Dependencies:
csv, urllib, xml

## Details
NLM features transformed into CSV: <br>
DescriptorClass, DescriptorUI, NLMClassificationNumber, DescriptorName, DateCreated, Annotation, AllowableQualifiersList, PharmacologicalActionList, OnlineNote, HistoryNote, PublicMeSHNote

## Licensing (The MIT License)
Copyright 2020 Clark Xu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
