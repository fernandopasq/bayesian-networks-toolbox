# teste
from pylab import *

class DFactor:
	"""varsdict is a dict whose keys are variables and values are tuples with the possible assuming values
	for example: { x:(x1, x2, x3), y:(y1, y2) }
	"""
	def __init__(self,varsdict):
		self.varsdict = varsdict
		numvalues = 1
		for variable in varsdict.keys():
			numvalues = numvalues * len(varsdict[variable])
		self.values = zeros((numvalues))
		print self.values

	def getValueIndex(vars_values_dict):
		indexes = dict(zip(self.varsdict.keys(),[0]*len(self.varsdict.keys())))
		for variable in vars_values_dict.keys():
			if(self.varsdict[variable]):
				indexes[variable] = 
			else:
				print "ERROR!!!"
