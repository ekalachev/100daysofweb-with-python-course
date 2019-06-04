def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if maximum < number:
            maximum = number

    return maximum
