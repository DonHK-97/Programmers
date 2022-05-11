"""
def solution(s):
    string_len = len(s)
    compression_result = []

    for unit in range(1, string_len):
        index = 0
        last = index + unit
        temp_words = s[index: last]
        answer_len = string_len

        compression = 0
        match = 0

        while 1:
            print(last)
            if last + unit >= string_len:
                break
            elif s[last: last + unit] == temp_words:
                answer_len -= unit
                match = 1
            else:
                if match:
                    compression += 1
                    match = 0
                temp_words = s[last: last + unit]

            last += unit
        compression_result.append(answer_len + compression)

    return min(compression_result)
"""

def compress(text, tok_len):
    words = [text[i:i + tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        print(a, b)
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text) / 2) + 1)) + [len(text)])
