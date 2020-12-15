import pandas as pd
import numpy as np


data = {"name": ["Moon", "Choi", "Song", "Jang"],
           "math": [4.0, 2.1, 4.7, 2.6],
           "science": [3.8, 1.7, 0.7, 2.4]}
df = pd.DataFrame(data, columns=["name", "math", "science"])

def solution(df) :

    avgList = []
    avgHighList = []

    for i in range(len(df)) :
        avg = np.mean([df.loc[i, 'math'], df.loc[i, 'science'] ])
        avgList.append(avg)

        if avg > 2.5 :
            avgHighList.append(True)
        else :
            avgHighList.append(False)

    df['avg'] = avgList
    df['avg_high'] = avgHighList

    return df

print(solution(df))
print('-'*50)


# 저자 코드 --------------------------------------------------------------------------------------
# link : https://github.com/doorBW/Django_with_PracticeExamples/blob/master/example/chapter1/1-5_using_pandas.py
# import pandas as pd
def solution(df):
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - #
	# Write your code here.
	df['avg'] = (df['math']+df['science'])/2
	df['avg_high'] = df['avg']>2.5
	return df
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - #

print(solution(df))
print('-'*50)

# 저자 코드 보니, 내가 파이썬을 파이썬 답게 쓰지 못하고 있다는 걸 알게 되었다.
# dataframe의 사용법을 제대로 파악하지 못하고 있구나 싶다.
