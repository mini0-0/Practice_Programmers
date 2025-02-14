import bisect


def solution(words, queries):
    word_dict = {}
    reverse_word_dict = {}

    # 각 단어들을 길이별로 분리하여 저장
    for word in words:
        l = len(word)
        if l not in word_dict:
            word_dict[l] = []
            reverse_word_dict[l] = []
        word_dict[l].append(word)
        reverse_word_dict[l].append(word[::-1])

    # 각 길이별 리스트 정렬 (정방향, 역방향)
    for l in word_dict:
        word_dict[l].sort()
        reverse_word_dict[l].sort()

    answer = []
    for query in queries:
        l = len(query)
        # 해당 길이의 단어가 없으면 0 추가
        if l not in word_dict:
            answer.append(0)
            continue

        # 정방향 쿼리: 접두사가 고정된 경우 (예: "fro??")
        if query[0] != '?':
            # '?'를 최소 글자 'a'와 최대 글자 'z'로 대체하여 범위를 구함
            left_query = query.replace('?', 'a')
            right_query = query.replace('?', 'z')
            left_index = bisect.bisect_left(word_dict[l], left_query)
            right_index = bisect.bisect_right(word_dict[l], right_query)
            answer.append(right_index - left_index)
        else:
            # 역방향 쿼리: 접미사가 고정된 경우 (예: "????o")
            # 단어와 쿼리를 뒤집어서 접두사 검색으로 처리
            rev_query = query[::-1]
            left_query = rev_query.replace('?', 'a')
            right_query = rev_query.replace('?', 'z')
            left_index = bisect.bisect_left(reverse_word_dict[l], left_query)
            right_index = bisect.bisect_right(reverse_word_dict[l], right_query)
            answer.append(right_index - left_index)

    return answer


```