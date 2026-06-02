### Axis (operation)
- e.g., np.array([[3, 7, 2], [8, 4, 6]])
- np.max(array, axis=0) == [8 7 6]
- 행(axis=0)의 인덱스를 바꿔가며 연산을 수행하라
- 해당 axis를 축소(제거)하라

### 깨짐 문제
- 한글: plt.rc('font', family='Malgun Gothic')
- 음수기호: plt.rcParams['axes.unicode_minus'] = False

### Yfinance
- 시계열 데이터로 사용
- Yahoo Finance에서 제공하는 금융 데이터에 쉽게 접근할 수 있게 해주는 강력한 Python 패키지
- yf.download() 함수를 사용하면 별도의 변환 없이 자동으로 Pandas DataFrame 형태로 반환
- AAPL: 애플, MSFT: 마이크로소프트, GOOGL: 알파벳 


### 소감
 미니퀘스트마다 교재에 수록된 범주 내의 예제들로 구성되어 있어 난이도가 무난했고, 전반적인 내용을 따라가며 어떤 기능들이 있는지 가볍게 확인해 보기에 적절했습니다.실습을 진행하면서 직접 코드를 짜서 시각화하는 것보다, AI를 활용하는 것이 훨씬 더 정교하고 뛰어난 결과물을 훨씬 빠르게 만들어 줄 것 같다는 생각이 들었습니다. 앞으로의 데이터 시각화 작업에서 AI 기술의 활용 가치와 발전 방향에 대해 다시 한번 체감할 수 있었습니다.