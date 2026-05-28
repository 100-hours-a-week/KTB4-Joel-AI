# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# 1. Matplotlib으로 간단한 선 그래프 그리기
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 130, 180, 210]

plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker="o", color="royalblue")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()



# %%
# 2. Seaborn으로 DataFrame 기반 막대 그래프 그리기
score_data = {
    "student": ["Minji", "Jisoo", "Daniel", "Hana", "Leo"],
    "subject": ["Python", "Python", "Data", "Data", "Python"],
    "score": [95, 72, 88, 64, 81],
}

score_df = pd.DataFrame(score_data)

plt.figure(figsize=(8, 4))
sns.barplot(data=score_df, x="student", y="score", hue="subject")
plt.title("Student Scores")
plt.xlabel("Student")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
plt.close()


print("Saved seaborn_bar_chart.png")

# %%
