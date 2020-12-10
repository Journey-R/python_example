# 알파벳으로 구성된 문자열 파라미터에 각 알파벳의 갯수
# 예제 출처 : Django 한그릇 뚝딱(문범우 님)

#input
input_str1 = "aaabbccd"
input_str2 = "ffaafddde"
input_str3 = "aabcdadbbfweeaddfadf"

# 내 소스 --------------------------------------------------------------------------------------
import pandas as pd

def solution(input_str) :
    answer = ''

    # 글자별 개수
    index = pd.Index(list(input_str))
    serValueCounts = index.value_counts()

    # 시리즈 타입, 글자, 글자별 개수
    # print(serValueCounts)
    # print(serValueCounts.index)
    # print(serValueCounts.values)

    # index 기준으로 sort
    serValueCounts = serValueCounts.sort_index()

    # 반환값 형태 : 글자개수글자개수(ex: a3b2)
    for idx in range(len(serValueCounts)) :
        answer += serValueCounts.index[idx] + str(serValueCounts.values[idx])

    return answer

print(solution(input_str1), solution(input_str2), solution(input_str3))
# print : a3b2c2d1 a2d3e1f3 a5b3c1d5e2f3w1


# 저자 코드 --------------------------------------------------------
# link : https://github.com/doorBW/Django_with_PracticeExamples/blob/master/example/chapter1/1-4_counting_character.py
def solution_book(input_str):
    answer = ""
    input_dic = {}

    for i in input_str:
        if i in input_dic.keys():
            input_dic[i] += 1

        else:
            input_dic[i] = 1
    input_list = list(input_dic.keys())
    input_list.sort()

    for i in input_list:
        answer += i
        answer += str(input_dic[i])

    return answer

print(solution_book(input_str1), solution_book(input_str2), solution_book(input_str3))
# print : a3b2c2d1 a2d3e1f3 a5b3c1d5e2f3w1