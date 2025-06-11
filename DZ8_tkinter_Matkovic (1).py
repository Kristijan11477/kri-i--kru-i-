from tkinter import *
from tkinter.messagebox import *

# DODANO: Funkcija za unos parametara korisnika
def unesi_parametre():
    pozadina = input("Unesi engleski naziv željene boje pozadine: ")
    boja_gumba = input("Unesi engleski naziv željene boje gumba: ")
    font_simbola = input("Unesi naziv željenog fonta za križiće i kružiće: ")
    stil_simbola = input("Unesi željeni tip teksta za križiće i kružiće (normal, bold, italic): ")
    boja_X = input("Unesi engleski naziv željene boje križića: ")
    boja_O = input("Unesi engleski naziv željene boje kružića: ")
    boja_pobjednickih = input("Unesi engleski naziv željene boje pobjedničkih gumbiju: ")
    boja_semafora = input("Unesi engleski naziv željene boje teksta semafora: ")
    font_semafora = input("Unesi naziv željenog fonta teksta semafora: ")
    velicina_semafora = int(input("Unesi željenu veličinu teksta semafora u pikselima: "))
    stil_semafora = input("Unesi željeni tip teksta semafora (normal, bold, italic): ")

    return {
        'pozadina': pozadina,
        'boja_gumba': boja_gumba,
        'font_simbola': font_simbola,
        'stil_simbola': stil_simbola,
        'boja_X': boja_X,
        'boja_O': boja_O,
        'boja_pobjednickih': boja_pobjednickih,
        'boja_semafora': boja_semafora,
        'font_semafora': font_semafora,
        'velicina_semafora': velicina_semafora,
        'stil_semafora': stil_semafora
    }

class KrizicKruzic(Frame):
    def __init__(self, root, stil):
        self.root = root
        super().__init__(self.root)
        self.grid()
        self.stil = stil
        self.rezultat_X = 0
        self.rezultat_O = 0

        # DODANO: Font semafora iz korisničkog unosa
        self.font_teksta = (self.stil['font_semafora'], self.stil['velicina_semafora'], self.stil['stil_semafora'])

        # DODANO: Boja semafora iz korisničkog unosa
        self.semafor = Label(self, text='X \u2192 {} : {} \u2190 O'.format(self.rezultat_X, self.rezultat_O),
                             font=self.font_teksta, bg=self.stil['pozadina'], fg=self.stil['boja_semafora'])
        self.semafor.grid(row=3, column=0, sticky='ew', columnspan=3)
        self.KreirajSucelje()
        return

    def KreirajSucelje(self):
        self.trenutni_igrac = 'X'
        self.praznih = 9

        self.tG = [[StringVar() for j in range(3)] for i in range(3)]
        self.G = [[None for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                gumb = Button(self,
                              font=(self.stil['font_simbola'], 40, self.stil['stil_simbola']),
                              width=6,
                              height=2,
                              bg=self.stil['boja_gumba'],
                              command=lambda x=i, y=j: self.Klik(x, y))
                gumb.grid(row=i, column=j)
                self.G[i][j] = gumb
        return

    def Klik(self, i, j):
        if self.tG[i][j].get():
            return

        if self.trenutni_igrac == 'X':
            self.tG[i][j].set('X')
            self.G[i][j].config(text='X', fg=self.stil['boja_X'])
            self.praznih -= 1
            self.trenutni_igrac = 'O'
        else:
            self.tG[i][j].set('O')
            self.G[i][j].config(text='O', fg=self.stil['boja_O'])
            self.praznih -= 1
            self.trenutni_igrac = 'X'

        pobjednik = self.ImaLiPobjednika()

        if pobjednik == 'X':
            self.rezultat_X += 1
        elif pobjednik == 'O':
            self.rezultat_O += 1

        self.semafor.config(text='X \u2192 {} : {} \u2190 O'.format(self.rezultat_X, self.rezultat_O))

        if pobjednik:
            self.NapisiPoruku('Kraj igre!', 'Pobjeda!\nPobijedio je igrač {}!'.format(pobjednik))
        if not self.praznih and not pobjednik:
            self.NapisiPoruku('Kraj igre!', 'Neriješeno!\nNitko nije pobijedio!')
        return

    def ImaLiPobjednika(self):
        for i in range(3):
            if self.tG[i][0].get() == self.tG[i][1].get() == self.tG[i][2].get() != '':
                self.OznaciPobjednickeGumbe([(i, 0), (i, 1), (i, 2)])
                return self.tG[i][0].get()
        for i in range(3):
            if self.tG[0][i].get() == self.tG[1][i].get() == self.tG[2][i].get() != '':
                self.OznaciPobjednickeGumbe([(0, i), (1, i), (2, i)])
                return self.tG[0][i].get()
        if self.tG[0][0].get() == self.tG[1][1].get() == self.tG[2][2].get() != '':
            self.OznaciPobjednickeGumbe([(0, 0), (1, 1), (2, 2)])
            return self.tG[0][0].get()
        if self.tG[2][0].get() == self.tG[1][1].get() == self.tG[0][2].get() != '':
            self.OznaciPobjednickeGumbe([(2, 0), (1, 1), (0, 2)])
            return self.tG[0][2].get()

    def NapisiPoruku(self, naslov, tekst):
        showinfo(naslov, tekst)
        if askyesno('Igrati ponovo?', 'Želite li igrati ponovo?'):
            self.KreirajSucelje()
        else:
            self.root.destroy()
        return

    def OznaciPobjednickeGumbe(self, koordinate):
        for x, y in koordinate:
            self.G[x][y].config(bg=self.stil['boja_pobjednickih'])
        return

def main():
    stil = unesi_parametre()
    tkinter_okvir = Tk()
    tkinter_okvir.config(bg=stil['pozadina'])
    igra = KrizicKruzic(tkinter_okvir, stil)
    igra.mainloop()

if __name__ == '__main__':
    main()
