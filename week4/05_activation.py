from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# 5. 활성화 함수를 직접 정의하고, 활성화 함수를 적용한 출력을 계산하고, 결과를 그래프로 시각화하세요.

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

def step(x):
    return np.where(x >= 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

x = np.linspace(-5, 5, 200)

functions = {
    "Step": step,
    "Sigmoid": sigmoid,
    "ReLU": relu,
    "Tanh": tanh,
}

for name, func in functions.items():
    print("====================", name, "====================")
    sample_x = np.array([-2, -1, 0, 1, 2])
    print(func(sample_x))

plt.figure(figsize=(10, 6))
for name, func in functions.items():
    plt.plot(x, func(x), label=name)

plt.title("Activation Functions")
plt.xlabel("x")
plt.ylabel("output")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

save_path = OUTPUT_DIR / "activation_functions.png"
plt.savefig(save_path)
