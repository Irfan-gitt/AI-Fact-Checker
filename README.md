# 🔍 AI Fact Checker

An AI-powered web application that detects fake news from **text**, verifies claims using real-time web search, and generates clear explanations with supporting sources.

---

## 🚀 Features

- 🧠 AI Fact Verification – Analyze text-based claims using LLMs  
- 🌐 Real-time Web Search – Cross-check information from multiple sources  
- 📄 Detailed Explanations – Understand why a claim is true/false  
- 🔗 Source References – Get supporting evidence  

⚠️ Image-based fact checking is planned for a future update.
---

## 🛠️ Tech Stack

* **Backend:** Django
* **AI / LLM:** Groq API
* **Search:** DDGS (DuckDuckGo Search)
* **Environment:** Python, dotenv
* **Frontend:** Minimal UI (AI-assisted design, customized and integrated manually)

---

## 📸 How It Works

1. Enter a claim or upload an image
2. The system performs a web search
3. AI analyzes the claim against available information
4. Returns:

   * ✅ Verdict (True / False / Uncertain)
   * 📄 Explanation
   * 🔗 Supporting sources

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/ai-fact-checker.git

cd ai-fact-checker

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 💡 Future Improvements

* 🔄 Add conversation memory
* 📊 Confidence scoring improvements
* 🧠 RAG-based document verification
* 🎙️ Voice-based fact checking
* 🌍 Deploy as a public API
* 🖼️ Image-based fact checking (coming soon)

---

## ⚠️ Disclaimer

This tool uses AI and web data for analysis. Results may not always be 100% accurate. Always verify critical information from trusted sources.

---

## 👨‍💻 Author

Built as part of my journey into **Generative AI development**, focusing on real-world AI applications and system integration.

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork or contribute!

