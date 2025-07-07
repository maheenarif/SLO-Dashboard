import streamlit as st
import pandas as pd
from classifier import classify_bloom_levels
from matcher import match_slos

# Load SLO database
@st.cache_data
def load_slo_database():
    df = pd.read_excel("slo_database.xlsx", sheet_name=None)
    merged = pd.concat([df[sheet] for sheet in list(df.keys())[:3]], ignore_index=True)
    slo_col = merged.columns[3]
    bloom_col = merged.columns[4]
    return merged[[slo_col, bloom_col]].rename(columns={slo_col: "SLO_Text", bloom_col: "Bloom_Level"})

slo_df = load_slo_database()

# Streamlit UI
st.title("SLO Alignment & Bloom's Taxonomy Dashboard")

user_input = st.text_area("Enter your question or paragraph:")

if user_input:
    st.subheader("Analysis Result")

    # Bloom Classification
    bloom_level = classify_bloom_levels(user_input)
    st.write(f"**Bloom's Level:** {bloom_level}")

    # SLO Matching
    matches = match_slos(user_input, slo_df)
    if matches is not None and not matches.empty:
        st.write("**Top Matching SLOs:**")
        st.dataframe(matches)
    else:
        st.write("No strong SLO match found.")
