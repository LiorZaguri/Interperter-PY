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
                VAR getFirstElement = GET(arr, 0);
                VAR contains = CONTAINS(arr, 1);
                VAR length = LENGTH(arr);
                VAR indexOfElement = INDEX(arr, 2);
                VAR addElement = ADD(arr, 4);
                VAR addArray = ADD(arr, arr2);
                VAR removeElement = REMOVE(arr, 2);
                PRINT(arr);
                """,
        "expected": {'arr': [1, 2, 4], 'arr2': [3, 4, 5], 'getFirstElement': 1, 'contains': True, 'length': 3,
                     'indexOfElement': 1, 'addElement': [1, 2, 4], 'addArray': [1, 2, 3, 4, 3, 4, 5],
                     'removeElement': 3
                     }
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
    },
    {
        "description": "Tuple creation and element access",
        "code": """
            VAR my_tuple = (1, 2, 3);
            VAR first_element = GET(my_tuple, 0);
            VAR second_element = GET(my_tuple, 1);
            VAR third_element = GET(my_tuple, 2);
        """,
        "expected": {'my_tuple': (1, 2, 3), 'first_element': 1, 'second_element': 2, 'third_element': 3}
    },
    {
        "description": "Tuple concatenation",
        "code": """
            VAR tuple1 = (1, 2, 3);
            VAR tuple2 = (4, 5, 6);
            VAR concatenated = tuple1 + tuple2;
        """,
        "expected": {'tuple1': (1, 2, 3), 'tuple2': (4, 5, 6), 'concatenated': (1, 2, 3, 4, 5, 6)}
    },
    {
        "description": "Tuple length",
        "code": """
            VAR my_tuple = (1, 2, 3);
            VAR length = LENGTH(my_tuple);
        """,
        "expected": {'my_tuple': (1, 2, 3), 'length': 3}
    }
]
