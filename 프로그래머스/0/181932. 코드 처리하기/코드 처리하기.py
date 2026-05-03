def solution(code):
    answer = ''
    mode = 0
    for idx,value in enumerate(code):
        if value == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
            continue
            
        if mode == 1:
            if idx % 2 == 1:
                answer += value
                
        else:
            if idx % 2 == 0:
                answer += value
                
    if answer == "":
        answer = "EMPTY"
    return answer