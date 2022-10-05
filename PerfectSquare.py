def perfect(num):
    for i in range(1,num):
        if i*i==num:
            return True
    return False
    
num=int(input("Enter Number: "))

if perfect(num):
    print("It is a Perfect Square")     
    
else:
    print("It is not a Perfect Square")
    
