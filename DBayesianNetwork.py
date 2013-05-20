'''
File: DBayesianNetwork.py
Author: Me
Description:
'''

import numpy as np
import math as mt
from matplotlib import pyplot as plt
import itertools
from DFactor import *

class DBayesianStruct():
	"""docstring for BayesianStruct"""
	def __init__(self, varstuples):
		self.variables = varstuples
		self.children = {}
		for var in self.variables:
			self.children[var] = []
		print self.children

	def addChild(self,parentvar,childvar):
		"""docstring for setChildren"""
		if (childvar not in self.variables) or (parentvar not in self.variables):
			raise RuntimeError("incorrect variables in the Bayesian Struct")
		self.children[parentvar].append(childvar)

	def checkDAG():
		"""checks if we have a DAG in the structure"""
		pass

class DBayesianNetwork():
	"""docstring for DBayesianNetwork"""
	def __init__(self, varstuples, initialize=True):
		self.variables = varstuples
		self.jd = DPDF(varstuples)
