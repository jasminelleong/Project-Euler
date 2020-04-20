def fibonacci_sequence():
    second_previous_value = 1
    previous_value = 2
    yield second_previous_value
    yield previous_value
    while True:
        next_value = second_previous_value + previous_value
        second_previous_value = previous_value
        previous_value = next_value
        yield next_value
