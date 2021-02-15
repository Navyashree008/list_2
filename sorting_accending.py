num = [23 ,36,24,5,6,4,8,9]
i = 0
b = len(num)
while i < b:
    j = 0
    while j<len(num):
        if num[i]<num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
        j+=1
    i+=1
print( num)
