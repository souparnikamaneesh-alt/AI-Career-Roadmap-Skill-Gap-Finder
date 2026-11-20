# 🎯 AI Career Roadmap & Skill Gap Finder

A working AI-powered web prototype built with **Python**, **Streamlit**, and the **Google Gemini API** (`gemini-2.5-flash`).

This application solves a critical problem faced by students: **they know which job role they want to target, but don't know what to learn, what order to learn it in, or what hands-on projects to build to get hired.**

---

## 📌 Problem Statement & Solution

| Item | Details |
| :--- | :--- |
| **Problem** | Students often have disjointed skills (e.g., C programming from college, basic Python syntax, HTML) and aspire to roles like **Data Scientist** or **Full Stack Developer**, but suffer from tutorial paralysis, lack of structured sequencing, and missing portfolio proof. |
| **Inputs** | 1. Current skills baseline (e.g. `C, basic Python, HTML`)<br>2. Target dream role (e.g. `Data Scientist`)<br>3. Available study time (e.g. `15 hours/week`) |
| **Outputs** | 1. **Skill Gap Analysis**: Side-by-side comparison table of "Skills You Have" vs. "Skills to Learn" with priority badges and action items.<br>2. **8-Week Structured Roadmap**: Sequential, week-by-week curriculum tailored to available weekly study hours with weekly milestones.<br>3. **3 Portfolio Mini-Projects**: Practical resume-worthy projects with tech stacks and demonstrated skills.<br>4. **Downloadable Report**: One-click `.md` export of the entire career plan. |
| **AI Model** | Google Gemini API (`gemini-2.5-flash`) via official `google-genai` SDK + built-in offline simulation engine for immediate testing. |

---

## 🚀 How to Run the App

### Option A: One-Click Launch (Windows)
Simply double-click the included file:
```
run_app.bat
```
This automatically launches Streamlit in your default browser at `http://localhost:8501`.

---

### Option B: From Terminal / Command Prompt / VS Code
1. Open PowerShell or Command Prompt in this folder:
   ```powershell
   cd "c:\Users\D E L L\OneDrive\Desktop\anti gravity\GEN AI"
   ```

2. Run Streamlit using Python:
   ```powershell
   & "C:\Users\D E L L\AppData\Local\Python\bin\python.exe" -m streamlit run app.py
   ```
   *(Or if `python` is added to your PATH, simply: `streamlit run app.py`)*

3. The application will open in your browser at:
   ```
   http://localhost:8501
   ```

---

## 🔑 How to Add Your Gemini API Key (Free)

1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in with your Google account.
2. Click **"Get API key"** and create a free key.
3. You can use your key in either of two ways:
   - **In the Web App:** Paste it into the **Google Gemini API Key** field in the left sidebar.
   - **In a `.env` file:** Copy `.env.example` to `.env` and paste:
     ```env
     GEMINI_API_KEY=AIzaSy...
     ```
4. **Note:** The app also includes a **"Built-in AI Simulation"** checkbox enabled by default. This ensures you can test the app, review the full UI, and take your submission screenshot immediately without waiting for an API key!

---

## 📸 Taking Your Submission Screenshot

1. Open `http://localhost:8501` in your browser.
2. Under **Quick Presets** in the sidebar, select **"Data Science Aspirant (C, basic Python, HTML)"** (or enter your own custom skills and target role).
3. Click the purple button: **"🚀 Analyze Gap & Generate 8-Week Roadmap"**.
4. You will see:
   - Strategy Overview with 4 KPI cards (Match Readiness %, 8 Weeks, Total Hours, 3 Projects).
   - **Tab 1:** Skills You Have vs. Skills You Need to Learn (Clean table with color status badges).
   - **Tab 2:** 8-Week Week-by-Week Learning Roadmap (Expandable cards for each week).
   - **Tab 3:** 3 Portfolio Mini-Projects (Project cards with tech stack badges).
5. Take a screenshot showing the header, inputs, and output sections for your Google Form submission!

---

## 🧠 Code Architecture & Explanation (Viva Guide)

If asked to explain your prototype in an interview or viva, here is what you need to know:

### 1. User Interface Layer (`Streamlit`)
- **`st.set_page_config` & Custom CSS:** Injects modern dark-theme styles, gradient typography, and hover-animated cards for an attractive, recruiter-ready presentation.
- **`st.columns` & `st.tabs`:** Separates user inputs cleanly from results, and divides the 3 main outputs into organized tabs so the user is not overwhelmed by text.
- **`st.dataframe`:** Renders the skill gap analysis in an interactive tabular grid with customized column configurations.

### 2. AI Intelligence Layer (`google-genai` + Gemini 2.5 Flash)
- **Prompt Engineering:** The prompt uses role conditioning (`You are an expert AI Career Coach...`) and provides few-shot structured constraints.
- **Strict JSON Schema (`response_mime_type="application/json"`):** Guarantees that Gemini returns structured, parseable JSON rather than unformatted prose, making it reliable to render into tables, roadmap accordions, and cards.
- **Low Temperature (`0.2`):** Low temperature ensures the output is focused, deterministic, and accurate to technical career paths rather than hallucinatory.

### 3. Graceful Fallback Architecture
- If network connection drops or the user doesn't have an API key, `get_mock_roadmap()` provides realistic, role-specific curriculum data so the application never breaks or throws an unhandled crash.

---

## 📦 Project File Structure
```
GEN AI/
├── app.py              # Main Streamlit application source code
├── requirements.txt    # Python dependencies (streamlit, google-genai, pandas, python-dotenv)
├── run_app.bat         # 1-click launcher script for Windows
├── .env.example        # Environment variable template for GEMINI_API_KEY
└── README.md           # Documentation, viva explanation, and instructions
```
