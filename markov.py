"""Outils pour les chaînes de Markov en temps discret (espace d'états fini).

Une distribution est une liste de réels positifs dont la somme vaut 1.
Une matrice de transition est une liste de lignes, chaque ligne étant
une distribution.
"""

# Matrice de transition de l'exercice 1.2 (états 1, 2, 3).
P = [
    [0.0, 0.6, 0.4],
    [0.2, 0.8, 0.0],
    [0.3, 0.2, 0.5],
]


def multiplier(pi, matrice):
    """Retourne pi x matrice : la distribution après un pas de la chaîne.

    La composante j du résultat est la somme, sur tous les états i,
    de pi[i] * matrice[i][j] (ce que chaque état i envoie vers j).
    """
    n = len(pi)
    return [sum(pi[i] * matrice[i][j] for i in range(n)) for j in range(n)]


def iterer(pi0, matrice, n_max=12):
    """Retourne la liste [pi(0), pi(1), ..., pi(n_max)]."""
    suite = [list(pi0)]
    for _ in range(n_max):
        suite.append(multiplier(suite[-1], matrice))
    return suite


def produit(a, b):
    """Retourne le produit matriciel a x b (matrices carrées)."""
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def puissances_de_deux(matrice, exposant_max=10):
    """Retourne {2: P^2, 4: P^4, ..., 2**exposant_max: P^(2**exposant_max)}.

    Chaque matrice est obtenue en mettant la précédente au carré :
    seulement 10 produits matriciels pour atteindre P^1024.
    """
    resultat = {}
    courante = matrice
    for k in range(1, exposant_max + 1):
        courante = produit(courante, courante)
        resultat[2 ** k] = courante
    return resultat


def ecart(u, v):
    """Retourne la norme 1 de u - v (somme des écarts en valeur absolue)."""
    return sum(abs(a - b) for a, b in zip(u, v))
