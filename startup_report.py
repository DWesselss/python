# startup_report.py — Sprint 1 Project

from djitellopy import Tello

# 1. Tello-object maken en verbinden
tello = Tello()
tello.connect()

try:
    # 2. Sensordata ophalen
    battery = tello.get_battery()
    height = tello.get_height()
    temperature = tello.get_temperature()

    # 3. Controleren of alle sensorwaarden gehele getallen zijn
    assert isinstance(battery, int), "Batterij moet een int zijn!"
    assert isinstance(height, int), "Hoogte moet een int zijn!"
    assert isinstance(temperature, int), "Temperatuur moet een int zijn!"

    # 4. Status bepalen: precies 20% is NO-GO
    if battery > 20:
        status = "GO ✅"
    else:
        status = "NO-GO ❌  (batterij te laag)"

    # 5. Het systeemrapport opbouwen
    line = "=" * 40

    report = (
        f"{line}\n"
        f"  TELLO SYSTEEMRAPPORT\n"
        f"{line}\n"
        f"  {'Batterij':<12}: {battery} %\n"
        f"  {'Hoogte':<12}: {height} cm\n"
        f"  {'Temperatuur':<12}: {temperature} °C\n"
        f"{line}\n"
        f"  {'STATUS':<12}: {status}\n"
        f"{line}"
    )

    # Het volledige rapport in de terminal tonen
    print(report)

    # Extra: het nieuwste rapport opslaan
    with open("startup_log.txt", "w", encoding="utf-8") as log_file:
        log_file.write(report)

finally:
    # 6. De verbinding altijd netjes afsluiten
    tello.end()