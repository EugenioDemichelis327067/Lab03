class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti={}
        self.prestiti={}
    def crea_codiceStrumento(self):
        massimo=0
        for key in self.strumenti:
            numero=int(key[1:])
            if numero > massimo:
                massimo=numero
        return f's{massimo +1}'
    def crea_codicePrestiti(self):
        massimo=0
        for key in self.prestiti:
            numero=int(key[1:])
            if numero > massimo:
                massimo=numero
        return f'p{massimo + 1}'
    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            self.filepath = file_path
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip().split(",")
                    code=line[0]
                    name=line[1]
                    brand=line[2]
                    year=line[3]
                    value=line[4]
                    strument=Strumento(code, name, brand, year, value)
                    self.strumenti[code]=strument
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        code = self.crea_codice()
        strument=Strumento(code,tipo, marca, anno_acquisto, valore)
        self.strumenti[code]=strument



    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        strumentiOrdinati=dict(sorted(self.strumenti.items(), key=lambda item: item[1].marcaStrumento)).values()
        return strumentiOrdinati

    def nuovo_prestito(self, dataInizio, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        codicePrestito=self.crea_codicePrestiti()
        prestito=Prestito(codicePrestito,dataInizio, id_strumento, cognome_allievo)
        self.prestiti[codicePrestito]=prestito
        return f"{codicePrestito} prestito"

    def termina_prestito(self, id_prestito):
        self.prestiti[id_prestito].turnedOff()


class Strumento:
    def __init__(self, codice, nomeStrumento,marcaStrumento,anno,valore):
        self.codice = codice
        self.nomeStrumento = nomeStrumento
        self.marcaStrumento = marcaStrumento
        self.anno = anno
        self.valore = valore
    def __str__(self):
        return f"{self.codice} {self.nomeStrumento} {self.marcaStrumento} {self.anno} {self.valore}"

class Prestito:
    def __init__(self,codice,dataInizio,id_strumento, cognome_allievo):
        self.codice = codice
        self.dataInizio = dataInizio
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo
        self.prestitoAttivo = True
    def __str__(self):
        return f"{self.codice} {self.id_strumento} {self.cognome_allievo} {self.prestitoAttivo}"
    def turnedOff(self):
        self.prestitoAttivo = False


