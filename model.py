import pandas as pd

# ==================================================
# LOAD DATASET
# ==================================================

data = pd.read_csv("Candidate job role.csv")


# ==================================================
# TECHNICAL ROLES
# ==================================================

technical_roles = [
    "AIML",
    "Data Scientist",
    "Data Analyst",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Python Developer",
    "Full Stack Java Developer",
    "Mobile Developer",
    "Game Developer",
    "Web Developer"
]


# ==================================================
# ROLE-WISE SKILLS
# ==================================================

role_skills = {

    "AIML": [
        "Deep Learning",
        "Machine Learning",
        "NLP",
        "Python",
        "TensorFlow"
    ],

    "Data Scientist": [
        "Communication",
        "Data Science",
        "Keras",
        "Machine Learning",
        "NLP",
        "Python",
        "R",
        "SQL",
        "TensorFlow"
    ],

    "Data Analyst": [
        "Data Analysis",
        "Data Visualization",
        "Pandas",
        "Python",
        "R",
        "SQL",
        "Statistics",
        "Tableau"
    ],

    "Backend Developer": [
        "Hibernate",
        "Java",
        "Microservices",
        "Problem Solving",
        "REST APIs",
        "SQL",
        "Spring"
    ],

    "Frontend Developer": [
        "CSS",
        "HTML",
        "JavaScript",
        "React",
        "Redux",
        "Teamwork",
        "TypeScript"
    ],

    "Full Stack Python Developer": [
        "Agile",
        "Django",
        "Flask",
        "JavaScript",
        "PostgreSQL",
        "Python",
        "React",
        "SQL"
    ],

    "Full Stack Java Developer": [
        "AWS",
        "Angular",
        "Hibernate",
        "Java",
        "Microservices",
        "React",
        "Spring",
        "Spring Boot"
    ],

    "Mobile Developer": [
        "Android Development",
        "Android SDK",
        "Core Data",
        "Java",
        "Kotlin",
        "Objective-C",
        "REST APIs",
        "Swift",
        "UI/UX",
        "Xcode",
        "iOS",
        "iOS Development"
    ],

    "Game Developer": [
        "3D Modeling",
        "C#",
        "C++",
        "Game Design",
        "Game Physics",
        "Teamwork",
        "Unity",
        "Unreal Engine",
        "VR",
        "VR Development"
    ],

    "Web Developer": [
        "Angular",
        "CSS",
        "Express",
        "HTML",
        "JavaScript",
        "MongoDB",
        "Node.js",
        "Vue.js"
    ]
}


# ==================================================
# RELATED SKILL GROUPS
# ==================================================
# These groups identify skills that are connected.
#
# Important:
# Related skills are NOT common skills.
# A skill is shown as related only when the user
# already has another skill from the same group.

related_skill_groups = [

    ["Python", "Django", "Flask"],

    ["Java", "Spring", "Spring Boot", "Hibernate"],

    ["JavaScript", "HTML", "CSS", "TypeScript"],

    ["React", "Redux", "Angular", "Vue.js"],

    ["SQL", "PostgreSQL", "MongoDB"],

    ["C++", "C#", "Java"],

    ["Android Development", "Android SDK", "Kotlin", "Java"],

    ["iOS", "iOS Development", "Swift", "Objective-C"],

    ["REST APIs", "Microservices"],

    ["Machine Learning", "Deep Learning", "NLP"],

    ["Unity", "Unreal Engine", "Game Design", "Game Physics"],

    ["Teamwork", "Communication", "Problem Solving"]
]


# ==================================================
# ROLE-TO-ROLE RELATEDNESS
# ==================================================
# This represents how naturally one role can
# transition into another role.
#
# 1.00 = Very closely related
# 0.90 = Highly related
# 0.80 = Closely related
# 0.70 = Moderately related
# 0.60 = Somewhat related
# 0.50 = Less related
# 0.40 = Low relatedness


