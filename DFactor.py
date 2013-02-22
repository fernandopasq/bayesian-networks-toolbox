'''
File: DFactor.py
Author: Fernando Pasquini
Description: Class for factor with discrete parameters
'''

from pylab import *
import itertools

class DFactor:
	"""
	Discrete Factor to use in calculations.
	self.possibilities: all combinations of variables in the factor
	self.values: values for all the tuples
	"""

	def __init__(self,varstuples):
		""" varstuples: ((x1,x2,x3), (y1, y2))"""
		self.possibilities = list(itertools.product(*varstuples))
		self.values = dict.fromkeys(self.possibilities)

	def setValueForVariables(self,varstuple,val):
		"""sets the value indicated *val* to the combination of variables indicated in the tuple *varstuple* """
		self.values[varstuple] = val

class DPDF(DFactor):
	""" Probability Density Fucntion"""
	def __init__(self, varstuples):
		super(DPDF, self).__init__()
		
	"""pdf related functions"""
	def initializePdf(self):
		"""initializes factor as a pdf (sum = 1)"""
		pass

	def checkPdf(self):
		"""returns an error if the values in the factor don't correspond to pdfs"""
		pass
