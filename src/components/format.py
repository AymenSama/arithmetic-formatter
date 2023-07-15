def format_problem(first_operand, second_operand, operator, result, first_line, second_line, third_line, fourth_line):
    four_spaces = " " * 4
    if len(first_operand) > len(second_operand):
        first_line += f"  {first_operand}" + four_spaces
        second_line += f"{operator}" + " " * (
                len(first_operand) - len(second_operand) + 1) + f"{second_operand}" + four_spaces
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
    return first_line, fourth_line, second_line, third_line
