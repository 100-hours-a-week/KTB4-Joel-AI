#%%
import io
import re
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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
# %%
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



print("\n21===============================================================\n")



print("\n23===============================================================\n")



print("\n25===============================================================\n")


print("\n27===============================================================\n")



print("\n29===============================================================\n")



print("\n31===============================================================\n")



print("\n33===============================================================\n")



print("\n36===============================================================\n")



print("\n38===============================================================\n")



print("\n40===============================================================\n")



print("\n42===============================================================\n")
# %%
