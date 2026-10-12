from djitellopy import Tello
import cv2
import time

tello = Tello()
tello.connect()
tello.streamon()

time.sleep(2)

frame_read = tello.get_frame_read()

brightness_values = []
contrast_values = []
red_values = []
green_values = []
blue_values = []
motion_values = []

previous_frame = None

for i in range(50):
    img = frame_read.frame

    if img is None:
        print(f"Frame {i + 1}: geen beeld")
        time.sleep(0.033)
        continue

    img_small = cv2.resize(img, (360, 240))

    brightness = img_small.mean()
    contrast = int(img_small.max()) - int(img_small.min())

    blue = img_small[:, :, 0].mean()
    green = img_small[:, :, 1].mean()
    red = img_small[:, :, 2].mean()

    brightness_values.append(brightness)
    contrast_values.append(contrast)
    red_values.append(red)
    green_values.append(green)
    blue_values.append(blue)

    print(f"Frame {i + 1}: helderheid {brightness:.1f}, contrast {contrast}")
    print(f"R: {red:.1f}, G: {green:.1f}, B: {blue:.1f}")

    if previous_frame is not None:
        diff = cv2.absdiff(previous_frame, img_small)
        motion = diff.mean()
        motion_values.append(motion)
        print(f"Bewegingsscore: {motion:.1f}")

    previous_frame = img_small.copy()

    time.sleep(0.033)

if brightness_values:
    print(f"Gemiddelde helderheid: {sum(brightness_values) / len(brightness_values):.1f}")
    print(f"Minimum contrast: {min(contrast_values)}")
    print(f"Maximum contrast: {max(contrast_values)}")
    print(f"Gemiddeld R: {sum(red_values) / len(red_values):.1f}")
    print(f"Gemiddeld G: {sum(green_values) / len(green_values):.1f}")
    print(f"Gemiddeld B: {sum(blue_values) / len(blue_values):.1f}")

if motion_values:
    print(f"Piek beweging: {max(motion_values):.1f}")
    print(f"Minimum beweging: {min(motion_values):.1f}")
    print(f"Gemiddelde beweging: {sum(motion_values) / len(motion_values):.1f}")

tello.streamoff()
tello.end()