""" If the longer operand comes first: first line: leave 2 spaces at the beginning, one for the operator position in the next line and one space for after the operator
second line: subtract the length of the first operand from the one for the second operand, add 1 to the result and leave it as the number of spaces to be put before the second operand
third line: length of the longer operand + 2 is the number of dashes to be inserted, the 2 dashes added to account for the operator and the space
fourth line:
"""
""" If the longer operand comes second, we insert subtraction of lengths result + 2 spaces in the first line then the operand, 
we then leave a space between the operator and the operand in the second line  """


def arithmetic_arranger(problems, evaluate=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    for problem in problems:

        operation_elements = problem.split()
        first_operand = operation_elements[0]
        operator = operation_elements[1]
        second_operand = operation_elements[2]
        four_spaces = " " * 4

        try:
            first_number = int(first_operand)
            second_number = int(second_operand)
        except:
            return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            evaluation = first_number + second_number
        elif operator == "-":
            evaluation = first_number - second_number
        else:
            return "Error: Operator must be '+' or '-'."

        # Adjust the spacing based on which operand is longer
        if len(first_operand) > len(second_operand):
            first_line += "  {}".format(first_operand) + four_spaces
            second_line += "{}".format(operator) + " " * (len(first_operand) - len(second_operand) + 1) + "{}".format(
                second_operand) + four_spaces
            third_line += "-" * (len(first_operand) + 2) + "    "
            if len(first_operand) >= len(str(evaluation)):
                fourth_line += " " * (2 + len(first_operand) - len(str(evaluation))) + "{}".format(
                    evaluation) + four_spaces
            else:
                fourth_line += " {}".format(evaluation) + four_spaces
        else:
            first_line += " " * (len(second_operand) - len(first_operand) + 2) + "{}".format(
                first_operand) + four_spaces
            second_line += "{} {}".format(operator, second_operand) + four_spaces
            third_line += "-" * (len(second_operand) + 2) + four_spaces
            if len(second_operand) >= len(str(evaluation)):
                fourth_line += " " * (2 + len(second_operand) - len(str(evaluation))) + "{}".format(
                    evaluation) + four_spaces
            else:
                fourth_line += " {}".format(evaluation) + four_spaces
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