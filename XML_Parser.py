# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:01:19 2020

@author: CBX033
"""

import csv 
import urllib.request as request
import xml.etree.ElementTree as ET 

def addElements(record,recordInfo,featureList):
    """
    Input: record - node from XML File, 
                    recordInfo - dict of info about record, 
                    featureList - list of features to parse
    Output: Updated recordInfo with text of features in featureList
    """
    for entry in featureList:
        try:
            #Locate feature in the record
            feature = record.find(entry)
            #Add feature text under feature tag to record info
            recordInfo[feature.tag] = feature.text.strip()
        except AttributeError:
            print(entry,'of type',type(entry),'in record',record,'is missing text method')
    return recordInfo

def loadXML(url): 
    """
    Input: url - str for URL of XML File
    Returns: data - bytes object of XML File
    """
    response = urllib.request.urlopen(url)
    data = response.read()
    return data

def parseXML(data,recordAttribute,recordFeatures): 
    """
    Input: data - bytes object of XML File,
           recordAttribute - attribute of the top node in the XML
           recordFeatures - features of the top node in the XML
    Returns: descriptorRecords - list of dict with record info
    """
    root = ET.fromstring(data)
    
    #Get Descriptor Record
    descriptorRecords = []
    for record in root:
        #Initialize dictionary of record info
        recordInfo = {}
        #Add record attribute to record info
        recordInfo[recordAttribute] = record.attrib
        #Update record features in record info
        recordInfo = addElements(record,recordInfo,recordFeatures)
        #Add record info to list of all records
        descriptorRecords.append(recordInfo)
    return descriptorRecords

def createCSV(data,headers,fileName):
    """
    Input: data - dict to read in,
           headers - list of csv headers,
           fileName - str for csv file name
    Output: Writes csv to directory under fileName
    """
    with open(fileName,mode='w',newline='',errors="ignore") as csvFile: 
        #CSV writer from dict
        csvWriter = csv.DictWriter(csvFile,fieldnames=headers) 
        #Writing headers 
        csvWriter.writeheader() 
        #Writing data 
        csvWriter.writerows(data) 
    return True

def main():
    meshData = loadXML(url='ftp://nlmpubs.nlm.nih.gov/online/mesh/MESH_FILES/xmlmesh/desc2020.xml')
    if meshData:
        print('XML loading complete')
    xmlData = parseXML(data=meshData,
                       recordAttribute='DescriptorClass',
                       recordFeatures=['DescriptorUI','NLMClassificationNumber','DescriptorName','DateCreated',
                                       'Annotation','AllowableQualifiersList','PharmacologicalActionList',
                                       'OnlineNote','HistoryNote','PublicMeSHNote'])
    if xmlData:
        print('XML parsing complete')
    complete = createCSV(data=xmlData,
                         headers=['DescriptorClass',
                                  'DescriptorUI','NLMClassificationNumber','DescriptorName','DateCreated',
                                  'Annotation','AllowableQualifiersList','PharmacologicalActionList',
                                  'OnlineNote','HistoryNote','PublicMeSHNote'],
                         fileName='MeSH_2020_Desc.csv')
    if complete:
        print("Script Done")

if __name__ == '__main__':
    main()