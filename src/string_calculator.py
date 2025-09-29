def stringSum(num1: str, num2: str) -> str:
    try:
        return str(int(num1) + int(num2))
    except ValueError:
        return "0"