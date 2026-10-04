"""TD1, exercice 1.2 : limite, limite (MIN26102, Modèles stochastiques)."""

from markov import P, ecart, iterer, multiplier, puissances_de_deux

VECTEURS_INITIAUX = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [1 / 3, 1 / 3, 1 / 3],
]


def texte(vecteur):
    """Met en forme un vecteur sur une ligne."""
    return "(" + ", ".join(f"{x:.4f}" for x in vecteur) + ")"


def texte_matrice(matrice):
    """Met en forme une matrice, une ligne par ligne."""
    return "\n".join("    " + texte(ligne) for ligne in matrice)


def questions_3_a_6():
    print("=== Questions 3 à 6 : pi(n+1) = pi(n) x P ===")
    print("Un pas depuis (1, 0, 0) :", texte(multiplier([1, 0, 0], P)))

    limites = []
    for pi0 in VECTEURS_INITIAUX:
        print(f"\nDépart {texte(pi0)}")
        suite = iterer(pi0, P, 12)
        for n, pi in enumerate(suite):
            print(f"  n = {n:2d} : {texte(pi)}")
        limites.append(suite[-1])

    pire_ecart = max(ecart(limites[0], autre) for autre in limites)
    print("\nConstat : après 12 pas, tous les départs donnent le même vecteur.")
    print(f"Écart maximal entre les résultats : {pire_ecart:.2e}")
    return limites


def questions_7_et_8():
    print("\n=== Questions 7 et 8 : P^2, P^4, ..., P^1024 ===")
    puissances = puissances_de_deux(P, 10)
    for exposant in (2, 4, 8, 16, 1024):
        print(f"\nP^{exposant} =")
        print(texte_matrice(puissances[exposant]))
    return puissances[1024]


def question_9(limites, p1024):
    print("\n=== Question 9 : lien entre P^1024 et les vecteurs ===")
    for i, ligne in enumerate(p1024):
        print(
            f"Ligne {i + 1} de P^1024 vs limite depuis e{i + 1} : "
            f"écart = {ecart(ligne, limites[i]):.2e}"
        )
    print(
        "\nConclusion : chaque ligne de P^1024 est la limite de pi(n) quand "
        "on part de l'état i.\nComme la chaîne est ergodique, toutes les "
        "lignes sont égales à la distribution stationnaire :"
    )
    print("  pi =", texte(p1024[0]))
    print("  Vérification pi x P = pi, écart :",
          f"{ecart(multiplier(p1024[0], P), p1024[0]):.2e}")


if __name__ == "__main__":
    limites_pi = questions_3_a_6()
    matrice_1024 = questions_7_et_8()
    question_9(limites_pi, matrice_1024)
