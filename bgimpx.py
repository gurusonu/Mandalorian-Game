from PIL import Image
from sys import argv
import numpy as np
class Pxl:
	def __init__(self,path):
		self._path=path
		self._pixel_values=[]
		self._width=238
		self._height=50
	def getpx(self):	
		image=Image.open(self._path, 'r')
		image=image.resize((self._width,self._height ), Image.ANTIALIAS)
		image=image.convert('RGB')
		self._pixel_values = list(image.getdata())
		self._pixel_values = np.array(self._pixel_values).reshape((self._height,self._width, 3))
		return self._pixel_values















