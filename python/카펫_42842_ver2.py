def solution(brown, yellow):
    w = ((brown+4) / 2 + (((brown+4)/2) ** 2 - 4 *(brown+yellow))**0.5) / 2
    h = ((brown+4) / 2 -(((brown+4)/2) ** 2 - 4 *(brown+yellow))**0.5) / 2
    return [w, h]
