'''
File: DFactor.py
Author: Fernando Pasquini
Description: Class for factor with discrete parameters
'''

import numpy as np
import math as mt
from matplotlib import pyplot as plt
import itertools

class DFactor:
	"""
	Discrete Factor to use in calculations.
	self.possibilities: all combinations of variables in the factor
	self.values: values for all the tuples
	"""

	def __init__(self,varstuples):
		""" varstuples: ((x1,x2,x3), (y1, y2))"""
		self.variables = varstuples
		self.possibilities = list(itertools.product(*varstuples))
		self.values = dict.fromkeys(self.possibilities)

	def __str__(self):
		"""docstring for __str__"""
		return self.values.__str__()

	def setValueForVariables(self,varstuple,val):
		"""sets the value indicated *val* to the combination of variables indicated in the tuple *varstuple* """
		self.values[varstuple] = val

	def __mul__(self,other):
		"""overloads the multiplication operator to make a dot product between two factors"""
		new = self.__class__(self.variables + other.variables,initialize=False)
		# Multiply values
		return new

class DPDF(DFactor):
	""" Probability Density Fucntion"""
	def __init__(self, varstuples, initialize=True):
		DFactor.__init__(self,varstuples)
		if initialize:
			self.initializePdf()

	"""pdf related functions"""
	def initializePdf(self):
		"""initializes factor as a pdf (sum = 1)"""
		basedivision = []
		for i in range(len(self.variables)):
			basedivision.append(float(1./len(self.variables[i])))
		for value in self.values:
			self.values[value] = np.prod(basedivision)

	def checkPdf(self):
		"""returns an error if the values in the factor don't correspond to pdfs"""
		pass
