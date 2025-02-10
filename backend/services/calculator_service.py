import re
from models.calculator_interface import ICalculator

class StringCalculator(ICalculator):
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [",", "\n"]
        custom_delimiter_match = re.match(r"^//(.)\n", numbers)

        if custom_delimiter_match:
            delimiters.append(custom_delimiter_match.group(1))
            numbers = numbers[4:]

        delimiter_regex = "|".join(map(re.escape, delimiters))
        num_list = [int(num) for num in re.split(delimiter_regex, numbers) if num]

        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers are  not allowed: {','.join(map(str, negatives))}")

        return sum(num for num in num_list if num <= 1000)
