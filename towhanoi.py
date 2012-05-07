def towers(n,frompeg,topeg,auxpeg):
		#if only 1 disk, make the move and return 
		if n==1:
				print "\nMove disk 1 from peg %c to peg %c"%(frompeg,topeg)
				return 
		# Move top n-1 disks from A to B, using C as auxiliary 
		towers(n-1,frompeg,auxpeg,topeg)
		#Move remaining disks from A to C 
		print "\nMove disk %d from peg %c to peg %c"%(n,frompeg,topeg)
		#Move n-1 disks from B to C using A as auxiliary 
		towers(n-1,auxpeg,topeg,frompeg)
	
n = input("Enter No. of disks:")
print "The Tower of Hanoi involves the moves :\n"
towers(n,'A','C','B')

	 
