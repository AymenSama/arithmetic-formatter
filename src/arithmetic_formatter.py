from src.components.formatter import format_problem, format_last, join
from src.components.parser import parse_problem


def arithmetic_arranger(problems, evaluate=False) -> str:
    if not (type(problems) == list or type(problems) == tuple):
        raise TypeError("Expected list or tuple")

    if len(problems) > 5:
        return "Error: Too many problems."

    lines = ["", "", "", ""]

    for problem in problems:
        try:
            first_operand, operator, second_operand = parse_problem(problem)
        except RuntimeError:
            return "Error: Operands cannot be longer than four digits."

        try:
            first_number = int(first_operand)
            second_number = int(second_operand)
        except ValueError:
            return "Error: Numbers must only contain digits."

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        else:
            return "Error: Operator must be '+' or '-'."

        format_problem(lines, first_operand, second_operand, operator, result)

        if problem == problems[-1]:
            format_last(lines)

    arranged_problems = join(lines, evaluate)

    return arranged_problems
