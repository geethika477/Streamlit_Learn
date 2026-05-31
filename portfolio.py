import streamlit as st
from streamlit_option_menu import option_menu
import base64

st.set_page_config(
    page_title="Geethika Portfolio",
    page_icon="✨",
    layout="wide"
)


def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


photo = get_base64("red.jpeg")


st.markdown(
    f"""

    <style>

    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}

    .stApp {{
        background: linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: white;
    }}

    @keyframes gradientBG {{
        0% {{
            background-position: 0% 50%;
        }}
        50% {{
            background-position: 100% 50%;
        }}
        100% {{
            background-position: 0% 50%;
        }}
    }}

    section[data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.03);
        border-right: 1px solid rgba(255,255,255,0.08);
    }}

    .hero-card {{
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(18px);
        border-radius: 30px;
        padding: 45px;
        box-shadow: 0px 10px 40px rgba(0,0,0,0.4);
        animation: fadeUp 1s ease;
    }}

    .main-card {{
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(14px);
        border-radius: 25px;
        padding: 35px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
        animation: fadeUp 1s ease;
    }}

    .project-card {{
        background: rgba(255,255,255,0.05);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.4s;
        backdrop-filter: blur(14px);
        animation: fadeUp 1s ease;
    }}

    .project-card:hover {{
        transform: translateY(-10px);
        border: 1px solid #38bdf8;
        box-shadow: 0px 0px 35px rgba(56,189,248,0.35);
    }}

    .skill-card {{
        background: rgba(255,255,255,0.05);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255,255,255,0.08);
        transition: 0.4s;
        height: 100%;
        backdrop-filter: blur(14px);
        animation: fadeUp 1s ease;
    }}

    .skill-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0px 0px 30px rgba(99,102,241,0.35);
        border: 1px solid #818cf8;
    }}

    .section-title {{
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 25px;
        background: linear-gradient(to right,#38bdf8,#818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .stDownloadButton{{
        display: flex;
        justify-content: center;
    }}

    .stDownloadButton button{{
        background: linear-gradient(135deg,#0ea5e9,#6366f1);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 18px;
        font-size: 17px;
        font-weight: 600;
        transition: 0.35s;
        box-shadow: 0px 0px 20px rgba(56,189,248,0.25);
    }}

    .stDownloadButton button:hover{{
        transform: translateY(-5px);
        box-shadow: 0px 0px 35px rgba(99,102,241,0.45);
    }}

    .name-title {{
        font-size: 65px;
        font-weight: 800;
        color: white;
        line-height: 1;
    }}

    .gradient-text {{
        background: linear-gradient(to right,#38bdf8,#818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
        font-size: 24px;
        color: #cbd5e1;
        margin-top: 20px;
    }}

    .hero-description {{
        font-size: 18px;
        line-height: 1.9;
        color: #dbeafe;
        margin-top: 25px;
    }}

    .social-buttons {{
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
        margin-top: 35px;
    }}

    .social-btn {{
        padding: 13px 26px;
        border-radius: 15px;
        background: linear-gradient(to right,#0ea5e9,#6366f1);
        color: white !important;
        text-decoration: none;
        font-weight: 600;
        transition: 0.3s;
    }}

    .social-btn:hover {{
        transform: translateY(-5px);
        box-shadow: 0px 0px 25px rgba(56,189,248,0.5);
    }}

    .profile-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }}

    .profile-ring {{
        width: 282px;
        height: 282px;
        border-radius: 50%;
        background: linear-gradient(45deg,#38bdf8,#818cf8,#0ea5e9,#6366f1);
        padding: 6px;
        animation: None;
        box-shadow: 0px 0px 40px rgba(56,189,248,0.45);
    }}

    .profile-wrapper img{{
        border-radius: 50%;
        width: 270px !important;
        height: 270px !important;
        object-fit: cover;
        border: 7px solid #020617;
    }}

    .floating {{
        animation: floating 4s ease-in-out infinite;
    }}

    .gallery-image img {{
        border-radius: 20px;
        transition: 0.4s;
    }}

    .gallery-image img:hover {{
        transform: scale(1.04);
    }}

    @keyframes rotate {{
        0% {{
            transform: rotate(0deg);
        }}
        100% {{
            transform: rotate(360deg);
        }}
    }}

    @keyframes floating {{
        0% {{
            transform: translateY(0px);
        }}
        50% {{
            transform: translateY(-15px);
        }}
        100% {{
            transform: translateY(0px);
        }}
    }}

    @keyframes fadeUp {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0px);
        }}
    }}

    </style>

    """,
    unsafe_allow_html=True
)


selected = option_menu(
    menu_title=None,
    options=["Home", "Skills", "Projects", "Gallery"],
    icons=["house", "code-slash", "kanban", "image"],
    orientation="horizontal",
)


