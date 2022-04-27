def solution(lottos, win_nums):
    answer = []
    correct_nums = 0
    expect = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    
    for number in lottos:
        if number in win_nums:
            correct_nums = correct_nums + 1
        elif not number:
            expect = expect + 1
            
    max = correct_nums + expect
    min = correct_nums
    if max >= 6:
        max = 6
        
    answer.append(rank[max])
    answer.append(rank[min])
    
    return answer