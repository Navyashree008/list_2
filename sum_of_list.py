num = []
even_sum = 0
odd_sum = 0
i = 1
while i<=5:
    user = int(input("enter no"))
    num.append(user)
    if user%2 == 0:
        even_sum = even_sum+user
    else:
        odd_sum = odd_sum+user
        
    i+=1
print(num)
print(even_sum,odd_sum)