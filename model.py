STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'w'
PORAZ = 'x'

class Igra:
    def __init__(self, geslo):
        self.geslo = geslo
        self.crke = []
    def napacne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka not in self.geslo:
                seznam.append(crka)
        return seznam
    def pravilne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam.append(crka)
        return seznam
    def stevilo_napak(self):
        return len(self.napacne_crke())
    def zmaga(self):
        if len(self.pravilne_crke()) == len(self.geslo):
            return True
        return False
    def poraz(self):
        if len(self.napacne_crke()) > STEVILO_DOVOLJENIH_NAPAK:
            return True
        return False
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz
    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.napacne_crke():
            niz += crka + ' '
        return niz
    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.upper()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke.append(ugibana_crka)
        if self.zmaga():
            return ZMAGA
        if self.poraz():
            return PORAZ
        if ugibana_crka in self.pravilne_crke():
            return PRAVILNA_CRKA
        return NAPACNA_CRKA
        

