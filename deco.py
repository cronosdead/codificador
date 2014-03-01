import Str2Bin as s2b
import binascii

s = s2b.Str2Bin('shit dos.')
print s
cad = ''
for i in range(len(s)):
	cad = cad + s2b.Bin2Str(s[i])
print cad
