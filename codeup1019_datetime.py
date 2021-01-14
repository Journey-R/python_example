# CodeUp 알고리즘 기초 100제 : https://codeup.kr/problem.php?id=1019
# input
# 년, 월, 일이 ".(닷)"으로 구분되어 입력된다.
# 2013.8.5

# output
# 입력받은 년, 월, 일을 yyyy.mm.dd 형식으로 출력한다.
# (%02d를 사용하면 2칸을 사용해 출력하는데, 한 자리 수인 경우 앞에 0을 붙여 출력한다.)
# 2013.08.05

# 내 풀이 -------------------------------------------------------------------------------------
import datetime

t = input()
st = t.split('.')

# 년도가 4자리 미만일 때 (월, 일은 1자리 일때 앞에 0이 채워짐)
if len(st[0]) < 4 :

    # zfill(n) : n자리 미만일 때 앞을 0으로 채워줌
    st[0] = st[0].zfill(4)
    t = st[0] + '.' + st[1] + '.' + st[2]

# strptime()  : 다양한 포맷의 문자열을 datetime 객체로 변환 (문자열에 시간이 없을 경우 '00:00:00' 출력됨)
# strftime() : datetime 객체를 다양한 포맷의 문자열로 변환
t = datetime.datetime.strptime(t, '%Y.%m.%d').strftime('%Y.%m.%d')
print(t)
# input : 99.1.1
# output : 0099.01.01

print('-'*50)

# test code -------------------------------------------------------------------------------------
# strptime()에서 datetime으로 변환되면서 포하되었던 시:분:초가 strftime()에서는 출력되지 않아 추가한 테스트 코드
s = datetime.datetime.strptime('0099.01.01 00:00:00', '%Y.%m.%d %H:%M:%S')

# datetime 객체에서 추출하고자하는 일시만 문자열로 변환
# 년월일만
print(s.strftime('%Y.%m.%d'))   # output : 0099.01.01
print(s.strftime('%Y:%m:%d'))   # output : 0099:01:01
print(s.strftime('%Y/%m/%d'))   # output : 0099/01/01

# 년월일에 시간 추가
print(s.strftime('%H:%M:%S'))   # output : 00:00:00

# 일시
print(s.strftime('%Y/%m/%d %H:%M:%S'))  # output : 0099/01/01 00:00:00


print('-'*50)

# 다른 사람 코드 : https://jihyehwang09.github.io/2019/05/30/codeup-4/ -------------------------------
yyyy, mm, dd = input().split('.')
print(yyyy.zfill(4), mm.zfill(2), dd.zfill(2), sep = '.')

print('-'*50)

# CodeUp 코드 ----------------------------------------------------------------------------------------
a, b, c = input().split('.')

# 문자열 formatting : 형식 % 데이터
# %04d : 4자리 정수 출력(4자리 미만일 경우 앞에 '0'으로 채움)
# end : 개행하지 않고 이어서 출력
print('%04d' % int(a), end = '.')
print('%02d' % int(b), end = '.')
print('%02d' % int(c))

# -----------------------------------------------------------------------------------------------------
# 다른 사람 코드와 CodeUp 코드를 보니 datetime이 필요없는 문제였다. (단순 입출력 문제)