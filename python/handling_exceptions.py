def perform_division(x: str, y: str) -> None:
    try:
        print(int(x) // int(y))
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x_, y_ = input().split()
        perform_division(x=x_, y=y_)
