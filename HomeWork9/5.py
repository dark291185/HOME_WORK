class Stationery:
    def __init__(self, title: str):
        self._title = title

    def draw(self):
        print(f'Запуск отрисовки {self._title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Штрихуем ручкой {self._title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Малюем карандашом {self._title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Рисуем маркером {self._title}')


paintbrush = Stationery('Paintbrush')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

paintbrush.draw()
pen.draw()
pencil.draw()
handle.draw()