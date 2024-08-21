# Custom Python Interpreter

## Project Overview

This project was developed as a final project for the "Principles of Programming Languages" course during my Bachelor of Science (B.Sc) studies. It serves as a demonstration of various concepts and techniques learned throughout the course.

The interpreter can handle a wide range of mathematical, logical, string, and list operations. It supports the execution of predefined functions and allows users to manipulate data types such as numbers, strings, lists, tuples, and sets

## Table of Contents

*   [Installation](#installation)
*   [Usage](#usage)
    *   [Running the Interpreter](#running-the-interpreter)
    *   [Functionality Overview](#functionality-overview)
        *   [Mathematical Operations](#mathematical-operations)
        *   [Logical Operations](#logical-operations)
        *   [String Operations](#string-operations)
        *   [List Operations](#list-operations)
    *   [Test Cases](#test-cases)

## Installation

1.  Clone this repository:
    
    ```bash
    git clone https://github.com/LiorZaguri/Interperter-PY.git
    ```
    
2.  Navigate to the project directory:
    
    ```bash
    cd Interperter-PY
    ```
    
3.  Ensure you have Python 3 installed.

### Usage

Provide instructions on how to use the interpreter, including example commands and expected outputs:


To use the interpreter, run the `LBGE.py` script and input your commands. Here are a few examples:

*   **Addition**: `ADD(5,3)` -> Output: `8`
*   **Concatenation**: `CONCAT("Hello","World")` -> Output: `"HelloWorld"`
*   **Direct Commands**: 
      - `2 + 3` -> Output: `5`
      - `PRINT("Hello")` -> Output: `Hello`

For a full list of supported commands and their syntax, refer to the [Functionality Overview](#functionality-overview) section.

### Running the Interpreter

#### 1. Run the Predefined Tests:
To run the interpreter and execute predefined test cases, follow these steps:

You can execute the predefined test cases by running the LBGE.py script:
```bash
python lbge.py run_tests
```

This script will run a series of predefined test cases to validate the functionality of the interpreter. Each test case includes a description, the code to be executed, and the expected results. The function compares the interpreter's output against the expected results and reports any discrepancies.

#### 2. Run a Script File:
To execute your script using the LBGE interpreter, follow these steps:

You can execute the predefined test cases by running the LBGE.py script:
```bash
python lbge.py your_script_file.LBGE
```

Replace your_script_file.LBGE with the path to your LBGE script file.

### 3. Interactive Shell:

Interactive Shell:

If you run the script without arguments, it will start an interactive shell. In this shell, you can:
```bash
python lbge.py
```

Type your code directly.
*   **Use (`/run`) or (`/RUN`)** followed by a file name to execute a script file.
*   **Use (`/run_tests`)** to run the predefined test cases.
*   **Use (`/exit`)** to exit the interactive shell.

Example usage in the interactive shell:

    >>> 2 + 3
    5
    >>> PRINT("Hello")
    Hello
    >>> /run_tests
    >>> /run your_script_file.LBGE
    >>> /exit

### Running the Tests
The run_tests function executes a series of predefined test cases and compares the results of the interpreter against expected values. If all tests pass, a success message will be displayed; otherwise, the function will report any failures.

### Example Test Cases

Here are some of the test cases included:

* **Simple Function Call**:

    Tests basic function calls, including addition and subtraction.


* **Array Operations**:

    Tests various array operations such as appending, removing, and checking contents.


* **String Manipulations**:

    Tests basic string operations like concatenation, replacement, and splitting.


* **Control Structures**:

    Tests if-else statements, while loops, and for loops.


* **Mathematical Operations**:

    Tests various mathematical operations including addition, subtraction, multiplication, division, and more.

Feel free to add more test cases or scripts to test different functionalities of the interpreter.

### Functionality Overview

#### Mathematical Operations

The interpreter supports various mathematical operations:

*   **Addition (`ADD`)**: Adds two numbers, concatenates two strings, or merges two lists or sets.
*   **Subtraction (`SUB`)**: Subtracts two numbers or removes elements of one list from another.
*   **Multiplication (`MUL`)**: Multiplies two numbers, or repeats a string or list.
*   **Division (`DIVIDE`)**: Divides one number by another.
*   **Floor Division (`FLOOR_DIVIDE`)**: Returns the floor division of two numbers.
*   **Power (`POWER`)**: Raises a number to the power of another.
*   **Square (`SQUARE`)**: Returns the square of an integer.
*   **Factorial (`FACTORIAL`)**: Returns the factorial of an integer.
*   **Absolute Value (`ABS`)**: Returns the absolute value of a number.
*   **Modulo (`MOD`)**: Returns the remainder of the division of two integers.
*   **Square Root (`SQRT`)**: Returns the square root of a number.

#### Logical Operations

The interpreter provides basic logical operations:

*   **Equal (`EQUAL`)**: Checks if two elements are equal.
*   **Not Equal (`NOT_EQUAL`)**: Checks if two elements are not equal.
*   **Greater Than (`GREATER`)**: Checks if one element is greater than another.
*   **Greater Than or Equal (`GREATER_EQUAL`)**: Checks if one element is greater than or equal to another.
*   **Smaller Than (`SMALLER`)**: Checks if one element is smaller than another.
*   **Smaller Than or Equal (`SMALLER_EQUAL`)**: Checks if one element is smaller than or equal to another.
*   **Logical OR (`OR`)**: Performs a logical OR operation on two boolean values.
*   **Logical AND (`AND`)**: Performs a logical AND operation on two boolean values.
*   **Logical NOT (`NOT`)**: Performs a logical NOT operation on a boolean value.

#### String Operations

The interpreter supports a variety of string manipulations:

*   **Concatenation (`CONCAT`)**: Concatenates two strings.
*   **Splitting (`SPLIT`)**: Splits a string into a list of substrings.
*   **Replacing (`REPLACE`)**: Replaces a substring within a string.
*   **Reversing (`REVERSE`)**: Reverses a string.
*   **Uppercase Check (`ISUPPER`)**: Checks if all characters in a string are uppercase.
*   **Lowercase Check (`ISLOWER`)**: Checks if all characters in a string are lowercase.

#### List Operations

The interpreter allows various operations on lists:

*   **Appending (`APPEND`)**: Appends an element to a list.
*   **Removing (`REMOVE`)**: Removes an element from a list by its index.
*   **Length (`LENGTH`)**: Returns the length of a list or string.
*   **Contains (`CONTAINS`)**: Checks if an element is in a list, string, or set.
*   **Index (`INDEX`)**: Returns the index of an element in a list, string, or set.


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
