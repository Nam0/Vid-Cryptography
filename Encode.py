import os
from PIL import Image, ImageDraw

def bits_to_rgb(bit1, bit2, bit3):
    r = bit1 * 255
    g = bit2 * 255
    b = 0
    return r, g, b

try:
    file_name = input("Enter the file name: ")
    binlist = []

    with open(file_name, 'rb') as file:
        binary_data = file.read()

        for byte in binary_data:
            binary_string = bin(byte)[2:].zfill(8)
            binlist.extend(binary_string)

        if not os.path.exists("frames"):
            os.makedirs("frames")

        resWidth, resHeight = 640, 360
        background_color = (0, 0, 255)
        image = Image.new('RGB', (resWidth, resHeight), background_color)
        draw = ImageDraw.Draw(image)

        x, y = 0, 0
        frame_counter = 0

        for i in range(0, len(binlist), 2):
            bit1 = int(binlist[i])
            bit2 = int(binlist[i + 1])
            pixel_color = bits_to_rgb(bit1, bit2, 0)
            draw.point((x, y), fill=pixel_color)
            x += 1

            if x == resWidth:
                x = 0
                y += 1

            if y == resHeight:
                frame_filename = os.path.join("frames", f"frame{frame_counter}.png")
                image.save(frame_filename, "PNG")
                frame_counter += 1
                image = Image.new('RGB', (resWidth, resHeight), background_color)
                draw = ImageDraw.Draw(image)
                x, y = 0, 0

        # Save any remaining pixels as the last frame
        if x > 0 or y > 0:
            frame_filename = os.path.join("frames", f"frame{frame_counter}.png")
            image.save(frame_filename, "PNG")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
