if __name__ == '__main__':
    n=int(input())
    list=[]
    list1=[]
    for i in range(1,n):
        if(i%2==0):
            list.append(i)
        else:
            list1.append(i)
    print("even num:",list);
    print("odd num:",list1)   
    