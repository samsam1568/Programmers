def solution(lines):
    arr = [0 for _ in range(200)]
    answer = 0
    for i in lines:
        start, end = i[0], i[1]
        for j in range(start+100,end+100):
            arr[j] += 1
    print(arr)
    for k in arr:
        if k >1:
            answer += 1
        
    return answer