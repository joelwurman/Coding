def find_max(input_list):
    max_number = 0.0
    for position in input_list:
        if max_number < position:
            max_number = position
    return max_number
