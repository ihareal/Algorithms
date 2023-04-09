def fibonacci_table_algorithm(n):
    if n <= 1:
        return n
    array = [0 for i in range(0, n)]
    array[0] = 1
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]
    return array[n-1]
    first = 1
    second = 1
    for i in range(2, n):
        result = first + second
        first = second
        second = result
    return result


def fibonacci_table_solution(n):
    # print("enter the number")
    # number = int(input())
    result = fibonacci_table_algorithm(n)
    print(result)
