def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "Файл не знайдено"
    except UnicodeDecodeError:
        return "Непідтримуване кодування файлу"



print(count_words_in_file('test.txt'))