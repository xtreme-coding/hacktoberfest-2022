def sum_of_all_number(s):
    num=0
    sum=0
    for i in s:
        if i.isdigit():
            num=num*10+int(i)
        else:
            sum=sum+num
            num=0
    return sum+num

s=input("Enter String: ")
print("The Sum of Number Present in the Given String is",sum_of_all_number(s))
