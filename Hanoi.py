from sys import argv



def hanoi_animation(taille):
    t1 = [taille - k for k in range(taille)]
    t2 = []
    t3 = []
    
    def afficher_plateau():
        
        hauteur = taille
        largeur = taille * 2 + 1

        
        
        for niveau in range(hauteur - 1 , -1, -1):
            
            ligne = ""
            
            def etage(tour):
                if niveau < len(tour) :
                    taille_palet = tour[niveau]
                    return  " " * (largeur - taille_palet) + "=" * (taille_palet * 2 + 1) + " " * (largeur - taille_palet)
                    
                    
                else :
                    #la non
                    return  " " * (largeur) + "|" + " " * (largeur)
                    
            ligne += etage(t1)
            ligne += etage(t2)
            ligne += etage(t3)
            
            
            print(ligne)
        print()
        print("---------------------------------------")
        print()
            
        
            
        
    def deplacer_palet (a, b) :
        b.append(a.pop())
        afficher_plateau()
        
    def deplacer_tour (a, b, intermediaire, taille_tour) :
       
        if taille_tour == 1:
            deplacer_palet (a, b)
            
        else :
            
            deplacer_tour(a, intermediaire, b, taille_tour - 1)
            
            deplacer_palet (a, b)
            
            deplacer_tour(intermediaire, b, a, taille_tour - 1)
            
            
    
    
    afficher_plateau()
    deplacer_tour(t1, t3, t2, taille)
    





try :
     
    if len(argv) > 1:
        taille = int(argv[1])

        if taille <= 0:
            raise ValueError("La taille de doit etre un entier positif. (0 exclus)")
        if taille > 15:
            raise ValueError("Attention la valeur est trop élever, cela prendrait beaucoup trop de temps")
    else : 
        raise ValueError("Aucun argument n'a été fourni.")
     
     
     
     
    hanoi_animation(taille)
     
except ValueError as e : 
    print(f"Erreur : {e}")
    print("Exemple d'utilisation : python nom_fichier.py <taille du jeu>")

except Exception as e :
    print(f"Une erreur inattendue est survenue : {e}")