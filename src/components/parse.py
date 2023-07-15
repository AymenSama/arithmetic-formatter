def parse_problem(problem):
    if type(problem) != str:
        raise TypeError("Expected string")

    elements = problem.split()
    if len(elements) != 3:
        raise ValueError("Expected two operands and one operator")

    first_operand = elements[0]
    operator = elements[1]
    second_operand = elements[2]

    if len(first_operand) > 4 or len(second_operand) > 4:
        raise RuntimeError("Operands too long")

    return first_operand, operator, second_operand
