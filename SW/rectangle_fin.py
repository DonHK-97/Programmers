def solution(w, h):
    answer = w * h
    grad = h / w

    if round(grad) != grad:
        grad = int(grad) + 1

    return answer - (w + h - gcd(w, h))


def gcd(w, h):
    a, b = max(w, h), min(w, h)
    while 1:
        r = a % b
        if not r:
            return b
        a = b
        b = r


print(solution(4, 15))
