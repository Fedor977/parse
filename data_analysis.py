import pandas as pd
import matplotlib.pyplot as plt


def analyze_data(filename, category_name):
    # загрузка данных из Excel файла
    df = pd.read_excel(filename, sheet_name=category_name)

    # проверка наличия столбца 'Цена'
    if 'Цена' in df.columns:
        # расчет математического ожидания (среднего значения)
        mean_price = df['Цена'].mean()
        print(f"Математическое ожидание (средняя цена): {mean_price}")

        # расчет стандартного отклонения
        std_deviation = df['Цена'].std()
        print(f"Стандартное отклонение: {std_deviation}")

        # построение графика
        plt.figure(figsize=(10, 6))

        # гистограмма цен
        plt.hist(df['Цена'], bins=30, alpha=0.6, color='g', edgecolor='black', label='Цены')

        # вертикальные линии для математического ожидания и стандартного отклонения
        plt.axvline(mean_price, color='r', linestyle='dashed', linewidth=1,
                    label=f'Математическое ожидание ({mean_price:.2f})')
        plt.axvline(mean_price + std_deviation, color='b', linestyle='dashed', linewidth=1,
                    label=f'+1 Std. отклонение ({mean_price + std_deviation:.2f})')
        plt.axvline(mean_price - std_deviation, color='b', linestyle='dashed', linewidth=1,
                    label=f'-1 Std. отклонение ({mean_price - std_deviation:.2f})')

        # добавление легенды и подписей
        plt.legend()
        plt.title('Гистограмма цен с математическим ожиданием и стандартным отклонением')
        plt.xlabel('Цена')
        plt.ylabel('Частота')

        # сохранение графика в файл
        plt.savefig('price_analysis.png')

        # показываем график
        plt.show()
    else:
        print("Столбец 'Цена' не найден в таблице.")
