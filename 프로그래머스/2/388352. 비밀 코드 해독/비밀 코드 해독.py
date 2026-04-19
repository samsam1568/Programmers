from itertools import combinations


def solution(n, q, ans):
    answer= 0
    all_candidate = list(combinations(range(1, n+1), 5))
    
    for candidate in all_candidate:
        answer_cnt = 0
        for q_idx in range(len(q)):
            cnt = 0
            for p_idx in q[q_idx]:
                if p_idx in candidate:
                    cnt += 1
            if cnt == ans[q_idx]:
                answer_cnt += 1

        if answer_cnt == len(q):
            answer += 1
                         
    return answer