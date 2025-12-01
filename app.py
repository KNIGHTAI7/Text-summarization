import streamlit as st
import pickle
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# Load Pickle Model
with open("nlp_multidim.pkl", "rb") as f:
    model = pickle.load(f)

domain_classifier = model["domain_classifier"]
summarizer = model["summarizer"]

st.title("🤖 NLP - Text Analyzer")

article = st.text_area("Paste your long article here:", height=250)

if st.button("Generate Output"):
    if article.strip():

        # Predict Domain
        domain = domain_classifier.predict([article])[0]

        # Generate Summary (medium: 3–4 sentences approx)
        parser = PlaintextParser.from_string(article, Tokenizer("english"))
        summary_sentences = summarizer(parser.document, 4)  # 4 key sentences

        summary = " ".join(str(s) for s in summary_sentences)

        # Generate Title (first summary sentence shortened)
        title = summary.split(".")[0][:60]

        # Final outputs
        st.subheader("📝 Title")
        st.write(title)

        st.subheader("🌐 Domain")
        st.write(domain)

        st.subheader("✅ Summary")
        st.write(summary)

    else:
        st.warning("Please enter some text!")
