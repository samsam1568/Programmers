def solution(s):
    answer = ''
    lst_space = []
    cnt_space = 0 
    in_word = False
    arr=list(map(str,s.split()))
    for k in s:
        if k == " ":
            cnt_space += 1
            in_word = False
        else:
            if not in_word:
                lst_space.append(cnt_space)
                cnt_space = 0
            in_word = True

    lst_space.append(cnt_space)
            
    for idx, i in enumerate(arr):
        char_list = list(i)
        for idx2, j in enumerate(char_list):
            if idx2 == 0 and j.isalpha():
                char_list[idx2] = j.upper()
            elif j.isalpha():
                char_list[idx2] = j.lower()
        arr[idx] = ''.join(char_list)
        
    for idx, i in enumerate(arr):
        answer += i + " " * lst_space[idx+1]

    return answer