role_relatedness = {

    # ----------------------------------------------
    # DATA CAREER
    # ----------------------------------------------

    ("Data Analyst", "Data Scientist"): 0.80,

    ("Data Analyst", "AIML"): 0.65,

    ("Data Scientist", "AIML"): 0.90,

    ("AIML", "Data Scientist"): 0.90,

    ("Data Scientist", "Data Analyst"): 0.80,

    ("AIML", "Data Analyst"): 0.65,


    # ----------------------------------------------
    # FRONTEND / WEB
    # ----------------------------------------------

    ("Frontend Developer", "Web Developer"): 0.90,

    ("Web Developer", "Frontend Developer"): 0.90,


    # ----------------------------------------------
    # FRONTEND / FULL STACK
    # ----------------------------------------------

    (
        "Frontend Developer",
        "Full Stack Python Developer"
    ): 0.80,

    (
        "Full Stack Python Developer",
        "Frontend Developer"
    ): 0.80,


    # ----------------------------------------------
    # BACKEND / FULL STACK
    # ----------------------------------------------

    (
        "Backend Developer",
        "Full Stack Python Developer"
    ): 0.80,

    (
        "Full Stack Python Developer",
        "Backend Developer"
    ): 0.80,

    (
        "Backend Developer",
        "Full Stack Java Developer"
    ): 0.90,

    (
        "Full Stack Java Developer",
        "Backend Developer"
    ): 0.90,


    # ----------------------------------------------
    # WEB / BACKEND
    # ----------------------------------------------

    ("Backend Developer", "Web Developer"): 0.75,

    ("Web Developer", "Backend Developer"): 0.75,


    # ----------------------------------------------
    # WEB / FULL STACK
    # ----------------------------------------------

    (
        "Web Developer",
        "Full Stack Python Developer"
    ): 0.75,

    (
        "Full Stack Python Developer",
        "Web Developer"
    ): 0.85,

    (
        "Full Stack Java Developer",
        "Web Developer"
    ): 0.75,

    (
        "Web Developer",
        "Full Stack Java Developer"
    ): 0.70,


    # ----------------------------------------------
    # MOBILE
    # ----------------------------------------------

    ("Game Developer", "Mobile Developer"): 0.65,

    ("Mobile Developer", "Game Developer"): 0.65,

    ("Frontend Developer", "Mobile Developer"): 0.65,

    ("Mobile Developer", "Frontend Developer"): 0.65,

    ("Backend Developer", "Mobile Developer"): 0.55,

    ("Mobile Developer", "Backend Developer"): 0.55,


    # ----------------------------------------------
    # GAME / WEB
    # ----------------------------------------------

    ("Game Developer", "Web Developer"): 0.50,

    ("Web Developer", "Game Developer"): 0.35,

    ("Game Developer", "Frontend Developer"): 0.45,

    ("Frontend Developer", "Game Developer"): 0.45
}


# ==================================================
# GET ROLE RELATEDNESS
# ==================================================

def get_role_relatedness(current_role, target_role):

    if current_role == target_role:
        return 1.00

    if (current_role, target_role) in role_relatedness:

        return role_relatedness[
            (current_role, target_role)
        ]

    return 0.40


# ==================================================
# EXPERIENCE MATCH
# ==================================================

def experience_match(user_experience, target_role):

    if user_experience == "Senior":
        return 100

    elif user_experience == "Mid":
        return 80

    elif user_experience == "Entry":
        return 60

    return 0


# ==================================================
# EDUCATION MATCH
# ==================================================

def education_match(user_qualification, target_role):

    qualification = user_qualification.lower()


    # Data Science qualification

    if "data science" in qualification:

        if target_role in [
            "Data Scientist",
            "Data Analyst",
            "AIML"
        ]:

            return 100

        else:

            return 80


    # Computer Science

    elif "computer science" in qualification:

        return 100


    # Information Technology

    elif "information technology" in qualification:

        return 95


    # Software Engineering

    elif "software engineering" in qualification:

        return 95


    # Artificial Intelligence

    elif "artificial intelligence" in qualification:

        if target_role == "AIML":

            return 100

        else:

            return 85


    return 70


