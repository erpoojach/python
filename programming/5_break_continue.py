for n in range(2, 10):
 print('outer loop ', n)
 for x in range(2, n):
    print(n % x)
    if n % x == 0:
        print(n, 'equals', x, '*', n//x)
        break
 else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
...

print('----------------')
for num in range(2, 10):
 print('number', num)
 if num % 2 == 0:
    print("Found an even number", num)
    continue
print("Found an odd number", num)