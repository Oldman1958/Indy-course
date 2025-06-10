"""
В вашем распоряжении список words, который определяется во входных данных и состоит из строк.

Ваша задача — пройтись в цикле по элементам списка и вывести на экран только те из них,
длина которых больше 6 символов.

Выводить каждый элемент нужно на отдельной строке в том же порядке, в котором слова расположены в списке words.

Так как words определяется внутри входных данных, вам считывать данные не нужно. Сразу пользуйтесь переменной words.
"""

# Список words отправлять не нужно. Он приведен только для того, чтобы проверить работоспособность кода.
words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
         'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
         'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
         'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
         'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
         'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
         'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
         'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
         'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']

for i in range(len(words)):
    if len(words[i]) > 6:
        print(words[i])
