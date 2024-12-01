def max_pairwise_product(numbers):
    length = len(numbers) - 1
    max_value = 0
    max_second_value = 0
    for i in range(length, -1, -1):
        if numbers[i] > max_value:
            max_second_value = max_value
            max_value = numbers[i]
        elif numbers[i] > max_second_value:
            max_second_value = numbers[i]

    return max_value * max_second_value


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
