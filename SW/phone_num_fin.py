def solution(phone_book):
    phone_book.sort()
    index = 0

    while index < len(phone_book) - 1:
        string = phone_book[index]

        if string == phone_book[index + 1][:len(string)]:
            return False
        else:
            index += 1
    return True


print(solution(["12", "123", "1232", "567", "88"]))
