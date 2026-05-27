import numpy as np

# 다음 NumPy 배열의 차원 수를 출력하는 코드를 작성하세요.
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array.ndim)

# 1차원 배열 [10, 20, 30, 40, 50, 60]을 2차원 배열로 변환하여 (2, 3) 형태로 출력하는 코드를 작성하세요.
array = np.array([10, 20, 30, 40, 50, 60])
print(array.reshape(2, 3))


# 다음 1차원 배열에 새로운 차원을 추가하여 2차원 배열로 변환하고, 최종 배열의 차원 수를 출력하세요. newaxis를 사용하여 배열의 차원을 추가하고, 새로운 차원에서의 배열 모양을 확인한 후 최종 차원 수를 출력하세요.
array = np.array([7, 14, 21])
print(array[:, np.newaxis])
print(array.shape, "->", array[:, np.newaxis].shape)
print(array[:, np.newaxis].ndim)

print()
print("===================================================================")
print()

# 주어진 2차원 NumPy 배열의 형태(Shape)를 출력하는 코드를 작성하세요.
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array.shape)

# 1차원 배열 [10, 20, 30, 40, 50, 60]을 (2, 3) 형태로 변경한 후, 새로운 배열의 형태를 출력하는 코드를 작성하세요.
array = np.array([10, 20, 30, 40, 50, 60])
print(array.reshape(2, 3).shape)

# 다음 3차원 배열의 형태를 변경하여 (3, 2, 2) 형태로 조정하고, 최종 배열의 형태를 출력하는 코드를 작성하세요.
array = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
print(array.shape)
print(array.reshape(3, 2, 2)) # 원래 3, 2, 2인데??
print(array.reshape(3, 2, 2).shape)

print()
print("===================================================================")
print()

# 아래의 NumPy 배열의 데이터 타입을 확인하는 코드를 작성하세요.
array = np.array([10, 20, 30])
print(array.dtype)

# 정수형 배열 [1, 2, 3]을 부동소수점형 배열로 변환하고, 변환된 배열의 데이터 타입을 출력하는 코드를 작성하세요.
array = np.array([1, 2, 3])
#print(array.astype(np.float64))
print(array.astype(np.float64).dtype)

# NumPy 배열 [100, 200, 300]을 uint8로 변환한 후, 메모리 사용량(바이트)을 출력하는 코드를 작성하세요.
array = np.array([100, 200, 300])
# print(array.astype(np.float64).itemsize)
print(array.astype(np.float64).nbytes)

print()
print("===================================================================")
print()

# 주어진 1차원 배열에서 첫 번째 요소와 마지막 요소를 출력하는 코드를 작성하세요.
array = np.array([10, 20, 30, 40, 50])
print(array[0], array[-1])

# 주어진 2차원 배열에서 첫 번째 열과 두 번째 행을 출력하는 코드를 작성하세요.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix[:, 0])

# 주어진 배열에서 10보다 큰 요소들만 선택하고, 해당 요소들의 인덱스를 출력하는 코드를 작성하세요.
array = np.array([5, 15, 8, 20, 3, 12])
print(np.where(array > 10))
print(np.where(array > 10)[0])

print()
print("===================================================================")
print()

# 주어진 NumPy 배열에서 요소별(Element-wise) 덧셈을 수행하는 코드를 작성하세요.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)

# 다음 NumPy 배열에서 브로드캐스팅을 활용하여 각 행에 [1, 2, 3]을 더하는 코드를 작성하세요.
matrix = np.array([[10, 20, 30], [40, 50, 60]])
vector = np.array([1, 2, 3])
print(matrix + vector)

# 주어진 2차원 NumPy 배열에 대해, 축(axis)을 기준으로 최댓값을 구하고 최종 배열의 차원을 출력하는 코드를 작성하세요.
array = np.array([[3, 7, 2], [8, 4, 6]])
max_axis0 = np.max(array, axis=0) # 행(axis=0)의 인덱스를 바꿔가며 연산을 수행하라 == 해당 axis를 축소(제거)하라
print(max_axis0, max_axis0.ndim)
max_axis1 = np.max(array, axis=1)
print(max_axis1, max_axis1.ndim)

print()
print("===================================================================")
print()

# 배열 [1, 2, 3, 4]에 대해 NumPy의 유니버설 함수를 사용하여 모든 요소를 제곱한 결과를 출력하는 코드를 작성하세요. 
a = np.array([1, 2, 3, 4])
print(np.multiply(a, a))

# 다음 두 배열의 요소별 합을 계산하고, 결과를 새로운 배열이 아닌 기존 배열에 저장하는 코드를 작성하세요.
array1 = np.array([10, 20, 30])
array2 = np.array([1, 2, 3])
array1 += array2
print(array1)

# 다음 배열에 대해 NumPy 유니버설 함수를 사용하여 요소별로 자연로그(log)를 계산하고, 특정 조건(log 값 > 1)을 만족하는 요소만 출력하는 코드를 작성하세요.
array = np.array([1, np.e, 10, 100])
log_arr = np.log(array)
print(log_arr)
print(log_arr[log_arr > 1])