import unittest

from src.arithmetic_formatter import arithmetic_arranger


class ArithmeticFormatterTest(unittest.TestCase):
    def test_empty_list(self):
        """Returns an empty string for an empty list"""
        problems = []

        formatted = arithmetic_arranger(problems)

        self.assertEqual(formatted, "")

    def test_long_operands_first(self):
        """Returns the expected format for the longer operands coming first"""
        problems = ['3801 - 2', '123 + 49']

        formatted = arithmetic_arranger(problems)

        actual, expected = (formatted,
                            '  3801      123\n' +
                            '-    2    +  49\n' +
                            '------    -----')
        self.assertEqual(actual, expected)

    def test_long_operands_second(self):
        """Returns the expected format for the longer operands coming last"""
        problems = ['1 + 2', '1 - 9380']

        formatted = arithmetic_arranger(problems)

        actual, expected = (formatted,
                            '  1         1\n' +
                            '+ 2    - 9380\n' +
                            '---    ------')
        self.assertEqual(actual, expected)

    def test_mixed_four_problems(self):
        """Returns the expected format for arbitrary operand choice in 4 operations"""
        problems = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']

        formatted = arithmetic_arranger(problems)

        actual, expected = (formatted,
                            '    3      3801      45      123\n' +
                            '+ 855    -    2    + 43    +  49\n' +
                            '-----    ------    ----    -----')
        self.assertEqual(actual, expected)

    def test_mixed_five_problems(self):
        """Returns the expected format for arbitrary operand choice in 5 operations"""
        problems = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']

        formatted = arithmetic_arranger(problems)

        actual, expected = (formatted,
                            '  11      3801      1      123         1\n' +
                            '+  4    - 2999    + 2    +  49    - 9380\n' +
                            '----    ------    ---    -----    ------')
        self.assertEqual(actual, expected)

    def test_too_many_problems(self):
        """Returns an error message for more than five problems"""
        problems = ['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']

        formatted = arithmetic_arranger(problems)

        self.assertIn("Error" and "problems", formatted)

    def test_incorrect_operator(self):
        """Returns an error message for unknown operator"""
        problems = ['3 / 855', '3801 - 2', '45 + 43', '123 + 49']

        formatted = arithmetic_arranger(problems)

        self.assertIn("Error" and "Operator", formatted)

    def test_too_many_digits(self):
        """Returns an error message for an operand having more than four digits"""
        problems = ['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']

        formatted = arithmetic_arranger(problems)

        self.assertIn("Error" and "digits", formatted)

    def test_only_digits(self):
        """Returns an error message for an operand not being numeric"""
        problems = ['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']

        formatted = arithmetic_arranger(problems)

        self.assertIn("Error" and "digits", formatted)

    def test_two_problems_with_solutions(self):
        """Returns the correct format and result for two problems"""
        problems = ['3 + 855', '988 + 40']

        formatted = arithmetic_arranger(problems, True)

        actual, expected = (formatted,
                            '    3      988\n' +
                            '+ 855    +  40\n' +
                            '-----    -----\n' +
                            '  858     1028')
        self.assertEqual(actual, expected)

    def test_five_problems_with_solutions(self):
        """Returns the correct format and result for five problems"""
        problems = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']

        formatted = arithmetic_arranger(problems, True)

        actual, expected = (formatted,
                            '   32         1      45      123      988\n' +
                            '- 698    - 3801    + 43    +  49    +  40\n' +
                            '-----    ------    ----    -----    -----\n' +
                            ' -666     -3800      88      172     1028')
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
