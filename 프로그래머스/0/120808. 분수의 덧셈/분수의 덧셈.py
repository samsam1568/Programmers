def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(numer1, denom1, numer2, denom2):
    answer = []
    a,b = numer1*denom2+ numer2*denom1, denom1 * denom2
    d = gcd(a, b)
    answer.append(a//d)
    answer.append(b//d)
    
    return answer