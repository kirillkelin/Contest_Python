def is_lucky(num: str):
    left_sum = sum(int(digit) for digit in num[:3])
    right_sum = sum(int(digit) for digit in num[3:])
    return left_sum == right_sum


if __name__ == "__main__":
    input_num = input()

    left_num = right_num = input_num
    result_num = None
    while True:
        if int(left_num) > 99999 and is_lucky(left_num):
            result_num = left_num
            break
        if int(right_num) < 1000000 and is_lucky(right_num):
            result_num = right_num
            break
        left_num = str(int(left_num) - 1)
        right_num = str(int(right_num) + 1)

    print(result_num)
