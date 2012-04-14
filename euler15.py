size=21
grid=[[0 for x in xrange(size+1)]for x in xrange(size+1)]
for i in range(0,size,1):
		grid[i][size-1]=1;grid[size-1][i]=1
for i in range(size):
		for j in range(size):
				print grid[i][j],
		print "\n"
for i in range(size-2,-1,-1):
		for j in range(size-2,-1,-1):
				#print i,j,grid[i+1][j],grid[i][j+1]
				grid[i][j]=grid[i+1][j]+grid[i][j+1]
				#print grid[i][j]
print "the number of paths are", grid[0][0]