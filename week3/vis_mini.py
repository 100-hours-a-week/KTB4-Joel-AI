#%%
import io
import re
import pandas as pd

import matplotlib.pyplot as plt
# !pip install matplotlib_venn
from matplotlib_venn import venn2
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


# 샘플 데이터프레임을 생성한 후, 데이터의 기본 정보를 출력하는 코드를 작성하세요.
data = {
    "이름": ["김철수", "이영희", "박민수", "최지현", "홍길동"],
    "나이": [25, 30, 35, 28, 40],
    "직업": ["개발자", "마케터", "개발자", "디자이너", "CEO"],
    "연봉": [4000, 3500, 5000, 4200, 10000],
    "가입일": ["2020-05-21", "2019-07-15", "2021-01-10", "2018-11-03", "2017-09-27"]
}

df = pd.DataFrame(data)
print(df.info())

# 샘플 데이터에서 나이가 30 이상이고 연봉이 5000 이하인 사람들만 필터링하는 코드를 작성하세요.
print(df[(df["나이"] >= 30) & (df["연봉"] <= 5000)])

#샘플 데이터에서 가입 연도가 2019년 이전인 사람들을 찾아 연봉을 10% 인상한 후, 전체 평균 연봉을 계산하는 코드를 작성하세요.
df["가입일"] = pd.to_datetime(df["가입일"])
df.loc[df["가입일"].dt.year < 2019, "연봉"] *= 1.10
print(df["연봉"].mean())


print("\n5===============================================================\n")
#%%
# JSON 형식의 데이터를 직접 생성한 후, Pandas 데이터프레임으로 변환하는 코드를 작성하세요.
data = '''
[
    {"이름": "김철수", "나이": 25, "직업": "개발자", "연봉": 4000},
    {"이름": "이영희", "나이": 30, "직업": "마케터", "연봉": 3500},
    {"이름": "박민수", "나이": 35, "직업": "디자이너", "연봉": 4200}
]
'''
df = pd.read_json(io.StringIO(data)) # 문자열 데이터를 실제 "텍스트 파일"처럼 작동하게 만들어주는 도구
print(df)

# 아래 샘플 데이터에서 한글과 공백을 제외한 모든 문자를 제거하고, 공백을 하나로 정리하는 코드를 작성하세요
text = "안녕하세요!!! 저는 AI 모델-입니다. 12345 데이터를   정리해 보겠습니다."
cleaned = re.sub(r'[^가-힣\s]', '', text)
cleaned = re.sub(r"\s+", " ", cleaned).strip()
print(cleaned)

# 주어진 텍스트 데이터를 문장 단위로 분리한 후, 각 문장의 단어 개수를 데이터프레임으로 변환하는 코드를 작성하세요.
text = "자연어 처리는 재미있다. 파이썬과 pandas를 활용하면 편리하다. 데이터 분석은 흥미롭다."
sentences = [s.strip() for s in text.split(".") if s.strip()]
print(sentences)
df_sentences = pd.DataFrame({
    "문장": sentences,
    "단어수": [len(s.split()) for s in sentences]
})
print(df_sentences)


print("\n8===============================================================\n")
#%%
# matplotlib을 활용하여 5개의 카테고리와 각각의 값이 포함된 기본 세로 막대 그래프를 생성하는 코드를 작성하세요.
categories = ["A", "B", "C", "D", "E"]
values = [12, 25, 18, 30, 22]

plt.rc("font", family="Malgun Gothic")
plt.bar(categories, values)
plt.title("기본 세로 막대 그래프")
plt.xlabel("카테고리")
plt.ylabel("값")
plt.show()

# 누적형 막대 그래프를 생성하여, 두 개의 연도별 데이터를 각각 다른 색상으로 누적하여 표현하는 코드를 작성하세요.
categories = ["A", "B", "C", "D", "E"]
values_2023 = [10, 15, 20, 25, 30]
values_2024 = [5, 10, 12, 18, 22]

plt.bar(categories, values_2023, label="2023")
plt.bar(categories, values_2024, bottom=values_2023, label="2024")
plt.title("누적형 막대 그래프")
plt.xlabel("카테고리")
plt.ylabel("값")
plt.legend()
plt.show()

