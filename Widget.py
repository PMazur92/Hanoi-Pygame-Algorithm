__author__ = 'piotrek'

import sys

import pygame


class Widget(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Hanoi')

        self.kolor_bialy = (255, 255, 255)
        self.kolor_brazowy = (172, 36, 36)
        self.kolor_czerwony = (255, 0, 0)
        self.kolor_zielony = (0, 255, 0)
        self.kolor_niebieski = (0, 0, 255)
        self.kolor_czarny = (0, 0, 0)
        self.rozmiar = self.szerokosc, self.wysokosc = 800, 600
        self.okno = pygame.display.set_mode(self.rozmiar)

        self.czcionka = pygame.font.SysFont("arial", 20)
        self.czcionka_bloczkow = pygame.font.SysFont("arial", 28)
        self.element = (0, 0, 0)
        self.czy_przestawiono = False

        self.ilosc_bloczkow = 5
        self.tworz_bloczki()

    def hanoi(self, n, a, b, c):
        """Algorytm przekladajacy klocki na 3 slupek"""
        if n > 0:
            self.hanoi(n - 1, a, c, b)
            self.przestaw(a, c)
            self.wyswietl_hanoi()
            self.hanoi(n - 1, b, a, c)

    def tworz_bloczki(self):
        """Tworzy bloczki"""
        self.slupek_a = ('A', [(str(i), 40 + i * 20) for i in range(self.ilosc_bloczkow, 0, -1)])
        self.slupek_b = ('B', [])
        self.slupek_c = ('C', [])

    def wyswietl_bloczki(self):
        """Wyswietla bloczki ze slupkow na ekranie"""

        # wyswietlenie bloczkow slupka A
        for i, (nazwa, szerokosc) in enumerate(self.slupek_a[1]):
            pol_szer = szerokosc/2
            pygame.draw.rect(self.okno, self.kolor_czerwony, (200 - pol_szer, 365 - i * 26, szerokosc, 26))
            self.okno.blit(self.czcionka_bloczkow.render(nazwa, True, (0, 0, 255)), (190, 365 - i * 26))

        # wyswietlenie bloczkow slupka B
        for i, (nazwa, szerokosc) in enumerate(self.slupek_b[1]):
            pol_szer = szerokosc/2
            pygame.draw.rect(self.okno, self.kolor_czerwony, (400 - pol_szer, 365 - i * 26, szerokosc, 26))
            self.okno.blit(self.czcionka_bloczkow.render(nazwa, True, (0, 0, 255)), (390, 365 - i * 26))

        # wyswietlenie bloczkow slupka C
        for i, (nazwa, szerokosc) in enumerate(self.slupek_c[1]):
            pol_szer = szerokosc/2
            pygame.draw.rect(self.okno, self.kolor_czerwony, (600 - pol_szer, 365 - i * 26, szerokosc, 26))
            self.okno.blit(self.czcionka_bloczkow.render(nazwa, True, (0, 0, 255)), (590, 365 - i * 26))

    def przestaw(self, slupek1, slupek2):
        """Przestawia element ze slupka1 na slupek2"""
        element = slupek1[1].pop()
        slupek2[1].append(element)
        self.element = (element[0], slupek1[0], slupek2[0])
        self.czy_przestawiono = True

    def wyswietl_hanoi(self):
        # ustawia kolor tla na bialy
        self.okno.fill(self.kolor_bialy)

        # wyswietl napisy nad slupkami
        self.wyswietl_napisy()

        # wyswietl podstawke
        self.wyswietl_podstawke()

        # wyswietl bloczki
        self.wyswietl_bloczki()

        # wyswietl informacje
        if self.czy_przestawiono:
            if len(self.slupek_c[1]) != self.ilosc_bloczkow:
                self.okno.blit(self.czcionka.render(
                               'Przestawienie elementu {0} ze slupka {1} na slupek {2}'.format(
                                                                                        self.element[0],
                                                                                        self.element[1],
                                                                                        self.element[2]),
                               True, (0, 0, 0)), (170, 500))
            else:
                self.okno.blit(self.czcionka.render('Koniec', True, (0, 0, 0)), (360, 500))
        pygame.display.update()
        # nasluchuje zdarzen
        self.nasluchuj_zdarzen()
        pygame.time.delay(1000)

    def wyswietl_podstawke(self):
        """Wyswietl brazowa podstawke"""
        # pionowe
        pygame.draw.line(self.okno, self.kolor_brazowy, (195, 100), (195, 400), 10)
        pygame.draw.line(self.okno, self.kolor_brazowy, (395, 100), (395, 400), 10)
        pygame.draw.line(self.okno, self.kolor_brazowy, (595, 100), (595, 400), 10)

        # pozioma
        pygame.draw.line(self.okno, self.kolor_brazowy, (100, 395), (700, 395), 10)

    def wyswietl_napisy(self):
        """Wyswietla napisy nad slupkami"""
        self.okno.blit(self.czcionka.render('Slupek A', True, (0, 0, 0)), (160, 50))
        self.okno.blit(self.czcionka.render('Slupek B', True, (0, 0, 0)), (360, 50))
        self.okno.blit(self.czcionka.render('Slupek C', True, (0, 0, 0)), (560, 50))

    def wyswietl(self):

        while True:
            Widget.nasluchuj_zdarzen()
            self.wyswietl_hanoi()
            if len(self.slupek_a[1]):
                self.hanoi(self.ilosc_bloczkow, self.slupek_a, self.slupek_b, self.slupek_c)
            pygame.display.update()

    @staticmethod
    def nasluchuj_zdarzen():
        """Nasluchuje zdarzen"""
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                sys.exit()
