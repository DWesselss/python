measurements = [22, 25, 18, 30, 28]

total = 0
high_count = 0
normal_count = 0

for i, temp in enumerate(measurements):
    total += temp

    if temp > 25:
        high_count += 1

    if 18 <= temp <= 28:
        print(f"Meting #{i + 1}: {temp}°C")
        normal_count += 1

average = total / len(measurements)

print(f"Hoge metingen: {high_count}")
print(f"Gemiddelde: {average:.1f}°C")
print(f"Normale metingen: {normal_count}")