# 한 기업의 부서별 연간 성과(2023년 vs 2024년)를 비교하는 그룹형 막대 그래프를 생성하는 코드를 작성하세요.
departments = ["Sales", "Marketing", "IT", "HR", "Finance"]
performance_2023 = [80, 70, 90, 60, 75]
performance_2024 = [85, 75, 95, 65, 80]

x = np.arange(len(departments))
width = 0.4
plt.bar(x - width / 2, performance_2023, width, label="2023")
plt.bar(x + width / 2, performance_2024, width, label="2024")
plt.title("부서별 연간 성과 비교")
plt.xticks(x, departments)
plt.xlabel("부서")
plt.ylabel("성과")
plt.legend()
plt.show()


print("\n10===============================================================\n")


# 정규 분포를 따르는 1000개의 데이터를 생성한 후, 구간을 15개로 설정한 히스토그램을 그리는 코드를 작성하세요.
data = np.random.randn(1000)

plt.hist(data, bins=15, edgecolor="black")
plt.title("Basic Histogram")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()

# 두 개의 서로 다른 정규 분포를 따르는 데이터셋을 생성한 후, 두 히스토그램을 같은 그래프에서 겹쳐서 비교하는 코드를 작성하세요.
# 첫 번째 데이터셋 (평균 0, 표준편차 1)
data1 = np.random.randn(1000)
# 두 번째 데이터셋 (평균 3, 표준편차 1)
data2 = np.random.randn(1000) + 3

plt.hist(data1, bins=30, alpha=0.5, label="data1", edgecolor="black")
plt.hist(data2, bins=30, alpha=0.5, label="data2", edgecolor="black")
plt.title("Histogram Comparison of Two Group")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# 한 데이터셋의 **누적 히스토그램**을 그린 후, X축과 Y축의 적절한 레이블을 설정하는 코드를 작성하세요.
# 정규 분포를 따르는 1000개의 데이터 생성
data = np.random.randn(1000)

plt.hist(data, bins=30, cumulative=True)
plt.title("Cumulative Histogram")
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()


print("\n12===============================================================\n")


# 두 개의 리스트 `x = [1, 2, 3, 4, 5]`, `y = [3, 1, 4, 5, 2]`를 사용하여 **산점도를 그리고, X축과 Y축의 라벨을 추가하는 코드**를 작성하세요.
# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [3, 1, 4, 5, 2]

plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Scatter Plot")
plt.show()

# numpy를 활용하여 **난수를 생성한 후, 산점도를 그리고 점의 색상과 투명도를 설정하는 코드**를 작성하세요.
# 난수 데이터 생성
np.random.seed(42)
x = np.random.rand(50) * 10  # 0~10 범위의 난수 50개
y = np.random.rand(50) * 10  # 0~10 범위의 난수 50개

plt.scatter(x, y, color="green", alpha=0.1)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Random Scatter Plot")
plt.show()

#numpy를 활용하여 **세 개의 그룹("A", "B", "C")에 속하는 데이터의 산점도를 서로 다른 색상으로 그리는 코드**를 작성하세요.
# 데이터 생성
np.random.seed(10)
x = np.random.randn(50) * 2
y = np.random.randn(50) * 2
categories = np.random.choice(["A", "B", "C"], size=50)

color_dict = {"A": "green", "B": "red", "C": "blue"}
for group in ["A", "B", "C"]:
    mask = categories == group
    plt.scatter(x[mask], y[mask], color=color_dict[group], label=group)
plt.title("Scatter Plot by Category")
plt.legend()
plt.show()


print("\n14===============================================================\n")

#%%
# 평균 0, 표준편차 1을 따르는 정규분포 난수 50개를 생성한 후, 해당 데이터를 이용해 기본 박스 플롯을 출력하는 코드를 작성하세요
# 정규분포를 따르는 난수 50개 생성
np.random.seed(42)
data = np.random.randn(50)

plt.boxplot(data)
plt.title("Basic Box Plot")
plt.show()

