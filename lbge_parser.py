class Parser:
    """
    Initializes the Parser object.

    Parameters:
        tokens (list): A list of tokens to be parsed.

    Attributes:
        self.tokens (list): Stores the list of tokens to be processed by the parser.
        self.current (int): Tracks the current position in the token list, initialized to 0.
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    """
    Starts parsing the tokens and returns a list of statements.

    Returns:
        list: A list of parsed statements.
    """
    def parse(self):
        return self.parse_statements()

    """
    Parses statements from the tokens until a block end or end of file is reached.

    Returns:
        list: A list of parsed statements.
    """
    def parse_statements(self):
        statements = []
        while self.current < len(self.tokens):
            # Skip any NEWLINE tokens
            while self.current < len(self.tokens) and self.tokens[self.current][0] == 'NEWLINE':
                self.current += 1

            if self.current >= len(self.tokens) or self.tokens[self.current][0] == 'EOF':
                break

            statement = self.parse_statement()
            if statement is None:
                break
            statements.append(statement)

            # Handle end of block or end of file
            if self.current < len(self.tokens) and self.tokens[self.current][0] in {'CLOSE_CURLY_BRACKET', 'EOF'}:
                break
        return statements

    def parse_statement(self):
        while self.current < len(self.tokens) and self.tokens[self.current][0] == 'NEWLINE':
            self.current += 1

        if self.current >= len(self.tokens) or self.tokens[self.current][0] == 'EOF':
            return None

        token_type, token_value = self.tokens[self.current]

        if token_type == 'CLOSE_CURLY_BRACKET':
            return None  # End of the current block, return to the previous context
        elif token_type == 'FUN':
            return self.parse_function()
        elif token_value == 'RETURN':
            return self.parse_return_statement()
        elif token_type == 'ID':
            if token_value == 'VAR':
                return self.parse_variable_declaration()
            elif token_value == 'IF':
                return self.parse_if_statement()
            elif token_value == 'WHILE':
                return self.parse_while_statement()
            elif token_value == 'PRINT':  # Recognize the PRINT statement
                return self.parse_print_statement()
            elif token_value == 'FOR':
                return self.parse_for_statement()
            else:
                # Attempt to parse an assignment if the initial token is an ID
                return self.parse_assignment_statement()
        else:
            raise RuntimeError(f'Unexpected token: {self.tokens[self.current][1]}')

    """
    Parses a variable declaration statement.

    Returns:
        dict: A dictionary representing the variable declaration, including the variable name and assigned value.
    """
    def parse_variable_declaration(self):
        self.consume('ID')  # Consume 'var'
        variable = self.consume('ID')  # Variable name
        self.consume('ASSIGN')  # Consume '='

        # Check if the next token is a function/method call
        value = self.parse_expression  # Parse the value (expression or method call)

        self.consume('END')  # Consume ';'
        return {'type': 'assignment', 'variable': variable, 'value': value}

    """
    Parses an if statement, including its condition and branches.

    Returns: 
        dict: A dictionary representing the if statement, including the condition, true branch, and false branch 
              (if present).
    """
    def parse_if_statement(self):
        self.consume('ID')  # Consume 'if'

        # Parse the condition expression
        condition = self.parse_if_expression()
        # Expect an opening brace for the true branch
        if self.tokens[self.current][0] != 'LBRACE' and self.tokens[self.current][0] != 'OPEN_CURLY_BRACKET':
            if self.tokens[self.current][0] == 'ASSIGN':
                raise RuntimeError(f"you can't assign inside a if condition '{self.tokens[self.current - 1][1]} "
                                   f"{self.tokens[self.current][1]} {self.tokens[self.current + 1][1]}'")
            else:
                raise RuntimeError(f"Expected LBRACE but got {self.tokens[self.current]}")

        self.consume('OPEN_CURLY_BRACKET')  # Consume '{' for the start of the true branch
        true_branch = self.parse_statements()  # Parse the true branch statements
        self.consume('CLOSE_CURLY_BRACKET')  # Consume '}' for the end of the true branch

        false_branch = None
        while self.tokens[self.current][0] == 'NEWLINE':
            self.consume('NEWLINE')

        if (self.current < len(self.tokens)
                and self.tokens[self.current][0] == 'ID'
                and self.tokens[self.current][1] == 'ELSE'):
            self.consume('ID')  # Consume 'else'
            self.consume('OPEN_CURLY_BRACKET')  # Consume '{' for the start of the false branch
            false_branch = self.parse_statements()  # Parse the false branch statements
            self.consume('CLOSE_CURLY_BRACKET')  # Consume '}' for the end of the false branch

        return {'type': 'if', 'condition': condition, 'true': true_branch, 'false': false_branch}

    """
    Parses the condition expression for an if statement.

    Returns:
        dict: A dictionary representing the condition expression.
    """
    def parse_if_expression(self):
        if self.tokens[self.current][0] == 'ID' and self.tokens[self.current][1] == 'NOT':
            self.consume('ID')
            return {'type': 'expression', 'op': 'NOT', 'right': self.parse_comparison()}

        left = self.parse_comparison()
        while self.current < len(self.tokens) and self.tokens[self.current][0] in {'LOGIC'}:
            op = self.consume(self.tokens[self.current][0])
            right = self.parse_comparison()
            left = {'type': 'expression', 'left': left, 'op': op, 'right': right}

        return left

    """
    Parses a while loop statement, including its condition and body.

    Returns:
        dict: A dictionary representing the while loop statement, including the condition and loop body.
    """
    def parse_while_statement(self):
        self.consume('ID')  # Consume 'while'
        condition = self.parse_expression  # Condition
        self.consume('OPEN_CURLY_BRACKET')  # Consume '{'
        body = self.parse_statements()  # Loop body
        self.consume('CLOSE_CURLY_BRACKET')  # Consume '}'
        return {'type': 'while', 'condition': condition, 'body': body}

    """
    Parses a for loop statement, including its variable, range, and body.

    Returns:
        dict: A dictionary representing the for loop statement, 
              including the loop variable, 
              initial value, 
              range, 
              and loop body.
    """
    def parse_for_statement(self):
        self.consume('ID')  # Consume 'for'
        variable = self.consume('ID')  # var name example x, i, y
        self.consume('LPAREN')  # Consume '('
        value = self.consume('NUMBER')  # Consume value of variable of for
        self.consume('COMMA')  # Consume ','
        top_number = self.consume('NUMBER')  # Consume value of the top range
        self.consume('RPAREN')  # Consume ')'
        self.consume('OPEN_CURLY_BRACKET')  # Consume '{'
        body = self.parse_statements()  # Loop body
        self.consume('CLOSE_CURLY_BRACKET')  # Consume '}'
        return {'type': 'for', 'variable': variable, 'value': value, 'range': top_number, 'body': body}

    """
    Placeholder for parsing range expressions (currently not implemented).

    Returns:
        None
    """
    def parse_range(self):
        pass

    """
    Parses an assignment statement, including the variable being assigned and its value.

    Returns:
        dict: A dictionary representing the assignment statement, including the variable and assigned value.
    """
    def parse_assignment_statement(self):
        variable = self.consume('ID')  # Variable name
        if self.tokens[self.current][0] == 'ASSIGN':
            self.consume('ASSIGN')  # Consume '='
            value = self.parse_expression
        elif self.tokens[self.current][0] == 'LPAREN':
            self.current = self.current - 1
            value = self.parse_expression  # Value could be a method call or a complex expression
        else:
            value = self.parse_expression
        self.consume('END')  # Consume ';'
        return {'type': 'assignment', 'variable': variable, 'value': value}

    """
    Parses an expression, handling terms, operators, and function calls.

    Returns:
        dict: A dictionary representing the parsed expression.
    """
    @property
    def parse_expression(self):
        left = self.parse_term()
        while self.current < len(self.tokens) and self.tokens[self.current][0] in {'OP', 'COMPARE', 'LOGIC', 'ID'}:
            if self.tokens[self.current][0] == 'ID':
                method_name = self.consume('ID')
                self.consume('LPAREN')
                args = []
                while self.current < len(self.tokens) and self.tokens[self.current][0] != 'RPAREN':
                    args.append(self.parse_expression)
                    if self.tokens[self.current][0] == 'COMMA':
                        self.consume('COMMA')
                self.consume('RPAREN')
                left = {'type': 'method_call', 'method': method_name, 'object': left, 'args': args}
            else:
                op = self.consume(self.tokens[self.current][0])
                right = self.parse_term()
                left = {'type': 'expression', 'left': left, 'op': op, 'right': right}

        return left

    """
    Parses a term within an expression, handling factors and operators.

    Returns:
        dict: A dictionary representing the parsed term.
    """
    def parse_term(self):
        left = self.parse_factor()

        while self.current < len(self.tokens):
            token_type, token_value = self.tokens[self.current]

            if token_type == 'OP' and token_value in {'*', '/'}:
                op = self.consume('OP')
                right = self.parse_factor()
                left = {'type': 'expression', 'left': left, 'op': op, 'right': right}
            elif token_type == 'LPAREN':
                self.consume('LPAREN')
                args = []
                while self.current < len(self.tokens) and self.tokens[self.current][0] != 'RPAREN':
                    args.append(self.parse_expression)
                    if self.tokens[self.current][0] == 'COMMA':
                        self.consume('COMMA')
                self.consume('RPAREN')
                left = {'type': 'method_call', 'method': left, 'args': args}
            else:
                break

        return left

    """
    Parses a factor within a term, handling numbers, strings, identifiers, and parenthesized expressions.

    Returns:
        dict: A dictionary representing the parsed factor.
    """
    def parse_factor(self):
        if self.current < len(self.tokens):
            token_type, token_value = self.tokens[self.current]
            if token_type == 'NUMBER':
                return self.consume('NUMBER')
            elif token_type == 'STRING':
                return self.consume('STRING')
            elif token_type == 'ID':
                if self.tokens[self.current + 1][0] == 'LPAREN':  # Lookahead to check for function call
                    function_name = self.consume('ID')
                    self.consume('LPAREN')
                    args = []
                    while self.tokens[self.current][0] != 'RPAREN':
                        args.append(self.parse_expression)
                        if self.tokens[self.current][0] == 'COMMA':
                            self.consume('COMMA')
                    self.consume('RPAREN')
                    return {'type': 'function_call', 'name': function_name, 'args': args}
                else:
                    return self.consume('ID')
            elif token_type == 'LPAREN':
                self.consume('LPAREN')
                expr = self.parse_expression
                self.consume('RPAREN')
                return expr
            elif token_type == 'LBRACE':
                return self.parse_array()
            elif token_type == 'FUN':
                return self.parse_function()
            elif token_type == 'LOGIC' and token_value == 'NOT':
                self.consume('LOGIC')
                return {'type': 'expression', 'op': 'NOT', 'right': self.parse_comparison()}
            else:
                raise RuntimeError(
                    f'Expected ID, NUMBER, STRING, LPAREN, LBRACE or LOGIC but got {self.tokens[self.current]}')

    """
    Parses a print statement, including the expression to be printed.

    Returns:
        dict: A dictionary representing the print statement, including the expression to be printed.
    """
    def parse_print_statement(self):
        self.consume('ID')  # Consume 'PRINT'
        self.consume('LPAREN')  # Consume '('
        expression = self.parse_expression
        self.consume('RPAREN')  # Consume ')'
        self.consume('END')  # Consume ';'
        return {'type': 'print', 'expression': expression}

    """
    Parses an array literal, including its elements.

    Returns:
        dict: A dictionary representing the array literal, including its elements.
    """
    def parse_array(self):
        self.consume('LBRACE')  # Consume '['
        elements = []
        while self.current < len(self.tokens) and self.tokens[self.current][0] != 'RBRACE':
            elements.append(self.parse_expression)
            if self.tokens[self.current][0] == 'COMMA':
                self.consume('COMMA')
        self.consume('RBRACE')  # Consume ']'
        return {'type': 'array', 'elements': elements}

    """
    Parses a function definition, including its name, parameters, and body.

    Returns:
        dict: A dictionary representing the function definition, including the function name, parameters, and body.
    """
    def parse_function(self):
        self.consume('FUN')
        function_name = self.consume('ID')
        self.consume('LPAREN')
        parameters = self.parse_parameters()
        self.consume('OPEN_CURLY_BRACKET')
        body = self.parse_statements()
        self.consume('CLOSE_CURLY_BRACKET')
        return {'type': 'function', 'name': function_name, 'parameters': parameters, 'body': body}

    """
    Parses parameters within a function definition.

    Returns:
        list: A list of parameter names.
    """
    def parse_parameters(self):
        parameters = []
        while self.current < len(self.tokens) and self.tokens[self.current][0] != 'RPAREN':
            parameters.append(self.consume('ID'))
            if self.tokens[self.current][0] == 'COMMA':
                self.consume('COMMA')
        self.consume('RPAREN')
        return parameters

    """
    Parses a return statement, including the expression to be returned.

    Returns:
        dict: A dictionary representing the return statement, including the expression to be returned.
    """
    def parse_return_statement(self):
        self.consume('RETURN')  # Consume 'RETURN'
        expression = self.parse_expression
        self.consume('END')  # Consume ';'
        return {'type': 'return', 'expression': expression}

    """
        Parses a comparison expression.

        Returns:
        dict: A dictionary representing the comparison expression.
    """
    def parse_comparison(self):
        left = self.parse_term()

        while self.current < len(self.tokens) and self.tokens[self.current][0] in {'COMPARE'}:
            op = self.consume(self.tokens[self.current][0])
            right = self.parse_term()
            left = {'type': 'expression', 'left': left, 'op': op, 'right': right}

        return left

    """
    Consumes the current token if it matches the expected type.

    Parameters:
    token_type (str): The type of token to consume.

    Returns:
    str: The value of the consumed token.

    Raises:
    RuntimeError: If the current token does not match the expected type.
    """
    def consume(self, token_type):
        if self.current < len(self.tokens) and self.tokens[self.current][0] == token_type:
            value = self.tokens[self.current][1]
            self.current += 1
            return value
        else:
            if self.tokens[self.current][0] == 'EOF' or self.tokens[self.current][0] == 'NEWLINE':
                string = ""
                y = 1
                while self.tokens[self.current - y][0] != 'NEWLINE' and self.current - y != 0:
                    y = y + 1
                if self.tokens[self.current - y][0] == 'NEWLINE':
                    y = y - 1
                for x in self.tokens[self.current - y:self.current]:
                    braces = ['LPAREN', 'LBRACE', 'RBRACE', 'RPAREN', 'OPEN_CURLY_BRACKET', 'CLOSE_CURLY_BRACKET',
                              'COMMA']
                    next_tokens = ['LPAREN', 'LBRACE', 'RBRACE', 'RPAREN', 'OPEN_CURLY_BRACKET', 'CLOSE_CURLY_BRACKET',
                                   'COMMA', 'EOF', 'NEWLINE']
                    if x[0] in braces or self.tokens[self.tokens.index(x) + 1][0] in next_tokens:
                        string = string + x[1]
                    else:
                        string = string + x[1] + " "
                if token_type == 'LPAREN':
                    token_type = '('
                elif token_type == 'LBRACE':
                    token_type = '['
                elif token_type == 'RBRACE':
                    token_type = ']'
                elif token_type == 'RPAREN':
                    token_type = ')'
                elif token_type == 'OPEN_CURLY_BRACKET':
                    token_type = '{'
                elif token_type == 'CLOSE_CURLY_BRACKET':
                    token_type = '}'
                elif token_type == 'COMMA':
                    token_type = ','
                elif token_type == 'END':
                    token_type = ';'
                raise RuntimeError(f"Expected {string}{token_type} but got {string}'{self.tokens[self.current][0]}'")
            else:
                raise RuntimeError(f'Expected token {token_type} but got {self.tokens[self.current]}')
