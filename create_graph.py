'''
Created on Dec 21, 2015

@author: redward
'''
import sys
from arelle import CntlrCmdLine
sys.argv = ['','-f', 'http://www.sec.gov/Archives/edgar/data/66740/000155837015002024/mmm-20150930.xml', '--keepOpen',
             '--store-to-XBRL-DB',
            'rdfTurtleFile,None,None,None,/home/redward/Downloads/turtle_3m.rdf,None,rdfDB']

result, model, graph = CntlrCmdLine.xbrlTurtleGraphModel('http://www.sec.gov/Archives/edgar/data/1333822/000155837016006627/0001558370-16-006627-xbrl.zip')
print(model)

x = 5