temperatures = [22, 25, 18, 30, 28]

print(f"Eerste meting: {temperatures[0]}")
print(f"Derde meting: {temperatures[2]}")
print(f"Laatste meting: {temperatures[-1]}")

print(f"Aantal metingen: {len(temperatures)}")

temperatures.append(24)
temperatures.append(27)

print(f"Nieuw aantal metingen: {len(temperatures)}")

print(f"Index 1 tot 4: {temperatures[1:5]}")