import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Researcher Profile | CSS2026",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #0EA5E9;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .project-card {
        background-color: #F8FAFC;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0EA5E9;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150/0EA5E9/FFFFFF?text=RP", width=150)
    st.title("Researcher Profile")
    st.markdown("---")
    st.markdown("**Contact:**")
    st.markdown("📧 researcher@university.edu")
    st.markdown("🔗 [Google Scholar](#)")
    st.markdown("🐙 [GitHub](#)")
    st.markdown("📄 [CV / Resume](#)")
    
# Main content
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="main-header">Dr. Data Scientist</div>', unsafe_allow_html=True)
    st.markdown("**Associate Professor | Data Science & Statistics**")
    st.markdown("*Center for Statistical Science, University of Research*")
    
with col2:
    st.markdown("### Research Keywords")
    st.markdown("""
    - Statistical Learning
    - Data Visualization
    - Bayesian Methods
    - Computational Statistics
    - Reproducible Research
    """)

st.markdown("---")

# About section
st.markdown('<div class="section-header">About My Research</div>', unsafe_allow_html=True)
st.markdown("""
My research focuses on developing statistical methods and computational tools to extract meaningful 
insights from complex data. I work at the intersection of statistics, computer science, and 
domain-specific applications, with particular emphasis on:

- **Methodological Development**: Creating robust statistical models for high-dimensional data
- **Computational Tools**: Building open-source software for data analysis and visualization
- **Applied Research**: Collaborating with domain experts in healthcare, environmental science, and social sciences
- **Reproducibility**: Promoting transparent and reproducible research practices through modern workflow tools

My work emphasizes both theoretical foundations and practical implementations that are accessible 
to researchers across disciplines.
""")

# Research Projects
st.markdown('<div class="section-header">Featured Research Projects</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 📈 **Bayesian Methods for Uncertainty Quantification**")
        st.markdown("*2023–Present*")
        st.markdown("Developing novel Bayesian approaches to quantify uncertainty in machine learning predictions, with applications in climate modeling.")
        st.markdown("**Tools:** Python, PyMC, TensorFlow Probability")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🎨 **Interactive Data Visualization Framework**")
        st.markdown("*2022–Present*")
        st.markdown("Creating an open-source framework for building interactive statistical visualizations that communicate uncertainty effectively.")
        st.markdown("**Tools:** Streamlit, Altair, D3.js")
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🧬 **Statistical Genomics for Precision Medicine**")
        st.markdown("*2021–Present*")
        st.markdown("Collaborative project developing statistical methods for analyzing high-throughput genomic data to identify biomarkers for personalized treatment.")
        st.markdown("**Tools:** R, Bioconductor, Python")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### 🔄 **Reproducible Research Workflows**")
        st.markdown("*2020–Present*")
        st.markdown("Developing best practices and tools for reproducible statistical analysis, focusing on containerization and workflow automation.")
        st.markdown("**Tools:** Docker, Git, GitHub Actions, Quarto")
        st.markdown("</div>", unsafe_allow_html=True)

# Publications
st.markdown('<div class="section-header">Selected Publications</div>', unsafe_allow_html=True)
st.markdown("""
1. **Researcher, D.**, Colleague, A., & Partner, B. (2024). "Advanced visualization techniques for communicating statistical uncertainty." *Journal of Computational Statistics*, 45(3), 123-145.

2. **Researcher, D.** (2023). "Bayesian approaches to high-dimensional inference: A practical guide." *Statistical Science Review*, 38(2), 89-112.

3. Colleague, A., **Researcher, D.**, & Expert, C. (2022). "Open-source tools for reproducible data science workflows." *Journal of Open Source Software*, 7(75), 4501.

4. **Researcher, D.**, & Statistician, E. (2021). "Modern data science education: Integrating computation and statistics." *Statistics Education Journal*, 29(1), 56-78.
""")

# Teaching/Outreach
st.markdown('<div class="section-header">Teaching & Outreach</div>', unsafe_allow_html=True)
st.markdown("""
- **CSS2026: Computational Statistical Science** – Core course on statistical computing with Python/R
- **Workshops** on data visualization, reproducible research, and Bayesian statistics
- **Open-source contributor** to several statistical software packages
- **Mentor** to undergraduate and graduate students in data science

---

*This page was built with [Streamlit](https://streamlit.io) for CSS2026.*
""")