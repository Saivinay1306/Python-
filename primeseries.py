if __name__ == '__main__':
    print("startvalue:")
    m=int(input())
    list=[]
    print("Endvalue:")
    n=int(input())
    for num in range(m, n):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    list.append(num)
                    break
    print(list)

		
