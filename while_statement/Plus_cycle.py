a=b= int(input())
count = 0

while(1):
    ten = int(a // 10)
    one = int(a % 10)
    result = ten + one    
    count += 1
    
    a = int(str(a % 10)+str(result%10))
   

    if(b == a):
        break
#---------------------
print(count)

