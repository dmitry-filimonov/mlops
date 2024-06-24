import numpy as np
import pandas as pd
import os

# Создание папок для данных
os.makedirs('data/train', exist_ok=True)
os.makedirs('data/test', exist_ok=True)

# Функция для создания набора данных
def create_dataset(num_samples, num_features, noise=False):
    data = np.random.randn(num_samples, num_features)
    if noise:
        data += np.random.normal(0, 0.5, data.shape)
    return pd.DataFrame(data, columns=[f'feature_{i}' for i in range(num_features)])

# Создание тренировочных и тестовых данных
train_data = create_dataset(1000, 10)
test_data = create_dataset(500, 10, noise=True)

# Сохранение данных в соответствующие папки
train_data.to_csv('data/train/train_data.csv', index=False)
test_data.to_csv('data/test/test_data.csv', index=False)
