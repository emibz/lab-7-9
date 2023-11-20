from studenti import Student
from discipline import disciplina
from catalog import Catalog
from business import *
from ui import *
import os


def main():
    lista_studenti = []
    lista_discipline = []
    catalog = Catalog()

    while True:
        n = get_command()
        
        if n > 13:
            break
        if n < 0:
            print(lista_studenti)
            print(lista_discipline)
            input("Press Enter to continue")

        if n == 1:
            adauga_student(lista_studenti, get_string("Introdu Nume"))
            enter("Student Adaugat cu succes")

        if n == 2:
            sterge_student(lista_studenti, get_int("Introduceti id-ul Studentului"))
            enter("Student Sters cu succes")

        if n == 3:
            modifica_student(lista_studenti, get_int("Introduceti id-ul Studentului"), get_string("Introduceti noul nume al studentului"))
            enter("Student modificat cu succes")

        if n == 4:
            adauga_disciplina(lista_discipline, get_string("Introduceti numele disciplinei"), get_string("Introduceti numele profesorului"))
            enter("Disciplina adaugata cu succes")

        if n == 5:
            sterge_disciplina(lista_discipline, get_int("Introduceti id-ul disciplinei"))
            enter("Disciplina stearsa cu succes")

        if n == 6:
            option = get_int("1-Modificati numele disciplinei\n2-modificati profesorul")
            if option == 1:
                modifica_nume_disiciplina(lista_discipline, get_int("Introduceti id-ul disciplinei"), get_string("Introfuceti noul nume al disciplinei"))
                enter("Numele disciplinei modificat cu succes")
            elif option == 2:
                modifica_profesor_disciplina(lista_discipline, get_int("Introduceti id-ul disciplinei"), get_string("Introfuceti numele noului Profesor"))
                enter("Profesorul disciplinei modificat cu succes")
            else:
                enter("Input Invalid")

        if n == 7:
            print(cauta_student(lista_studenti, get_int("Introduceti id-ul studentului")))
            enter()

        if n == 8:
            print(cauta_disciplina(lista_discipline, get_int("Introduceti id-ul disciplinei")))
            enter()

        if n == 9:
            if adauga_nota(catalog, lista_studenti, lista_discipline, get_int("Introduceti id-ul studentului"), get_int("Introduceti id-ul disciplinei"), get_int("Introduceti Nota")):
                enter("Nota adaugata cu succes")
            else:
                enter("Nu exista studentul sau materia")

        if n == 10:
            catalog.print_catalog()
            enter()

        if n == 11:
            pass
        if n == 12:
            pass
        if n == 13:
            pass

        os.system("cls")

if __name__ == "__main__":
    os.system("cls")
    main()
