import sys

data = sys.stdin.readlines()

values = list(map(int,data[1].strip().split()))
frequencies = list(map(int,data[2].split()))

dataset = []

for i in range(min(len(frequencies),len(values))):
    dataset.extend([values[i]]*frequencies[i])

sorted_dataset = sorted(dataset)

dataset_size = len(dataset)
if dataset_size% 2 == 0:
    l = sorted_dataset[:dataset_size//2]
    u = sorted_dataset[dataset_size//2:]
    q_2 = (sorted_dataset[dataset_size//2 - 1] + sorted_dataset[dataset_size//2]) /2
else:
    l = sorted_dataset[:dataset_size//2]
    u = sorted_dataset[dataset_size//2+1:]
    q_2 = sorted_dataset[dataset_size//2]
    
l_length = len(l)
u_length = len(u)

if l_length % 2 == 0:
    q_1 = round((l[l_length//2 - 1] + l[l_length//2]) / 2,1)
    q_3 = round((u[u_length//2 - 1] + u[u_length//2]) / 2,1)
else:
    q_1 = float(l[l_length//2])
    q_3 = float(u[u_length//2])

print(q_3 - q_1)
