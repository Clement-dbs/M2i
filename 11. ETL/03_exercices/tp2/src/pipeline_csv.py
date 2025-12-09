import os
import pandas as pd

from src.pipeline.pipeline_base import ETLPipeline        # ETLPipeline générique déjà existante
from src.extractors.extractors import CSVExtractor

class CSVPipeline(ETLPipeline):


    def _extract(self) -> pd.DataFrame:
        """Extraction des posts depuis l'API JSONPlaceholder."""

        # 1) Récupérer l'URL de base de l'API depuis la config
        base_url = self.config["csv"]["base_url"]

        self.extractor = CSVExtractor(
            logger=self.logger,
            base_url=base_url
        )

        df = self.extractor.extract("products.csv")


        # À ce stade, df est un DataFrame avec les colonnes JSONPlaceholder :
        # userId, id, title, body
        return df
    
    def _transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """Nettoie, valide et enrichit les données issues de l'API."""

        # 1) Nettoyage générique (doublons, colonnes vides, trim des strings)
        df_clean = self.transformer.clean(data)

        # 2) Validation de la présence de colonnes clés
        required_cols = ["date", "produit_id", "quantite", "prix_unitaire", 'client_id']
        required_cols = ["nom", "categorie"]

        self.transformer.validate(df_clean, required_cols)

        # 3) Enrichissement : ajout d'une colonne "title_length"
        def add_enrich(df: pd.DataFrame) -> pd.DataFrame:
            df = df.copy()
            return df

        df_enriched = self.transformer.enrich(df_clean, add_enrich)

        return df_enriched
    
    def _load(self,data: pd.DataFrame) -> None:
        """Charge les données transformées dans un fichier Excel."""

        # Dossier de sortie depuis la config
        output_dir = self.config["paths"]["output"]
        os.makedirs(output_dir, exist_ok=True)

        # Nom du fichier de sortie Excel
        output_file = os.path.join(output_dir, "products.xlsx")

        # Utilisation du DataLoader pour écrire en Excel
        self.loader.load_excel(
            df=data,
            filepath=output_file,
            sheet_name="products"
        )

        # À la fin, on aura un fichier data/output/posts_api.xlsx