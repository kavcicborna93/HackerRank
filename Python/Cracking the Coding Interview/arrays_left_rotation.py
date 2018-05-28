#rotate left function
def rotLeft(a, d):
    length = len(a)
    rotated_arr = [0]*length
    for ind,el in enumerate(a):
        rotated_arr[ind] = a[(ind + d) % length]
    return rotated_arr
