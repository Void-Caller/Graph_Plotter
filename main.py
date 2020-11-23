import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import networkx as nx


def fill_matrix(m, v):
    '''Funkcja odpowiadająca za wypełniania mecierzy sąsiedztwa'''
    #index wektora v
    k = 0

    #dla każdego rzędu macierzy i
    for i in range(len(m)-1):
        #dla kolum od i+1 do ostatniej, czyli nad przekątną.
        for j in range(i+1, len(m[i])):
            #element macierzy [i][j] jest równy k-temu elementowi wektora v.
            m[i][j] = v[k]
            k += 1
    #tak zostaje wypełniona część macierzy nad przekątną.
    #transpozycją macierzy wypełnionej nad przekątną jest wypełnienie pod przekątną.
    m2 = m.transpose()
    #złożenie górnej i dolnej macierzy w wypełnioną macierz sąsiedzttwa.
    m += m2

def increment_vector(v, i = 0):
    '''Zwiększa wartość binarną zapisaną w wektorze o jeden'''
    if i == len(v):
        return True
    else:
        if v[i]:
            v[i] = 0
            increment_vector(v, i + 1)
        else:
            v[i] = 1


if __name__ == '__main__':
    #otwarcie pliku
    pp = PdfPages('test1.pdf')
    #pobranie rozmiaru tablicy
    x = int(input("Input the size of the graph: "))
    # utworzenie pustej macierzy sąsiedztwa.
    M = np.zeros([x, x], dtype=int)
    #obliczenie liczby wartości nad przekątną.
    k = int(((x - 1) / 2) * x)
    #utworzenie wektora o liczbie odpowiadającej liczbie pól nad przekątną.
    V = np.zeros(k, dtype=int)
    #Powtarzając procedurę dla 2 do potęgi k-tej przypadków
    for i in range(2**k):
        #wypełniam macierz M
        fill_matrix(M, V)
        #traktuję wartości w wektorze V jako zapis binarny liczby i podnoszę ją o jeden.
        increment_vector(V)

        #rysuję graf
        G = nx.from_numpy_matrix(np.array(M))
        g = nx.draw(G, with_labels=True)
        #zapisuję graf do pliku
        pp.savefig(g)
        #ustawiam Macierz sąsiedztwa na pustą.
        M = np.zeros([x, x], dtype=int)
        #czyszcze rysowaną figurę przed następnym rysunkiem.
        plt.clf()
    #zamykam plik.
    pp.close()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
