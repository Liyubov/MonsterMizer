# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:07:43 2016

@author: Olivier
"""

import defineTables as tabDef
import dataset
import csvToDatabase

csvFile='../1_initialRawData/screensaver.csv'

csvToDatabase.csvToDatabase(csvFile,tabDef.screenSaverTab)

db = dataset.connect('sqlite:///olidata.db')
