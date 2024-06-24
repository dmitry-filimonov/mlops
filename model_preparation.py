import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Создание папок, если они не существуют
os.makedirs('model', exist_ok=True)

# Загрузка данных
train_data = pd.read_csv('data/train/train_data_scaled.csv')

# Разделение данных на признаки и целевую переменную
X = train_data.iloc[:, :-1]  # Предполагаем, что последняя колонка - целевая переменная
y = (X.sum(axis=1) > 0).astype(int)  # Пример создания целевой переменной

# Создание и обучение модели
model = LogisticRegression()
model.fit(X, y)

# Сохранение модели
joblib.dump(model, 'model/model.pkl')
