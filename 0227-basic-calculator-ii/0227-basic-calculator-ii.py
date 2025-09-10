class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        last_operator = '+'  # Assume '+' before first number

        for i, ch in enumerate(s):
            if ch.isdigit():
                current_number = current_number * 10 + int(ch)

            # If current char is an operator or last character of string
            if ch in '+-*/' or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    last = stack.pop()
                    stack.append(int(last / current_number))  # Truncate toward zero

                last_operator = ch
                current_number = 0

        return sum(stack)