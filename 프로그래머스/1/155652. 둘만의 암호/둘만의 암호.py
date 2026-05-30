def solution(s, skip, index):
    answer = ''
    for i in s:
        idx = 0
        count = 0

        while count < index:
            idx += 1
            next_ch = chr((ord(i) - ord('a') + idx) % 26 + ord('a'))
            if next_ch not in skip:
                count += 1  # skip 아닐 때만 카운트

        answer += chr((ord(i) - ord('a') + idx) % 26 + ord('a'))
        
    return answer