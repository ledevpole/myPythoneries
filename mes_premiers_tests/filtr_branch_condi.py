liste_origine = [1,2,3,4,5,6]

print([nb * nb for nb in liste_origine if nb%2==0])



qtt_a_retirer = 7 # on retire chaque semaine 7 fruits de chaque sorte

stock_de_fruits = [15,34,23,18,3]

print('\n fruits: \n'+ str(stock_de_fruits)+'\n')

print('moins '+ str(qtt_a_retirer))

print([nb_fruits - qtt_a_retirer 
	for nb_fruits in stock_de_fruits if nb_fruits > qtt_a_retirer])

inventaire = [("pommes",22),("melons",4),("poires",18),
	("fraises",76),("prunes",51),]

print(inventaire)

print([produit for produit in inventaire])



