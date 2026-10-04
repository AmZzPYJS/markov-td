# Chaînes de Markov : TD1, exercice 1.2

Projet d'apprentissage pour le module *Modèles stochastiques et simulation*
(M1 Informatique). Python 3, sans bibliothèque externe.

On étudie la chaîne de Markov à 3 états de matrice de transition :

    P = | 0    0.6  0.4 |
        | 0.2  0.8  0   |
        | 0.3  0.2  0.5 |

## Contenu

- `markov.py` : multiplication d'une distribution par P, itération de
  pi(n+1) = pi(n) x P, produit de matrices, calcul de P^2, P^4, ..., P^1024
  par mises au carré successives.
- `td1_2.py` : réponses aux questions 3 à 9 de l'exercice (affichages).
- `test_markov.py` : tests unitaires.

## Lancer

    python td1_2.py
    python -m unittest -v

## Résultats

- Depuis (1,0,0), (0,1,0), (0,0,1) ou (1/3,1/3,1/3), pi(n) converge vers le
  même vecteur : pi ≈ (0.1786, 0.6786, 0.1429), c'est-à-dire (5/28, 19/28, 4/28).
- Les matrices P^n ont des lignes de plus en plus proches ; dès P^16 elles
  sont égales à 4 décimales. P^1024 a trois lignes identiques.
- Chaque ligne de P^1024 est la limite de pi(n) en partant de l'état
  correspondant : e_i x P^n est la ligne i de P^n.
- Ce vecteur vérifie pi x P = pi : c'est la distribution stationnaire.

## Pourquoi

La chaîne est irréductible et apériodique (donc ergodique) : elle oublie son
état de départ, et la limite ne dépend pas de la distribution initiale.
Ce même principe est utilisé par PageRank (distribution stationnaire de la
matrice G du surfer aléatoire).
