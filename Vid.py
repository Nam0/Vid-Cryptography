import os
from moviepy.editor import ImageSequenceClip
import numpy as np
from PIL import Image

input_folder = 'frames'
output_video = 'output_video.avi'
frame_rate = 2 
new_width = 1280
new_height = 720

def resize_image(image):
    return image.resize((new_width, new_height), resample=Image.NEAREST)

image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]r
image_files.sort()
image_paths = [os.path.join(input_folder, image_file) for image_file in image_files]
images = [Image.open(image_path) for image_path in image_paths]
resized_images = [resize_image(image) for image in images]
resized_images_np = [np.array(image) for image in resized_images]
clip = ImageSequenceClip(resized_images_np, fps=frame_rate)
clip.write_videofile(output_video, codec='libx264', fps=frame_rate)
