from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    idx = 0
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for i in goal:
        if len(cards1) > 0 and cards1[0] == i:
            idx += 1
            cards1.popleft()
        elif len(cards2) > 0 and cards2[0] == i:
            idx += 1
            cards2.popleft()
        else:
            answer = 'No'

    if idx == len(goal):
        answer = 'Yes'
    return answer