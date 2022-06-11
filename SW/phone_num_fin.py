def solution(phone_book):
    # 어두를 기준으로 전화번호를 정렬 가능
    phone_book.sort()
    index = 0

    # 마지막 번호는 오름차순 정렬상, 다른 곳의 접두사일수 없음
    while index < len(phone_book) - 1:
        string = phone_book[index]

        # 바로 다음요소의 접두사가 아닌경우, 더 뒤의 번호의 접두사가 될리 없음.
        if string == phone_book[index + 1][:len(string)]:
            return False
        else:
            index += 1
    return True


print(solution(["12", "123", "1232", "567", "88"]))
