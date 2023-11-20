menu_text = """Alege o categorie:
        1. Adauga student
        2. Sterge student
        3. Modifica student
        4. Adauga disciplina
        5. Sterge disciplina
        6. Modifica disciplina
        7. Cauta student
        8. Cauta disciplina
        9. Adauga nota 
        10. Afiseaza studenti ordonati alfabetic
        11. Afiseaza studenti ordonati dupa nota
        12. Afiseaza primii 20% din studenti dupa medie
        13. Afiseaza primii 20% din studenti dupa nume
>>>"""

def get_command():
    try:
        n = int(input(menu_text))
    except ValueError:
        return 0
    else:
        return n

def enter(msg = ""):
    if msg:
        input(f"{msg}\nPress Enter to continue")
    else:
        input("Press Enter to continue")


def get_string(msg):
    return input(f"{msg}\n>>>")

def get_int(msg):
    while True:
        try:
            return int(input(f"{msg}\n>>>"))
        except ValueError:
            pass