def solution(nums):
    answer = 0
    dic = dict()
    
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    for k,v in dic.items():
        if v >= 1:
            answer += 1
    answer = min(answer, len(nums)//2)
    return answer