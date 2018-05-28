import sys

data = sys.stdin.readlines()
sample_size = int(data[0].strip())
sorted_values = sorted(map(int,data[1].split()))

if sample_size % 2 == 0:
    l = sorted_values[:sample_size//2]
    u = sorted_values[sample_size//2:]
    q_2 = (sorted_values[sample_size//2 - 1] + sorted_values[sample_size//2]) //2
else:
    l = sorted_values[:sample_size//2]
    u = sorted_values[sample_size//2+1:]
    q_2 = sorted_values[sample_size//2]
l_length = len(l)
u_length = len(u)
if l_length % 2 == 0:
    q_1 = (l[l_length//2 - 1] + l[l_length//2]) // 2
    q_3 = (u[u_length//2 - 1] + u[u_length//2]) // 2
else:
    q_1 = l[l_length//2]
    q_3 = u[u_length//2]
print(q_1)
print(q_2)
print(q_3)
