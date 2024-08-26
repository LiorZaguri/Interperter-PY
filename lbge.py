from lbge_lexer import Tokenizer
from lbge_parser import Parser
from lbge_interpreter import Interpreter
from lbge_test_cases import test_cases
import sys

"""
Executes a series of predefined test cases to validate the functionality of the interpreter.


Each test case includes a description, the code to be executed, and the expected results.
The function compares the interpreter's output against the expected results and reports any discrepancies.

If all tests pass, the function prints a success message. 
If any test fails, the function reports the failure and stops further testing.

"""


def run_tests():
    print("Running tests...")
    print("Please notice that the 'result' is a dictionary with the variables and their values is not a real print of "
          "the code")

    print()
    count_tests = 0
    for test in test_cases:
        count_tests += 1
        print(f"Running test #{count_tests}: {test['description']}")
        # Tokenize
        result = execute_code(test['code'])

        # Print results
        print(f"Code:\n{test['code']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}\n")

        if result != test['expected']:
            print(f"Test number: {count_tests} failed.")
            return

    print(f"All {count_tests} tests passed!")


"""
Executes the code contained in the specified file using the interpreter.

Args:
    file_name (str): The name of the file containing the code to be executed.

This function is used to run and interpret scripts written in the language the interpreter supports.
"""


def run_file(file_name):
    with open(file_name, 'r') as file:
        code = file.read()

    execute_code(code)


def execute_code(code, interpreter=None):
    # Create a new interpreter if one is not provided
    if interpreter is None:
        interpreter = Interpreter([])

    # Tokenize
    tokenizer = Tokenizer(code)
    tokens = tokenizer.get_tokens()

    # Parse
    parser = Parser(tokens)
    ast = parser.parse()

    # Interpret
    interpreter.ast = ast
    interpreter.interpret()

    return interpreter.variables


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Entering LBGE shell. Type your code, or '/run & /RUN' to run file, or '/exit' to exit. "
              "(You can type '/run_tests' to run example tests)")
        interpreter = Interpreter([])
        while True:
            try:
                code = input(">>> ")
                if code == '/exit':
                    break
                elif code == '/run_tests':
                    run_tests()
                    continue
                elif code.startswith('/run ') or code.startswith('/RUN '):
                    filename = code.split(' ', 1)[1]
                    if filename == '':
                        run_file(input(">>> Enter file name: "))
                        continue
                    else:
                        run_file(filename)
                        continue
                elif code == '/run' or code == '/RUN':
                    run_file(input(">>> Enter file name: "))
                    continue

                code = code.strip()

                if not (code.startswith("PRINT(") or code.startswith("VAR") or code.startswith("FUN") or "=" in code):
                    code = "PRINT(" + code + ");"

                execute_code(code, interpreter)

            except Exception as e:
                print(f"Error: {e}")
    else:
        if sys.argv[1] == 'run_tests':
            run_tests()
        else:
            run_file(sys.argv[1])
