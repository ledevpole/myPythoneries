

def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print."""
    parametres = list(parametres)
    for i, param in enumerate(parametres):
        param[i] = str(param)
        chaine = sep.join(param)
        chaine += fin
     
    print(chaine, end='')


afficher(['1',' 2', '3','5'])
