# Оператор "with

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name) as file:
                all_words.update({file_name: [i.strip(',.=!?;:-') for i in file.read().lower().split()]})
        return all_words

    def find(self, word):
        return {name: words.index(word.lower()) + 1 for name, words in self.get_all_words().items() if
                word.lower() in words}

    def count(self, word):
        return {name: words.count(word.lower()) for name, words in self.get_all_words().items()}


if __name__ == '__main__':
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))