# 세 개의 그룹(Group A, Group B, Group C) 에 대해 각각 다른 평균을 가지는 데이터를 생성하고, 이를 이용해 다중 박스 플롯을 그리는 코드를 작성하세요.
# 랜덤 데이터 생성 (각 그룹별 평균 다르게 설정)
np.random.seed(42)
group_a = np.random.randn(50) * 1.5  # 표준편차 1.5, 평균 0
group_b = np.random.randn(50) * 1.5 + 3  # 표준편차 1.5, 평균 3
group_c = np.random.randn(50) * 1.5 - 3  # 표준편차 1.5, 평균 -3

plt.boxplot([group_a, group_b, group_c], tick_labels=["Group A", "Group B", "Group C"])
plt.title("Box Plot of Multiple Groups")
plt.show()

# 평균이 **서로 다른 두 개의 그룹(Group X, Group Y)** 을 비교하는 박스 플롯을 그리세요. 단, **이상값을 강조하고, 스타일을 커스터마이징**해야 합니다.

# 랜덤 데이터 생성 (두 그룹의 평균 다르게 설정)
np.random.seed(42)
group_x = np.random.randn(50) * 2  # 표준편차 2, 평균 0
group_y = np.random.randn(50) * 2 + 5  # 표준편차 2, 평균 5

plt.boxplot(
    [group_x, group_y],
    labels=["Group X", "Group Y"],
    flierprops=dict(marker="o", markerfacecolor="red", markersize=8),
    medianprops=dict(color="orange", linewidth=2),
    boxprops=dict(color="blue"),
    whiskerprops=dict(color="blue", linestyle="--"),
)
plt.title("Box Plot with Outliers Highlighted")
plt.show()


print("\n16===============================================================\n")

# plt.subplots()를 사용하여 2x1 형태의 서브플롯을 만들고, 첫 번째 서브플롯에는 y = x^2, 두 번째 서브플롯에는 y = x^3을 그리는 코드를 작성하세요.
# 데이터 생성
x = np.linspace(-5, 5, 100)
y1 = x ** 2  # x의 제곱
y2 = x ** 3  # x의 세제곱

# X축을 공유하는 1행 2열 형태의 서브플롯을 생성하고, 첫 번째 서브플롯에는 정규 분포를 따르는 난수의 히스토그램, 두 번째 서브플롯에는 균등 분포를 따르는 난수의 히스토그램을 그리세요.
# 데이터 생성
normal_data = np.random.randn(1000)  # 정규 분포 난수 1000개
uniform_data = np.random.rand(1000)  # 균등 분포 난수 1000개

# gridspec을 사용하여 불규칙한 레이아웃의 서브플롯을 생성하고, 각각 선 그래프, 산점도, 막대 그래프, 히스토그램을 그리세요.
# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.random.randn(100)
categories = ["A", "B", "C", "D", "E"]
values = [3, 7, 5, 2, 8]


print("\n18===============================================================\n")
# 두 개의 과일 집합을 정의하고, 두 집합의 차집합(한 집합에만 존재하는 요소)을 출력하는 코드를 작성하세요.
# 두 개의 과일 집합 정의
set_A = {"사과", "바나나", "체리", "망고"}
set_B = {"바나나", "망고", "포도", "수박"}
print(set_A - set_B)

#벤 다이어그램을 그리지 않고, 세 개의 집합을 비교하여 각 집합이 단독으로 가지는 요소 개수와 교집합 개수를 계산하는 코드를 작성하세요.
# 세 개의 과일 집합 정의
set_A = {"사과", "바나나", "체리", "망고"}
set_B = {"바나나", "망고", "포도", "수박"}
set_C = {"망고", "수박", "딸기", "오렌지"}

print(len(set_A - set_B - set_C))
print(len(set_B - set_A - set_C))
print(len(set_C - set_A - set_B))

print(len(set_A & set_B))
print(len(set_B & set_C))
print(len(set_C & set_A))
print(len(set_A & set_B & set_C))


# 벤 다이어그램을 그리면서, 특정 조건을 만족하는 경우 색상을 다르게 지정하는 코드를 작성하세요 
# 조건: 두 개의 집합을 비교할 때, 교집합이 2개 이상이면 노란색, 그렇지 않으면 기본 색상을 사용하세요.
# 두 개의 집합 정의
set_A = {"사과", "바나나", "체리", "망고"}
set_B = {"바나나", "망고", "포도", "수박"}

