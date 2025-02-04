class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                c = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    c = c.replace(i, '')
                words = c.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        res = {}
        for name, words in all_words.items():
            word = word.lower()
            if word in words:
                res[name] = words.index(word)+1
        return res

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower()
        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего