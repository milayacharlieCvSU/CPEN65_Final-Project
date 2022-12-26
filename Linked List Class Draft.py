# Code about attendance using linked list
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


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, next_data):
        self.next = next_data

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.getData() == item:
                if previous is not None:
                    previous.setNext(current.getNext())
                self.head = current.getNext()
            previous = current
            current = current.getNext()

    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.getNext()
        previous.setNext(temp)

    def insert(self, pos, item):
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        while current is not None:
            if count == pos:
                temp.setNext(current)
                previous.setNext(temp)
                break
            count += 1
            previous = current
            current = current.getNext()

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.getData() == item:
                return count
            count += 1
            current = current.getNext()

    def __repr__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.getData())
            current = current.getNext()
        return str(items)


directory = LinkedList()
for numbers, names in zip(directory_numbers, directory_names):
    directory.add([numbers, names])
