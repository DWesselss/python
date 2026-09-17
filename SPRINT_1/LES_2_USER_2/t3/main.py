drone_name = "Tello"
battery_percentage = int(input("Battery percentage: "))
cost_per_minute = float(input("Battery cost per minute: "))

flight_time = battery_percentage / cost_per_minute
total_seconds = int(flight_time * 60)

# Met // krijgen we hele minuten in plaats van een kommagetal.
minutes = total_seconds // 60
seconds = total_seconds % 60

print(
    f"{drone_name} | battery {battery_percentage}% | "
    f"usage {cost_per_minute:.1f}%/m | flight time {minutes}m {seconds}s"
)