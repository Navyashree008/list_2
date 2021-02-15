a = [6,8,9,3,1,0,8]
i = 0
sum = a[0]
while i < len(a):
    if a[i] < sum:
        sum = a[i]
    i= i+1
print(sum)
