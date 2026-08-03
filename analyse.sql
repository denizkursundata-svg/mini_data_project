SELECT
    categorie,
    count(id_vente) AS nombre_ventes,
    ROUND(AVG(montant), 2) AS panier_moyen,
    SUM(montant) AS chiffre_affaires_total
FROM ventes
WHERE data_vente >= '2026-01-01'
GROUP BY categorie
ORDER BY chiffre_affaires_total DESC;    