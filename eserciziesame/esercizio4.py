import json
path='./jsonfile.json'

def apri_file(path):
        jsonfile=json.loads(path)
        if jsonfile['Users']=='root' and jsonfile['IsModifiable']==True:
            utenti=input('Inserisci una lista di utenti separati da spazio: ').split(' ')
            jsonfile['Users']=utenti
            json.dump(jsonfile, utenti, indent=4)

apri_file(path) 