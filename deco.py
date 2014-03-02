import Str2Bin as s2b
import binascii
import numpy as np

s = s2b.Str2Bin('ddshitdos')
n = np.array(s)
ns = np.transpose(n)

for i in range(len(ns)):
	print str(ns[i]).strip('[]')
	
cad = ''
(f, c) = ns.shape
cad = ''
aux = []
for i in range(c):
	for j in range(f):
		cad = cad + str(ns[j][i])
	aux.append(cad)
	cad = ''
print aux
m = ''
for i in range(len(aux)):
	h = int(aux[i], 2)
	m += binascii.unhexlify('%x' % h)
print m
