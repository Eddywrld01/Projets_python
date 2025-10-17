import logging
from compte import Compte
logging.basicConfig(filename= "app.log",filemode="w" , level = logging.INFO)

compte1 = Compte(1,9000.00)
compte2 = Compte(2,13000.00)
compte1.verser(5000)
logging.info(f"Versement d'un montant")
compte2.retirer(3000)
logging.info(f"Retrait d'un montant")
compte2.afficher()
logging.info("Montant affiché")
