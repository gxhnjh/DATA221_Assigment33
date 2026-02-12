threshold = 50
product = 1
currentNumber = 1

while product <= threshold:
    product = product * currentNumber
    currentNumber = currentNumber + 1

print("Final product:", product)
print("Number that exceeded the threshold:", currentNumber - 1)