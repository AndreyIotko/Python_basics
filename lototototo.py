from random import randint, choice


class LotoCard:
    def __init__(self, name):
        self.name = name
        rand_numbers = []
        self.num_card = []
        while len(rand_numbers) < 15:
            new = randint(1, 90)
            if new not in rand_numbers:
                rand_numbers.append(new)
        for i in range(3):
            line = sorted(rand_numbers[5 * i:5 * (i + 1)])
            for _ in range(4):
                line.insert(randint(0, len(line)), 'space')
            self.num_card.append(line)

    def __str__(self):
        str_card = f'{self.name:}\n' + '-' * 26 + '\n'
        for el in self.num_card:
            for i in el:
                if i == 'space':
                    str_card += '  '
                elif i != ' -':
                    str_card += f'{str(i):2}'
                str_card += ' '
            str_card += '\n'
        return str_card


class LotoGame:
    def __init__(self, player):
        self.player = player
        self.computer = LotoCard('Computer')

    @property
    def start(self):
        __numbers_player = []
        __numbers_computer = []
        for i in range(len(player.num_card)):
            for el in range(9):
                if self.player.num_card[i][el] != 'space':
                    __numbers_player.append(self.player.num_card[i][el])
                if self.computer.num_card[i][el] != 'space':
                    __numbers_computer.append(self.computer.num_card[i][el])
        cask_with_casks = list(range(1, 91))
        while True:
            cask = choice(cask_with_casks)
            cask_with_casks.remove(cask)

            print(f'Новый бочонок: {cask} (осталось {len(cask_with_casks)})')
            print(self.player)
            print(self.computer)

            cross_out = input('Зачеркнуть цифру? (y/n)\n:').upper()
            while True:
                if cross_out not in ['Y', 'N']:
                    cross_out = input('y = зачеркнуть / n = продолжить не зачеркивая\n').upper()
                else:
                    break

            if cross_out == 'Y' and cask in __numbers_player:
                __numbers_player.remove(cask)
                for el in self.player.num_card:
                    if cask in el:
                        el[el.index(cask)] = '-'
                if len(__numbers_player) == 0:
                    print('Вы выйграли!')
                    break
            elif cross_out == 'Y' and cask not in __numbers_player:
                print('Вы проиграли !')
                break
            elif cross_out == 'N' and cask in __numbers_player:
                print('Вы проиграли !')
                break

            if cask in __numbers_computer:
                __numbers_computer.remove(cask)
                for el in self.computer.num_card:
                    if cask in el:
                        el[el.index(cask)] = '-'
                if len(__numbers_computer) == 0:
                    print('Вы проиграли !')
                    break


player = LotoCard('Player')

game = LotoGame(player)
game.start