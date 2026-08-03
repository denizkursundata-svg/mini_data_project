import sqlite3
import pandas as pd

def main():
    print("🚀 Démarrage du pipeline d'analyse Data...")
    
    # Création d'une base SQLite temporaire en mémoire
    conn = sqlite3.connect(":memory:")
    
    # Création de la table et données de test
    data = pd.DataFrame({
        'id_vente': [1, 2, 3, 4, 5],
        'categorie': ['Electronique', 'Livres', 'Electronique', 'Vetements', 'Livres'],
        'montant': [299.99, 15.50, 120.00, 45.00, 22.00],
        'date_vente': ['2026-02-10', '2026-02-12', '2026-03-01', '2026-03-05', '2026-03-10']
    })
    
    data.to_sql('ventes', conn, index=False, if_exists='replace')
    
    # Lecture de la requête SQL depuis analyse.sql
    with open("analyse.sql", "r", encoding="utf-8") as f:
        query = f.read()
        
    df_result = pd.read_sql_query(query, conn)
    print("\n📊 Résultats de l'analyse SQL :")
    print(df_result)

if __name__ == "__main__":
    main()