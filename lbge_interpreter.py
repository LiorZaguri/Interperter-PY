from lbge_functions import *

# Functions that allowed to be used in the shell
Functions = {'ADD', 'SUB', 'MUL', 'DIVIDE', 'FLOOR_DIVIDE', 'POWER', 'SQUARE', 'FACTORIAL', 'ABS', 'MOD', 'SQRT',
             'MIN', 'MAX', 'ASSIGN', 'EQUAL', 'NOT_EQUAL', 'GREATER', 'GREATER_EQUAL', 'REMOVE', 'APPEND', 'GET',
             'SPLIT', 'REPLACE', 'LENGTH', 'CONTAINS', 'ISUPPER', 'ISLOWER', 'CONCAT', 'REVERSE', 'PRINT', 'INDEX'}

Operators = [
            {"+": "ADD"},
            {"-": "SUB"},
            {"**": "POWER"},
            {"/": "DIVIDE"},
            {"//": "FLOOR_DIVIDE"},
            {"*": "MUL"},
            {"%": "MOD"},
            {"<": "SMALLER"},
            {"<=": "SMALLER_EQUAL"},
            {">": "GREATER"},
            {">=": "GREATER_EQUAL"},
            {"==": "EQUAL"},
            {"!=": "NOT_EQUAL"},
            {"AND": "AND"},
            {"OR": "OR"},
            {"NOT": "NOT"}
]

"""
Apply the given operator to the operands.

Args:
    left (Any): The left operand. Can be None if the operator is unary (e.g., "NOT").
    right (Any): The right operand.
    op (str): The operator to apply, as a string.

Returns:
    Any: The result of the operation.

Raises:
    RuntimeError: If the operator is unknown.

Notes:
    - If the operator is "NOT" and the left operand is None, the function performs a unary NOT operation on the right operand.     - The function iterates through a list of operators (`Operators`) and evaluates the appropriate function using `eval`.
"""
def apply_operator(left, right, op):
    if left is None and op == "NOT":
        return NOT(right)
    for operator in Operators:
        if op in operator:
            return eval(operator[op])(left, right)

    raise RuntimeError(f"Unknown operator: {op}")

"""
A simple interpreter for executing abstract syntax trees (ASTs).

"""
class Interpreter:
    """
       Initializes the Interpreter with an abstract syntax tree (AST).

       Args:
           ast (list): The abstract syntax tree to be interpreted.
       """
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}
        self.functions = {}
        self.return_value = None

    """
         Interprets and executes all statements in the AST.
    """
    def interpret(self):
        for statement in self.ast:
            self.execute(statement)

    """
    Executes a single statement based on its type.

    Args:
        statement (dict): A dictionary representing a statement in the AST.

    Raises:
        RuntimeError: If the statement type is unknown.
    """
    def execute(self, statement):
        if statement['type'] == 'assignment':
            self.variables[statement['variable']] = self.evaluate(statement['value'])
        elif statement['type'] == 'if':
            if self.evaluate(statement['condition']):
                for stmt in statement['true']:
                    self.execute(stmt)
            elif statement['false']:
                for stmt in statement['false']:
                    self.execute(stmt)
        elif statement['type'] == 'while':
            while self.evaluate(statement['condition']):
                for stmt in statement['body']:
                    self.execute(stmt)
        elif statement['type'] == 'for':
            self.variables[statement['variable']] = self.evaluate(statement['value'])
            for self.variables[statement['variable']] in range(self.evaluate(statement['value']), self.evaluate(statement['range'])):
                for stmt in statement['body']:
                    self.execute(stmt)
                self.variables[statement['variable']] += 1
        elif statement['type'] == 'print':  # Handle the PRINT statement
            value = self.evaluate(statement['expression'])
            PRINT(value)
        elif statement['type'] == 'number':
            return statement['value']
        elif statement['type'] == 'function':
            self.functions[statement['name']] = statement
        elif statement['type'] == 'function_call':  # Handle function calls
            function_name = statement['name']
            args = [self.evaluate(arg) for arg in statement['args']]
            return self.call_function(function_name, args)
        elif statement['type'] == 'return':
            self.return_value = self.evaluate(statement['expression'])

    """
    Evaluates an expression and returns the result.

    Args:
        expr (Any): The expression to evaluate.

    Returns:
        Any: The result of the evaluation.
        
    Raises:
        RuntimeError: If the expression is missing an operator or is otherwise malformed.
    """
    def evaluate(self, expr):
        if isinstance(expr, dict):
            # Handle function calls
            if expr['type'] == 'function_call':
                function_name = expr['name']
                args = [self.evaluate(arg) for arg in expr['args']]
                return self.call_function(function_name, args)

            # Handle unary operations (e.g., 'not')
            if expr['type'] == 'NOT':
                operand = self.evaluate(expr['operand'])
                return not operand

            # Handle binary operations
            if 'op' in expr:
                left = self.evaluate(expr['left']) if 'left' in expr else None
                right = self.evaluate(expr['right']) if 'right' in expr else None

                if left is None:
                    return apply_operator(None, right, expr['op'])
                return apply_operator(left, right, expr['op'])
            elif expr['type'] == 'array':
                return [self.evaluate(element) for element in expr['elements']]
            elif expr['type'] == 'tuple':
                return tuple([self.evaluate(element) for element in expr['elements']])
            elif expr['type'] == 'function':
                self.functions[expr['name']] = expr
                return None
            else:
                raise RuntimeError(f"Expression missing operator: {expr}")
        elif expr.isdigit():
            return int(expr)
        elif expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]  # Strip quotes from string literals
        elif expr == "True":
            return True
        elif expr == "False":
            return False
        else:
            return self.variables.get(expr, expr)

    """
    Calls a function by its name with the provided arguments.

    Args:
        name (str): The name of the function to call.
        args (list): A list of arguments to pass to the function.

    Returns:
        Any: The result of the function call.

    Raises:
        RuntimeError: If the function is unknown.
    """
    def call_function(self, name, args):
        if name in self.functions:
            function = self.functions[name]
            parameters = function['parameters']
            body = function['body']

            old_variables = self.variables.copy()
            self.variables = {parameter: arg for parameter, arg in zip(parameters, args)}
            for statement in body:
                self.execute(statement)
                if self.return_value is not None:
                    break

            result = self.return_value
            self.return_value = None

            self.variables = old_variables
            return result
        else:
            if name in Functions:
                return eval(name)(*args)
            else:
                raise RuntimeError(f"Unknown function: {name}")
