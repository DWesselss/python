from djitellopy import Tello
import time

tello = Tello()
tello.connect()
tello.streamon()

time.sleep(2)

frame_read = tello.get_frame_read()

start = time.time()
frame_count = 0

for i in range(100):
    img = frame_read.frame

    if img is None:
        print(f"Frame {i + 1}: geen beeld")
        time.sleep(0.033)
        continue

    height, width = img.shape[:2]

    print(f"Frame {i + 1}: {height} x {width}, type: {img.dtype}, min/max: {img.min()}/{img.max()}")

    frame_count += 1
    time.sleep(0.033)

elapsed = time.time() - start
fps = frame_count / elapsed if elapsed > 0 else 0

print(f"Tijd: {elapsed:.2f} seconden")
print(f"Frames opgehaald: {frame_count}")
print(f"FPS: {fps:.1f}")

tello.streamoff()
tello.end()