# ==================================================
# FIND RELATED SKILLS
# ==================================================

def find_related_skills(current_skills, target_skills):

    related_skills = []


    for group in related_skill_groups:

        current_group_skills = []

        target_group_skills = []


        for skill in current_skills:

            if skill in group:

                current_group_skills.append(skill)


        for skill in target_skills:

            if skill in group:

                target_group_skills.append(skill)


        # Only consider target skills related when
        # the current role has another skill from
        # the same skill group.

        if current_group_skills:

            for skill in target_group_skills:

                if skill not in current_skills:

                    related_skills.append(skill)


    return sorted(
        list(set(related_skills))
    )


# ==================================================
# CAREER TRANSITION ANALYSIS
# ==================================================

def analyze_transition(
    current_role,
    target_role,
    user_experience,
    user_qualification
):

    current_skills = set(
        role_skills[current_role]
    )

    target_skills = set(
        role_skills[target_role]
    )


    # ==================================================
    # COMMON SKILLS
    # ==================================================
    # Only EXACT skill matches are common skills.

    common_skills = sorted(
        current_skills.intersection(
            target_skills
        )
    )


    # ==================================================
    # RELATED SKILLS
    # ==================================================

    related_skills = find_related_skills(
        current_skills,
        target_skills
    )


    # ==================================================
    # SKILLS REQUIRED
    # ==================================================
    # These are target-role skills that are neither
    # already possessed nor meaningfully related.

    skills_to_learn = sorted(
        target_skills
        - current_skills
        - set(related_skills)
    )


    # ==================================================
    # SKILL MATCH
    # ==================================================
    #
    # Exact common skill = full credit
    # Related skill = half credit
    #
    # This is ONLY the skill compatibility score.
    # It is not the overall career transition score.

    total_target_skills = len(
        target_skills
    )


    exact_points = len(
        common_skills
    )


    related_points = (
        len(related_skills) * 0.50
    )


    if total_target_skills > 0:

        skill_match = (
            (
                exact_points
                + related_points
            )
            / total_target_skills
        ) * 100

    else:

        skill_match = 0


    skill_match = round(
        min(skill_match, 100)
    )


    # ==================================================
    # EXPERIENCE
    # ==================================================

    exp_match = experience_match(
        user_experience,
        target_role
    )


    # ==================================================
    # EDUCATION
    # ==================================================

    edu_match = education_match(
        user_qualification,
        target_role
    )


    # ==================================================
    # ROLE RELATEDNESS
    # ==================================================

    role_match = get_role_relatedness(
        current_role,
        target_role
    )


    role_match_percentage = round(
        role_match * 100
    )


    # ==================================================
    # TRANSITION SCORE
    # ==================================================
    #
    # Skill Match      = 40%
    # Role Relatedness = 30%
    # Experience       = 15%
    # Education        = 15%
    #
    # This means a career can still be a reasonable
    # transition even when exact common skills are low.

    transition_score = (

        skill_match * 0.40

        + role_match_percentage * 0.30

        + exp_match * 0.15

        + edu_match * 0.15

    )


    transition_score = round(
        transition_score
    )


    # ==================================================
    # DIFFICULTY
    # ==================================================

    if transition_score >= 65:

        difficulty = "Easy"

    elif transition_score >= 45:

        difficulty = "Medium"

    else:

        difficulty = "Difficult"


    # ==================================================
    # RESULT
    # ==================================================

    return {

        "common_skills": common_skills,

        "related_skills": related_skills,

        "skills_to_learn": skills_to_learn,

        "skill_match": skill_match,

        "experience_match": exp_match,

        "education_match": edu_match,

        "transition_score": transition_score,

        "difficulty": difficulty
    }


