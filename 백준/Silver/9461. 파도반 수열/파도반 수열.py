n = int(input())

padovan=[0 for i in range(100)]
padovan[0]=1
padovan[1]=1
padovan[2]=1
padovan[3]=2
padovan[4]=2

for x in range(n):
    num=int(input())
    for i in range(5,num):
        padovan[i]=padovan[i-5]+padovan[i-1]
    print(padovan[num-1])
