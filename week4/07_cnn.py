from pathlib import Path
import matplotlib.pyplot as plt
import torch
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


# 7. CNN(Convolutional Neural Network)을 직접 구성하여 이미지 분류를 수행하세요.

SEED = 42
torch.manual_seed(SEED) # pytorch에서 random seed 고정

digits = load_digits() # digits dataset (1797, 8, 8)
X = digits.images / 16.0 # 정규화 (0 ~ 15) -> (0 ~ 1)
y = digits.target

# (배치크기, H, W) -> (배치크기, C=1 , H, W)
X_tensor = torch.tensor(X, dtype=torch.float32).unsqueeze(1) # 흑백
y_tensor = torch.tensor(y, dtype=torch.long)

X_train, X_test, y_train, y_test = train_test_split(
    X_tensor,
    y_tensor,
    test_size=0.25,
    stratify=y_tensor,
    random_state=SEED,
)

train_loader = DataLoader(
    TensorDataset(X_train, y_train),
    batch_size=64,
    shuffle=True,
)
test_loader = DataLoader(
    TensorDataset(X_test, y_test),
    batch_size=128,
)

class MyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=3, padding=1), # 입력 1 channel, feature map 8개 => (8, 8, 8)
            nn.ReLU(),
            nn.MaxPool2d(2), # 절반 축소 => (8, 4, 4)
            nn.Conv2d(8, 16, kernel_size=3, padding=1), # feature map 16개 => (16, 4, 4)
            nn.ReLU(),
            nn.MaxPool2d(2), # 절반 축소 => (16, 2, 2)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(16 * 2 * 2, 32),
            nn.ReLU(),
            nn.Linear(32, 10),
        )

    def forward(self, x):
        x = self.features(x)
        return self.classifier(x)


model = MyCNN()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

loss_history = []

for epoch in range(1, 11):
    model.train()
    epoch_loss = 0.0

    for batch_X, batch_y in train_loader:
        optimizer.zero_grad()
        logits = model(batch_X)
        loss = criterion(logits, batch_y)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item() * len(batch_X)

    avg_loss = epoch_loss / len(train_loader.dataset)
    loss_history.append(avg_loss)
    print(f"epoch {epoch} - loss: {avg_loss}")

model.eval()
preds = []
answers = []

with torch.no_grad():
    for batch_X, batch_y in test_loader:
        logits = model(batch_X)
        pred = logits.argmax(dim=1)
        preds.extend(pred.tolist())
        answers.extend(batch_y.tolist())

print(accuracy_score(answers, preds)) # 정확도

plt.figure(figsize=(7, 4))
plt.plot(range(1, len(loss_history) + 1), loss_history, marker="o")
plt.title("CNN Training Loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.grid(True, alpha=0.3)
plt.tight_layout()

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)
save_path = OUTPUT_DIR / "loss.png"
plt.savefig(save_path)
