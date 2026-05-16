def solution(name):
    answer = 0
    mydic = {
        'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
        'K': 10, 'L':11, 'M':12, 'N':13, 'O':12, 'P':11, 'Q':10, 'R':9, 'S':8, 'T':7,
        'U': 6, 'V':5, 'W':4, 'X':3 ,'Y':2, 'Z':1
    }
    
    for c in name:
        answer += mydic[c]
    
    n = len(name)
    move = n - 1  # 패턴 1: 오른쪽으로 쭉

    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':  # A 연속 구간 끝 찾기
            next_i += 1
        
        move = min(move,
            i + i + (n - next_i),        # 패턴 2: 오른쪽 갔다 되돌아오기
            (n - next_i) + (n - next_i) + i  # 패턴 3: 왼쪽 먼저
        )

    answer += move
    return answer