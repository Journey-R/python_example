# 숫자와 문자로 구성된 입력 문자열을 받아서 숫자만 제거하고 문자만 반환
# 예제 출처 : Django 한그릇 뚝딱(문범우 님)

# input
input_str1 = "H123e4l5l6o7, P8y9t1h2o3n.4"
input_str2 = "6L11if3e 4is 5to1o0 sh00or3t."
input_str3 = "7Y3o7u n456ee2d5 6pyt9h5on2."


# 내 소스 --------------------------------------------------------------------------------------
def solution(input_str) :
    answer = ''

    # 문자열을 한그자씩 loop
    for s in input_str :

        # 숫자여부
        if s.isdigit() == False :
            answer += s

    return answer

print(solution(input_str1)+", "+solution(input_str2)+", "+solution(input_str3))
# print : Hello, Python., Life is too short., You need python.

# 저자 코드 --------------------------------------------------------------------------------------
# number_list와 input_str 비교하는 방식
# link : https://github.com/doorBW/Django_with_PracticeExamples/blob/master/example/chapter1/1-3_remove_num.py
def solution_book(input_str):
    answer = ""
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 또는 아래와 같이 map함수를 이용하여 number_list를 만들 수 있습니다.
    # number_list = list(map(str,range(10)))

    for i in input_str:
        if i in number_list:
            pass
        else:
            answer += i

    return answer

print(solution_book(input_str1)+", "+solution_book(input_str2)+", "+solution_book(input_str3))
# print : Hello, Python., Life is too short., You need python.