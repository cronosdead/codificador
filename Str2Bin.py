import binascii

def Str2Bin(s):
    A=[bin(ord(c))[2:] for c in s]
    B=[]
    for i in range(len(A)):
        B.append([int(d) for d in str(A[i])])	
    return B

def Bin2Str(array):
	s = ''.join(str(e) for e in array)
	s = int(s, 2)
	s = binascii.unhexlify('%x' % s)
	return s
    
