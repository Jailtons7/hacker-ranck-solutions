from typing import Set


def perform_operation(set_: Set[int], command: str) -> Set[int]:
    split_ = command.split(" ")
    if len(split_) == 1:
        operation = split_[0]
        method = getattr(set_, operation)
        method()
    else:
        operation, value = command.split()[0], int(command.split()[1])
        method = getattr(set_, operation)
        method(value)
    return set_


if __name__ == '__main__':
    n = int(input())
    int_set = set(map(int, input().split()))
    commands = int(input())
    for _ in range(commands):
        int_set = perform_operation(set_=int_set, command=input())
    print(sum(int_set))
