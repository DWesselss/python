from djitellopy import Tello

# Constanten
SIMULATION = True
MIN_DISTANCE = 20
MAX_DISTANCE = 500
MIN_BATTERY = 20
MAX_HEIGHT = 5
MAX_TEMP = 60
MIN_WIFI = 70
MAX_FLIGHT_TIME = 300
WARM_TEMP = 45
LOW_BATTERY = 35
ECO_LIMIT = 35
NORMAL_LIMIT = 70
ECO_DISTANCE = 100
NORMAL_DISTANCE = 300
FULL_DISTANCE = 500
CONFIRM_WORD = "yes"

# Testwaarden (alleen gebruikt in simulatiemodus)
TEST_BATTERY = 80
TEST_HEIGHT = 0
TEST_TEMP = 30
TEST_WIFI = 90
TEST_FLIGHT_TIME = 0

tello = None


def close_connection():
    if tello is not None:
        tello.end()


def read_sensor(method):
    try:
        return method()
    except Exception:
        return None


# Invoer en invoerguards
name = input("Naam piloot: ").strip()
if not name:
    print(f"Ongeldige naam: '{name}' (naam mag niet leeg zijn).")
    close_connection()
    exit()

distance_text = input("Afstand in cm: ").strip()
if not distance_text.isdigit():
    print(f"Ongeldige afstand: '{distance_text}' (geheel getal van {MIN_DISTANCE} t/m {MAX_DISTANCE} nodig).")
    close_connection()
    exit()

distance = int(distance_text)
if not MIN_DISTANCE <= distance <= MAX_DISTANCE:
    print(f"Afstand {distance} cm buiten bereik ({MIN_DISTANCE} t/m {MAX_DISTANCE} cm).")
    close_connection()
    exit()

confirmation = input("Bevestigen met yes: ").strip().lower()
if confirmation != CONFIRM_WORD:
    print(f"Bevestiging '{confirmation}' ongeldig (vereist: {CONFIRM_WORD}).")
    close_connection()
    exit()

# Metingen
if SIMULATION:
    battery = TEST_BATTERY
    height = TEST_HEIGHT
    temperature = TEST_TEMP
    wifi = TEST_WIFI
    flight_time = TEST_FLIGHT_TIME
else:
    tello = Tello()
    try:
        tello.connect()
    except Exception as error:
        print(f"Verbinding mislukt: {error} (drone moet verbonden zijn).")
        close_connection()
        exit()
    battery = read_sensor(tello.get_battery)
    height = read_sensor(tello.get_height)
    temperature = read_sensor(tello.get_temperature)
    wifi = read_sensor(tello.query_wifi_signal_noise_ratio)
    flight_time = read_sensor(tello.get_flight_time)
    try:
        wifi = int(wifi) if wifi is not None else None
    except (ValueError, TypeError):
        wifi = None

# Guards
if any(value is None for value in (battery, height, temperature, wifi, flight_time)):
    print(f"Meting mislukt: batterij={battery}, hoogte={height}, temperatuur={temperature}, wifi={wifi}, vliegtijd={flight_time} (geen waarde mag None zijn).")
    close_connection()
    exit()

if battery <= MIN_BATTERY:
    print(f"Batterij te laag: {battery}% (moet meer dan {MIN_BATTERY}% zijn).")
    close_connection()
    exit()

if height > MAX_HEIGHT:
    print(f"Drone niet op de grond: {height} cm (maximaal {MAX_HEIGHT} cm).")
    close_connection()
    exit()

if temperature >= MAX_TEMP:
    print(f"Temperatuur te hoog: {temperature}°C (moet onder {MAX_TEMP}°C zijn).")
    close_connection()
    exit()

if wifi < MIN_WIFI:
    print(f"Wifi te zwak: {wifi} (minimaal {MIN_WIFI}).")
    close_connection()
    exit()

if flight_time > MAX_FLIGHT_TIME:
    print(f"Vliegtijd te hoog: {flight_time} s (maximaal {MAX_FLIGHT_TIME} s).")
    close_connection()
    exit()

if temperature >= WARM_TEMP and battery <= LOW_BATTERY:
    print(f"Te warm en bijna leeg: {temperature}°C / {battery}% (grenzen: vanaf {WARM_TEMP}°C én hooguit {LOW_BATTERY}%).")
    close_connection()
    exit()

# Vliegmodus
if battery <= ECO_LIMIT:
    mode = "ECO"
    max_mode_distance = ECO_DISTANCE
elif battery <= NORMAL_LIMIT:
    mode = "NORMAL"
    max_mode_distance = NORMAL_DISTANCE
else:
    mode = "FULL"
    max_mode_distance = FULL_DISTANCE

if distance > max_mode_distance:
    print(f"Afstand te groot: {distance} cm (modus {mode}, maximaal {max_mode_distance} cm).")
    close_connection()
    exit()

# Checklist en happy path
print(f"\nPRE-FLIGHT CHECK - piloot: {name}")
print(f"{'✓' if battery > MIN_BATTERY else '✗'} Batterij: {battery}% (meer dan {MIN_BATTERY}%)")
print(f"{'✓' if height <= MAX_HEIGHT else '✗'} Hoogte: {height} cm (maximaal {MAX_HEIGHT} cm)")
print(f"{'✓' if temperature < MAX_TEMP else '✗'} Temperatuur: {temperature}°C (onder {MAX_TEMP}°C)")
print(f"{'✓' if wifi >= MIN_WIFI else '✗'} Wifi: {wifi} (minimaal {MIN_WIFI})")
print(f"{'✓' if flight_time <= MAX_FLIGHT_TIME else '✗'} Vliegtijd: {flight_time} s (maximaal {MAX_FLIGHT_TIME} s)")
print(f"{'✓' if not (temperature >= WARM_TEMP and battery <= LOW_BATTERY) else '✗'} Warm en bijna leeg")
print(f"{'✓' if distance <= max_mode_distance else '✗'} Afstand: {distance} cm (maximaal {max_mode_distance} cm)")
print(f"Vliegmodus: {mode} - maximaal {max_mode_distance} cm")
print(f"STATUS: GO - {distance} cm vooruit")

if SIMULATION:
    print("SIMULATIE: geen echte dronevlucht uitgevoerd.")
else:
    took_off = False
    try:
        tello.takeoff()
        took_off = True
        tello.move_forward(distance)
    finally:
        if took_off:
            tello.land()
        close_connection()

print("Vlucht voltooid!")
