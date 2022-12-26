# Code about attendance using queues
directory_numbers = [202012159, 202015206, 202101036, 202101441, 202101447, 202101462, 202101468, 202101486,
                     202101487, 202101495, 202101502, 202101513, 202101555, 202101624, 202101628, 202101633,
                     202101672, 202101677, 202101723, 202101726, 202101759, 202101777, 202101864, 202101869,
                     202101875, 202101886, 202102048, 202102057, 202102061, 202102187, 202102226, 202102319,
                     202102333, 202102562, 202103531]
directory_names = ['Esporas, Javibe M.',
                   'Trias Jr., Ysmael R.',
                   'Julian, Ma. Kaethe Joy A.',
                   'Nicart, Ben Piolo G.',
                   'Bangay, Rhonan Richmond D.',
                   'Blasco, Marc Christian M.',
                   'Alcala, Lance Wesley B.',
                   'Eugenio, Julius Caezar R.',
                   'Angeles, Miro G.',
                   'Crusem, Deen Reinier B.',
                   'Ocasion, Alessandro Xavier T.',
                   'Argente, Allen Patrick M.',
                   'Albero, Justine Kate P.',
                   'Atencia, Joshua D.',
                   'Marasigan, Dominic Z.',
                   'Gloriani, Franz Louise B.',
                   'Daguio, John Hendrick S.',
                   'Anciado, Alexis Jelyn P.',
                   'Baguio, Wearl Ian G.',
                   'Camandono, Gabriel Q.',
                   'Cueno, Trisha Faye C.',
                   'Alegre, Ericka Jane A.',
                   'Cubol, Elise Brixe S.',
                   'Milaya, Charlie',
                   'Anogante, Ryan Nico',
                   'Catamisan, Lanz Andrei A.',
                   'Tayab, Dirk M.',
                   'Serenio, Marc Jay D.',
                   'Paglinawan, King John Adamz R.',
                   'Mendoza, Jessa Mae D.',
                   'Alcantara, Ulysses S.',
                   'Guasis, Chelsey L.',
                   'Aguado, Danielle Ysabelle M.',
                   'Samonte, Jeffrey R.',
                   'Rupido, Baby Angel E.']


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

    def list(self):
        return self.items


directory = Queue()
for numbers, names in zip(directory_numbers, directory_names):
    directory.enqueue([numbers, names])