if len(set_A & set_B) >= 2:
    venn2([set_A, set_B], set_labels=("Set A", "Set B"), set_colors=("yellow", "yellow"))
else:
    venn2([set_A, set_B], set_labels=("Set A", "Set B"))

("\n21===============================================================\n")

# 샘플 데이터를 직접 생성한 후 Seaborn을 활용하여 막대 그래프(bar plot)를 생성하는 코드를 작성하세요.
# 샘플 데이터 생성
plt.rc('font', family='Malgun Gothic')
data = pd.DataFrame({
    "카테고리": ["X", "X", "Y", "Y", "Z", "Z", "Z", "X", "Y", "Z"],
    "값": [5, 9, 4, 6, 12, 10, 14, 7, 5, 18]
})
sns.barplot(x="카테고리", y="값", data=data)
plt.title("Basic Categorical Bar Plot")
plt.show()

# Seaborn의 sns.boxplot()을 활용하여 범주형 데이터의 분포를 시각화하는 코드를 작성하세요.
# 샘플 데이터 생성
data = pd.DataFrame({
    "group": ["A", "A", "B", "B", "C", "C", "C", "A", "B", "C"],
    "score": [65, 70, 55, 60, 90, 85, 95, 72, 58, 88]
})

sns.boxplot(x="group", y="score", data=data)
plt.title("Box Plot for Categorical Data")
plt.show()

# Seaborn의 sns.violinplot()과 sns.stripplot()을 함께 사용하여 범주형 데이터의 분포를 더욱 자세히 시각화하는 코드를 작성하세요.
# 샘플 데이터 생성
data = pd.DataFrame({
    "category": ["A", "A", "B", "B", "C", "C", "C", "A", "B", "C"],
    "score": [80, 85, 70, 75, 95, 90, 100, 82, 72, 98]
})
sns.violinplot(x="category", y="score", data=data)
sns.stripplot(x="category", y="score", data=data, jitter=True) 
plt.title("Violin Plot & Strip Plot for Categorical Data")
plt.show()


print("\n23===============================================================\n")
# 평균 0, 표준편차 1을 따르는 정규 분포 데이터를 500개 생성한 후, 히스토그램과 KDE를 함께 시각화하는 코드를 작성하세요.
# 정규 분포를 따르는 데이터 생성
np.random.seed(42)
data = np.random.randn(500)

plt.figure(figsize=(8, 6))
sns.histplot(data, bins=30, kde=True, color='darkorange')
plt.xlabel("Value")
plt.ylabel("Density / Frequency")
plt.title("Histogram with KDE")
plt.show()