if selected == "Home":

    col1, col2 = st.columns([1.7,1])

    with col1:

        st.markdown(
            """
            <div class="hero-card">

            <div class="name-title">
            Hi, I'm
            <span class="gradient-text">
            Geethika
            </span>
            </div>

            <div class="hero-subtitle">
            B.Tech CSE Student • Python Developer • Streamlit Builder
            </div>

            <div class="hero-description">

            Passionate about building visually polished and interactive
            applications using Python and Streamlit.

            Focused on dashboards, modern UI design, analytics,
            productivity systems, and solving real-world problems
            through software.

            </div>

            <div class="social-buttons">

            <a href="https://github.com"
            target="_blank"
            class="social-btn">
            GitHub
            </a>

            <a href="https://linkedin.com"
            target="_blank"
            class="social-btn">
            LinkedIn
            </a>

            <a href="mailto:example@gmail.com"
            class="social-btn">
            Contact
            </a>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
        f"""
        <div class="profile-wrapper floating">
            <div class="profile-ring">
                <img src="data:image/jpeg;base64,{photo}" />
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="section-title">
        Education
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-card">

        <h2>NSRIT</h2>

        <p>
        B.Tech in Computer Science and Engineering
        </p>

        <p>
        2024 - Present
        </p>

        <hr>

        <h2>Intermediate</h2>

        <p>
        Your College Name
        </p>

        <p>
        2022 - 2024
        </p>

        <hr>

        <h2>Schooling</h2>

        <p>
        Your School Name
        </p>

        <p>
        2021 - 2022
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
    st.write("")
    st.write("")
    with open("Geethika_Resume.pdf","rb") as f:
        resume = f.read()
    c1, c2, c3 = st.columns([2,2,1])
    with c2:
        st.download_button(
            label="Download Resume",
            data=resume,
            file_name="Geethika_Resume.pdf",
            mime="application/pdf"
        )


if selected == "Skills":

    st.markdown(
        """
        <div class="section-title">
        Skills & Technologies
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="skill-card">

            <h2>Programming</h2>

            <ul>
                <li>Python</li>
                <li>C</li>
                <li>Java</li>
                <li>SQL</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="skill-card">

            <h2>Libraries</h2>

            <ul>
                <li>Streamlit</li>
                <li>Pandas</li>
                <li>NumPy</li>
                <li>Matplotlib</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="skill-card">

            <h2>Tools</h2>

            <ul>
                <li>Git</li>
                <li>GitHub</li>
                <li>VS Code</li>
                <li>Jupyter Notebook</li>
                <li>Problem Solving</li>
            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    st.markdown(
        """
        <div class="section-title">
        Certifications
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="main-card">

        <ul>
            <li>Python Zero To Hero</li>
            <li>NPTEL Joy Of Computing Using Python</li>
            <li>HackerRank Python Certificate</li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True
    )


if selected == "Projects":

    st.markdown(
        """
        <div class="section-title">
        Featured Projects
        </div>
        """,
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Mini Projects",
            "Currently Working On",
            "Streamlit Projects"
        ]
    )

    with tab1:

        st.markdown(
            """
            <div class="project-card">

            <h2>Food Ordering System</h2>

            <p>
            C programming based application for handling orders,
            menu systems, and billing.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h2>Expense Tracker</h2>

            <p>
            Expense management dashboard with analytics,
            charts, and financial insights.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with tab2:

        st.markdown(
            """
            <div class="project-card">

            <h2>DefenderX</h2>

            <p>
            Cybercrime awareness platform for detecting
            fraudulent links and suspicious numbers.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h2>Professional Portfolio</h2>

            <p>
            Modern interactive Streamlit portfolio with animations,
            glassmorphism UI, and responsive sections.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with tab3:

        st.markdown(
            """
            <div class="project-card">

            <h2>Analytics Dashboard</h2>

            <p>
            Interactive dashboard with visualizations,
            charts, and data-driven insights.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h2>Image Editor</h2>

            <p>
            Streamlit-based image processing tool supporting
            multiple operations and effects.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

if selected == "Gallery":

    st.markdown("""
        <div class="section-title">
        Achievements & Gallery
        </div>
    """, unsafe_allow_html=True)

    def achievement(title, images):
        st.markdown(f"""
        <div class="main-card">
            <h2>{title}</h2>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)

        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, use_container_width=True)


    with st.expander("🏆 SheHack Achievement"):
        achievement("2nd Place in SheHack", ["a.jpeg", "f.jpeg", "g.jpeg"])

    with st.expander("🏆 Code Vinyas"):
        achievement("2nd Place in Code Vinyas", ["b.jpeg", "c.jpeg"])

    with st.expander("🥇 Codeathon"):
        achievement("1st Place in Codeathon", ["h.jpeg"])

    with st.expander("🥇 IntroCode"):
        achievement("1st Place in IntroCode", ["e.jpeg"])

    with st.expander("✨ Hack With Vizag"):
        achievement("Consolation Prize", ["l.jpeg", "d.jpeg"])