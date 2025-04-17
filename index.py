def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.readlines()

        modified_content = [line.upper() for line in content]

        with open(output_filename, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read/write file '{input_filename}'.")

def main():
    input_filename = input("Enter the filename to read: ")
    output_filename = "modified_" + input_filename

    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
