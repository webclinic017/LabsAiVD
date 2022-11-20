"""
Лабораторная работа №2 - работа с данными.
Данная ЛР включает в себя код для обработки csv файлов (в файле utils.py) и анализ данных,
содержащихся в них
"""

from utils import load_data

if __name__ == '__main__':
    # Загружаем предварительно обработанные данные
    etf = load_data()
    # Далее выводим статистику по ETF за последние полгода
    # В статистике указаны среднее значение, минимальное, максимальное и значения для положений цены по вероятностям
    print(etf[-120:].describe().to_string())