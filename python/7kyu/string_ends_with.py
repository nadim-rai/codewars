def solution(text, ending):
    # your code here...
    if text.endswith(ending):
        return True
    else:
        return False

print(solution("abc", "bc"))