from src.components.format import format_problem
from src.components.parse import parse_problem


def arithmetic_arranger(problems, evaluate=False) -> str:
    if not (type(problems) == list or type(problems) == tuple):
        raise TypeError("Expected list or tuple")

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line, second_line, third_line, fourth_line = "", "", "", ""

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

        # Adjust the spacing based on which operand is longer
        first_line, fourth_line, second_line, third_line = format_problem(first_operand, second_operand, operator,
                                                                          result,
                                                                          first_line, second_line, third_line,
                                                                          fourth_line)
        # Strip the four spaces from the last problem and add new lines
        if problem == problems[len(problems) - 1]:
            first_line, fourth_line, second_line, third_line = _handle_last(evaluate, first_line, second_line,
                                                                            third_line, fourth_line)

    # Handle the optional argument, it defaults to False if not precised
    if evaluate:
        arranged_problems = first_line + second_line + third_line + fourth_line
    else:
        arranged_problems = first_line + second_line + third_line

    return arranged_problems


def _handle_last(evaluate, first_line, second_line, third_line, fourth_line):
    first_line = first_line.rstrip() + "\n"
    second_line = second_line.rstrip() + "\n"
    third_line = third_line.rstrip()
    if evaluate:
        third_line += "\n"
    fourth_line = fourth_line.rstrip()
    return first_line, fourth_line, second_line, third_line
