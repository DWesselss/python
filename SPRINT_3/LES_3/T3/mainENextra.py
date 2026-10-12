from djitellopy import Tello
import cv2
import time
import os

output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

tello = Tello()
tello.connect()
tello.streamon()

time.sleep(2)

frame_read = tello.get_frame_read()

saved_files = []
saved_times = []
start = time.time()

while len(saved_files) < 10:
    img = frame_read.frame

    if img is None:
        print("Geen frame ontvangen")
        time.sleep(0.033)
        continue

    img_small = cv2.resize(img, (360, 240))

    frame_count = len(saved_files) + 1
    filename = f"frame_{frame_count:03d}.jpg"
    filepath = os.path.join(output_dir, filename)

    success = cv2.imwrite(
        filepath,
        img_small,
        [cv2.IMWRITE_JPEG_QUALITY, 90]
    )

    if success:
        saved_files.append(filename)
        saved_times.append(time.time() - start)
        print(f"Saved: {filename} (360 x 240)")
    else:
        print(f"Fout bij opslaan: {filename}")

    time.sleep(0.033)

tello.streamoff()
tello.end()

print(f"Totaal opgeslagen: {len(saved_files)}")

if saved_files:
    print(f"Eerste bestand: {saved_files[0]}")
    print(f"Laatste bestand: {saved_files[-1]}")

print("Vluchtoverzicht:")

for i, filename in enumerate(saved_files):
    print(f"{filename}: {saved_times[i]:.2f} seconden")

print("Laatste drie frames:")

for i, filename in enumerate(saved_files[-3:]):
    print(f"{filename}")