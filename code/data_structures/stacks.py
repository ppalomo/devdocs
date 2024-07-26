def stack_list():
    stack = ["Pablo", "Daniel", "Anthony"]

    # PUSH
    stack.append("Gabriel")

    # POP
    print(stack.pop())


def stack_deque():
    from collections import deque

    stack = deque(["Ram", "Tarun", "Asif", "John"])
    stack.append("Akbar")
    print(stack.pop())


stack_list()
stack_deque()
