# 숫자로 구성된 입력 문자열을 받아서 해당 문자열에 없는 숫자를 찾아 반환
# 예제 출처 : Django 한그릇 뚝딱(문범우 님)

# input
input_str1 = '012345678'
input_str2 = '483750219'
input_str3 = '242810485760109726496'

# 내가 추가한 input
input_str4 = "0123"

# 내 소스 --------------------------------------------------------------------------------------
def solution(input_str) :
    answer = ''

    # string을 list에 담으면 한글자씩 요소에 담김
    setInput = list(input_str)

    # set 타입으로 변환
    setInput = set(setInput)

    # 차집합, replace(불필요한 특수문자 제거)
    answer = str(setInt - setInput).replace('{', '').replace('}', '').replace("'", '')

    return answer

# 0~9까지의 숫자를 set 타입으로 변환
setInt = str(list(range(0, 10))).replace('[', '').replace(']', '')
setInt = setInt.split(', ')
setInt = set(setInt)

print(solution(input_str1) + ', ' + solution(input_str2) + ', ' + solution(input_str3))  # print : 9, 6, 3
print(solution(input_str4)) # print : 9, 7, 6, 8, 4, 5


# 저자 코드 --------------------------------------------------------------------------------------
# 저자 코드에서 else 내부에 break가 있어서 없는 다음 숫자의 존재 여부를 체크하지 않는다.
# link : https://github.com/doorBW/Django_with_PracticeExamples/blob/master/example/chapter1/1-2_find_num.py
def solution_book(input_str):
    answer = ""
    for i in range(10):
        if str(i) in input_str:
            pass
        else:
            answer = str(i)
            break

    return answer

print(solution_book(input_str1) + ', ' + solution_book(input_str2) + ', ' + solution_book(input_str3))  # print : 9, 6, 3
print(solution_book(input_str4)) # print : 4

# 저자 코드 수정 버전 --------------------------------------------------------------------------------------
# 저자 코드에서 else 내부에 break가 있어서 없는 다음 숫자의 존재 여부를 체크하지 않는다.
# -> else 다음 코드부터 수정

def solution_book_modfy(input_str):
    answer = ""
    for i in range(10):
        if str(i) in input_str:
            pass
        else:
            # 수정 코드 --------------------------------------------------------------------
            answer += str(i)

    # answer을 str에서 list로 변환
    strList = []
    strList[:] = answer

    # replace(불필요한 특수문자 제거)
    answer = str(strList).replace('[', '').replace(']', '').replace("'", '')

    return answer

print(solution_book_modfy(input_str1) + ', ' + solution_book_modfy(input_str2) + ', ' + solution_book_modfy(input_str3))  # print : 9, 6, 3
print(solution_book_modfy(input_str4)) # print : 4, 5, 6, 7, 8, 9