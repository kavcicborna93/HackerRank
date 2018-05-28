import sys

data = sys.stdin.readlines()
sample_size = int(data[0].strip())
listOfValuesSorted = sorted(list(map(int,data[1].split())))
arithmeticMean = round(sum(listOfValuesSorted)/sample_size,1)

if sample_size % 2 == 0:
    median = round((listOfValuesSorted[sample_size//2 - 1] +  listOfValuesSorted[sample_size//2])/2,1)       
else:
    median = listOfValuesSorted[sample_size//2]

mode = listOfValuesSorted[0]
current = listOfValuesSorted[0]
counter_max = 1
counter_temp = 1

for value in listOfValuesSorted[1:]:
    if value == mode:
        counter_max += 1
    if value == current:
        counter_temp += 1
    else:
        current = value
        counter_temp = 1
    if counter_temp > counter_max:
        mode = current
        counter_max = counter_temp


print(arithmeticMean)
print(median)
print(mode)


