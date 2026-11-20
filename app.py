"""
AI Career Roadmap & Skill Gap Finder
A simple, powerful Streamlit web app powered by Google Gemini API.
"""

import json
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Load local environment variables if available
load_dotenv()

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Career Roadmap & Skill Gap Finder",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern, clean, recruiter-ready UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #0e1117;
    }
    
    /* Header typography */
    .app-title {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #4F46E5, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .app-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    
    /* Metric Cards */
    .metric-card {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: #6366F1;
    }
    .metric-num {
        font-size: 1.8rem;
        font-weight: 700;
        color: #38BDF8;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.3rem;
    }
    
    /* Project Cards */
    .project-card {
        background: #1E293B;
        border-left: 4px solid #6366F1;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .project-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.4rem;
    }
    .project-desc {
        color: #CBD5E1;
        font-size: 0.93rem;
        margin-bottom: 0.6rem;
    }
    .badge {
        display: inline-block;
        background: #312E81;
        color: #A5B4FC;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.4rem;
        margin-bottom: 0.3rem;
    }
    .badge-alt {
        display: inline-block;
        background: #064E3B;
        color: #6EE7B7;
        padding: 0.2rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Preset Scenarios for Quick Testing
# ---------------------------------------------------------
PRESETS = {
    "Select a preset (optional)...": {
        "role": "Data Scientist",
        "skills": "",
        "hours": 15
    },
    "Data Science Aspirant (C, basic Python, HTML)": {
        "role": "Data Scientist",
        "skills": "C, basic Python, HTML, basic Git",
        "hours": 15
    },
    "Full-Stack Web Dev Path (HTML, basic JS)": {
        "role": "Full Stack Web Developer",
        "skills": "HTML, CSS, basic JavaScript, Git",
        "hours": 12
    },
    "AI/ML Engineer Aspirant (Python, SQL)": {
        "role": "AI / Machine Learning Engineer",
        "skills": "Python, SQL, Linear Algebra, basic Linux",
        "hours": 20
    },
    "Cloud / DevOps Aspirant (Linux, Python Basics)": {
        "role": "Cloud & DevOps Engineer",
        "skills": "Basic Linux, Python scripting, Bash, Networking basics",
        "hours": 10
    }
}

ROLE_OPTIONS = [
    "Data Scientist",
    "Full Stack Web Developer",
    "AI / Machine Learning Engineer",
    "Cloud & DevOps Engineer",
    "Data Analyst",
    "Cybersecurity Analyst",
    "Mobile App Developer (Flutter / React Native)",
    "Backend Engineer (FastAPI / Go / Java)",
    "Custom (Type your own below)"
]


# ---------------------------------------------------------
# Sidebar Configuration & Keys
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/compass.png", width=64)
    st.title("Settings & Keys")
    st.markdown("Configure your Gemini AI model access.")
    
    api_key_env = os.getenv("GEMINI_API_KEY", "")
    api_key_input = st.text_input(
        "Google Gemini API Key",
        value=api_key_env,
        type="password",
        help="Get your free API key at https://aistudio.google.com"
    )
    
    use_demo = st.checkbox(
        "Use Built-in AI Simulation (No API key needed)",
        value=(not bool(api_key_input)),
        help="Check this if you want to test the app immediately without providing an API key."
    )
    
    st.markdown("---")
    st.markdown("### 💡 Quick Presets")
    selected_preset = st.selectbox("Load sample student profile:", list(PRESETS.keys()))
    
    st.markdown("---")
    st.markdown(
        """
        **About This Tool:**
        - **Target:** Bridge student skill gaps
        - **Model:** Gemini 2.5 Flash / Demo Engine
        - **Output:** Gap Table, 8-Week Plan, 3 Projects
        """
    )
    st.caption("Built for AI Prototype Assignment")


# ---------------------------------------------------------
# Mock / Fallback Generator (Ensures 100% Reliability)
# ---------------------------------------------------------
def get_mock_roadmap(target_role: str, current_skills: str, hours_per_week: int) -> dict:
    """Provides high-quality realistic roadmap data for testing without an API key."""
    role_lower = target_role.lower()
    
    # Generic skills categorization
    if "data" in role_lower or "scientist" in role_lower:
        have = ["Basic Python syntax", "C programming logic", "HTML markup basics"]
        to_learn = [
            ("Pandas & NumPy", "Data Manipulation", "Critical", "Learn vectorized operations & DataFrame aggregations"),
            ("Data Visualization (Matplotlib, Seaborn)", "Analysis", "High", "Build exploratory data analysis charts"),
            ("Statistical Inference & Probability", "Math/Stats", "Critical", "Hypothesis testing, distributions, p-values"),
            ("Scikit-Learn (Supervised ML)", "Machine Learning", "Critical", "Regression, classification, model evaluation"),
            ("Feature Engineering & Preprocessing", "Machine Learning", "High", "Encoding, scaling, imputation techniques"),
            ("SQL & Database Querying", "Data Management", "Critical", "Joins, window functions, aggregations"),
            ("Model Deployment (Streamlit / FastAPI)", "Production", "Medium", "Deploy ML models as interactive web apps")
        ]
        projects = [
            {
                "title": "Interactive Automated EDA & Dataset Profiler",
                "desc": "A web application where users upload any CSV file and get automated distribution plots, outlier flags, correlation heatmaps, and downloadable cleaning summaries.",
                "tech": ["Python", "Pandas", "Streamlit", "Plotly"],
                "skills_demonstrated": "Data wrangling, automated analytics, exploratory data visualization"
            },
            {
                "title": "End-to-End Customer Churn Predictor",
                "desc": "A production-grade machine learning model trained on telecom customer data with feature importance explanations (SHAP) and a live prediction interface.",
                "tech": ["Scikit-Learn", "XGBoost", "Streamlit", "SHAP"],
                "skills_demonstrated": "Supervised classification, metric evaluation (ROC-AUC, F1), model explainability"
            },
            {
                "title": "Real-Estate Price Estimation API & Dashboard",
                "desc": "A regression pipeline predicting housing valuations from multi-feature tabular inputs, complete with error analysis and residual diagnostic plots.",
                "tech": ["Python", "Pandas", "Scikit-Learn", "FastAPI / Streamlit"],
                "skills_demonstrated": "Feature engineering, regression tuning, interactive deployment"
            }
        ]
    elif "web" in role_lower or "full" in role_lower or "frontend" in role_lower:
        have = ["HTML structure", "Basic CSS styling", "Foundational programming concepts"]
        to_learn = [
            ("Modern JavaScript (ES6+)", "Frontend", "Critical", "Arrow functions, destructuring, async/await, promises"),
            ("DOM Manipulation & Events", "Frontend", "Critical", "Dynamic UI updates without reloading"),
            ("React.js & Component Architecture", "Frontend Framework", "Critical", "Hooks (useState, useEffect), state lifting"),
            ("Node.js & Express.js", "Backend", "Critical", "RESTful API routes, middleware, JSON responses"),
            ("PostgreSQL / MongoDB", "Database", "High", "CRUD schemas, relational querying, indexing"),
            ("Git & GitHub Collaboration", "DevOps", "High", "Branching, pull requests, resolving merge conflicts"),
            ("JWT Authentication & Security", "Backend", "High", "Secure login, token storage, protected endpoints")
        ]
        projects = [
            {
                "title": "Full-Stack Task & Project Management Board",
                "desc": "A Kanban-style task tracker with drag-and-drop columns, user authentication, and persistent MongoDB/PostgreSQL storage.",
                "tech": ["React", "Node.js", "Express", "MongoDB / Tailwind"],
                "skills_demonstrated": "Full CRUD architecture, state management, REST API integration"
            },
            {
                "title": "Collaborative Developer Snippet Stash",
                "desc": "A web platform where developers can save, tag, search, and share code snippets with syntax highlighting and like/save features.",
                "tech": ["React / Next.js", "Tailwind CSS", "Node.js / Supabase"],
                "skills_demonstrated": "Search indexing, responsive UI design, database relational mapping"
            },
            {
                "title": "E-Commerce Micro-Store with Stripe Integration",
                "desc": "A product catalog with cart state, checkout workflow, dummy payment processing, and order history tracking.",
                "tech": ["React", "Express", "Stripe API", "CSS Modules"],
                "skills_demonstrated": "Third-party payment gateways, cart persistence, secure checkout flow"
            }
        ]
    else:
        have = ["Basic coding logic", "Problem solving foundations"]
        to_learn = [
            ("Core Language Specialization", "Foundations", "Critical", "In-depth OOP, memory management, testing"),
            ("Data Structures & Algorithms", "Computer Science", "High", "Arrays, Trees, Graphs, Hash Maps, Big-O"),
            ("System Architecture & REST APIs", "Engineering", "Critical", "API design, status codes, async requests"),
            ("Databases & Data Modeling", "Data Storage", "Critical", "Relational SQL queries and normalization"),
            ("Version Control & CI/CD", "Tooling", "High", "Git workflows, GitHub Actions basic automation"),
            ("Containerization (Docker)", "DevOps", "Medium", "Dockerfiles, container isolation, multi-stage builds"),
            ("Testing & Documentation", "Quality", "High", "Unit tests, mocking, Swagger/OpenAPI docs")
        ]
        projects = [
            {
                "title": f"Production-Ready {target_role} Starter Service",
                "desc": "A containerized backend service featuring structured logging, rate limiting, and automated health checks.",
                "tech": ["Python / Node.js", "Docker", "SQLite / Postgres", "Pytest"],
                "skills_demonstrated": "Modular code organization, unit testing, container deployment"
            },
            {
                "title": "Real-Time Activity Monitor & Metrics Dashboard",
                "desc": "An operational dashboard displaying simulated sensor/system telemetry with live graphs and anomaly threshold alerts.",
                "tech": ["Streamlit / React", "WebSockets / REST", "Plotly"],
                "skills_demonstrated": "Real-time data feeds, event-driven architecture, dashboard design"
            },
            {
                "title": "Portfolio Showcase & Case Study Hub",
                "desc": "A clean personal engineering portfolio featuring interactive demos, live documentation, and contact integration.",
                "tech": ["Markdown", "GitPages / Streamlit / React", "Tailwind"],
                "skills_demonstrated": "Technical communication, project packaging, frontend polish"
            }
        ]
        
    skills_table = []
    for h in have:
        skills_table.append({
            "Skill Name": h,
            "Category": "Acquired Base",
            "Status": "✅ Already Have",
            "Priority": "Strong Base",
            "Action Plan": "Maintain proficiency and leverage in new projects"
        })
    for s, cat, prio, act in to_learn:
        skills_table.append({
            "Skill Name": s,
            "Category": cat,
            "Status": "🎯 Need to Learn",
            "Priority": prio,
            "Action Plan": act
        })

    # Generate 8-week roadmap scaled to available hours
    weekly_modules = [
        ("Week 1: Core Fundamentals & Environment Setup", "Set up professional dev environment, master intermediate language syntax and package managers.", ["Development Tools", "Intermediate Syntax", "Git Version Control"], "Setup repo & build first standalone script"),
        ("Week 2: Data Structures & Core Library Essentials", "Deep dive into essential domain libraries and foundational data transformations.", ["Core Collections", "Library Basics", "Data Ingestion"], "Complete 5 hands-on data manipulation challenges"),
        ("Week 3: In-Depth Applied Concepts & Pipelines", "Build structured functions and pipelines to clean, validate, and process real-world inputs.", ["Pipelines & Functions", "Error Handling", "Validation Rules"], "Create an automated parsing and validation utility"),
        ("Week 4: Mid-Term Portfolio Project #1", "Consolidate first 3 weeks of learning by building and documenting Project 1.", ["Project Scaffolding", "Core Logic Implementation", "Code Cleanliness"], "Publish Project 1 on GitHub with clean README"),
        ("Week 5: Advanced Domain Techniques & Modeling/APIs", "Advance into core role-specific competencies: algorithms, APIs, or advanced state/database handling.", ["Specialized Algorithms / APIs", "Database Integration", "Optimization"], "Implement a connected backend / model scoring routine"),
        ("Week 6: Quality, Testing & Performance Tuning", "Write unit tests, optimize performance, handle edge cases, and refine architectural structure.", ["Unit Testing", "Debugging & Profiling", "Edge Case Coverage"], "Reach >80% test coverage on core modules"),
        ("Week 7: Capstone Project #2 & User Interface", "Build an interactive UI or service layer making the solution accessible to non-technical users.", ["Interface Integration", "User Experience", "State Handling"], "Deploy Project 2 live on Streamlit Cloud or free host"),
        ("Week 8: Portfolio Polish, Packaging & Interview Prep", "Finalize Portfolio Project #3, polish GitHub profile, write case study write-ups for resumes.", ["Documentation Polish", "Resume Bullet Crafting", "Mock Technical Walkthrough"], "Complete 3 project showcase write-ups ready for applications")
    ]
    
    roadmap_list = []
    for idx, (title, summary, topics, milestone) in enumerate(weekly_modules, 1):
        roadmap_list.append({
            "week_num": idx,
            "title": title,
            "allocated_hours": hours_per_week,
            "summary": summary,
            "topics": topics,
            "milestone": milestone
        })
        
    return {
        "match_percentage": 35,
        "current_skills_count": len(have),
        "gap_skills_count": len(to_learn),
        "summary": f"Based on your current baseline ({current_skills}), you have a good logical foundation. To become competitive as a **{target_role}**, focus intensely on domain libraries, structured data handling, and deploying 3 portfolio-ready projects within your {hours_per_week} hrs/week budget.",
        "skills_table": skills_table,
        "roadmap": roadmap_list,
        "projects": projects
    }


# ---------------------------------------------------------
# Gemini API Call Handler
# ---------------------------------------------------------
def generate_gemini_roadmap(api_key: str, target_role: str, current_skills: str, hours_per_week: int) -> dict:
    """Invokes Google Gemini API to generate structured roadmap JSON."""
    try:
        from google import genai
        from google.genai import types

        client = genai.Client(api_key=api_key)
        
        prompt = f"""
You are an expert AI Career Coach and Technical Recruiter.
Analyze this student's profile and create a targeted, practical 8-week learning plan:

- Target Job Role: {target_role}
- Current Skills: {current_skills}
- Available Study Time: {hours_per_week} hours per week
- Target Timeline: 8 Weeks

Respond ONLY with valid, raw JSON (no markdown formatting, no ```json blocks, just the JSON string).
JSON schema to strictly follow:
{{
  "match_percentage": <integer between 10 and 90, e.g. 40>,
  "current_skills_count": <number of relevant skills they already have>,
  "gap_skills_count": <number of critical skills they need to learn>,
  "summary": "<2-3 sentence executive coaching summary>",
  "skills_table": [
    {{
      "Skill Name": "<Skill name>",
      "Category": "<e.g. Programming, Framework, Database, DevOps>",
      "Status": "<Either '✅ Already Have' or '🎯 Need to Learn'>",
      "Priority": "<Critical | High | Medium>",
      "Action Plan": "<Brief 1-line actionable guidance>"
    }}
  ],
  "roadmap": [
    {{
      "week_num": 1,
      "title": "<Week 1 Theme>",
      "allocated_hours": {hours_per_week},
      "summary": "<What to accomplish this week>",
      "topics": ["<Topic 1>", "<Topic 2>", "<Topic 3>"],
      "milestone": "<Concrete mini-task or deliverable for this week>"
    }}
    // Repeat for weeks 2 through 8
  ],
  "projects": [
    {{
      "title": "<Project 1 Title>",
      "desc": "<2-3 sentence description of the project and why it impresses recruiters>",
      "tech": ["<Tech 1>", "<Tech 2>", "<Tech 3>"],
      "skills_demonstrated": "<Key skills demonstrated>"
    }},
    {{
      "title": "<Project 2 Title>",
      "desc": "<Description>",
      "tech": ["<Tech 1>", "<Tech 2>"],
      "skills_demonstrated": "<Skills>"
    }},
    {{
      "title": "<Project 3 Title>",
      "desc": "<Description>",
      "tech": ["<Tech 1>", "<Tech 2>"],
      "skills_demonstrated": "<Skills>"
    }}
  ]
}}
Ensure the skills_table has at least 3 'Already Have' items and at least 5-7 'Need to Learn' items.
Ensure the roadmap has exactly 8 weeks.
Ensure projects has exactly 3 practical mini-projects tailored to the target role.
"""
        # Call Gemini 2.5 Flash
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                response_mime_type="application/json"
            )
        )
        
        raw_text = response.text.strip()
        # Clean any accidental markdown fence if present
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
            
        data = json.loads(raw_text.strip())
        return data
        
    except Exception as e:
        st.warning(f"⚠️ Gemini API returned an error ({e}). Switching smoothly to Built-in AI Engine...")
        return get_mock_roadmap(target_role, current_skills, hours_per_week)


