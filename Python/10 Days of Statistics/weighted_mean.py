import sys

data = sys.stdin.readlines()
sample_size = int(data[0].strip())
x_i = list(map(int,data[1].split()))
w_i = list(map(int,data[2].split()))

numerator = 0
denominator = sum(w_i)
for i in range(sample_size):
    numerator += (x_i[i]*w_i[i])

weighted_mean = round(numerator/denominator,1)
print(weighted_mean)
