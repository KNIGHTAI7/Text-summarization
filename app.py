import nltk
nltk.download("punkt")
nltk.download("punkt_tab")

import streamlit as st
import pickle
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Load model
with open("nlp_multidim.pkl", "rb") as f:
    model = pickle.load(f)

domain_classifier = model["domain_classifier"]
summarizer = model["summarizer"]


# ----------------------
# 🌈 PAGE CONFIGURATION
# ----------------------
st.set_page_config(
    page_title="AI Summarizer",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Beauty
st.markdown("""
<style>
/* Main Background */
.main {
    background-color: #f7f9fc;
}

/* Input box styling */
textarea {
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* Output card styling */
.output-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Title text */
.app-title {
    font-size: 40px;
    font-weight: bold;
    color: #2b2b2b;
    text-align: center;
    padding-bottom: 10px;
}

/* Domain badge */
.badge {
    display: inline-block;
    padding: 5px 15px;
    background-color: #007bff;
    color: white;
    border-radius: 20px;
    font-size: 14px;
    margin-bottom: 12px;
}

/* Summary text */
.summary-text {
    font-size: 17px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)


# ----------------------
# HEADER
# ----------------------
st.markdown("<h1 class='app-title'>📘 AI-Powered Text Summarization</h1>", unsafe_allow_html=True)
st.write("Transform long articles into clean **Title + Domain + Summary** effortlessly.")


# ----------------------
# INPUT AREA
# ----------------------
article = st.text_area("✍️ Paste your text/article below:", height=260)


# ----------------------
# PROCESS BUTTON
# ----------------------
if st.button("✨ Generate Summary", use_container_width=True):

    if article.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:

        # DOMAIN
        domain = domain_classifier.predict([article])[0]

        # SUMMARY (3–4 sentences)
        parser = PlaintextParser.from_string(article, Tokenizer("english"))
        summary_sentences = summarizer(parser.document, 4)
        summary = " ".join(str(s) for s in summary_sentences)

        # TITLE
        title = summary.split(".")[0][:60]


        # ----------------------
        # OUTPUT CARDS
        # ----------------------

        # Title Card
        st.markdown("<div class='output-card'>", unsafe_allow_html=True)
        st.subheader("🧾 Generated Title")
        st.markdown(f"### {title}")
        st.markdown("</div>", unsafe_allow_html=True)

        # Domain Card
        st.markdown("<div class='output-card'>", unsafe_allow_html=True)
        st.subheader("🏷 Predicted Domain")
        st.markdown(f"<span class='badge'>{domain}</span>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Summary Card
        st.markdown("<div class='output-card'>", unsafe_allow_html=True)
        st.subheader("📄 Summary (3–4 sentences)")
        st.markdown(f"<p class='summary-text'>{summary}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)


# ----------------------
# FOOTER
# ----------------------
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit + Python NLP")
