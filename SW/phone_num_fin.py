def solution(phone_book):
    phone_book.sort()
    for index in range(len(phone_book)-1):
        sample = phone_book[index]
        if sample == phone_book[index + 1][:len(sample)]:
            return False

    return True

print(solution(["123", "456", "789"]))
