import itertools

cnt = 0
s = 'ИВАН'
for i in itertools.product(s, repeat=5):
    if 'И' in i:
        cnt += 1

print(cnt)
