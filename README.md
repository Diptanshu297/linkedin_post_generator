# 🚀 LinkedIn Post Generator – AI-Powered Content Creator for LinkedIn

Welcome to the **LinkedIn Post Generator** — a simple yet powerful web app that uses AI to help you create professional, personalized, and engaging job-style posts for LinkedIn in just a few seconds.

Whether you're:

* A **job seeker** writing impactful posts about your journey,
* A **recruiter or company** looking to write attractive job listings, or
* A **content creator** trying to polish your voice on LinkedIn...

👉 This app helps you do it faster, better, and smarter — with **zero effort**.

---

## 🌟 Features – What This App Can Do

✔️ **Dynamic Job Post Creation**
Choose your own job title, tone, language (English or Hinglish), and topic. The app generates a customized LinkedIn post for you — using AI!

✔️ **Rewrite Any Post**
Already wrote a post? Just paste it in, type your instruction (like “make it funnier”), and let AI rewrite it for you.

✔️ **Enhance Posts with Hashtags & CTAs**
Get more reach with automatically added hashtags and strong calls-to-action like “What do you think?” or “Share your thoughts!”

✔️ **Live Preview**
As soon as your post is generated or rewritten, it appears instantly on screen — no reload, no wait.

✔️ **Streamlit UI**
A clean and minimal user interface built with [Streamlit](https://streamlit.io), which runs in your browser locally.

---

## 🧠 How It Works – Under the Hood

This project has two main parts:

### 1. **Frontend (User Interface) – app.py**

* Built using **Streamlit**
* Lets you select post length, tone, language, and topic
* Contains buttons to **Generate**, **Rewrite**, or **Enhance** a post
* Shows the output instantly in the browser

### 2. **Backend (Logic) – post\_generator.py**

* Uses an AI model (e.g. via Groq or Hugging Face API)
* Formats your inputs into prompts
* Sends prompts to the LLM (Language Model)
* Returns clean and well-structured post text

---

## 🛠️ Tech Stack

* 🐍 **Python 3.10+**
* ⚡ **Streamlit** for UI
* 🧠 **LangChain + Groq / Hugging Face** for AI
* 🔐 `.env` for API keys (not public)
* 📦 `requirements.txt` for dependencies

---

## 📁 File Overview

| File                | Purpose                                             |
| ------------------- | --------------------------------------------------- |
| `app.py`            | Streamlit frontend – handles UI                     |
| `post_generator.py` | Main logic – sends input to LLM and returns results |
| `llm_helper.py`     | Connects to the Groq AI model using secure API key  |
| `requirements.txt`  | All Python packages needed to run the app           |
| `.env`              | Contains your secret API key (not pushed to GitHub) |

---

## 🚀 How To Run It (For Total Beginners)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Diptanshu297/linkedin_post_generator.git
cd linkedin_post_generator
```

### Step 2: Install Dependencies

Make sure you have Python 3.10+ installed. Then run:

```bash
pip install -r requirements.txt
```

### Step 3: Set Your API Key

Create a `.env` file and add:

```
GROQ_API_KEY=your_real_key_here
```

You’ll need a [Groq API key](https://console.groq.com/) (or Hugging Face key if you're using those models).

### Step 4: Run the App

```bash
streamlit run app.py
```

Then go to `http://localhost:8501` in your browser. That’s it!

---

## 💡 Common Questions

### ❓ “Does this require a GPU?”

**No.** The app connects to Groq (or other hosted models), so your computer does **not** need a graphics card. It runs entirely using cloud-hosted AI.

### ❓ “Why not use Sentence Transformers?”

Because the app doesn’t need vector search or similarity — it needs **natural language generation**. Sentence Transformers are great for embeddings, not content creation. Also, Groq gives ultra-fast, clean outputs without setup.

### ❓ “Is this the same as a job simulator?”

**No!** This is a **LinkedIn Post Generator**, not a simulator or game. It helps write real text that can be published on LinkedIn.

---

## 🤝 Contribute

Want to improve this? You’re welcome to:

* Add more tones or languages
* Improve prompt logic
* Add post scheduling or image generation
* Enhance UI with CSS/custom layout

Fork it, build it, and submit a PR!

---

## 🚀 Try it Yourself!

Click that GitHub link, follow the steps, and start generating content like a pro 💼✨
Let the AI do the heavy lifting — you just hit "Post" 🙌