# ---------------------------------------------------------
# Main App Layout & User Inputs
# ---------------------------------------------------------
st.markdown('<div class="app-title">🎯 AI Career Roadmap & Skill Gap Finder</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Compare your current skills with your dream job, identify your gaps, and generate an actionable 8-week plan.</div>', unsafe_allow_html=True)

# Handle presets
default_role = PRESETS[selected_preset]["role"]
default_skills = PRESETS[selected_preset]["skills"]
default_hours = PRESETS[selected_preset]["hours"]

col_input1, col_input2 = st.columns([1, 1], gap="medium")

with col_input1:
    st.subheader("1️⃣ Target Career Goal")
    role_choice = st.selectbox(
        "Select your target job role:",
        options=ROLE_OPTIONS,
        index=ROLE_OPTIONS.index(default_role) if default_role in ROLE_OPTIONS else 0
    )
    if role_choice == "Custom (Type your own below)":
        target_job = st.text_input("Enter your custom target role:", value="Machine Learning Researcher")
    else:
        target_job = role_choice
        
    study_hours = st.slider(
        "Available study hours per week:",
        min_value=5,
        max_value=40,
        value=default_hours,
        step=1,
        help="How many hours you can dedicate each week to self-study and project building."
    )

with col_input2:
    st.subheader("2️⃣ Current Skills Baseline")
    user_skills = st.text_area(
        "List your current skills (languages, tools, libraries):",
        value=default_skills if default_skills else "C, basic Python, HTML, basic Git",
        height=110,
        placeholder="e.g. C programming, basic Python, HTML/CSS, Git basics, SQL"
    )

