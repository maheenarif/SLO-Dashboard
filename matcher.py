from sentence_transformers import SentenceTransformer, util
import pandas as pd

# Load model only once
model = SentenceTransformer('all-MiniLM-L6-v2')

def match_slos(user_input, slo_df, top_n=3):
    if slo_df is None or slo_df.empty:
        return None

    slo_texts = slo_df["SLO_Text"].fillna("").tolist()
    slo_embeddings = model.encode(slo_texts, convert_to_tensor=True)
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(user_embedding, slo_embeddings)[0]
    top_indices = scores.argsort(descending=True)[:top_n]

    matches = slo_df.iloc[top_indices]
    matches = matches.copy()
    matches["Similarity"] = [float(scores[i]) for i in top_indices]
    return matches[["SLO_Text", "Bloom_Level", "Similarity"]]
