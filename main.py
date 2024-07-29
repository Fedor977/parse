# main.py

from data_analysis import analyze_data


def main():
    filename = 'tehnomart.xlsx'
    category_name = 'tehnomart'

    analyze_data(filename, category_name)


if __name__ == "__main__":
    main()
