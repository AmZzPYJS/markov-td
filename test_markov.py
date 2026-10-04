import unittest

from markov import P, ecart, iterer, multiplier, produit, puissances_de_deux


class TestMarkov(unittest.TestCase):
    def test_un_pas_depuis_un_etat_donne_la_ligne_de_p(self):
        self.assertEqual(multiplier([1, 0, 0], P), P[0])
        self.assertEqual(multiplier([0, 0, 1], P), P[2])

    def test_une_distribution_reste_une_distribution(self):
        for pi in iterer([0.2, 0.5, 0.3], P, 12):
            self.assertAlmostEqual(sum(pi), 1.0)

    def test_p_au_carre(self):
        attendu = [
            [0.24, 0.56, 0.20],
            [0.16, 0.76, 0.08],
            [0.19, 0.44, 0.37],
        ]
        resultat = produit(P, P)
        for ligne, ligne_attendue in zip(resultat, attendu):
            for a, b in zip(ligne, ligne_attendue):
                self.assertAlmostEqual(a, b)

    def test_mise_au_carre_repetee(self):
        puissances = puissances_de_deux(P, 3)
        p4 = produit(produit(P, P), produit(P, P))
        for ligne, ligne_attendue in zip(puissances[4], p4):
            self.assertAlmostEqual(ecart(ligne, ligne_attendue), 0.0)

    def test_les_lignes_de_p1024_sont_identiques_et_stationnaires(self):
        p1024 = puissances_de_deux(P, 10)[1024]
        for ligne in p1024:
            self.assertAlmostEqual(sum(ligne), 1.0)
            self.assertAlmostEqual(ecart(ligne, p1024[0]), 0.0)
        self.assertAlmostEqual(ecart(multiplier(p1024[0], P), p1024[0]), 0.0)


if __name__ == "__main__":
    unittest.main()
