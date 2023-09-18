import os
from PIL import Image

def rgb_to_bits(r, g, b):
    bit1 = int(r > 100)  
    bit2 = int(g > 100)  
    return bit1, bit2


input_folder = 'extracted_frames'

try:
    output_file_name = input("Enter the output file name (including extension): ")
    output_file_path = os.path.join(input_folder, output_file_name)

    if not os.path.exists(input_folder):
        print("No extracted_frames folder found.")
    else:
        binary_data = []
        frame_counter = 0
        frame_filename = os.path.join(input_folder, f"frame{frame_counter}.png")

        while os.path.exists(frame_filename):
            image = Image.open(frame_filename)
            pixels = list(image.getdata())

            for pixel in pixels:
                r, g, b = pixel

                if r < 50 and g < 50 and b > 200:
                    continue

                bit1, bit2 = rgb_to_bits(r, g, 0)
                binary_data.append(f"{bit1}{bit2}")
                
            frame_counter += 1
            frame_filename = os.path.join(input_folder, f"frame{frame_counter}.png")

        binary_string = "".join(binary_data)

        with open(output_file_path, 'wb') as output_file:
            for i in range(0, len(binary_string), 8):
                byte = int(binary_string[i:i+8], 2)
                output_file.write(byte.to_bytes(1, byteorder='big'))

        print(f"Binary data saved to '{output_file_path}'.")

except Exception as e:
    print(f"An error occurred: {e}")