# 0부터 20까지 균등한 간격으로 생성된 데이터를 사용하여, 사인 함수의 선 그래프를 그리는 코드를 작성하세요.
# X 값 생성 (0부터 20까지 100개의 균등한 값)
x = np.linspace(0, 20, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
sns.lineplot(x=x, y=y, color='royalblue')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot Example")
plt.show()

# 랜덤한 100개의 연속형 데이터를 생성하여, 산점도와 회귀선을 포함한 그래프를 그리는 코드를 작성하세요.
# 난수 생성 (재현 가능성 유지)
np.random.seed(0)
x = np.random.rand(100) * 10  # 0~10 사이 난수
y = 2 * x + np.random.randn(100)  # x와 비례하는 관계, 약간의 변동 추가

plt.figure(figsize=(8, 6))
sns.regplot(x=x, y=y, color='green')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Regression Line")
plt.show()


print("\n25===============================================================\n")
# Seaborn의 `scatterplot`을 활용하여 "총 결제 금액"(`total_bill`)과 "팁"(`tip`)의 관계를 시각화하는 코드를 작성하세요.
# 단, `scatterplot`의 색상과 스타일을 다르게 설정하여 출력해야 합니다.
# 예제 데이터 로드 (Seaborn 내장 데이터셋: tips)
tips = sns.load_dataset("tips")
print(tips)

plt.figure(figsize=(8, 6))
sns.scatterplot(x="total_bill", y="tip", data=tips, color="blue")
plt.title("Scatter Plot: Total Bill vs. Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# `sns.regplot`을 사용하여 "총 결제 금액"(`total_bill`)과 "팁"(`tip`)의 관계를 나타내는 회귀선 그래프를 그리고, 산점도의 투명도를 조정하는 코드를 작성하세요.
# 단, 산점도에서 특정 성별(`sex`)만 필터링하여 표시해야 합니다
# 예제 데이터 로드
tips = sns.load_dataset("tips")

male_tips = tips[tips['sex'] == 'Male']
plt.figure(figsize=(8, 6))
sns.regplot(x="total_bill", y="tip", data=tips, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title("Regression Line: Total Bill vs. Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# `sns.pairplot`을 사용하여 다중 변수(`total_bill`, `tip`, `size`) 간의 관계를 성별(`sex`)과 요일(`day`)에 따라 시각화하는 코드를 작성하세요.
# 단, 요일(`day`)에 따라 다른 색상을 적용해야 합니다.
# 예제 데이터 로드
tips = sns.load_dataset("tips")

sns.pairplot(tips, vars=["total_bill", "tip", "size"], hue="day", palette="coolwarm")
plt.show()


print("\n27===============================================================\n")
# %%
# 100일간의 시계열 데이터를 생성하고, 이를 선 그래프로 시각화하는 코드를 작성하세요.
# 시계열 데이터 생성
np.random.seed(42)
date_range = pd.date_range(start="2023-01-01", periods=100, freq="D")  # 100일간의 날짜 생성
values = np.cumsum(np.random.randn(100))  # 랜덤 값의 누적합

df = pd.DataFrame({"Date": date_range, "Value": values})
plt.figure(figsize=(8, 6))  # 그래프 크기 설정
sns.lineplot(x="Date", y="Value", data=df, color="blue", marker="o")  # 시계열 선 그래프
plt.xlabel("Date")  # X축 라벨 설정
plt.ylabel("Value")  # Y축 라벨 설정
plt.title("Time Series Line Plot")  # 그래프 제목 설정
plt.xticks(rotation=45)  # X축 눈금 회전
plt.show()  # 그래프 출력


# 1번 퀘스트에서 생성한 데이터를 기반으로 7일 이동 평균을 계산하고, 원본 데이터와 함께 그래프로 비교하는 코드를 작성하세요.
# 시계열 데이터 생성
df["Moving_Avg"] = df["Value"].rolling(window=7).mean()
plt.figure(figsize=(8, 6))
sns.lineplot(x="Date", y="Value", data=df, label="Original Data", color="gray")
sns.lineplot(x="Date", y="Moving_Avg", data=df, label="7-Day Moving Average", color="red") 
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Time Series with Moving Average")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# 1번 퀘스트에서 생성한 시계열 데이터에서 이상치를 탐지하고, 이상치만 강조하여 그래프에 표시하는 코드를 작성하세요.
# 이상치는 사분위수 범위(IQR)를 이용해 판단합니다.
# 시계열 데이터 생성
Q1 = df["Value"].quantile(0.25)
Q3 = df["Value"].quantile(0.75)
IQR = Q3 - Q1
k = 0.5
lower_bound = Q1 - k * IQR  # 하한선
upper_bound = Q3 + k * IQR  # 상한선
df["Outlier"] = (df["Value"] < lower_bound) | (df["Value"] > upper_bound)
outliers = df[df["Outlier"]]
plt.figure(figsize=(8, 6))
sns.lineplot(x="Date", y="Value", data=df, label="Original Data", color="blue")
sns.scatterplot(x="Date", y="Value", data=outliers, color="red", label="Outliers", s=100)
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Time Series with Outlier Detection")
plt.legend()
plt.xticks(rotation=45)
plt.show()


print("\n29===============================================================\n")
# pandas를 사용하여 3시간 간격의 시계열 데이터를 생성한 후, 하루 단위(D)로 평균을 구하는 다운샘플링을 수행하는 코드를 작성하세요.
# 3시간 간격의 시계열 데이터 생성 (2024년 1월 1일부터 5일까지)
date_rng = pd.date_range(start="2024-01-01", end="2024-01-05", freq="3h")

df = pd.DataFrame({
    "datetime": date_rng,
    "value": np.random.randint(10, 100, size=len(date_rng))  # 10~100 사이 랜덤 값
})
df.set_index("datetime", inplace=True)
df_resampled = df.resample('D').mean()
print(df_resampled)

# 3시간 간격으로 생성된 시계열 데이터에서 1시간 단위로 업샘플링한 후, 선형 보간(linear)을 적용하는 코드를 작성하세요.
# 3시간 간격의 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-03", freq="3h")

df_hourly = df.resample("h").asfreq() 
print(df_hourly.head().reset_index())
df_hourly_interp = df_hourly.interpolate(method="linear") 
print(df_hourly_interp.head().reset_index())

print("\n31===============================================================\n")
# 주어진 시계열 데이터에서 7일 단순 이동평균(SMA) 을 계산하여 새로운 컬럼을 추가하는 코드를 작성하세요.
# 샘플 시계열 데이터 생성
date_rng = pd.date_range(start="2024-01-01", end="2024-01-20", freq="D")
df = pd.DataFrame({
    "datetime": date_rng,
    "value": np.random.randint(50, 150, size=len(date_rng))
})
df.set_index("datetime", inplace=True)
df["SMA_7"] = df["value"].rolling(window=7).mean()

# 시계열 데이터에서 7일 지수 이동평균(EMA) 을 계산하고, 기존 데이터와 비교하여 출력하는 코드를 작성하세요.
df["EMA_7"] = df["value"].ewm(span=7, adjust=False).mean()
print(df.reset_index())

# 주어진 시계열 데이터에서 **이동평균을 활용하여 변동성이 큰 날을 탐색하는 코드**를 작성하세요.
# 7일 단순 이동평균(SMA)과 비교하여 특정 일자의 값이 이동평균보다 ±20% 이상 차이가 나는 경우만 출력하세요.
print(df[abs(df["value"] - df["SMA_7"]) / df["SMA_7"] >= 0.2].dropna(subset=["SMA_7"]))

print("\n33===============================================================\n")
# 샘플 금융 데이터프레임을 직접 생성한 후, 데이터의 기본 정보(행 개수, 열 개수, 데이터 타입 등)를 출력하는 코드를 작성하세요.
# 샘플 금융 데이터 생성
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Open': [100, 102, 105, 103, 108, 107, 110, 112, 115, 118],
    'High': [102, 106, 108, 107, 110, 109, 112, 115, 117, 120],
    'Low': [98, 100, 103, 101, 106, 105, 108, 110, 113, 116],
    'Close': [101, 104, 106, 105, 109, 108, 111, 113, 116, 119],
    'Volume': [1000, 1200, 1500, 1300, 1600, 1400, 1700, 1800, 1900, 2000]
}
df = pd.DataFrame(data)
# print(df.info())

# 주어진 df 데이터프레임에서 5일 이동평균(SMA)과 5일 지수 이동평균(EMA)을 계산하는 코드를 작성하세요.
# 샘플 금융 데이터 생성
data = {
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Close': [101, 104, 106, 105, 109, 108, 111, 113, 116, 119]
}

df["SMA_5"] = df["Close"].rolling(window=5).mean()
df["EMA_5"] = df["Close"].ewm(span=5, adjust=False).mean()
# print(df.reset_index())

# df 데이터프레임에서 주간(7일) 단위로 종가(Close) 평균을 리샘플링한 후, 이를 바탕으로 주간 변동성(표준편차)을 계산하는 코드를 작성하세요.
# 샘플 금융 데이터 생성 (30일치)
date_rng = pd.date_range(start='2024-01-01', periods=30, freq='D')
close_prices = np.random.uniform(100, 200, size=len(date_rng))  # 100~200 사이의 랜덤 종가 생성
df = pd.DataFrame({'Date': date_rng, 'Close': close_prices})

df.set_index('Date', inplace=True)
weekly_summary = df['Close'].resample('7D').agg(['mean', 'std'])
print(weekly_summary.reset_index())

print("\n36===============================================================\n")
# 평균 60, 표준 편차 15를 갖는 정규 분포에서 500개의 데이터를 생성한 후, 데이터의 기본 통계 정보(평균, 표준 편차, 최소값, 최대값)를 출력하는 코드를 작성하세요.
# 평균 60, 표준 편차 15인 정규 분포에서 500개의 난수 생성
data = np.random.normal(loc=60, scale=15, size=500)
print(f"평균: {np.mean(data):.2f}, 표준편차: {np.std(data):.2f}, 최소: {np.min(data):.2f}, 최대: {np.max(data):.2f}")

# 평균 50, 표준 편차 10을 갖는 정규 분포에서 특정 값 x=65의 확률 밀도 함수(PDF) 값을 계산하고 출력하는 코드를 작성하세요.
print(stats.norm.pdf(65, loc=50, scale=10))

# 평균 70, 표준 편차 8을 갖는 정규 분포에서 (1) 특정 값 x=80 이하일 확률을 CDF로 계산하고, (2) 상위 5%에 해당하는 점수를 PPF로 계산하여 출력하는 코드를 작성하세요.
print(stats.norm.cdf(80, loc=70, scale=8))
print(stats.norm.ppf(0.95, loc=70, scale=8))


print("\n38===============================================================\n")
# 주어진 데이터에서 평균과 중앙값의 차이를 계산하는 코드를 작성하세요.
# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # 평균 50, 표준편차 10인 정규 분포 데이터 생성
df = pd.DataFrame(data, columns=["value"])  # 데이터프레임 생성

print(df["value"].mean() - df["value"].median())

# **데이터에서 이상값(Outlier)을 찾아 제거한 후, 원래 데이터와 이상값 제거 후 데이터의 평균을 비교하는 코드**를 작성하세요.
# 이상값은 **IQR(사분위 범위)를 사용하여 탐지**하세요
# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # 평균 50, 표준편차 10인 정규 분포 데이터 생성
df = pd.DataFrame(data, columns=["value"])  # 데이터프레임 생성

q1 = np.percentile(df["value"], 25)
q3 = np.percentile(df["value"], 75)
iqr = q3 - q1
df_clean = df[(df["value"] >= q1 - 1.5 * iqr) & (df["value"] <= q3 + 1.5 * iqr)]
print(df['value'].mean(), df_clean['value'].mean())

# 데이터의 왜도(Skewness)와 첨도(Kurtosis)를 계산하여 데이터의 분포 특성을 분석하는 코드를 작성하세요.
# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(loc=50, scale=10, size=100)  # 평균 50, 표준편차 10인 정규 분포 데이터 생성
df = pd.DataFrame(data, columns=["value"])  # 데이터프레임 생성
print(df['value'].skew(), df['value'].kurt())


print("\n40===============================================================\n")
# **단일 표본 t-검정(One-Sample t-test)** 을 수행하여 샘플 데이터의 평균이 특정 값과 유의미한 차이가 있는지 검정하는 코드를 작성하세요.
# (평균 `50`, 표준 편차 `5`를 따르는 정규 분포에서 30개의 데이터를 생성하고, 해당 데이터가 평균 `52`와 차이가 있는지 확인하세요.)
# 샘플 데이터 생성
np.random.seed(42)
sample_data = np.random.normal(loc=50, scale=5, size=30)  # 평균 50, 표준편차 5인 데이터 30개 생성

t_stat, p_value = stats.ttest_1samp(sample_data, popmean=52)
print(t_stat, p_value)

# 카이제곱 검정(Chi-Square Test) 을 수행하여 관측된 데이터와 기대값이 유의미한 차이가 있는지 확인하는 코드를 작성하세요.
# 관측된 데이터 (Observed)
observed = np.array([50, 60, 90])
# 기대값 (Expected)
expected = np.array([66, 66, 66]) * (observed.sum() / np.sum([66, 66, 66]))

chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
print(chi2_stat, p_value)

# 분산 분석(ANOVA, Analysis of Variance) 을 수행하여 여러 그룹의 평균이 서로 다른지 검정하는 코드를 작성하세요
# 샘플 데이터 생성
np.random.seed(42)
group_1 = np.random.normal(loc=50, scale=10, size=30)  # 평균 50, 표준편차 10
group_2 = np.random.normal(loc=55, scale=10, size=30)  # 평균 55, 표준편차 10
group_3 = np.random.normal(loc=60, scale=10, size=30)  # 평균 60, 표준편차 10

f_stat, p_value = stats.f_oneway(group_1, group_2, group_3)
print(f_stat, p_value)


print("\n42===============================================================\n")
# %%
# NumPy를 사용하여 평균 70, 표준편차 20을 따르는 정규 분포 데이터 1000개를 생성한 후, Matplotlib을 활용하여 박스플롯을 그리는 코드를 작성하세요.
# 데이터 생성 (평균=70, 표준편차=20인 정규 분포 데이터 1000개)
np.random.seed(42)
data = np.random.normal(loc=70, scale=20, size=1000)

df = pd.DataFrame(data, columns=["value"])

plt.figure(figsize=(8, 6))
plt.boxplot(df["value"], vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.title("Boxplot of Data Distribution")
plt.xlabel("Value")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

# 평균이 각각 55와 60이고, 표준편차가 8인 두 개의 그룹(A, B) 데이터를 생성한 후, **두 그룹의 데이터 분포를 Seaborn을 활용하여 KDE(커널 밀도 함수)와 함께 히스토그램으로 시각화**하세요.
# 이후, **두 그룹 간 평균 차이가 유의미한지 t-검정을 수행하는 코드**를 작성하세요.
# 데이터 생성
np.random.seed(42)
group_A = np.random.normal(loc=55, scale=8, size=200)  # 평균 55, 표준편차 8
group_B = np.random.normal(loc=60, scale=8, size=200)  # 평균 60, 표준편차 8

df_A = pd.DataFrame(group_A, columns=["value"])
df_B = pd.DataFrame(group_B, columns=["value"])

plt.figure(figsize=(8, 6))
sns.histplot(df_A["value"], bins=30, kde=True, color="skyblue", alpha=0.7)
sns.histplot(df_B["value"], bins=30, kde=True, color="orange", alpha=0.7)
plt.title("Histogram with KDE")  
plt.xlabel("Value")
plt.ylabel("Density")

t_stat, p_value = stats.ttest_ind(group_A, group_B)
print(t_stat, p_value)

# 광고 A를 본 500명 중 120명이 클릭하였고, 광고 B를 본 500명 중 150명이 클릭을 한 데이터가 있습니다.
# 이 데이터를 바탕으로 **카이제곱 검정을 수행하여 광고 A와 B의 클릭률 차이가 유의미한지 분석하고, Seaborn의 barplot을 사용하여 클릭률을 비교하는 그래프를 그리는 코드**를 작성하세요.
# 데이터 생성 (광고 A와 B의 클릭 여부)
observed_data = pd.DataFrame({
    "Ad_A": [120, 380],  # 광고 A 클릭(120명) vs 미클릭(380명)
    "Ad_B": [150, 350]   # 광고 B 클릭(150명) vs 미클릭(350명)
}, index=["Click", "No Click"])

chi2_stat, p_value, dof, _ = stats.chi2_contingency(observed_data)
print(chi2_stat, p_value, dof)

plt.figure(figsize=(6, 5))
sns.barplot(x=observed_data.columns, y=observed_data.loc["Click"], hue=observed_data.columns, palette=["lightblue", "lightcoral"])
plt.title("Ad A vs. Ad B - Click Rate")
plt.xlabel("Advertisement Group")
plt.ylabel("Number of Clicks")
plt.show()


print("\n[시계열 데이터 시각화]=============================================\n")
# !pip install yfinance
import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOGL"]
raw = yf.download(tickers, period="1y", auto_adjust=True, progress=False, threads=False)
df_close = raw["Close"].dropna()

# 1) 종가 선 그래프 (matplotlib)
plt.figure(figsize=(12, 5))
for col in df_close.columns:
    plt.plot(df_close.index, df_close[col], label=col)
plt.title("Stock Closing Prices (1 Year)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2) AAPL 종가 + 20일/60일 이동평균 (seaborn lineplot)
aapl = df_close[["AAPL"]].copy()
aapl["SMA_20"] = aapl["AAPL"].rolling(20).mean()
aapl["SMA_60"] = aapl["AAPL"].rolling(60).mean()
aapl = aapl.reset_index()

plt.figure(figsize=(12, 5))
sns.lineplot(data=aapl, x="Date", y="AAPL",   label="Close",  color="gray",  alpha=0.7)
sns.lineplot(data=aapl, x="Date", y="SMA_20", label="SMA 20", color="blue")
sns.lineplot(data=aapl, x="Date", y="SMA_60", label="SMA 60", color="red")
plt.title("AAPL Close Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
