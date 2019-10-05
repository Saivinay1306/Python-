
## easy approach
n=int(input())
a,b=0,1
while n!=0:
  print(b)
  a,b=b,a+b
  n=n-1;







#traditional met 
n=int(input())
a=0;
b=1;
print(a,b)
while(b<=n):
 	c=a+b
 	print(c)
 	a=b
 	b=c