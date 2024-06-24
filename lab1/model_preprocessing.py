import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Загрузка данных
train_data = pd.read_csv('data/train/train_data.csv')
test_data = pd.read_csv('data/test/test_data.csv')

# Предобработка данных
scaler = StandardScaler()
train_data_scaled = scaler.fit_transform(train_data)
test_data_scaled = scaler.transform(test_data)

# Создание папок, если они не существуют
os.makedirs('data/train', exist_ok=True)
os.makedirs('data/test', exist_ok=True)

# Сохранение предобработанных данных
pd.DataFrame(train_data_scaled, columns=train_data.columns).to_csv('data/train/train_data_scaled.csv', index=False)
pd.DataFrame(test_data_scaled, columns=test_data.columns).to_csv('data/test/test_data_scaled.csv', index=False)
