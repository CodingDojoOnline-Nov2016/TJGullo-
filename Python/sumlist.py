a = [1,2,5,10,255,3]
numsum = sum(list(a))
print numsum

#for loop of same question
sum = 0
for num in a:
    sum += num

print sum

#print the avg of the list

avg = 0
sum = 0
for num in a:
    sum += num
avg = sum / len(a)
print avg
