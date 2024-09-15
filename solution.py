with open('input.txt',  'r' ) as f:
    size= f.readline().strip()
    first_arr = f.readline().strip().split(' ')
    second_arr = f.readline().strip().split(' ')

res = []
for i in range(int(size)):
    res.append(first_arr[i])
    res.append(second_arr[i])

with open('output.txt', 'w') as f:
    f.write(' '.join(res))
