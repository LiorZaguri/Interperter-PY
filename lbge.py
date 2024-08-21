from lbge_lexer import Tokenizer
from lbge_parser import Parser
from lbge_interpreter import Interpreter
import sys

"""
Executes a series of predefined test cases to validate the functionality of the interpreter.


Each test case includes a description, the code to be executed, and the expected results.
The function compares the interpreter's output against the expected results and reports any discrepancies.

If all tests pass, the function prints a success message. 
If any test fails, the function reports the failure and stops further testing.

"""


def run_tests():
    test_cases = [{
        "description": "Simple Function Call",
        "code": """
                    FUN add(x, y) {
                        VAR z = x + y;
                        RETURN z;
                    }
                    FUN sub(x, y) {
                        VAR z = x - y;
                        RETURN z;
                    }
                    VAR result = add(2, 3);
                    VAR result2 = sub(5, 3);
                    """,
        "expected": {"result": 5, "result2": 2}
    },
        {
            "description": "Simple array assignment",
            "code": """
                    VAR arr = [1, 2, 3];
                    VAR arr2 = [3, 4, 5];
                    VAR contains = CONTAINS(arr, 1);
                    VAR length = LENGTH(arr);
                    VAR indexOfElement = INDEX(arr, 2);
                    VAR addElement = ADD(arr, 4);
                    VAR addArray = ADD(arr, arr2);
                    VAR removeElement = REMOVE(arr, 2);
                    PRINT(arr);
                    """,
            "expected": {'arr': [1, 2, 4], 'arr2': [3, 4, 5], 'contains': True, 'length': 3, 'indexOfElement': 1,
                         'addElement': [1, 2, 4], 'addArray': [1, 2, 3, 4, 3, 4, 5], 'removeElement': 3}
        },
        {
            "description": "Basic strings manipulation",
            "code": """
                    VAR text = "Hello, World";
                    VAR split = SPLIT(text);
                    VAR replaced = REPLACE(text, "World", "universe");
                    VAR length = LENGTH(text);
                    VAR contains = CONTAINS(text, "World");
                    VAR contains2 = CONTAINS(text, "Universe");
                    """,
            "expected": {'text': 'Hello, World',
                         'split': ['Hello,', 'World'],
                         'replaced': 'Hello, universe',
                         'length': 12,
                         'contains': True,
                         'contains2': False}
        },
        {
            "description": "Basic strings manipulation 2",
            "code": """
                    VAR text = "hello, World";
                    VAR replaced = REPLACE(text, "World", "universe");
                    VAR index = INDEX(text, "W");
                    VAR concat = CONCAT(text, "!");
                    VAR isupper = ISUPPER(text);
                    VAR islower = ISLOWER(replaced);
                    VAR reversed = REVERSE(text);
                    PRINT("\nThis should be printed after " + "'Running test: Basic strings manipulation 2'");
                    PRINT("'text' variable is: " + text);
                    PRINT("'replaced' variable is: " + replaced + "\n");
                    """,
            "expected": {'text': 'hello, World',
                         'replaced': 'hello, universe',
                         'index': 7,
                         'concat': 'hello, World!',
                         'isupper': False,
                         'islower': True,
                         'reversed': 'dlroW ,olleh'}
        },
        {
            "description": "Basic assignment and if-else",
            "code": """
                VAR x = 5;
                IF x < 10 {
                    x = x + 1;
                } ELSE {
                    x = x - 1;
                }
                WHILE x < 20 {
                    x = x * 2;
                }
                """,
            "expected": {'x': 24}
        },
        {
            "description": "Nested if-else",
            "code": """
                VAR x = 5;
                IF x < 10 {
                    IF x < 5 {
                        x = x - 1;
                    } ELSE {
                        x = x + 1;
                    }
                } ELSE {
                    x = x * 2;
                }
                """,
            "expected": {'x': 6}
        },
        {
            "description": "Simple while loop",
            "code": """
                VAR x = 1;
                WHILE x < 10 {
                    x = x * 2;
                }
                """,
            "expected": {'x': 16}
        },
        {
            "description": "Simple for loop",
            "code": """
                VAR x = 2;
                FOR i (0,7) {
                    x = x * 2;
                }
                """,
            "expected": {'x': 256, 'i': 7}},
        {
            "description": "Expression with multiple operators",
            "code": """
                VAR x = 2;
                x = x + 3 * 4 - 5;
                """,
            "expected": {'x': 9}
        },
        {
            "description": "Handling of division",
            "code": """
                VAR x = 10;
                x = x / 2;
                """,
            "expected": {'x': 5.0}
        },
        {
            "description": "Condition false branch",
            "code": """
                VAR x = 10;
                IF x < 5 {
                    x = x - 1;
                } ELSE {
                    x = x + 1;
                }
                """,
            "expected": {'x': 11}
        },
        {
            "description": "Variable reassignment",
            "code": """
                VAR x = 10;
                x = 20;
                x = x + 5;
                """,
            "expected": {'x': 25}
        },
        {
            "description": "Modulo operation",
            "code": """
                VAR x = 10;
                x = x % 3;
                """,
            "expected": {'x': 1}
        },
        {
            "description": "Exponentiation operation",
            "code": """
                VAR x = 2;
                x = x ** 3;
                """,
            "expected": {'x': 8}
        },
        {
            "description": "Floor division operation",
            "code": """
                VAR x = 7;
                x = x // 2;
                """,
            "expected": {'x': 3}
        },
        {
            "description": "Logical AND operation",
            "code": """
                VAR x = 5;
                IF x > 3 AND x < 10 {
                    x = x + 2;
                }
                """,
            "expected": {'x': 7}
        },
        {
            "description": "Logical OR operation",
            "code": """
                VAR x = 5;
                IF x < 3 OR x < 10 {
                    x = x * 2;
                }
                """,
            "expected": {'x': 10}
        },
        {
            "description": "Logical NOT operation",
            "code": """
                VAR x = 5;
                IF NOT x > 10 {
                    x = x + 1;
                }
                """,
            "expected": {'x': 6}
        },
        {
            "description": "Complex expression with multiple operators",
            "code": """
                VAR x = 10;
                x = (x + 2) * 3 - 4 / 2;
                """,
            "expected": {'x': 34.0}
        }
    ]

    print("Running tests...")
    print("Please notice that the 'result' is a dictionary with the variables and their values is not a real print of "
          "the code")

    print()
    count_tests = 0
    for test in test_cases:
        count_tests += 1
        print(f"Running test #{count_tests}: {test['description']}")
        # Tokenize
        tokenizer = Tokenizer(test['code'])
        tokens = tokenizer.get_tokens()

        # Parse
        parser = Parser(tokens)
        ast = parser.parse()

        # Interpret
        interpreter = Interpreter(ast)
        interpreter.interpret()
        result = interpreter.variables

        # Print results
        print(f"Code:\n{test['code']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        print()

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

    # Tokenize
    tokenizer = Tokenizer(code)
    tokens = tokenizer.get_tokens()

    # Parse
    parser = Parser(tokens)
    ast = parser.parse()

    # Interpret
    interpreter = Interpreter(ast)
    interpreter.interpret()


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

                if not (code.startswith("PRINT(") or code.startswith("VAR") or code.startswith("FUN") or code.__contains__("=")):
                    code = "PRINT(" + code + ");"

                # Tokenize
                tokenizer = Tokenizer(code)
                tokens = tokenizer.get_tokens()

                # Parse
                parser = Parser(tokens)
                ast = parser.parse()

                # Interpret
                interpreter.ast = ast
                interpreter.interpret()


            except Exception as e:
                print(f"Error: {e}")
    else:
        if sys.argv[1] == 'run_tests':
            run_tests()
        else:
            run_file(sys.argv[1])
