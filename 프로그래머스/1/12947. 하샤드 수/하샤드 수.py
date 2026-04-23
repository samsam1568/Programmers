def solution(x):
    answer = True
    tot = 0
    for i in str(x):
        tot += int(i)
    if x % tot == 0:
        answer = True
    else:
        answer = False
    
    return answer