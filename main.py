from src.arithmetic_formatter import arithmetic_arranger


def main():
    string = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"], False)
    print(string)


if __name__ == '__main__':
    main()
