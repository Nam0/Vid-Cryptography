def file_to_binary(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as input_file:
            binary_data = input_file.read()
        
        with open(output_filename, 'w') as output_file:
            for byte in binary_data:
                binary_string = bin(byte)[2:].zfill(8)
                output_file.write(binary_string + '\n')
        
        print(f"Binary data from '{input_filename}' saved to '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_filename = input("Enter the name of the file to read: ")
    output_filename = f"bindata_{input_filename}.txt"

    file_to_binary(input_filename, output_filename)

if __name__ == "__main__":
    main()
