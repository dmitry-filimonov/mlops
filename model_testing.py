import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

# Загрузка данных и модели
test_data = pd.read_csv('data/test/test_data_scaled.csv')
model = joblib.load('model/model.pkl')

# Разделение данных на признаки и целевую переменную
X_test = test_data.iloc[:, :-1]
y_test = (X_test.sum(axis=1) > 0).astype(int)  # Пример создания целевой переменной

# Предсказание и оценка модели
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
