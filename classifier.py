from sentence_transformers import SentenceTransformer, util

# Load your fine-tuned model
model = SentenceTransformer('fine_tuned_model')

def classify_question(question, slo_texts):
    question_embedding = model.encode(question, convert_to_tensor=True)
    slo_embeddings = model.encode(slo_texts, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(question_embedding, slo_embeddings)
    best_score, best_idx = float(cosine_scores.max()), int(cosine_scores.argmax())

    return best_score, slo_texts[best_idx]
