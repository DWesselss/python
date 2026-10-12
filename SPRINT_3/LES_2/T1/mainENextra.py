days = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
steps = [8200, 11500, 9700, 12040, 6300, 15200, 10000]

total = 0
goal_days = 0
best_steps = 0
best_day = ""

for i in range(len(steps)):
    print(f"{days[i]}: {steps[i]} stappen")
    total += steps[i]

    if steps[i] >= 10000:
        goal_days += 1

    if steps[i] > best_steps:
        best_steps = steps[i]
        best_day = days[i]

average = total / len(steps)

print(f"Totaal: {total}")
print(f"Gemiddelde: {average:.1f}")
print(f"Doel gehaald: {goal_days} dagen")
print(f"Beste dag: {best_day} met {best_steps} stappen")