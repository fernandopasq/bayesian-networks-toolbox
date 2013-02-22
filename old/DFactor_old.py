from pylab import *

""" Discrete Factor """
class DFactor:
	"""varsdict is a dict whose keys are variables and values are tuples with the possible assuming values
	for example: { x:(x1, x2, x3), y:(y1, y2) }
	"""
	def __init__(self,varsdict):
		self.varsdict = varsdict
		numvalues = 1
		for variable in varsdict.keys():
			numvalues = numvalues * len(varsdict[variable])
		# self.values will be a vector with values for each variable
		self.values = zeros((numvalues))
	
	"""
	vars_values_dict is a dictionary like { x:(x1,0), y:(y2,0) }
	"""
	def setValuesFor(vars_values_dict)
		indexes = []
		for variableToSet in vars_values_dict.keys():
			something = vars_values_dict[variableToSet]
		for i in range(len(varsdict.keys())):
			for j in range(len(self.varsdict[self.varsdict.keys()[i]])):
				if self.varsdict[i][j] == vars_values[i]:
					indexes[i] = i

	def getValueIndex(self,vars_values_dict):
		indexes = dict(zip(self.varsdict.keys(),[0]*len(self.varsdict.keys())))
		for variable in vars_values_dict.keys():
			for i in range(len(self.varsdict[variable])):
				if (self.varsdict[variable][i] == vars_values_dict[variable][0])
					indexes[variable] = i 
		print indexes
		"""possible_values = zeros(len(varsdict.keys()))
		for i in range(len(varsdict.keys())):
			possible_values[i] = len(self.varsdict[self.varsdict.keys()[i]])
			print possible_values
                        for j in range(len(self.varsdict[self.varsdict.keys()[i]])):
                                if self.varsdict[self.varsdict.keys()[i]][j] == vars_values_dict[self.varsdict.keys()[i]][0]:
                                        index = i*j
		"""

