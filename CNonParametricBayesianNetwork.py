'''
File: CNonParametricBayesianNetwork.py
Author: Fernando Pasquini
Description: ---
'''

import numpy as np
import math as mt
from matplotlib import pyplot as plt
from scipy.stats import norm
import itertools
from scipy.stats.kde import gaussian_kde
from DFactor import *
from CBayesianNetwork import *

class CNonParametricBayesianNetwork(CBayesianNetwork):
	"""docstring for CNonParametricBayesianNetwork"""
	def __init__(self, variables):
		# initialize distribution parameters
		self.variables = variables
		self.children = {}
		self.parents = {}
		self.varorder = []
		for var in self.variables:
			self.children[var] = []
			self.parents[var] = []
			self.varorder.append(var)
		self.singlekdes = {}
		for variable in self.variables:
			self.singlekdes[variable] = 0

	def trainMLE(self,trainingDict):
		"""docstring for trainMLE"""
		trainingValues = []
		for v in self.varorder:
			trainingValues.append(trainingDict[v])
		trainingValues = np.array(trainingValues)
		for variable in self.variables:
			# indice of current variable
			varindex = self.varorder.index(variable)
			# indexes of parent variables
			indexes = [self.varorder.index(j) for j in self.variables if j in self.parents[variable]]
			indexes.sort()
			self.singlekdes[variable] = gaussian_kde(trainingValues[varindex])
		# now we need to know how to use the joint probability distribution!
		self.jointkde = gaussian_kde(trainingValues)

	def inferVariable(self,variable,valuesDict):
		"""docstring for inferVariable"""
		pass

if __name__=='__main__':
	print 'Testing Bayesian Network!'
	bay = CNonParametricBayesianNetwork(('A','B','C','D'))
	bay.addChild('A','B')
	bay.addChild('B','C')
	bay.addChild('B','D')
	bay.addChild('A','D')
	print bay
	print 'Training with MLE'
	trainingDict = {}
	# all variable values are correlated! (trainingDict[x][0] refers to same instance of trainingDict[y][0])
	trainingDict['A'] = np.array([1.0,3.0,6.0,7.0,2.0,6.0,3.0,3.0,6.0,2.0,6.0,3.0,5.0,4.0])
	trainingDict['B'] = np.array([5.0,7.0,3.0,7.0,3.0,5.0,2.0,7.0,2.0,5.0,1.0,1.0,1.0,4.0])
	trainingDict['C'] = np.array([3.0,4.0,5.0,6.0,3.0,5.0,6.0,4.0,9.0,3.0,3.0,3.0,3.0,1.0])
	trainingDict['D'] = np.array([2.0,5.0,5.0,2.0,3.0,5.0,9.0,3.0,1.0,2.0,5.0,2.0,2.0,2.0])
	bay.trainMLE(trainingDict)
	bay.inferVariable('D',{'A':2,'B':2,'C':2})
