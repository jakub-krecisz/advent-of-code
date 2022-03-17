""" --- Day 10: Syntax Scoring --- """


def check_brackets(string=''):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    complete_score_dict = {')': 1, ']': 2, '}': 3, '>': 4}

    score = 0
    complete_score = 0
    brackets_ok = True

    for symbol in string:
        if symbol in brackets.keys():
            stack.append(symbol)
        elif symbol in brackets.values():
            if stack:
                bracket = stack.pop()
                if brackets.get(bracket) != symbol:
                    score += score_dict[symbol]
                    brackets_ok = False
                    break

    if stack and brackets_ok:
        complete_stack = []
        for item in stack[::-1]:
            complete_stack.append(brackets.get(item))
            complete_score = complete_score * 5 + complete_score_dict[
                brackets.get(item)]
    return score, complete_score


if __name__ == "__main__":
    score = 0
    middle_score = []
    with open("data.txt") as f:
        for line in f:
            cur_score, cur_complete_score = check_brackets(
                line.replace('\n', ''))
            score += cur_score
            if cur_complete_score != 0:
                middle_score.append(cur_complete_score)

    print(score, sorted(middle_score)[len(middle_score) // 2])
