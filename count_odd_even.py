num = []
even_count = 0
odd_count = 0
zero = 0
i = 1
while i<=5:
    user = int(input("enter no"))
    num.append(user)
    if user != 0:
        if user%2 == 0:
            even_sum = even_count+1
        else:
            odd_sum = odd_count+1
    else:
        zero = zero+1
    i+=1
print(num)
print(even_count)
print(odd_count)
print(zero)