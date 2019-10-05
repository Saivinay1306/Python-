n=int(input())
for num in range(1, n + 1):   
   if num > 1:
       for i in range(2, int(num/2)+1):
           if (num % i) == 0:
               break
       else:
           print(num)


		
