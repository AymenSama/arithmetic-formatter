def format_problem(lines, first_operand, second_operand, operator, result):
    four_spaces = " " * 4
    if len(first_operand) > len(second_operand):
        lines[0] += f"  {first_operand}" + four_spaces
        lines[1] += f"{operator}" + " " * (
                len(first_operand) - len(second_operand) + 1) + f"{second_operand}" + four_spaces
        lines[2] += "-" * (len(first_operand) + 2) + "    "
        if len(first_operand) >= len(str(result)):
            lines[3] += " " * (2 + len(first_operand) - len(str(result))) + f"{result}" + four_spaces
        else:
            lines[3] += f" {result}" + four_spaces
    else:
        lines[0] += " " * (len(second_operand) - len(first_operand) + 2) + f"{first_operand}" + four_spaces
        lines[1] += f"{operator} {second_operand}" + four_spaces
        lines[2] += "-" * (len(second_operand) + 2) + four_spaces
        if len(second_operand) >= len(str(result)):
            lines[3] += " " * (2 + len(second_operand) - len(str(result))) + f"{result}" + four_spaces
        else:
            lines[3] += f" {result}" + four_spaces


def format_last(lines):
    lines[0] = lines[0].rstrip() + "\n"
    lines[1] = lines[1].rstrip() + "\n"
    lines[2] = lines[2].rstrip()
    lines[3] = lines[3].rstrip()


def join(lines, evaluate):
    if evaluate:
        lines[2] += "\n"
        arranged_problems = "".join(lines)
    else:
        arranged_problems = "".join(lines[:-1])
    return arranged_problems
