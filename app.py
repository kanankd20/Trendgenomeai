import streamlit as st

from utils.github_fetcher import fetch_github_trends
from utils.arxiv_fetcher import fetch_arxiv_papers
from utils.trends_score import calculate_trends_score


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="TrendGenome IQ",
    page_icon="🚀",
    layout="wide"
)


# =====================================
# HEADER
# =====================================

st.title("🚀 TrendGenome IQ")

st.subheader(
    "AI-Powered Trend Analysis & Opportunity Discovery Platform"
)

st.markdown("""
### Welcome to TrendGenome IQ

This platform combines:

✅ GitHub Trend Intelligence

✅ Research Paper Intelligence

✅ Trend Scoring Engine

✅ Future Opportunity Discovery

to identify emerging technologies and future opportunities.
""")

st.divider()


# =====================================
# USER INPUT
# =====================================

topic = st.text_input(
    "🔍 Enter Technology or Topic",
    placeholder="Example: Artificial Intelligence"
)


# =====================================
# ANALYZE BUTTON
# =====================================

if st.button("📈 Analyze Trends"):

    if not topic.strip():

        st.warning(
            "Please enter a valid topic."
        )

    else:

        github_trends = []
        papers = []

        # =====================================
        # GITHUB
        # =====================================

        try:

            with st.spinner(
                "Fetching GitHub repositories..."
            ):

                github_trends = fetch_github_trends(
                    topic
                )

            st.header(
                "💻 GitHub Intelligence"
            )

            st.success(
                f"{len(github_trends)} repositories found"
            )

            for repo in github_trends:

                with st.container():

                    st.subheader(
                        repo["name"]
                    )

                    st.write(
                        f"⭐ Stars: {repo['stars']}"
                    )

                    st.write(
                        f"💻 Language: {repo['language']}"
                    )

                    if repo["description"]:

                        st.write(
                            f"📝 {repo['description']}"
                        )

                    st.write(
                        repo["url"]
                    )

                    st.divider()

        except Exception as e:

            st.error(
                f"GitHub Error: {e}"
            )

        # =====================================
        # ARXIV
        # =====================================

        try:

            with st.spinner(
                "Fetching research papers..."
            ):

                papers = fetch_arxiv_papers(
                    topic
                )

            st.header(
                "📚 Research Intelligence"
            )

            st.success(
                f"{len(papers)} research papers found"
            )

            for paper in papers:

                with st.container():

                    st.subheader(
                        paper["title"]
                    )

                    st.write(
                        f"👨‍🔬 Authors: {', '.join(paper['authors'])}"
                    )

                    st.write(
                        paper["summary"][:500]
                        + "..."
                    )

                    st.write(
                        paper["url"]
                    )

                    st.divider()

        except Exception as e:

            st.error(
                f"Arxiv Error: {e}"
            )

        # =====================================
        # TREND SCORE
        # =====================================

        try:

            if github_trends or papers:

                score = calculate_trends_score(
                    github_trends,
                    papers
                )

                st.header(
                    "📊 Trend Score"
                )

                st.metric(
                    label="Trend Strength",
                    value=f"{score}/100"
                )

        except Exception as e:

            st.error(
                f"Trend Score Error: {e}"
            )

        # =====================================
        # GEMINI TEMPORARY PLACEHOLDER
        # =====================================

        st.header(
            "🤖 AI Trend Analysis"
        )

        st.info(
            """
Gemini integration is temporarily disabled.

Current Working Modules:

✅ GitHub Intelligence

✅ Research Intelligence

✅ Trend Scoring

Next Upgrade:

🔜 Gemini AI Insights

🔜 Future Demand Prediction

🔜 Opportunity Discovery

🔜 Startup Potential Analysis
"""
        )


# =====================================
# FOOTER
# =====================================

st.divider()

st.caption(
    "❤️ Developed by Kanan | Powered by Streamlit, GitHub API & Arxiv API"
)