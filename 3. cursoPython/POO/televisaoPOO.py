class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentaCanal(self):
        self.canal += 1
    
    def diminuiCanal(self):
        self.canal -= 1

if __name__ == "__main__":
    televisao = Televisao()
    print('TV Ligada:', televisao.ligada)
    print('Canal:', televisao.canal)
    televisao.power()
    televisao.aumentaCanal()
    print('\nTV Ligada:', televisao.ligada)
    print('Canal:', televisao.canal)
    televisao.aumentaCanal()
    print('\nTV Ligada:', televisao.ligada)
    print('Canal: ', televisao.canal)
    televisao.aumentaCanal()
    print('\nTV Ligada:', televisao.ligada)
    print('Canal:', televisao.canal)
    televisao.diminuiCanal()
    print('\nTV Ligada:', televisao.ligada)
    print('Canal:', televisao.canal)