# Project: File Handling in Python

## Overview
This project contains two Python programs that demonstrate reading from and writing to files using Python's built-in file handling methods.

### Files Included
1. **task1.py**: Reads and displays the content of `sample.txt`, handling file-not-found errors.
2. **task2.py**: Writes user input to `output.txt`, appends additional input, and displays the final content of the file.

---

## File Details

### 1. `task1.py` - Reading from a File
This program attempts to open and read a file named `sample.txt`. If the file exists, its content is printed line by line. If the file is not found, an error message is displayed.

**Example Output (if `sample.txt` exists):**
```
Line 1: Hello, World!
Line 2: Welcome to Python File Handling.
```
**Example Output (if `sample.txt` is missing):**
```
Error: The file 'sample.txt' was not found.
```

### 2. `task2.py` - Writing and Appending to a File
This program does the following:
- Takes user input and writes it to `output.txt`.
- Takes additional user input and appends it to `output.txt`.
- Reads and prints the final content of `output.txt`.

**Example Input/Output:**
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling.
```

---

## How to Run
Follow these steps to execute the programs:

1. **Prerequisites:**
    - Python 3.x installed on your system.
    - A text file named `sample.txt` should be present in the same directory as `task1.py` for reading.
2. **Run the Programs:**
    - Open a terminal or command prompt.
    - Navigate to the project directory.
    - Run the desired program using the following commands:
      
      For `task1.py`:
      ```bash
      python task1.py
      ```
      
      For `task2.py`:
      ```bash
      python task2.py
      ```

---

## Conclusion
This project demonstrates fundamental file-handling operations in Python, including reading from, writing to, and appending files while handling potential errors. It is an essential concept for working with data storage in Python applications.