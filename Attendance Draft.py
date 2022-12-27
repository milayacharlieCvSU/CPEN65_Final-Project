from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime

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


class Application(Tk):
    # Initialization
    def __init__(self):
        super().__init__()

        # Window Properties
        main_window_height = 300
        main_window_width = 500
        self.geometry(f'{main_window_width}x{main_window_height}+25+25')
        today = datetime.now().strftime('%B %d, %Y')
        self.title(f'Attendance of BSCpE 2-1 for {today}')

        # Labels
        self.title_label = Label(self, text='BSCpE 2-1 Attendance', font=('Arial', 16))
        self.title_label.grid(column=0, row=0, columnspan=2, padx=10, pady=3)

        self.name_label = Label(self, text='Name: ', font=('Arial', 12))
        self.name_label.grid(column=0, row=1, padx=10, pady=3, sticky=W)

        self.studentNo_label = Label(self, text='Student Number: ', font=('Arial', 12))
        self.studentNo_label.grid(column=0, row=2, padx=10, pady=3, sticky=W)

        # Entries
        self.name_data = Combobox(self, font=('Arial', 11))
        self.name_data.grid(column=1, row=1, padx=10, pady=3, sticky=W)

        temp_directory = directory_names.copy()
        temp_directory.sort()
        self.name_data['values'] = temp_directory

        self.name_data['state'] = 'readonly'

        self.studentNo_data = Entry(self,  font=('Arial', 12))
        self.studentNo_data.grid(column=1, row=2, padx=10, pady=3, sticky=W)

        # Buttons
        self.time_in = Button(self, text='Time In', font=('Arial', 10))
        self.time_in.grid(column=0, row=3, padx=10, pady=3)

        self.time_out = Button(self, text='Time Out', font=('Arial', 10))
        self.time_out.grid(column=1, row=3, padx=10, pady=3)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