# ==================================================
# PERSONALIZED ROADMAP
# ==================================================

def create_roadmap(
    current_role,
    target_role,
    skills_to_learn
):

    roadmap = []


    # ==================================================
    # STEP 1
    # ==================================================

    roadmap.append({

        "phase": "Phase 1 - Understand the Target Role",

        "tasks": [

            f"Understand the main skills required for {target_role}.",

            f"Compare the requirements of {target_role} with your current {current_role} background."

        ]

    })


    # ==================================================
    # STEP 2
    # ==================================================

    if skills_to_learn:

        skill_tasks = []

        for skill in skills_to_learn[:4]:

            skill_tasks.append(
                f"Learn and practice {skill} through small exercises."
            )


        roadmap.append({

            "phase": "Phase 2 - Build Required Skills",

            "tasks": skill_tasks

        })

    else:

        roadmap.append({

            "phase": "Phase 2 - Strengthen Your Skills",

            "tasks": [

                "Practice your existing skills.",

                "Work on more advanced problems related to the target role."

            ]

        })


    # ==================================================
    # STEP 3
    # ==================================================

    roadmap.append({

        "phase": "Phase 3 - Build a Practical Project",

        "tasks": [

            f"Build a project related to {target_role}.",

            f"Use important {target_role} skills in the project."

        ]

    })


    # ==================================================
    # STEP 4
    # ==================================================

    roadmap.append({

        "phase": "Phase 4 - Prepare for the Target Role",

        "tasks": [

            f"Practice interview questions for {target_role}.",

            "Improve your resume and practical portfolio."

        ]

    })


    return roadmap


# ==================================================
# MAIN RECOMMENDATION
# ==================================================

def get_main_recommendation(
    current_role,
    target_role,
    skills_to_learn
):

    if not skills_to_learn:

        return (

            f"You already have a strong skill base for {target_role}. "
            f"Focus on projects, practical experience and interview preparation."

        )


    if len(skills_to_learn) <= 2:

        return (

            f"The transition from {current_role} to {target_role} "
            f"is a good option. Focus on the remaining required skills "
            f"and build a practical project."

        )


    elif len(skills_to_learn) <= 4:

        return (

            f"You can move from {current_role} to {target_role}, "
            f"but you should first strengthen the required target-role skills."

        )


    else:

        return (

            f"The transition from {current_role} to {target_role} "
            f"will require more preparation. Build the required skills "
            f"step by step before applying for the target role."

        )


# ==================================================
# TEST
# ==================================================

if __name__ == "__main__":

    test_transitions = [

        (
            "Game Developer",
            "Web Developer"
        ),

        (
            "Game Developer",
            "Mobile Developer"
        ),

        (
            "Frontend Developer",
            "Web Developer"
        ),

        (
            "Backend Developer",
            "Full Stack Python Developer"
        ),

        (
            "Data Analyst",
            "Data Scientist"
        ),

        (
            "Data Scientist",
            "AIML"
        )
    ]


    print("\nCareer Transition Analysis")
    print("===========================")


    for current_role, target_role in test_transitions:

        result = analyze_transition(

            current_role,

            target_role,

            "Entry",

            "Bachelor's in Computer Science"

        )


        print("\n----------------------------------")

        print(
            f"{current_role} -> {target_role}"
        )

        print(
            "Common Skills:",
            result["common_skills"]
        )

        print(
            "Related Skills:",
            result["related_skills"]
        )

        print(
            "Skills Required:",
            result["skills_to_learn"]
        )

        print(
            "Skill Match:",
            result["skill_match"],
            "%"
        )

        print(
            "Experience Match:",
            result["experience_match"],
            "%"
        )

        print(
            "Education Match:",
            result["education_match"],
            "%"
        )

        print(
            "Transition Score:",
            result["transition_score"],
            "%"
        )

        print(
            "Difficulty:",
            result["difficulty"]
        )
