import re

# Define token patterns
token_specification = [
    ('FUN', r'FUN'),  # Function keyword
    ('RETURN', r'RETURN'),  # Return keyword
    ('COMMA', r','),  # Add this to handle commas
    ('STRING', r'"(?:\\.|[^"\\])*"'),  # String literals (supporting escape sequences)
    ('NUMBER', r'\d+'),  # Integer number
    ('COMPARE', r'!=|<=|>=|<|>|=='),  # Comparison operators
    ('ASSIGN', r'='),  # Assignment operator
    ('END', r';'),  # Statement terminator
    ('OP', r'\*\*|//|[+\-*/%]|&'),  # Arithmetic operators including modulo
    ('LOGIC', r'AND|OR|NOT'),  # Logical operators
    ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),  # Identifiers
    ('LPAREN', r'\('),  # Left Parenthesis
    ('LBRACE', r'\['),  # Left Parenthesis
    ('RBRACE', r'\]'),  # Right Parenthesis
    ('RPAREN', r'\)'),  # Right Parenthesis
    ('OPEN_CURLY_BRACKET', r'\{'),  # Left Brace
    ('CLOSE_CURLY_BRACKET', r'\}'),  # Right Brace
    ('SKIP', r'[ \t]+'),  # Skip over spaces and tabs
    ('NEWLINE', r'\n'),  # Newline characters
    ('MISMATCH', r'.'),  # Any other character
]

"""
Tokenizer:
    A class to convert a string of code into a list of tokens based on defined patterns.

Attributes:
    code (str): The input string of code to be tokenized.
    tokens (list): A list of tuples where each tuple contains a token type and the matched string.
"""
# Define a tokenizer class
class Tokenizer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.tokenize()


    """
    Processes the input code and converts it into a list of tokens.

    This method iterates over the code, matches it against each pattern in `token_specification`,
    and appends the corresponding token to `self.tokens`.

    - If the `SKIP` token type is matched, it skips the whitespace or tab.
    - If the `MISMATCH` token type is matched, it raises a `RuntimeError` with an error message.
    - Appends an 'EOF' (End of File) token at the end of the token list to indicate the end of input.

    Raises:
        RuntimeError: If an unexpected character is encountered (not matching any token).
    """
    def tokenize(self):
        while self.code:
            for token_type, pattern in token_specification:
                regex = re.compile(pattern)
                match = regex.match(self.code)
                if match:
                    if token_type == 'SKIP':
                        self.code = self.code[match.end():]
                        break
                    elif token_type == 'MISMATCH':
                        raise RuntimeError(f'Unexpected character {self.code[0]}')
                    else:
                        self.tokens.append((token_type, match.group()))
                        self.code = self.code[match.end():]
                        break

        self.tokens.append(('EOF', ''))  # End of input

    """
    Returns the list of tokens generated from the input code.

    Returns:
        list: A list of tuples, each containing a token type and the matched string.
    """
    def get_tokens(self):
        return self.tokens
