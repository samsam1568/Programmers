def solution(wallet, bill):
    answer = 0
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        if bill[0] <= wallet[1] and bill[1] <= wallet[0]:
            bill[0], bill[1] = bill[1], bill[0]
            break
            
        else:
            if bill[0] > bill[1]:
                bill[0] = bill[0]// 2
                
            else:
                bill[1] = bill[1] // 2
            answer += 1
            print(answer)
    return answer