st.markdown("<br>", unsafe_allow_html=True)
generate_clicked = st.button("🚀 Analyze Gap & Generate 8-Week Roadmap", type="primary", use_container_width=True)


# ---------------------------------------------------------
# Result Processing & Visualization
# ---------------------------------------------------------
if generate_clicked or ("career_data" in st.session_state and st.session_state.get("career_data")):
    if generate_clicked:
        if not user_skills.strip():
            st.error("Please enter at least one current skill to analyze.")
            st.stop()
            
        with st.spinner("Analyzing skill match and synthesizing personalized 8-week roadmap..."):
            active_key = api_key_input.strip()
            if use_demo or not active_key:
                plan_data = get_mock_roadmap(target_job, user_skills, study_hours)
            else:
                plan_data = generate_gemini_roadmap(active_key, target_job, user_skills, study_hours)
            st.session_state["career_data"] = plan_data
            st.session_state["saved_target_job"] = target_job
            st.session_state["saved_skills"] = user_skills
            st.session_state["saved_hours"] = study_hours
    else:
        plan_data = st.session_state["career_data"]
        target_job = st.session_state.get("saved_target_job", target_job)
        user_skills = st.session_state.get("saved_skills", user_skills)
        study_hours = st.session_state.get("saved_hours", study_hours)

    st.markdown("---")
    
    # ------------------ High Level KPIs ------------------
    st.markdown(f"### 📌 Strategy Overview: Path to **{target_job}**")
    st.info(plan_data.get("summary", "Personalized career roadmap ready."))
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        match_score = plan_data.get("match_percentage", 35)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-num">{match_score}%</div>
            <div class="metric-label">Current Role Readiness</div>
        </div>
        """, unsafe_allow_html=True)
    with kpi2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-num">8 Weeks</div>
            <div class="metric-label">Target Duration</div>
        </div>
        """, unsafe_allow_html=True)
    with kpi3:
        total_hrs = study_hours * 8
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-num">{total_hrs} hrs</div>
            <div class="metric-label">Total Planned Effort</div>
        </div>
        """, unsafe_allow_html=True)
    with kpi4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-num">3 Projects</div>
            <div class="metric-label">Portfolio Deliverables</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------ Tabs for Structured Outputs ------------------
    tab1, tab2, tab3 = st.tabs([
        "📊 1. Skill Gap Analysis Table",
        "🗓️ 2. 8-Week Learning Roadmap",
        "🚀 3. Portfolio Mini-Projects"
    ])
    
    # Tab 1: Skills Table
    with tab1:
        st.subheader("Skills You Have vs. Skills You Need to Learn")
        st.caption("A side-by-side gap breakdown based on industry recruiter benchmarks.")
        
        raw_skills = plan_data.get("skills_table", [])
        if raw_skills:
            df_skills = pd.DataFrame(raw_skills)
            
            # Summary counters
            acquired_count = sum(1 for item in raw_skills if "Have" in str(item.get("Status", "")))
            to_learn_count = sum(1 for item in raw_skills if "Need" in str(item.get("Status", "")))
            
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                st.success(f"**Foundational Skills Acquired:** {acquired_count}")
            with sub_col2:
                st.warning(f"**Target Skills to Master:** {to_learn_count}")
                
            st.dataframe(
                df_skills,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Skill Name": st.column_config.TextColumn("Skill / Technology", width="medium"),
                    "Category": st.column_config.TextColumn("Category", width="small"),
                    "Status": st.column_config.TextColumn("Status", width="small"),
                    "Priority": st.column_config.TextColumn("Importance", width="small"),
                    "Action Plan": st.column_config.TextColumn("Recommended Action", width="large")
                }
            )
        else:
            st.write("No skills data available.")

    # Tab 2: 8-Week Roadmap
    with tab2:
        st.subheader("8-Week Structured Study Roadmap")
        st.caption(f"Paced at {study_hours} hours per week with clear weekly milestones.")
        
        roadmap_items = plan_data.get("roadmap", [])
        for item in roadmap_items:
            week_num = item.get("week_num", "1")
            title = item.get("title", f"Week {week_num}")
            summary = item.get("summary", "")
            topics = item.get("topics", [])
            milestone = item.get("milestone", "")
            hrs = item.get("allocated_hours", study_hours)
            
            with st.expander(f"📅 **Week {week_num}: {title}**  —  ⏱️ {hrs} hours planned", expanded=(week_num in [1, 2])):
                st.markdown(f"**Focus:** {summary}")
                
                st.markdown("**Key Topics to Cover:**")
                topics_html = " ".join([f'<span class="badge">{t}</span>' for t in topics])
                st.markdown(topics_html, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"**🏆 Weekly Milestone Deliverable:** `{milestone}`")

    # Tab 3: 3 Mini Projects
    with tab3:
        st.subheader("3 Portfolio Mini-Projects for Your Resume")
        st.caption("Recruiters evaluate practical ability. These projects prove your hands-on competence.")
        
        projects = plan_data.get("projects", [])
        for i, proj in enumerate(projects, 1):
            p_title = proj.get("title", f"Project {i}")
            p_desc = proj.get("desc", "")
            p_tech = proj.get("tech", [])
            p_skills = proj.get("skills_demonstrated", "")
            
            tech_badges = " ".join([f'<span class="badge">{t}</span>' for t in p_tech])
            
            st.markdown(f"""
            <div class="project-card">
                <div class="project-title">Project #{i}: {p_title}</div>
                <div class="project-desc">{p_desc}</div>
                <div style="margin-bottom: 0.5rem;">
                    <strong>Tech Stack:</strong> {tech_badges}
                </div>
                <div>
                    <span class="badge-alt">Demonstrates: {p_skills}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ------------------ Downloadable Report ------------------
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Generate clean Markdown export
    report_md = f"""# AI Career Roadmap & Skill Gap Analysis
**Target Role:** {target_job}  
**Current Skills:** {user_skills}  
**Study Hours:** {study_hours} hrs/week  
**Timeline:** 8 Weeks ({study_hours * 8} Total Hours)  
**Readiness Match Score:** {plan_data.get('match_percentage', 35)}%  

---

## 1. Executive Summary
{plan_data.get('summary', '')}

---

## 2. Skill Gap Table
| Skill Name | Category | Status | Priority | Action Plan |
|---|---|---|---|---|
"""
    for row in plan_data.get("skills_table", []):
        report_md += f"| {row.get('Skill Name')} | {row.get('Category')} | {row.get('Status')} | {row.get('Priority')} | {row.get('Action Plan')} |\n"

    report_md += "\n---\n\n## 3. 8-Week Week-by-Week Roadmap\n"
    for r in plan_data.get("roadmap", []):
        report_md += f"\n### Week {r.get('week_num')}: {r.get('title')}\n"
        report_md += f"- **Study Time:** {r.get('allocated_hours', study_hours)} hours\n"
        report_md += f"- **Goal:** {r.get('summary')}\n"
        report_md += f"- **Topics:** {', '.join(r.get('topics', []))}\n"
        report_md += f"- **Milestone:** {r.get('milestone')}\n"

    report_md += "\n---\n\n## 4. Portfolio Mini-Projects\n"
    for idx, p in enumerate(plan_data.get("projects", []), 1):
        report_md += f"\n### Project {idx}: {p.get('title')}\n"
        report_md += f"- **Description:** {p.get('desc')}\n"
        report_md += f"- **Tech Stack:** {', '.join(p.get('tech', []))}\n"
        report_md += f"- **Key Skills:** {p.get('skills_demonstrated')}\n"

    st.download_button(
        label="📥 Download My Complete Roadmap & Report (.md)",
        data=report_md,
        file_name=f"{target_job.lower().replace(' ', '_')}_roadmap.md",
        mime="text/markdown"
    )
