🚀 STREAMLIT MODEL LINK 

https://text-summarization-zp73bsdnmhpjx3jxkpn7i9.streamlit.app/



📘 Text Summarization & Keyword Extraction (Multi-Dimensional NLP Project)
🚀 Project Overview

This project is a multi-task NLP system that analyzes long-form articles and generates structured insights including:

Auto-generated Title

Predicted Domain/Category

Medium-length Summary (3–4 sentences)

(Optional Internal Feature) Uses TextRank for extractive summarization and TF-IDF + Naive Bayes for domain classification.

No transformer models are used — making it lightweight, fast, and easy to deploy.

🧠 Features

✅ Extractive text summarization using TextRank algorithm
✅ Domain classification via TF-IDF + Multinomial Naive Bayes
✅ Automatic title generation from key summary sentence
✅ Generates clean structured output
✅ Deployable on Streamlit Cloud
✅ Works efficiently on small synthetic datasets

📊 Example Output Format

📝 Title
Initial Public Offering (IPO) can be defined as the process

🌐 Domain
health

✅ Summary
Initial Public Offering (IPO) can be defined as the process in which a private company or corporation can become public by selling a portion of its stake to the investors.
An IPO is generally initiated to infuse the new equity capital to the firm, to facilitate easy trading of the existing assets, to raise capital for the future or to
monetize the investments made by existing stakeholders. The institutional investors, high net worth individuals (HNIs) and the public can access the details of the first 
sale of shares in the prospectus. Once the IPO is done, the shares of the firm are listed and can be traded freely in the open market.

| Component             | Library / Tool                      |
| --------------------- | ----------------------------------- |
| Programming Language  | Python                              |
| Summary Generation    | sumy (TextRank)                     |
| Domain Classification | scikit-learn (TF-IDF + Naive Bayes) |
| Model Storage         | pickle (.pkl)                       |
| UI Dashboard          | Streamlit                           |
| Deployment            | Streamlit Cloud + GitHub            |

