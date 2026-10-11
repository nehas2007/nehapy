def copy_alternate_lines(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'w') as f2:
            for line_number, line in enumerate(f1, start=1):
                if line_number % 2 != 0:
                    f2.write(line)

        print("Alternate (odd-numbered) lines copied from",
              file1, "to", file2)

    except FileNotFoundError:
        print("Error: The file", file1, "does not exist")


copy_alternate_lines('file1.txt', 'file2.txt')
