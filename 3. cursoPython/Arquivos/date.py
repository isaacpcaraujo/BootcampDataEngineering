from datetime import date, time, datetime

def utilizandoDate():
    dataAtual = date.today()
    print(dataAtual.strftime(format="%d/%m/%Y"))
    print(dataAtual.strftime(format="%A %B %Y"))

def utilizandoTime():
    horario = time(hour=2, minute=55, second=30)
    print(horario.strftime(format="%H:%M:%S"))

def utilizandoDateTime():
    dataAtual = datetime.now()
    print(dataAtual.strftime(format="%c"))


if __name__ == "__main__":
    utilizandoDate()
    utilizandoTime()
    utilizandoDateTime()