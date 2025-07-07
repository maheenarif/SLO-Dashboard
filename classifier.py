def classify_bloom_levels(text):
    text = text.lower()

    # Simple keyword rules based on Bloom’s Taxonomy verbs
    rules = {
        "Remembering": ["define", "list", "recall", "identify", "label", "name", "state"],
        "Understanding": ["describe", "explain", "summarize", "interpret", "classify", "discuss"],
        "Applying": ["solve", "use", "demonstrate", "implement", "apply", "carry out"],
        "Analyzing": ["differentiate", "analyze", "compare", "contrast", "distinguish", "organize"],
        "Evaluating": ["evaluate", "justify", "critique", "argue", "defend", "assess"],
        "Creating": ["design", "create", "develop", "construct", "formulate", "compose"]
    }

    for level, keywords in rules.items():
        for kw in keywords:
            if kw in text:
                return level

    return "Unclassified"
