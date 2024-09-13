def write_and_read_file(filename):
    try:
        with open(filename, "a+") as file:
            lines = []
            for i in range(1, 4):
                line = input(f"Please enter the first lines {i}: ")
                lines.append(line)
            file.writelines(line + "\n" for line in lines)

            # Read the existing lines and print them
            file.seek(0)
            existing_lines = file.readlines()
            for line in existing_lines:
                print(line.strip())

            # Append three additional lines
            for i in range(1, 4):
                line = input(f"Now please enter the additional lines {i}: ")
                file.write(line + "\n")

            # Read all lines, including the new ones
            file.seek(0)
            lines = file.readlines()

        for line in lines:
            print(line.strip())

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied to access '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operation completed.")

if __name__ == "__main__":
    filename = "my_file.txt"
    write_and_read_file(filename)