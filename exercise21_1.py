def area_tri(l,b,h):
	print "Area Of Triangle %d * %d * %d" %(l,b,h)
	return l*b*h
area=area_tri(2,5,10)
print "area: %d" %area
def peri_rec(h,l,b):
	print "Area of Square 2*%d * %d + %d" %(h,l,b)
	return 2*h*(l+b)
perimeter=peri_rec(2,2,10)
print "perimeter of rectangle: %d" %perimeter
add=area+perimeter
print "tri+rec:",add
	