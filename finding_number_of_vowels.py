# created by Arunjay126
def countvowel():
    first = input('input a string')
    su = 0
    lis = []
    for x in first:
        if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
            su +=1
            lis.append(x)
        else: continue
    print('the total vowels are:',su)
    print('All the vowels are:',lis)
