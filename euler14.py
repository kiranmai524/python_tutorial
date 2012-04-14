var = 1000000
slen=0
num=0
for i in range(1,var):
		len=1
		seq=i
		while seq!=1:
				if seq%2==0:seq=seq/2
				else: seq=seq*3+1
				len+=1
		if len>slen:
				slen=len
				num=i
				
print " the starting number is %r, produces a sequence with %r numbers"%(num,slen)
				