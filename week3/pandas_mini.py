import pandas as pd

# Pandas의 Series를 리스트 [5, 10, 15, 20]을 사용하여 생성하고, Series의 인덱스를 확인하는 코드를 작성하세요.
series = pd.Series([5, 10, 15, 20])
print(series.index)


# 다음 딕셔너리를 이용하여 Pandas Series를 생성하고, 인덱스를 활용하여 'b'의 값을 출력하는 코드를 작성하세요.
data = {'a': 100, 'b': 200, 'c': 300}
print(pd.Series(data)['b'])

# 다음 Pandas Series에 대해 결측값(NaN)을 확인하고, 모든 결측값을 0으로 채운 후 Series의 값을 출력하는 코드를 작성하세요.
series = pd.Series([1, 2, None, 4, None, 6])
print(series.isnull())
series_filled = series.fillna(0)
print(series_filled)


print("\n===============================================================\n")


# 다음 데이터프레임에서 열(column)의 이름들을 출력하는 코드를 작성하세요.
data = {'이름': ['홍길동', '김철수', '박영희'], 
        '나이': [25, 30, 28], 
        '성별': ['남', '남', '여']}
df = pd.DataFrame(data)
# print(df)
print(df.columns)

# 다음 데이터프레임에서 나이 열(age)을 기준으로 오름차순으로 정렬된 새로운 데이터프레임을 생성하고 출력하는 코드를 작성하세요.
print(df.sort_values(by='나이'))


# 아래와 같은 데이터프레임이 있습니다. 각 학생의 총점을 계산하는 새로운 열을 추가한 후, 총점이 250점 이상인 학생들만 포함된 데이터프레임을 생성하세요.
data = {'이름': ['홍길동', '김철수', '박영희', '이순신'], 
        '국어': [85, 90, 88, 92], 
        '영어': [78, 85, 89, 87], 
        '수학': [92, 88, 84, 90]}
df = pd.DataFrame(data)
df['총점'] = df['국어'] + df['영어'] + df['수학']
print(df[df['총점'] >= 250])

print("\n===============================================================\n")

print("0. data를 pandas DataFrame으로 만들기")
population_df = pd.read_csv(
    "https://ourworldindata.org/grapher/population.csv?v=1&csvType=full&useColumnShortNames=true",
    storage_options={"User-Agent": "Our World In Data data fetch/1.0"},
) # 58824 * 4

country_df = population_df[population_df["code"].str.len() == 3].copy() # 국가 데이터 == ISO 3자리
latest_population_df = country_df[country_df["year"] == country_df["year"].max()].copy() # 가장 최근 연도의 정보
top10_countries = latest_population_df.sort_values(by="population_historical", ascending=False).head(10) # 가장 최근 연도에서 상위 10개국
print(top10_countries)
top10_all_years = country_df[country_df["entity"].isin(top10_countries["entity"])].copy() # 상위 10개국의 "모든 연도" 데이터

print("\n1. Groupby 사용하기")
print("\nTop 10 국가의 역사상 최대 인구수:")
max_pop = top10_all_years.groupby("entity")["population_historical"].max()
print(max_pop)

print("\n2. 특정 조건으로 Filtering 사용하기")
print("\n한국 since 2000")
korea_df = country_df[(country_df["code"] == "KOR") & (country_df["year"] >= 2000)]
print(korea_df)
