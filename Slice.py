import cv2
import os

input_video = 'output_video.avi'
output_folder = 'extracted_frames'
os.makedirs(output_folder, exist_ok=True)
cap = cv2.VideoCapture(input_video)
frame_count = 0
desired_width = 640
desired_height = 360

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    resized_frame = cv2.resize(frame, (desired_width, desired_height))
    frame_filename = os.path.join(output_folder, f"frame{frame_count}.png")
    cv2.imwrite(frame_filename, resized_frame)
    frame_count += 1

cap.release()
print(f'Extracted and resized {frame_count} frames to {output_folder}.')