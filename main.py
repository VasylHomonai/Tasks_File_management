"""додаткові задачі:
    1. Створіть функцію count_words(filename), яка читає текстовий файл і повертає кількість слів у ньому

    2. Напишіть функцію most_common_word(filename), яка повертає слово, що зустрічається найчастіше у файлі.
       Ігноруйте регістр і розділові знаки

    3. Функція remove_empty_lines(filename) повинна видалити всі порожні рядки з файлу та зберегти результат
       в новому файлі з назвою cleaned_<оригінальна_назва>.txt

    4. Реалізуйте функцію find_lines_with_keyword(filename, keyword), яка повертає список усіх рядків,
       де зустрічається задане ключове слово

    5. Функція read_first_n_lines(filename, n) повинна повертати список з перших n рядків файлу

    6. Функція reverse_lines(filename) повинна переписати файл так, щоб усі рядки були записані у зворотному порядку
       (останній — перший)

    7. Функція character_statistics(filename) повинна повертати словник з кількістю входжень кожного символу
       (включно з пробілами та розділовими знаками)
"""
import string
path = 'files/example.txt'

# Виніс окремо ф-цію яка зчитує інформацію з файлу
def read_text_file(file_path: str)->tuple[bool, str]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            cont = file.read()

        if not cont.strip():     # Якщо вміст пустий або містить тільки пробіли
            return False, f"Файл {file_path} порожній"

        return True, cont

    except FileNotFoundError:
        return False, f"Файл не знайдено: {file_path}"
    except Exception as e:
        return False, f"Сталася помилка при читанні файлу: {e}"


# Виніс окремо ф-цію яка видаляє зайві символи у тексті, тобто всі що містяться в string.punctuation
def cleaned_content(content: str)->str:
    cleaned_text = ''.join(char for char in content if char not in string.punctuation)
    return cleaned_text


print("Task 1:")

def count_words(filename: str)->str:
    words = cleaned_content(filename).split()
    return f"Кількість слів у файлі: {len(words)}"

success, content = read_text_file(path)
if success:
    count = count_words(content)
    print(count)
else:
    print(content)
print('*' *50, end='\n\n')

print("Task 2:")

def most_common_word(filename: str)-> str:
    words = cleaned_content(filename).lower().split()
    more_words = max(words, key=words.count)

    return f"Слово яке зустрічається максимальну к-сть разів: {more_words}"

success, content = read_text_file(path)
if success:
    max_word = most_common_word(content)
    print(max_word)
else:
    print(content)
print('*' *50, end='\n\n')

print("Task 3:")

def remove_empty_lines(filename):
    # Розбиваємо текст на рядки та видаляємо пусті
    cleaned_lines = [line for line in filename.splitlines() if line.strip()]
    # Об'єднуємо очищені рядки у текст
    cleaned_cont = '\n'.join(cleaned_lines)

    with open('files/cleaned_example.txt', 'w', encoding='utf-8') as f:
        f.write(cleaned_cont)
    print('Створено новий файл за шляхом: files/cleaned_example.txt')

success, content = read_text_file(path)

if success:
    remove_empty_lines(content)
else:
    print(content)
print('*' *50, end='\n\n')

print("Task 4:")

def find_lines_with_keyword(filename, keyword:str)->list[str]:
    keyword_lower = keyword.lower()
    expected_lines = [line for line in filename.splitlines() if keyword_lower in line.lower()]
    # Можна ще зробити на повне співпадіння слова в рядку, але там будуть нюанси: if keyword_lower in line.lower().split()
    return expected_lines

success, content = read_text_file(path)

if success:
    find_word = 'кохання'
    find_lines = find_lines_with_keyword(content, find_word)
    print(f"Всі рядки із текстового файлу, де зустрічається слово: '{find_word}'", end='\n\n')
    for line in find_lines:
        print(line)
else:
    print(content)
print('*' *50, end='\n\n')

print("Task 5:")

def read_first_n_lines(filename, n:int)->list[str]:
    count_lines = [line for line in filename.splitlines()[:n]]
    return count_lines

success, content = read_text_file(path)

if success:
    first_n = 4
    find_lines = read_first_n_lines(content, first_n)
    print(f"Вивід перших {first_n} рядків із текстового файлу", end='\n\n')
    for line in find_lines:
        print(line)
else:
    print(content)
print('*' *50, end='\n\n')

print("Task 6:")

def reverse_lines(filename):
    rev_lines = filename.splitlines()[::-1]
    new_cont = '\n'.join(rev_lines)     # Об'єднуємо рядки у текст
    with open('files/example_2.txt', 'w', encoding='utf-8') as f:
        f.write(new_cont)
    print('Поточний файл переписано: files/example_2.txt')

success, content = read_text_file('files/example_2.txt')

if success:
    reverse_lines(content)
else:
    print(content)
print('*' *50, end='\n\n')

print("Task 7:")

def character_statistics(filename)->dict:
    char_count = {}
    for line in filename.splitlines():
        for char in line:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


success, content = read_text_file(path)

if success:
    dict_result = character_statistics(content)
    print(dict_result)
else:
    print(content)