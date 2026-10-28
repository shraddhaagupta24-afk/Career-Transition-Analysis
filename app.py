import streamlit as st

from model import (
    technical_roles,
    analyze_transition,
    create_roadmap,
    get_main_recommendation
)


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Career Transition Analysis",
    page_icon="🎯",
    layout="wide"
)


# ==================================================
# CUSTOM STYLE
# ==================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f8f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .stButton > button {
        height: 50px;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 600;
    }

    [data-testid="stMetric"] {
        background-color: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e6e9ef;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    hr {
        margin-top: 30px;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HEADER
# ==================================================

st.title("🎯 Career Transition Analysis")

st.write(
    "Understand your career transition, explore your skill compatibility, "
    "and get a personalized roadmap for your target technical role."
)

st.write("")


# ==================================================
# STEP 1 - CAREER DETAILS
# ==================================================

st.header("1️⃣ Tell Us About Your Career")

st.write(
    "Select your current role, target role, experience level "
    "and qualification."
)

st.write("")


col1, col2 = st.columns(2)


with col1:

    current_role = st.selectbox(
        "💼 Current Role",
        ["-- Select your current role --"] + technical_roles
    )


with col2:

    target_role = st.selectbox(
        "🎯 Target Role",
        ["-- Select your target role --"] + technical_roles
    )


col3, col4 = st.columns(2)


with col3:

    user_experience = st.selectbox(
        "📈 Experience Level",
        [
            "-- Select your experience level --",
            "Entry",
            "Mid",
            "Senior"
        ]
    )


with col4:

    user_qualification = st.selectbox(
        "🎓 Qualification",
        [
            "-- Select your qualification --",
            "Bachelor's in Data Science",
            "Bachelor's in Computer Science",
            "Bachelor's in Information Technology",
            "Bachelor's in Software Engineering",
            "Master's in Data Science",
            "Master's in Computer Science",
            "PhD in Artificial Intelligence"
        ]
    )


st.write("")


analyze_button = st.button(
    "🚀 Analyze My Career Transition",
    use_container_width=True
)


# ==================================================
# VALIDATION
# ==================================================

if analyze_button:

    if current_role == "-- Select your current role --":

        st.warning(
            "Please select your current role."
        )


    elif target_role == "-- Select your target role --":

        st.warning(
            "Please select your target role."
        )


    elif user_experience == "-- Select your experience level --":

        st.warning(
            "Please select your experience level."
        )


    elif user_qualification == "-- Select your qualification --":

        st.warning(
            "Please select your qualification."
        )


    elif current_role == target_role:

        st.warning(
            "Current Role and Target Role should be different."
        )


    else:

        # ==================================================
        # ANALYSIS
        # ==================================================

        result = analyze_transition(

            current_role,

            target_role,

            user_experience,

            user_qualification

        )


        # ==================================================
        # STEP 2 - CAREER PATH
        # ==================================================

        st.divider()

        st.header("2️⃣ Your Career Transition")


        col1, col2, col3 = st.columns([2, 1, 2])


        with col1:

            st.info(
                f"**CURRENT ROLE**\n\n"
                f"### {current_role}"
            )


        with col2:

            st.markdown(
                "<h2 style='text-align:center; "
                "padding-top:20px;'>→</h2>",
                unsafe_allow_html=True
            )


        with col3:

            st.success(
                f"**TARGET ROLE**\n\n"
                f"### {target_role}"
            )


        # ==================================================
        # STEP 3 - RECOMMENDATION
        # ==================================================

        st.divider()

        st.header("3️⃣ Career Recommendation")


        recommendation = get_main_recommendation(

            current_role,

            target_role,

            result["skills_to_learn"]

        )


        st.success(
            f"💡 **Recommended Action**\n\n"
            f"{recommendation}"
        )


        # ==================================================
        # STEP 4 - TRANSITION SCORE
        # ==================================================

        st.divider()

        st.header("4️⃣ Transition Readiness")


        score = result["transition_score"]


        if score >= 70:

            score_message = (
                "You have a strong starting point for this transition."
            )

        elif score >= 45:

            score_message = (
                "You have a reasonable starting point, "
                "but some areas need improvement."
            )

        else:

            score_message = (
                "You have more areas to work on before "
                "making this transition."
            )


        col1, col2 = st.columns([1, 2])


        with col1:

            st.metric(
                "Overall Transition Score",
                f"{score}%"
            )


        with col2:

            st.write(
                "**Transition Readiness**"
            )

            st.progress(
                score / 100
            )

            st.caption(
                score_message
            )


        st.write("")


        # ==================================================
        # SUPPORTING SCORES
        # ==================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "🧠 Skill Match",
                f"{result['skill_match']}%"
            )


        with col2:

            st.metric(
                "📈 Experience Match",
                f"{result['experience_match']}%"
            )


        with col3:

            st.metric(
                "🎓 Education Match",
                f"{result['education_match']}%"
            )


        st.write("")


        # ==================================================
        # DIFFICULTY
        # ==================================================

        if result["difficulty"] == "Easy":

            st.success(
                "🟢 **Transition Difficulty: Easy**"
            )


        elif result["difficulty"] == "Medium":

            st.warning(
                "🟡 **Transition Difficulty: Medium**"
            )


        else:

            st.error(
                "🔴 **Transition Difficulty: Difficult**"
            )


        # ==================================================
        # STEP 5 - SKILL COMPATIBILITY
        # ==================================================

        st.divider()

        st.header(
            "5️⃣ Skill Compatibility Analysis"
        )


        st.write(
            "See how your current role skills compare "
            "with the skills needed for your target role."
        )


        st.write("")


        # ==================================================
        # COMMON SKILLS
        # ==================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            st.subheader(
                "✅ Common Skills"
            )


            if result["common_skills"]:

                for skill in result["common_skills"]:

                    st.write(
                        f"✓ **{skill}**"
                    )

            else:

                st.write(
                    "No common skills were found "
                    "between the two roles."
                )


        # ==================================================
        # RELATED SKILLS
        # ==================================================

        with col2:

            st.subheader(
                "🔄 Related Skills"
            )


            if result["related_skills"]:

                st.write(
                    "These skills are connected to "
                    "skills from your current role."
                )

                for skill in result["related_skills"]:

                    st.write(
                        f"↔ **{skill}**"
                    )

            else:

                st.write(
                    "No closely related skills were found."
                )


        # ==================================================
        # SKILLS REQUIRED
        # ==================================================

        with col3:

            st.subheader(
                "🎯 Skills Required"
            )


            if result["skills_to_learn"]:

                st.write(
                    "These are the target-role skills "
                    "you should focus on learning."
                )

                for skill in result["skills_to_learn"]:

                    st.write(
                        f"→ **{skill}**"
                    )

            else:

                st.success(
                    "Your current skills cover "
                    "the main target-role requirements."
                )


        # ==================================================
        # STEP 6 - PERSONALIZED ROADMAP
        # ==================================================

        st.divider()

        st.header(
            "6️⃣ Your Personalized Roadmap"
        )


        st.write(
            f"Follow these steps to move from "
            f"**{current_role}** to **{target_role}**."
        )


        st.write("")


        roadmap = create_roadmap(

            current_role,

            target_role,

            result["skills_to_learn"]

        )


        for number, phase in enumerate(
            roadmap,
            start=1
        ):

            st.subheader(

                f"Step {number} — "
                f"{phase['phase'].replace(f'Phase {number} - ', '')}"

            )


            for task in phase["tasks"]:

                st.write(
                    f"→ {task}"
                )


            st.write("")


        # ==================================================
        # STEP 7 - NEXT BEST ACTION
        # ==================================================

        st.divider()

        st.header(
            "7️⃣ Your Next Best Action"
        )


        if result["skills_to_learn"]:

            first_skill = result["skills_to_learn"][0]


            st.info(

                f"🎯 **Start with:** {first_skill}\n\n"

                f"Build this skill first, then move through "
                f"your roadmap toward the **{target_role}** role."

            )


        else:

            st.success(

                f"🎯 Your skill base is already strong for "
                f"**{target_role}**. Focus on projects, practical "
                f"experience and interview preparation."

            )


# ==================================================
# FOOTER
# ==================================================

st.write("")

st.divider()


st.caption(
    "🎯 Career Transition Prediction & Analysis System"
)