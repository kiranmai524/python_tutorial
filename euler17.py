def check(num):
		if num==1:count=3
		elif num==2:count=3
		elif num==3:count=5
		elif num==4:count=4
		elif num==5:count=4
		elif num==6:count=3
		elif num==7:count=5
		elif num==8:count=5
		elif num==9:count=4
		elif num==10:count=3
		elif num==11:count=6
		elif num==12:count=6
		elif num==13:count=8
		elif num==14:count=8
		elif num==15:count=7
		elif num==16:count=7
		elif num==17:count=9
		elif num==18:count=9
		elif num==19:count=8
		elif num==20:count=6
		elif num==30:count=6
		elif num==40:count=5
		elif num==50:count=5
		elif num==60:count=5
		elif num==70:count=7
		elif num==80:count=6
		elif num==90:count=6
		else: count=0
		return count

def les_hun(num):
		sum=0
		if num/20==0:
				sum+=check(num%20)
		elif num/100==0:
				c=num%10
				num-=c
				sum+=check(c)
				sum+=check(num)
		return sum
		
var = 1000
count=0
for i in range(1,var+1,1):
		if i%1000==0:count+=11
		elif i/100==0:
				count+=les_hun(i)
		else:
				c=i%100
				r=i/100
				if c==0:count+=(check(r)+7)
				else:count+=(check(r)+10)
				count+=les_hun(c)			
print count
