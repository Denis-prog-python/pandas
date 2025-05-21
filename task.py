import pandas as pd

# Загружаем данные из CSV файла в DataFrame
df = pd.read_csv('IEA-EV-dataEV salesHistoricalCars.csv')

# Выведем первые 5 строк набора данных
print("Первые 5 строк:")
print(df.head())

# Получение общей информации о датасете
print("\nИнформация о данных:")
print(df.info())

# Статистическое описание числовых столбцов
print("\nСтатистика по данным:")
print(df.describe())