import string

class WordsFinder:
    def __init__(self, *file_names: str): # Инициализация класса с именами файлов
        self.file_names = list(file_names)

    def get_all_words(self): # Получение всех слов из файлов
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as file: # Чтение файла, перевод в нижний регистр и разделение на слова
                words = file.read().lower().split()
                for word in words:
                    word = word.strip(string.punctuation) # Удаление пунктуации из слова
                    if file_name not in all_words:
                        all_words[file_name] = [] # Добавление нового ключа в словарь
                    all_words[file_name].append(word) # Добавление слова в список слов для данного файла
        return all_words

    def find(self, word: str): # Поиск слова в файлах
        word = word.lower()
        result_dict = {}
        for file_name, words in self.get_all_words().items():
            flag = False
            for i in range(len(words)):
                if words[i] == word: # Проверка наличия слова в списке слов для данного файла
                    flag = True
                    break
            if flag: # Если слово найдено, добавляем его в словарь результатов
                result_dict[file_name] = i + 1
        return result_dict

    def count(self, word: str): # Подсчет количества вхождений слова в файлы
        word = word.lower()
        result1_dict= {}
        for file_name, words in self.get_all_words().items():  # Подсчет количества вхождений слова в список слов для данного файла
            result1_dict[file_name] = words.count(word)
        return result1_dict

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())
# print(finder2.find('TEXT'))
# print(finder2.count('teXT'))


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',) # проверка на другом файле
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))