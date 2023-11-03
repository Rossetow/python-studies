
number = 4

output = 0
for x in range(number):
    if x%3 == 0 or x%5 == 0:
        output = output + x
print(output)