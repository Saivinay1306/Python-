
   
## recursive approach for factorial

def factorial(n):
   if n == 0:
     return 1
   else:
     return n *factorial(n-1)

n=int(input())
b=factorial(n)
print(b)

## factorial for traditional approach

n=int(input())
fact=1
for i in range(1,n):
   fact=fact*i

print(fact)
