from random import randint
    
def tah_pocitac():
    tah_pocitace = randint(1, 3)
    #print(tah_pocitace)
    if tah_pocitace == 1:
        tah_pocitace = "kámen"
        pc_kamen = True
        pc_nuzky = False
        pc_papir = False
    elif tah_pocitace == 2:
        tah_pocitace = "nůžky"
        pc_kamen = False
        pc_nuzky = True
        pc_papir = False
    else:
        tah_pocitace = "papír"
        pc_nuzky = False
        pc_kamen = False
        pc_papir = True
    return pc_kamen, pc_nuzky, pc_papir


def tah_clovek():
    tah_cloveka = input('kámen, nůžky, nebo papír? ')
    if tah_cloveka == 'kámen':
        cl_kamen = True
        cl_nuzky = False
        cl_papir = False
    elif tah_cloveka == 'nůžky':
        cl_kamen = False
        cl_nuzky = True
        cl_papir = False
    elif tah_cloveka == 'papír':
        cl_kamen = False
        cl_nuzky = False
        cl_papir = True
    else:
        print('Nerozumím.')
        return tah_clovek()
    return cl_kamen, cl_nuzky, cl_papir


def vyhodnoceni(cl_kamen, cl_nuzky, cl_papir, pc_kamen, pc_nuzky, pc_papir):
    if pc_kamen and cl_kamen or pc_nuzky and cl_nuzky or pc_papir and cl_papir:
        print('Plichta')
        return 0
    elif pc_kamen and cl_nuzky or pc_nuzky and cl_papir or pc_papir and cl_kamen:
        print('Počítač vyhrál!')
        return -1
    #else  # should be enough
    elif pc_kamen and cl_papir or pc_nuzky and cl_kamen or pc_papir and cl_nuzky:
        print('Vyhrálas!')
        return 1


def stats(score, hracovy_vyhry, vyhry_pc):
    if score == 1:
        hracovy_vyhry += 1
    elif score == -1:
        vyhry_pc += 1
    return hracovy_vyhry, vyhry_pc 


def main():
    hracovy_vyhry, vyhry_pc = 0, 0
    dalsi_kolo = True
    while dalsi_kolo == True:
        cl_kamen, cl_nuzky, cl_papir = tah_clovek()
        pc_kamen, pc_nuzky, pc_papir = tah_pocitac()
        hracovy_vyhry, vyhry_pc = stats(vyhodnoceni(cl_kamen, cl_nuzky, cl_papir, pc_kamen, pc_nuzky, pc_papir), hracovy_vyhry, vyhry_pc)
        dalsi_kolo = True if input('Zadej "znova" pro další kolo: ') == 'znova' else False
    if hracovy_vyhry > vyhry_pc: print("Gratuluji!")
    print("Máš", hracovy_vyhry, "vítězství a počítač tě porazil", vyhry_pc,"krát.")


main()

