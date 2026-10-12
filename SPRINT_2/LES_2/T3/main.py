disk_free = 55
cpu_load  = 70

# TODO: gebruik chained comparison voor safe_to_backup
safe_to_backup = 20 <= disk_free < 100 and 0 <= cpu_load < 80

# TODO: gebruik ternary om de status te omschrijven
status = "veilig" if safe_to_backup else "onveilig"

# TODO: schrijf in één f-string: vrije ruimte %, cpu %, status
print(f"Vrije ruimte: {disk_free}%, CPU belasting: {cpu_load}%, Status: {status}")