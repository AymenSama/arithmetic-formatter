def arithmetic_arranger(problems, evaluate=False) -> str:
    if not (type(problems) == list or type(problems) == tuple):
        raise TypeError("Expected list or tuple")

    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in problems:
        first_operand, operator, second_operand = _parse_problem(problem)

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Operands cannot be more than four digits."

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

        four_spaces = " " * 4
        # Adjust the spacing based on which operand is longer
        if len(first_operand) > len(second_operand):
            first_line += f"  {first_operand}" + four_spaces
            second_line += f"{operator}" + " " * (len(first_operand) - len(second_operand) + 1) + f"{second_operand}" + four_spaces
            third_line += "-" * (len(first_operand) + 2) + "    "
            if len(first_operand) >= len(str(result)):
                fourth_line += " " * (2 + len(first_operand) - len(str(result))) + f"{result}" + four_spaces
            else:
                fourth_line += f" {result}" + four_spaces
        else:
            first_line += " " * (len(second_operand) - len(first_operand) + 2) + f"{first_operand}" + four_spaces
            second_line += f"{operator} {second_operand}" + four_spaces
            third_line += "-" * (len(second_operand) + 2) + four_spaces
            if len(second_operand) >= len(str(result)):
                fourth_line += " " * (2 + len(second_operand) - len(str(result))) + f"{result}" + four_spaces
            else:
                fourth_line += f" {result}" + four_spaces
        # Strip the four spaces from the last problem and add new lines
        if problem == problems[len(problems) - 1]:
            first_line = first_line.rstrip() + "\n"
            second_line = second_line.rstrip() + "\n"
            third_line = third_line.rstrip()
            if evaluate:
                third_line += "\n"
            fourth_line = fourth_line.rstrip()

    # Handle the optional argument, it defaults to False if not precised
    if evaluate:
        arranged_problems = first_line + second_line + third_line + fourth_line
    else:
        arranged_problems = first_line + second_line + third_line

    return arranged_problems


def _parse_problem(problem):
    if type(problem) != str:
        raise TypeError("Expected string")

    elements = problem.split()
    if len(elements) != 3:
        raise ValueError("Expected two operands and one operator")

    first_operand = elements[0]
    operator = elements[1]
    second_operand = elements[2]
    return first_operand, operator, second_operand
