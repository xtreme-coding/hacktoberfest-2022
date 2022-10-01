test_string = "geekforgeeks"
 
# printing original string
print("The original string : " + str(test_string))
 
# using join() + sorted()
# Sorting a string
res = ''.join(sorted(test_string))
     
# print result
print("String after sorting : " + str(res))
