#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(root_dir)

from bencoder import PyBencoder

class PyBencoderTests(unittest.TestCase):
    ''' A test class for PyBencoder class '''
    
    def setUp(self):
        self.bencoder = PyBencoder()

    def testEncodeNoInputData(self):
        self.assertEqual(self.bencoder.encode(), None)

    def testEncodeIntegerInput(self):
        self.assertEqual(self.bencoder.encode(123), "i123e")

    def testEncodeIntegerInputNegative(self):
        self.assertEqual(self.bencoder.encode(-123), "i-123e")

    def testEncodeStringInput(self):
        self.assertEqual(self.bencoder.encode("123"), "3:123")
        
    def testEncodeStringNoASCIIData(self):
        self.assertEqual(self.bencoder.encode('şţoâîăăşâß'), None)        

    def testEncodeIntegerZero(self):
        self.assertEqual(self.bencoder.encode(0), "i0e")

    def testDecodeNoInput(self):
        self.assertEqual(self.bencoder.decode(), None)

    def testDecodeIntegerValidInput(self):
        self.assertEqual(self.bencoder.decode('i123e'), 123)
        
    def testDecodeIntegerInvalidInput(self):
        self.assertEqual(self.bencoder.decode('i12asd3e'), None)        

    def testDecodeStringValidInput(self):
        self.assertEqual(self.bencoder.decode('3:red'), 'red')

    def testDecodeStringInvalidInput(self):
        self.assertEqual(self.bencoder.decode('3:re'), None)

    def testEncodeEmptyList(self):
        self.assertEqual(self.bencoder.encode([]), "le")

    def testEncodeValidSimpleList(self):
        self.assertEqual(self.bencoder.encode([1, 2, 'string']), 'li1ei2e6:stringe')
        
    def testEncodeValidComplexList(self):
        self.assertEqual(self.bencoder.encode([1, 2, [3, 4]]), 'li1ei2eli3ei4eee')

    def testEncodeNotAllowedType(self):
        unknown_type = str
        self.assertEqual(self.bencoder.encode(unknown_type), None)
   
if __name__ == '__main__':
    #unittest.main()
    
    #suite = unittest.TestSuite()
    #suite.addTest(BenIntTest("testEncodeNoInputData"))


    suite = unittest.TestLoader().loadTestsFromTestCase(PyBencoderTests)    
    unittest.TextTestRunner(verbosity=3).run(suite)        
       