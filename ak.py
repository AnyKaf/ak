import pandas
import unidecode
import random
import string
data = pandas.read_csv(" ")

def jmeno(jmeno_a_prijmeni: str):
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return(rozdelene_jmeno[0])
    elif len(rozdelene_jmeno) == 3:
        return(f"{rozdelene_jmeno[0]} {rozdelene_jmeno[1]}")

def prijmeni(jmeno_a_prijmeni: str):
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return(rozdelene_jmeno[1])
    elif len(rozdelene_jmeno) == 3:
        return(rozdelene_jmeno[2])


def firemni_email(jmeno_a_prijmeni: str):
    jmeno_a_prijmeni = unidecode.unidecode(jmeno_a_prijmeni)
    jmeno_a_prijmeni = jmeno_a_prijmeni.lower()
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return(f"{rozdelene_jmeno[0]}.{rozdelene_jmeno[1]}@domena.pripona")
    elif len(rozdelene_jmeno) == 3:
        return(f"{rozdelene_jmeno[0]}-{rozdelene_jmeno[1]}.{rozdelene_jmeno[2]}@domena.pripona")

def uzivatelske_jmeno(jmeno_a_prijmeni: str):
    jmeno_a_prijmeni = unidecode.unidecode(jmeno_a_prijmeni)
    jmeno_a_prijmeni = jmeno_a_prijmeni.lower()
    rozdelene_jmeno = jmeno_a_prijmeni.split()
    if len(rozdelene_jmeno) == 2:
        return(f"{rozdelene_jmeno[0]}.{rozdelene_jmeno[1]}")
    elif len(rozdelene_jmeno) == 3:
        return(f"{rozdelene_jmeno[0]}-{rozdelene_jmeno[1]}.{rozdelene_jmeno[2]}")


data["Jméno"] = data["Jméno a příjmení"].apply(jmeno)
data["Příjmení"] = data["Jméno a příjmení"].apply(prijmeni)
data["Firemní e-mail"] = data["Jméno a příjmení"].apply(firemni_email)
data["Uživatelské jméno"] = data["Jméno a příjmení"].apply(uzivatelske_jmeno)


def heslo(delka=10):
    pismena = string.ascii_letters + string.digits
    znaky = string.punctuation
    vysledne_heslo = "".join(random.choice(pismena) for i in range(delka-2))
    vysledne_heslo = vysledne_heslo.join(random.choice(znaky) for i in range(2))
    vysledne_heslo = str(vysledne_heslo)
    return vysledne_heslo
