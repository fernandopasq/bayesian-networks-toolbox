'''
File: CBayesianNetwork.py
Author: Fernando Pasquini
Description: ---
'''

import numpy as np
import math as mt
from matplotlib import pyplot as plt
from scipy.stats import norm
import itertools
from DFactor import *

class CBayesianNetwork():
	"""docstring for CCBayesianNetwork"""
	def __init__(self, variables):
		self.variables = variables
		self.children = {}
		self.parents = {}
		self.varorder = []
		for var in self.variables:
			self.children[var] = []
			self.parents[var] = []
			self.varorder.append(var)

		self.beta = {}
		self.stdv = {}
		for variable in self.variables:
			# array with beta values in relationship to all other variables, beta0 is the position of the variable
			self.beta[variable] = [0]*len(self.variables)
			self.stdv[variable] = 0

	def addChild(self,parentvar,childvar):
		"""docstring for addChild"""
		if (childvar not in self.variables) or (parentvar not in self.variables):
			raise RuntimeError("incorrect variables in the Bayesian Struct")
		self.children[parentvar].append(childvar)
		self.parents[childvar].append(parentvar)

	def CheckDAG(self):
		"""docstring for CheckDAG"""
		pass

	def __str__(self):
		"""docstring for __str__"""
		s = 'Bayesian Network on variables %s\n'%(self.variables.__str__())
		for var in self.variables:
			s += '%s -> %s\n'%(var,self.children[var])
		return s

	def trainMLE(self,trainingDict):
		"""get network parameters using MLE estimates"""
		trainingValues = []
		for v in self.varorder:
			trainingValues.append(trainingDict[v])
		trainingValues = np.array(trainingValues)
		covM = np.matrix(np.cov(trainingValues))
		for variable in self.variables:
			varindex = self.varorder.index(variable)
			# indexes of parent variables
			indexes = [self.varorder.index(j) for j in self.variables if j in self.parents[variable]]
			indexes.sort()
			if indexes != []:
				covyx = np.matrix([covM[varindex,j] for j in indexes])
				covxy = np.matrix([[covM[j,varindex]] for j in indexes])
				covParentsInv = np.matrix(np.cov([trainingValues[i] for i in indexes])).I
				# beta[i]
				betam = covParentsInv*covxy
				for i in range(len(indexes)):
					self.beta[variable][indexes[i]] = betam[i,0]
				# beta0
				means = np.matrix([[trainingValues[j].mean()] for j in indexes])
				self.beta[variable][varindex] = trainingValues[varindex].mean() - float(covyx*covParentsInv*means)
				self.stdv[variable] = covM[varindex,varindex] - float(covyx*covParentsInv*covxy)
			else:
				# common gaussian
				self.beta[variable][varindex] = trainingValues[varindex].mean()
				self.stdv[variable] = trainingValues[varindex].std()
		print 'results of training:'
		print self.varorder
		print 'beta:'
		print self.beta
		print 'stdv:'
		print self.stdv

	def trainBayesian(self,trainingDict, meanPriorDict, stdvPriorDict):
		"""get network parameters using Bayesian training"""
		pass

	def inferVariable(self,variable,valuesDict):
		"""Returns mean and variance of the gaussian representing the pdf of a variable, given some observed values"""
		# still it's good to test if variables are coherent!
		varindex = self.varorder.index(variable)
		indexes = [self.varorder.index(j) for j in self.variables if j in self.parents[variable]]
		mean = self.beta[variable][varindex]
		for i in indexes:
			mean = mean + self.beta[variable][i]*valuesDict[self.varorder[i]]
		fig = plt.figure()
		x = np.arange(-15,15,0.1)
		ax1 = fig.add_subplot(111)
		ax1.plot(norm.pdf(x,mean,self.stdv[variable]))

if __name__=='__main__':
	print 'Testing Bayesian Network!'
	bay = CBayesianNetwork(('A','B','C','D'))
	bay.addChild('A','B')
	bay.addChild('B','C')
	bay.addChild('B','D')
	bay.addChild('A','D')
	print bay
	print 'Training with MLE'
	trainingDict = {}
	# all variable values are correlated! (trainingDict[x][0] refers to same instance of trainingDict[y][0])
	trainingDict['A'] = [1,3,6,7,2,6,3,3,6,2,6,3,5,4]
	trainingDict['B'] = [5,7,3,7,3,5,2,7,2,5,1,1,1,4]
	trainingDict['C'] = [3,4,5,6,3,5,6,4,9,3,3,3,3,1]
	trainingDict['D'] = [2,5,5,2,3,5,9,3,1,2,5,2,2,2]
	bay.trainMLE(trainingDict)
	bay.inferVariable('D',{'A':2,'B':2,'C':2})
