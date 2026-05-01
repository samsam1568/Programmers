def solution(dots):
    answer = 0
    for i in range(len(dots)):
        for j in range(len(dots)):
            print(i,j)
            if i >= j:
                continue
            dots_all = dots.copy()
            x1,y1 = dots[i]
            x2,y2 = dots[j]
            
            dots_all.remove(dots[i])
            dots_all.remove(dots[j])
            
            x3,y3 = dots_all[0]
            x4,y4 = dots_all[1]
       
            if (abs(x1-x2)/abs(y1-y2)) == (abs(x3-x4)/abs(y3-y4)):
                answer = 1
                return 1
            
                
            
    return answer