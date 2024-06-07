def bananas(s):
    """Given a string of letters a, b, n how many different ways
    can you make the word 'banana' by crossing out various letters
    and then reading left-to-right?"""
    banana_piece = ["", "b", "ba", "ban", "bana", "banan", "banana"]
    result_list = [""]
    temporary_list = []

    for i in range(len(s)):

        for j in range(len(result_list)):
            temporary_list += [result_list[j] + "-"]
            temporary_list += [result_list[j] + s[i]]
        result_list = []

        for elem in temporary_list:
            l = elem.replace("-", "")
            if l in banana_piece:
                result_list += [elem]
        temporary_list = []

    return [banana for banana in result_list if banana.replace("-","") == "banana"]

