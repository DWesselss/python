# fifty: ValueError, omdat dit niet naar een int kan worden omgezet.
# 6,5: ValueError, omdat Python een punt gebruikt voor decimalen.
# Alleen Enter: ValueError, omdat een lege string geen int is.
# -20: geen fout; Python accepteert negatieve gehele getallen.

battery_percentage = int(input("Battery percentage: "))
cost_per_minute = float(input("Battery cost per minute: "))

flight_time = battery_percentage / cost_per_minute

print("Flight time:", flight_time, "minutes")

# -20 is het gevaarlijkst omdat het programma niet crasht en met een
# onmogelijk accupercentage verder rekent.