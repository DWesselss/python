temperatures = []

temperatures.append(22)
temperatures.append(25)
temperatures.append(18)
temperatures.append(30)
temperatures.append(28)

print(f"Origineel: {temperatures}")
print(f"Omgekeerd: {temperatures[::-1]}")

lowest = temperatures[0]
highest = temperatures[0]

for temperature in temperatures:
    if temperature < lowest:
        lowest = temperature

    if temperature > highest:
        highest = temperature

print(f"Laagste meting: {lowest}")
print(f"Hoogste meting: {highest}")