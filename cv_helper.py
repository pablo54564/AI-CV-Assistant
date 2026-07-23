import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI CV ASSISTANT",
    page_icon="📄",
    layout="wide"
)

client = Groq(api_key="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")



# SIDEBAR - must come before main content
with st.sidebar:
    st.markdown("## 📄 AI CV Assistant")
    st.divider()
    st.markdown("### 🎯 What This Tool Does")
    st.markdown("""
    - 📊 Scores your CV (0-100)
    - 🎯 Matches to job description
    - ✍️ Rewrites your CV
    - 📝 Writes cover letter
    - 🎤 Preps you for interview
    """)
    st.divider()
    st.markdown("### ⚡ How To Use")
    st.markdown("""
    1. Paste your CV on the left
    2. Paste job description on right
    3. Click Analyze
    4. Check all 5 tabs
    5. Download your report
    """)
    st.divider()
    st.markdown("### 💡 Pro Tips")
    st.markdown("""
    - Be honest in your CV
    - Use the rewritten version
       as inspiration not copy paste
    - Practice interview questions
       out loud
    - Customize for each job
    """)
    st.divider()
    st.markdown("### 🔑 Get Free API Key")
    st.markdown("[Get Groq API Key](https://console.groq.com)")

# SYSTEM PROMPT
CV_SYSTEM_PROMPT = """
You are an expert CV consultant and career coach 
with 15 years experience in tech recruitment.

You understand:
- How ATS systems score CVs
- What hiring managers look for
- How to match CVs to job descriptions
- How to quantify achievements
- How to use strong action verbs
- Industry specific keywords

You are strategic, specific and accurate.
Never give generic advice.
Always reference specific parts of the CV.
Always reference specific parts of the job description.
Your match scores are calculated based on:
- Keyword matching (30%)
- Skills alignment (25%)
- Experience level (20%)
- Achievement focus (15%)
- Format quality (10%)

Always respond in a structured, clear format.
Use emojis sparingly for visual clarity.
"""

# ASK AI FUNCTION
def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": CV_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# TITLE
st.title("📄 AI CV Assistant")
st.write("Upload your CV and job description to get started.")
st.divider()

# TWO COLUMNS
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Your CV")
    cv_text = st.text_area(
        "Paste your CV here",
        height=400,
        placeholder="Paste your full CV text here..."
    )

with col2:
    st.header("💼 Job Description")
    job_text = st.text_area(
        "Paste the job description here",
        height=400,
        placeholder="Paste the full job description here..."
    )

st.divider()

# CENTER THE BUTTON
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    analyze_button = st.button("🔍 Analyze My CV", use_container_width=True)

if analyze_button:
    if cv_text == "" or job_text == "":
        st.warning("⚠️ Please fill in both!")
    else:
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 CV Analysis",
            "🎯 Job Match",
            "✍️ Rewritten CV",
            "📝 Cover Letter",
            "🎤 Interview Prep"
        ])

        with tab1:
            st.header("📊 CV Analysis")
            with st.spinner("Analyzing your CV... 📊"):
                cv_analysis = ask_ai(f"""
                Analyze this CV thoroughly:
                CV:
                {cv_text}

                Provide:
                1. OVERALL SCORE (0-100)
                   Break down by:
                   - Keyword strength (0-30)
                   - Skills presentation (0-25)
                   - Experience quality (0-20)
                   - Achievement focus (0-15)
                   - Format quality (0-10)

                2. TOP 3 STRENGTHS
                3. TOP 3 WEAKNESSES
                4. ATS COMPATIBILITY
                5. QUICK WINS
                """)
                st.write(cv_analysis)

        with tab2:
            st.header("🎯 Job Match Analysis")
            with st.spinner("Matching CV to job... 🎯"):
                job_match = ask_ai(f"""
                Compare this CV against this job:

                CV:
                {cv_text}

                JOB DESCRIPTION:
                {job_text}

                Provide:
                1. MATCH SCORE (0-100%)
                2. MATCHING SKILLS
                3. MISSING SKILLS
                4. MISSING KEYWORDS
                5. RECOMMENDATION
                """)
                st.write(job_match)

        with tab3:
            st.header("✍️ Rewritten CV")
            with st.spinner("Rewriting your CV... ✍️"):
                rewritten_cv = ask_ai(f"""
                Rewrite this CV to match this job:

                ORIGINAL CV:
                {cv_text}

                JOB DESCRIPTION:
                {job_text}

                Rules:
                1. Keep all real experience
                2. Add missing keywords naturally
                3. Strengthen weak descriptions
                4. Quantify achievements
                5. Use strong action verbs
                6. Optimize for ATS

                Provide complete rewritten CV.
                Then explain what you changed.
                """)
                st.write(rewritten_cv)

        with tab4:
            st.header("📝 Cover Letter")
            with st.spinner("Writing cover letter... 📝"):
                cover_letter = ask_ai(f"""
                Write a personalized cover letter:

                CV:
                {cv_text}

                JOB DESCRIPTION:
                {job_text}

                Rules:
                1. Opening hook
                2. Why perfect for this role
                3. Most relevant achievement
                4. Why this company
                5. Confident closing

                Professional but human tone.
                3-4 paragraphs max.
                """)
                st.write(cover_letter)

        with tab5:
            st.header("🎤 Interview Prep")
            with st.spinner("Preparing questions... 🎤"):
                interview_prep = ask_ai(f"""
                Prepare candidate for interview:

                CV:
                {cv_text}

                JOB DESCRIPTION:
                {job_text}

                Provide:
                1. TOP 10 LIKELY QUESTIONS
                   For each: why asked and how to answer
                2. RED FLAGS TO ADDRESS
                3. QUESTIONS TO ASK THEM
                """)
                st.write(interview_prep)

        # ALL OF THIS IS INSIDE THE IF BLOCK NOW
        st.divider()
        st.success("✅ Analysis Complete!")

        full_report = f"""
AI CV ANALYSIS REPORT
=====================

CV ANALYSIS:
{cv_analysis}

JOB MATCH:
{job_match}

REWRITTEN CV:
{rewritten_cv}

COVER LETTER:
{cover_letter}

INTERVIEW PREP:
{interview_prep}
        """

        st.download_button(
            label="📥 Download Full Report",
            data=full_report,
            file_name="cv_analysis_report.txt",
            mime="text/plain"
        )