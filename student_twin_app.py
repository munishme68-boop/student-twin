import json
import os
import streamlit as st


from knowledge_decay import apply_decay_to_student
from student_decision import decide_next_action
from adaptive_recommendation import generate_recommendation
from adaptive_question import (
    get_next_question,
    answer_question,
    get_next_difficulty
)

from question_bank import question_bank
from knowledge_graph import knowledge_graph


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Student Twin",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------
# PREMIUM UI THEME
# --------------------------------
st.markdown("""
<style>
:root { --st-radius: 18px; }
.block-container { padding-top: 1.5rem; padding-bottom: 3rem; max-width: 1500px; }
section[data-testid="stSidebar"] { border-right: 1px solid rgba(128,128,128,.18); }
section[data-testid="stSidebar"] > div { padding-top: 1.2rem; }
section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 0.65rem 0.8rem; border-radius: 12px; margin: 0.12rem 0;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background: rgba(99,102,241,.10); }
[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(127,127,127,.08), rgba(127,127,127,.025));
    border: 1px solid rgba(128,128,128,.16); border-radius: 16px; padding: 1rem;
}
.stButton > button { border-radius: 12px; font-weight: 650; min-height: 2.65rem; }
div[data-testid="stProgress"] > div > div { border-radius: 99px; }
.stAlert { border-radius: 14px; }
.twin-hero {
    padding: 1.7rem 1.9rem; border-radius: 24px; margin-bottom: 1.2rem;
    border: 1px solid rgba(99,102,241,.18);
    background: linear-gradient(135deg, rgba(99,102,241,.12), rgba(59,130,246,.06) 55%, rgba(16,185,129,.05));
}
.twin-hero h1 { margin: 0 0 .35rem 0; font-size: 2.15rem; }
.twin-hero p { margin: 0; opacity: .78; font-size: 1rem; }
.twin-card {
    padding: 1.15rem 1.2rem; border-radius: 18px;
    border: 1px solid rgba(128,128,128,.16);
    background: rgba(127,127,127,.045); height: 100%;
}
.twin-card .eyebrow { font-size: .78rem; opacity: .65; text-transform: uppercase; letter-spacing: .08em; }
.twin-card .value { font-size: 1.45rem; font-weight: 750; margin-top: .3rem; }
.twin-card .muted { opacity: .68; font-size: .86rem; margin-top: .25rem; }
.twin-focus {
    padding: 1.25rem 1.35rem; border-radius: 18px;
    border: 1px solid rgba(139,92,246,.22);
    background: linear-gradient(135deg, rgba(139,92,246,.10), rgba(99,102,241,.04));
}
.twin-badge { display:inline-block; padding:.28rem .62rem; border-radius:999px; font-size:.76rem; font-weight:700; background:rgba(99,102,241,.12); }
.twin-small { opacity:.68; font-size:.82rem; }
.twin-divider { height:1px; background:rgba(128,128,128,.16); margin:1rem 0; }
</style>
""", unsafe_allow_html=True)
# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------

# Apply page requests before the navigation widget is created.
# Streamlit does not allow changing a widget's own session-state key
# after that widget has already been instantiated.
if "nav_request" in st.session_state:
    st.session_state.nav_page = st.session_state.nav_request
    del st.session_state.nav_request

st.sidebar.title("🎓 Student Twin")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🧠 My Twin",
        "🎯 Learn",
        "📚 Topics",
        "📊 Analytics",
        "🤖 AI Twin",
        "⚙ Settings"
    ],
    key="nav_page"
)

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "previous_question_difficulty" not in st.session_state:
    st.session_state.previous_question_difficulty = None    

if "session_started" not in st.session_state:
    st.session_state.session_started = False

if "session_questions" not in st.session_state:
    st.session_state.session_questions = 0

if "session_correct_answers" not in st.session_state:
    st.session_state.session_correct_answers = 0

if "session_initial_mastery" not in st.session_state:
    st.session_state.session_initial_mastery = 0    

if "session_question_ids" not in st.session_state:
    st.session_state.session_question_ids = []    

if "session_topic" not in st.session_state:
    st.session_state.session_topic = None    

if "assessment_started" not in st.session_state:
    st.session_state.assessment_started = False

if "assessment_questions" not in st.session_state:
    st.session_state.assessment_questions = []

if "assessment_index" not in st.session_state:
    st.session_state.assessment_index = 0

if "assessment_answers" not in st.session_state:
    st.session_state.assessment_answers = []    

if "assessment_completed" not in st.session_state:
    st.session_state.assessment_completed = False

if "assessment_accuracy" not in st.session_state:
    st.session_state.assessment_accuracy = 0.0    

if "assessment_results_shown" not in st.session_state:
    st.session_state.assessment_results_shown = False


if "student_type" not in st.session_state:
    st.session_state.student_type = None
# --------------------------------
# LOAD STUDENT
# --------------------------------

def load_student():

    with open(
        "student_data.json",
        "r"
    ) as file:

        student = json.load(file)

    return student


def create_new_student(
    name,
    email,
    goal
):

    student_id = email.strip().lower()

    student = {

        "student_id": student_id,

        "email": email.strip().lower(),

        "name": name,

        "profile": {
            "goal": goal
        },

        "knowledge": {
            topic: 0.0
            for topic in knowledge_graph
        },

        "history": []

    }

    return student

def save_student(student):

    email = student["email"].strip().lower()

    safe_email = (
        email
        .replace("@", "_at_")
        .replace(".", "_")
    )

    students_folder = os.path.join(
        os.path.dirname(__file__),
        "students"
    )

    os.makedirs(
        students_folder,
        exist_ok=True
    )

    file_path = os.path.join(
        students_folder,
        f"{safe_email}.json"
    )

    with open(
        file_path,
        "w"
    ) as file:

        json.dump(
            student,
            file,
            indent=4
        )

def load_student_by_email(email):

    email = email.strip().lower()

    safe_email = (
        email
        .replace("@", "_at_")
        .replace(".", "_")
    )

    students_folder = os.path.join(
        os.path.dirname(__file__),
        "students"
    )

    new_file_path = os.path.join(
        students_folder,
        f"{safe_email}.json"
    )

    old_file_path = os.path.join(
        students_folder,
        f"{email}.json"
    )

    try:

        with open(
            new_file_path,
            "r"
        ) as file:

            student = json.load(file)

    except FileNotFoundError:

        with open(
            old_file_path,
            "r"
        ) as file:

            student = json.load(file)


    # --------------------------------
    # ADD NEW TOPICS TO EXISTING STUDENT
    # --------------------------------

    for topic in knowledge_graph:

        if topic not in student["knowledge"]:

            student["knowledge"][topic] = 0.0


    return student

def student_exists(email):

    email = email.strip().lower()

    safe_email = (
        email
        .replace("@", "_at_")
        .replace(".", "_")
    )

    students_folder = os.path.join(
        os.path.dirname(__file__),
        "students"
    )

    file_path = os.path.join(
        students_folder,
        f"{safe_email}.json"
    )

    return os.path.exists(file_path)


if "student" not in st.session_state:
    # --------------------------------
    # STUDENT TYPE SELECTION
    # --------------------------------

    st.header("🚀 Get Started")

    student_type = st.radio(
        "Are you a new or existing student?",
        [
            "New Student",
            "Existing Student"
        ],
        horizontal=True
    )
    st.session_state.student_type = student_type


    # --------------------------------
    # NEW STUDENT
    # --------------------------------

    if student_type == "New Student":

        st.subheader("Create Your Student Twin")

        new_name = st.text_input(
            "Enter your name"
        )

        new_email = st.text_input(
            "Enter your email"
        )

        new_goal = st.selectbox(
            "Choose your learning goal",
            [
                "Become an AI Engineer",
                "Become a Data Scientist",
                "Computer Vision",
                "Custom"
            ]
        )

        if st.button("Create Student Twin"):

            if new_name.strip() == "":
                st.warning("Please enter your name.")

            elif (
                "@" not in new_email
                or new_email.count("@") != 1
                or new_email.startswith("@")
                or new_email.endswith("@")
            ):
                st.warning(
                    "Please enter a valid email address."
                )

            elif student_exists(new_email):
                st.warning(
                    "A Student Twin with this email already exists. "
                    "Please use the Existing Student option to load it."
                )

            else:

                student = create_new_student(
                    new_name,
                    new_email,
                    new_goal
                )

                st.session_state.student = student

                save_student(student)

                st.success(
                    "Student Twin created successfully!"
                )

    # --------------------------------
    # EXISTING STUDENT
    # --------------------------------

    else:

        st.subheader("Load Your Student Twin")

        existing_email = st.text_input(
            "Enter your email"
        )

        if st.button("Load Student Twin"):

            try:

                student = load_student_by_email(
                    existing_email
                )

                student = apply_decay_to_student(
                    student
                )

                st.session_state.student = student

                st.success(
                    "Student Twin loaded successfully!"
                )

            except FileNotFoundError:

                st.error(
                    "No Student Twin found for this email."
                )

    # --------------------------------

else:
    student_type = st.session_state.student_type
# WAIT FOR STUDENT
# --------------------------------

if "student" not in st.session_state:
    st.info(
        "Please create or select a student profile to continue."
    )
    st.stop()

student = st.session_state.student

# --------------------------------
# SIDEBAR PROFILE
# --------------------------------
overall_sidebar_mastery = (
    sum(student.get("knowledge", {}).values()) / len(student.get("knowledge", {}))
    if student.get("knowledge") else 0
)
st.sidebar.markdown("<div class='twin-divider'></div>", unsafe_allow_html=True)
st.sidebar.markdown(
    f"<div class='twin-card'><div class='eyebrow'>Active learner</div>"
    f"<div class='value'>{student.get('name', 'Student')}</div>"
    f"<div class='muted'>{student.get('profile', {}).get('goal', 'Learning')}</div>"
    f"<div class='muted'>Twin mastery · {overall_sidebar_mastery * 100:.1f}%</div></div>",
    unsafe_allow_html=True
)

# --------------------------------
# ASSESSMENT RESULT SCREEN
# --------------------------------

if st.session_state.assessment_results_shown:

    st.header("📊 Your Assessment Result")

    accuracy = (
        st.session_state.assessment_accuracy
    )

    correct_answers = sum(
        1
        for answer in st.session_state.assessment_answers
        if answer["correct"]
    )

    total_questions = len(
        st.session_state.assessment_answers
    )

    st.metric(
        "Assessment Accuracy",
        f"{accuracy * 100:.0f}%"
    )

    st.write(
        f"You answered **{correct_answers} "
        f"out of {total_questions} questions correctly.**"
    )

    st.subheader("📚 Topic-wise Performance")

    for answer in st.session_state.assessment_answers:

        topic = answer["topic"]

        topic_name = (
            topic
            .replace("_", " ")
            .title()
        )

        mastery = student["knowledge"].get(
            topic,
            0.0
        )

        if answer["correct"]:

            st.success(
                f"{topic_name}: "
                f"{mastery * 100:.0f}% — Strong"
            )

        else:

            st.warning(
                f"{topic_name}: "
                f"{mastery * 100:.0f}% — Needs Improvement"
            )

    if accuracy >= 0.80:

        st.success(
            "Excellent starting knowledge! "
            "Your Student Twin will begin with more challenging topics."
        )

    elif accuracy >= 0.60:

        st.info(
            "Good starting knowledge! "
            "Your Student Twin will focus on strengthening your weaker areas."
        )

    else:

        st.warning(
            "Your Student Twin will begin with foundational topics "
            "and gradually increase difficulty as your mastery improves."
        )

    st.divider()

    st.write(
        "Your assessment results have been saved. "
        "The Student Twin will now personalize your learning."
    )

    if st.button("Continue to Student Twin"):

        st.session_state.assessment_results_shown = False

        st.rerun()

    st.stop()

# --------------------------------
# INITIAL ASSESSMENT
# --------------------------------

if (
    student_type == "New Student"
    and not st.session_state.assessment_completed
):

    st.header("🧠 Initial Skill Assessment")

    # --------------------------------
    # START ASSESSMENT
    # --------------------------------

    if not st.session_state.assessment_started:

        st.write(
            "Before creating your personalized Student Twin, "
            "we need to understand your current knowledge level."
        )

        st.info(
            "You will answer a short assessment covering "
            "different AI and machine-learning topics."
        )

        assessment_topic = st.selectbox(
            "Choose a topic for your initial assessment:",
            [
                "python",
                "probability",
                "statistics",
                "machine_learning",
                "neural_networks",
                "convolution",
                "cnn",
                "rnn",
                "lstm",
                "natural_language_processing",
                "transformers",
                "image_classification",
                "object_detection",
                "word_embeddings",
                "generative_ai",
                "large_language_models",
                "model_deployment",
                "mlops",
                "thermodynamics",
                "fluid_mechanics",
                "ros"
            ]
        )  
        
        if st.button("Start Initial Assessment"):

            assessment_questions = []

            # --------------------------------
            # SELECTED TOPIC
            # --------------------------------

            selected_topic = assessment_topic


            # --------------------------------
            # GET QUESTIONS FROM SELECTED TOPIC
            # --------------------------------

            selected_questions = [
                q
                for q in question_bank
                if q["topic"] == selected_topic
            ]


            # --------------------------------
            # 15 QUESTION ASSESSMENT
            # --------------------------------

            assessment_questions = (
                selected_questions[:15]
            )
            st.session_state.assessment_questions = (
                assessment_questions
            )

            st.session_state.assessment_index = 0

            st.session_state.assessment_answers = []

            st.session_state.assessment_started = True

            st.rerun()


    # --------------------------------
    # SHOW ASSESSMENT QUESTION
    # --------------------------------

    else:

        questions = (
            st.session_state.assessment_questions
        )

        current_index = (
            st.session_state.assessment_index
        )

        # --------------------------------
        # ASSESSMENT COMPLETE
        # --------------------------------

        if current_index >= len(questions):

            st.success(
                "🎉 Initial assessment completed!"
            )

            # Calculate assessment performance
            total_questions = len(
                st.session_state.assessment_answers
            )

            correct_answers = sum(
                1
                for answer in st.session_state.assessment_answers
                if answer["correct"]
            )

            if total_questions > 0:

                assessment_accuracy = (
                    correct_answers / total_questions
                )

            else:

                assessment_accuracy = 0.0


            # Save assessment summary
            st.session_state.assessment_accuracy = (
                assessment_accuracy
            )

            st.session_state.assessment_completed = True

            st.session_state.assessment_results_shown = True

            st.rerun()


        # --------------------------------
        # CURRENT QUESTION
        # --------------------------------

        question = questions[current_index]

        st.subheader(
            f"Question {current_index + 1} "
            f"of {len(questions)}"
        )

        st.write(
            f"**Topic:** "
            f"{question['topic'].replace('_', ' ').title()}"
        )

        st.write(
            question["question"]
        )

        selected_answer = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"assessment_answer_{current_index}"
        )

        if st.button("Submit Answer"):

            correct_answer = question["options"][
                question["answer"] - 1
            ]

            is_correct = (
                selected_answer == correct_answer
            )

            st.session_state.assessment_answers.append(
                {
                    "question_id": question["id"],
                    "topic": question["topic"],
                    "correct": is_correct
                }
            )

            # --------------------------------
            # UPDATE INITIAL MASTERY
            # --------------------------------

            topic = question["topic"]

            if is_correct:

                student["knowledge"][topic] = 0.70

            else:

                student["knowledge"][topic] = 0.30


            # --------------------------------
            # SAVE ASSESSMENT RESULT
            # --------------------------------

            save_student(student)


            # Move to next question

            st.session_state.assessment_index += 1

            st.rerun()


    # Prevent the normal Student Twin
    # from appearing during assessment

    st.stop()


# --------------------------------
# HEADER
# --------------------------------

if "student" in st.session_state:
    student = st.session_state.student
    st.markdown(
        f"<div class='twin-hero'><div class='twin-badge'>AI PERSONALIZED LEARNING</div>"
        f"<h1>Welcome back, {student['name']} 👋</h1>"
        f"<p>Your Student Twin continuously adapts the learning experience using mastery, performance, prerequisite relationships and AI decision signals.</p></div>",
        unsafe_allow_html=True
    )

if page == "🧠 My Twin":
    # --------------------------------
    # STUDENT OVERVIEW
    # --------------------------------



    if "student" in st.session_state:

        student = st.session_state.student

        st.header("👤 Student Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.caption("Student")

            st.write(
                student["name"]
            )

        with col2:

            st.caption("Learning Goal")

            st.write(
                student["profile"]["goal"]
            )

        with col3:

            st.caption("Field")

            st.write(
                "AI & Robotics"
            )

        with col4:

            st.caption("Student ID")

            st.write(
                student["student_id"]
            )

        st.divider()


decision = decide_next_action(
    student
)

recommendation = generate_recommendation(
    student
)




if page == "🏠 Home":
    # --------------------------------
    # DASHBOARD SUMMARY
    # --------------------------------

    if "student" in st.session_state:

        student = st.session_state.student

        st.divider()

        # --------------------------------
        # HOME HEADER
        # --------------------------------

        st.title(
            f"Good morning, {student['name']} 👋"
        )

        st.subheader(
            "Your AI learning state"
        )

        history = student.get(
            "history",
            []
        )

        # --------------------------------
        # QUICK OVERVIEW
        # --------------------------------
        answered_today = len(history[-5:])
        recent_correct = sum(1 for record in history[-5:] if record.get("correct") is True)
        streak = 0
        for record in reversed(history):
            if record.get("correct") is True:
                streak += 1
            else:
                break

        q1, q2, q3, q4 = st.columns(4)
        with q1:
            st.markdown(f"<div class='twin-card'><div class='eyebrow'>Questions answered</div><div class='value'>{len(history)}</div><div class='muted'>All recorded learning activity</div></div>", unsafe_allow_html=True)
        with q2:
            st.markdown(f"<div class='twin-card'><div class='eyebrow'>Recent accuracy</div><div class='value'>{(recent_correct / answered_today * 100) if answered_today else 0:.0f}%</div><div class='muted'>Latest {answered_today} questions</div></div>", unsafe_allow_html=True)
        with q3:
            st.markdown(f"<div class='twin-card'><div class='eyebrow'>Current streak</div><div class='value'>{streak}</div><div class='muted'>Consecutive correct answers</div></div>", unsafe_allow_html=True)
        with q4:
            focus_label = decision.get("topic") or "Balanced"
            focus_label = focus_label.replace("_", " ").title()
            st.markdown(f"<div class='twin-card'><div class='eyebrow'>AI focus</div><div class='value'>{focus_label}</div><div class='muted'>Current priority from the Twin</div></div>", unsafe_allow_html=True)

        st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)

        # --------------------------------
        # OVERALL MASTERY
        # --------------------------------

        if student["knowledge"]:

            overall_mastery = (
                sum(
                    student["knowledge"].values()
                )
                / len(
                    student["knowledge"]
                )
            )

        else:

            overall_mastery = 0

        # --------------------------------
        # ACCURACY
        # --------------------------------

        if history:

            correct_answers = sum(
                1
                for record in history
                if record.get("correct") is True
            )

            accuracy = (
                correct_answers
                / len(history)
            )

        else:

            correct_answers = 0
            accuracy = 0

        # --------------------------------
        # RISK
        # --------------------------------

        risk_level = decision.get(
            "risk_level",
            "Unknown"
        )

        # --------------------------------
        # HOME METRIC CARDS
        # --------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🧠 Mastery",
                f"{overall_mastery * 100:.1f}%"
            )

        with col2:

            st.metric(
                "🎯 Accuracy",
                f"{accuracy * 100:.1f}%"
            )

        with col3:

            st.metric(
                "⚠️ Risk",
                risk_level
            )

        # --------------------------------
        # OVERALL LEARNING PROGRESS
        # --------------------------------

        st.subheader(
            "📈 Overall Learning Progress"
        )

        st.progress(
            max(
                0.0,
                min(
                    1.0,
                    overall_mastery
                )
            )
        )

        st.caption(
            f"Overall mastery: "
            f"{overall_mastery * 100:.1f}%"
        )


    # --------------------------------
    # AI FOCUS AREA
    # --------------------------------

    priority_topic = decision.get("topic")

    if priority_topic is not None:

        priority_name = (
            priority_topic
            .replace("_", " ")
            .title()
        )

        st.subheader(
            "🎯 AI Focus Area"
        )

        st.info(
            f"The Student Twin currently recommends "
            f"focusing on **{priority_name}**."
        )

    else:

        st.subheader(
            "🎯 AI Focus Area"
        )

        st.success(
            "No immediate priority topic. "
            "Your current learning areas are performing well."
        )

    # --------------------------------
    # TODAY'S AI PLAN
    # --------------------------------
    if priority_topic is not None:
        focus_label = priority_topic.replace("_", " ").title()
        st.markdown(
            f"<div class='twin-focus'><div class='eyebrow'>TODAY'S AI PLAN</div>"
            f"<h3 style='margin:.35rem 0'>Focus on {focus_label}</h3>"
            f"<div class='twin-small'>The Twin has identified this area as the most useful next learning target based on your current state.</div></div>",
            unsafe_allow_html=True
        )
        st.markdown("<div style='height:.35rem'></div>", unsafe_allow_html=True)
        a1, a2 = st.columns(2)
        with a1:
            if st.button("🚀 Start AI Recommended Session", use_container_width=True):
                st.session_state.nav_request = "🎯 Learn"
                st.rerun()
        with a2:
            if st.button("🧠 Inspect AI Decision", use_container_width=True):
                st.session_state.nav_request = "🤖 AI Twin"
                st.rerun()

    # --------------------------------
    # AI LEARNING STATUS
    # --------------------------------

    if "student" in st.session_state:

        student = st.session_state.student

        st.subheader("🧠 AI Learning Status")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.info(
                "🎯 Personalized Learning\n\n"
                "Your learning path adapts "
                "to your performance."
            )

        with col2:

            st.info(
                "📈 Continuous Assessment\n\n"
                "Your mastery is updated "
                "after every question."
            )

        with col3:

            st.info(
                "🤖 AI Decision Making\n\n"
                "The system selects what "
                "you should study next."
            )



if page == "🤖 AI Twin":
    # --------------------------------
    # AI DECISION
    # --------------------------------



    st.divider()

    st.header("🤖 AI Decision Center")

    st.write(
        "The Student Twin analyzes your knowledge, "
        "recent performance, learning history and "
        "risk signals to determine what you should "
        "focus on next."
    )


    # --------------------------------
    # AI METRICS
    # --------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        if decision["topic"] is not None:

            priority_name = (
                decision["topic"]
                .replace("_", " ")
                .title()
            )

        else:

            priority_name = "No Priority"

        st.metric(
            "🎯 Priority Topic",
            priority_name
        )


    with col2:

        st.metric(
            "⚠️ Risk Level",
            decision["risk_level"]
        )


    with col3:

        st.metric(
            "📈 Risk Score",
            f"{decision['risk_score']:.1f}"
        )


    # --------------------------------
    # AI / ML INFORMATION
    # --------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if student["knowledge"]:

            overall_mastery = (
                sum(student["knowledge"].values())
                / len(student["knowledge"])
            )

        else:

            overall_mastery = 0

        st.metric(
            "🧠 Overall Mastery",
            f"{overall_mastery * 100:.1f}%"
        )


    with col2:

        ml_probability = decision.get(
            "ml_probability"
        )

        if ml_probability is not None:

            ml_prediction = (
                ml_probability * 100
            )

            st.metric(
                "🤖 ML Mistake Probability",
                f"{ml_prediction:.1f}%"
            )

        else:

            st.metric(
                "🤖 ML Mistake Probability",
                "N/A"
            )


    # --------------------------------
    # AI DECISION EXPLANATION
    # --------------------------------

    st.subheader(
        "🔎 What the AI Decided"
    )

    st.info(
        f"🤖 **Recommended Action:** "
        f"{decision['action']}"
    )


    # --------------------------------
    # RISK INTERPRETATION
    # --------------------------------

    risk_level = decision["risk_level"]

    if risk_level == "High":

        st.error(
            "🔴 High Risk — this area requires "
            "immediate attention and additional practice."
        )

    elif risk_level == "Medium":

        st.warning(
            "🟡 Medium Risk — this area may benefit "
            "from additional revision and practice."
        )

    elif risk_level == "Low":

        st.success(
            "🟢 Low Risk — your current performance "
            "does not indicate an immediate problem."
        )

    else:

        st.info(
            "🔵 Risk Unknown — the Student Twin needs "
            "more learning evidence before making a "
            "strong risk prediction."
        )


    # --------------------------------
    # ADAPTIVE RECOMMENDATION
    # --------------------------------

    st.divider()

    st.header(
        "🧠 Adaptive Recommendation"
    )

    st.write(
        "Based on your current mastery, "
        "performance and learning state, "
        "the Student Twin recommends the following action."
    )

    col1, col2 = st.columns(2)

    with col1:

        if recommendation["topic"] is not None:

            topic_name = (
                recommendation["topic"]
                .replace("_", " ")
                .title()
            )

        else:

            topic_name = "No Priority Topic"

        st.metric(
            "🎯 Recommended Topic",
            topic_name
        )

    with col2:

        st.metric(
            "⚡ Action Type",
            recommendation["action_type"]
        )

    st.subheader("💡 What You Should Do")

    st.info(
        recommendation["recommendation"]
    )


if page == "🎯 Learn":
        # --------------------------------
        # SESSION BUTTON
        # --------------------------------


    st.divider()
    st.header("🎯 Learning Session")

    st.write(
        "The Student Twin will select questions "
        "based on your current knowledge and "
        "performance."
    )

    selected_topic = st.selectbox(
        "Choose a topic for this session:",
        sorted(student["knowledge"].keys())
    )


    if st.button("Start Adaptive Learning Session"):

        st.session_state.session_questions = 0

        st.session_state.session_correct_answers = 0

        st.session_state.session_question_ids = []

        session_topic = selected_topic

        st.session_state.session_topic = session_topic

        st.session_state.session_initial_mastery = (
            student["knowledge"].get(
                session_topic,
                0
            )
        )

        question = get_next_question(
            student,
            session_topic=session_topic,
            recommended_difficulty=None,
            session_question_ids=(
                st.session_state.session_question_ids
            )
        )

        if question is not None:

            st.session_state.current_question = question
            st.session_state.previous_question_difficulty = (
                question["difficulty"]
            )
            st.session_state.session_started = True

        else:

            st.warning(
                "No suitable question is currently available."
            )



    if st.session_state.session_started:

        question = st.session_state.current_question

        st.write(
            f"### Question "
            f"{st.session_state.session_questions + 1} of 10"
        )

        st.progress(
            st.session_state.session_questions / 10
        )

        st.subheader(
            f"Topic: {question['topic'].replace('_', ' ').title()}"
        )

        st.write(
            f"Difficulty: **{question['difficulty'].title()}**"
        )

        st.write(
            f"### {question['question']}"
        )

        # --------------------------------
        # QUESTION FORM
        # --------------------------------

        with st.form(
            key=f"question_form_{question['id']}"
        ):

            selected_answer = st.radio(
                "Select your answer:",
                question["options"]
            )

            submitted = st.form_submit_button(
                "Submit Answer"
            )


        # --------------------------------
        # PROCESS ANSWER
        # --------------------------------

        if submitted:

            selected_index = (
                question["options"].index(
                    selected_answer
                ) + 1
            )

            correct = (
                selected_index ==
                question["answer"]
            )

            current_difficulty = question["difficulty"]



            next_difficulty = get_next_difficulty(
                current_difficulty,
                correct,
                st.session_state.session_questions
            )

            force_next_difficulty = None

            if st.session_state.session_questions < 1:
                force_next_difficulty = "medium"


            # Update Student Twin knowledge
            answer_question(
                student,
                question,
                correct
            )


            # Record this question in the
            # current session
            st.session_state.session_question_ids.append(
                question["id"]
            )


            # Save updated student data
            save_student(student)


            # Update session statistics
            st.session_state.session_questions += 1

            if correct:

                st.session_state.session_correct_answers += 1


            # --------------------------------
            # SESSION COMPLETE
            # --------------------------------

            if st.session_state.session_questions >= 10:

                st.session_state.current_question = None
                st.session_state.session_started = False


                session_accuracy = (
                    st.session_state.session_correct_answers /
                    st.session_state.session_questions
                )


                session_topic = (
                    st.session_state.session_topic
                )


                session_final_mastery = (
                    student["knowledge"].get(
                        session_topic,
                        0
                    )
                )


                mastery_change = (
                    session_final_mastery -
                    st.session_state.session_initial_mastery
                )


                # --------------------------------
                # SESSION RESULTS
                # --------------------------------

                st.success(
                    "🎉 10-question adaptive session completed!"
                )

                st.subheader(
                    "📊 Session Results"
                )

                st.write(
                    "Here is how you performed during this "
                    "learning session."
                )


                # --------------------------------
                # SESSION PERFORMANCE
                # --------------------------------

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "📝 Questions",
                        st.session_state.session_questions
                    )

                with col2:

                    st.metric(
                        "✅ Correct",
                        st.session_state.session_correct_answers
                    )

                with col3:

                    st.metric(
                        "🎯 Accuracy",
                        f"{session_accuracy * 100:.1f}%"
                    )


                # --------------------------------
                # MASTERY PROGRESS
                # --------------------------------

                st.subheader(
                    "🧠 Mastery Progress"
                )

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Starting Mastery",
                        f"{st.session_state.session_initial_mastery * 100:.1f}%"
                    )

                with col2:

                    st.metric(
                        "Final Mastery",
                        f"{session_final_mastery * 100:.1f}%"
                    )

                with col3:

                    st.metric(
                        "Mastery Change",
                        f"{mastery_change * 100:+.1f}%"
                    )


                # --------------------------------
                # MASTERY PROGRESS BAR
                # --------------------------------

                st.progress(
                    max(
                        0.0,
                        min(
                            1.0,
                            session_final_mastery
                        )
                    )
                )


                # --------------------------------
                # PERFORMANCE
                # --------------------------------

                st.subheader(
                    "📈 Session Performance"
                )

                if session_accuracy >= 0.80:

                    st.success(
                        "🌟 Performance: Excellent"
                    )

                elif session_accuracy >= 0.60:

                    st.info(
                        "👍 Performance: Good"
                    )

                else:

                    st.warning(
                        "📚 Performance: Needs Improvement"
                    )


                # --------------------------------
                # SESSION SUMMARY
                # --------------------------------

                st.subheader(
                    "📋 Session Summary"
                )

                if (
                    session_accuracy >= 0.80
                    and mastery_change > 0
                ):

                    st.success(
                        "Strong session — your performance "
                        "was good and your mastery improved."
                    )

                elif (
                    session_accuracy >= 0.60
                    and mastery_change > 0
                ):

                    st.info(
                        "Positive session — your performance "
                        "was reasonable and your mastery improved."
                    )

                elif (
                    session_accuracy < 0.60
                    and mastery_change > 0
                ):

                    st.warning(
                        "You made some mastery improvement, "
                        "but your accuracy shows that more practice "
                        "is needed."
                    )

                else:

                    st.warning(
                        "Your mastery did not improve during this "
                        "session. More focused practice is recommended."
                    )


                # --------------------------------
                # AI NEXT ACTION
                # --------------------------------

                st.divider()

                st.subheader(
                    "🤖 AI Next Action"
                )

                st.write(
                    "After analyzing your updated performance, "
                    "the Student Twin has selected the following "
                    "next action."
                )


                next_decision = decide_next_action(
                    student
                )

                next_topic = (
                    next_decision["topic"]
                )


                if next_topic is not None:

                    next_topic_name = (
                        next_topic
                        .replace("_", " ")
                        .title()
                    )

                else:

                    next_topic_name = (
                        "No Priority Topic"
                    )


                # --------------------------------
                # AI DECISION METRICS
                # --------------------------------

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "🎯 Priority Topic",
                        next_topic_name
                    )

                with col2:

                    st.metric(
                        "⚠️ Risk Level",
                        next_decision["risk_level"]
                    )


                st.info(
                    f"🤖 **Recommended Action:** "
                    f"{next_decision['action']}"
                )


                # --------------------------------
                # WHY THE AI CHOSE IT
                # --------------------------------

                if next_topic is not None:

                    topic_attempts = sum(
                        1
                        for record in student["history"]
                        if record.get("topic") == next_topic
                    )

                    topic_mastery = student["knowledge"].get(
                        next_topic,
                        0
                    )

                    st.write(
                        "### 🔎 Why did the AI choose this?"
                    )

                    st.write(
                        f"The Student Twin identified "
                        f"**{next_topic_name}** as the current "
                        f"priority based on your learning state."
                    )

                    st.caption(
                        f"Current mastery: "
                        f"{topic_mastery * 100:.1f}% · "
                        f"Recorded attempts: {topic_attempts}"
                    )

                else:

                    st.write(
                        "### 🔎 Why did the AI choose this?"
                    )

                    st.info(
                        "The Student Twin currently has no priority "
                        "topic. Your assessed areas are performing "
                        "strongly, so no immediate intervention is required."
                    )


                st.write(
                    "You can start another adaptive session "
                    "whenever you are ready."
                )


                # --------------------------------
                # GET NEXT QUESTION
                # --------------------------------

            else:

                # Keep the session locked to the same topic
                locked_topic = (
                    st.session_state.session_topic
                )



                next_question = get_next_question(
                    student,
                    session_topic=locked_topic,
                    recommended_difficulty=next_difficulty,
                    session_question_ids=(
                        st.session_state.session_question_ids
                    ),
                    force_difficulty=next_difficulty
                )


                if next_question is not None:

                    st.session_state.current_question = (
                        next_question
                    )

                    # Keep the session active
                    st.session_state.session_started = True

                    # Reload the page with the new question
                    st.rerun()

                else:

                    st.session_state.current_question = None
                    st.session_state.session_started = False

                    st.warning(
                        "No more suitable questions are available "
                        "for this session topic."
                    )



if page == "📚 Topics":
    # --------------------------------
    # MASTERY
    # --------------------------------


    st.divider()

    st.header("📊 Topic Mastery")

    st.write(
        "Your Student Twin continuously tracks your mastery "
        "across different learning topics."
    )

    knowledge = student["knowledge"]

    topic_filter = st.selectbox(
        "Topic view",
        ["All topics", "Strong", "Developing", "Needs improvement"],
        key="topic_filter"
    )

    if topic_filter == "Strong":
        topics = [(t, m) for t, m in knowledge.items() if m >= 0.80]
    elif topic_filter == "Developing":
        topics = [(t, m) for t, m in knowledge.items() if 0.60 <= m < 0.80]
    elif topic_filter == "Needs improvement":
        topics = [(t, m) for t, m in knowledge.items() if m < 0.60]
    else:
        topics = list(knowledge.items())


    for i in range(0, len(topics), 3):

        cols = st.columns(3)

        for j, (topic, mastery) in enumerate(
            topics[i:i + 3]
        ):

            with cols[j]:

                topic_name = (
                    topic
                    .replace("_", " ")
                    .title()
                )

                percentage = mastery * 100

                st.subheader(
                    topic_name
                )

                st.progress(
                    max(
                        0.0,
                        min(
                            1.0,
                            mastery
                        )
                    )
                )

                st.caption(
                    f"{percentage:.1f}% mastery"
                )

                if mastery >= 0.80:

                    st.success(
                        "Strong"
                    )

                elif mastery >= 0.60:

                    st.info(
                        "Developing"
                    )

                elif mastery > 0:

                    st.warning(
                        "Needs Practice"
                    )

                else:

                    st.caption(
                        "Not assessed yet"
                    )


    # --------------------------------
    # KNOWLEDGE GRAPH
    # --------------------------------

    st.divider()

    st.header("🕸️ Knowledge Graph")

    st.caption(
        "Your learning topics and their prerequisite relationships."
    )

    # --------------------------------
    # FIND AI PRIORITY CHAIN
    # --------------------------------

    priority_topic = decision["topic"]

    priority_chain = set(
        knowledge_graph.get(
            priority_topic,
            []
        )
    )

    # Include deeper prerequisites
    def collect_prerequisites(topic):

        for prerequisite in knowledge_graph.get(
            topic,
            []
        ):

            priority_chain.add(
                prerequisite
            )

            collect_prerequisites(
                prerequisite
            )


    collect_prerequisites(
        priority_topic
    )

    # --------------------------------
    # CREATE GRAPH
    # --------------------------------

    dot = """
    digraph {
        graph [
            rankdir=LR,
            bgcolor="transparent",
            nodesep=0.6,
            ranksep=1.0,
            pad=0.3
        ]

        node [
            shape=box,
            style="rounded,filled",
            fontname="Arial",
            fontsize=11,
            margin="0.18,0.12"
        ]

        edge [
            color="#888888",
            penwidth=1.5,
            arrowsize=0.7
        ]
    """

    # --------------------------------
    # CREATE TOPIC NODES
    # --------------------------------

    for topic in knowledge_graph:

        mastery = student["knowledge"].get(
            topic,
            0
        )

        percentage = mastery * 100

        topic_name = topic.replace(
            "_",
            " "
        ).title()

        # ----------------------------
        # NODE COLOR
        # ----------------------------

        if percentage >= 80:

            node_color = "#B7F7C5"

        elif percentage >= 60:

            node_color = "#B9D9FF"

        elif percentage >= 40:

            node_color = "#FFE6A7"

        else:

            node_color = "#FFB8B8"

        # ----------------------------
        # DEFAULT BORDER
        # ----------------------------

        border_color = "#888888"
        border_width = 1

        # ----------------------------
        # PRIORITY TOPIC
        # ----------------------------

        if topic == priority_topic:

            border_color = "#6366F1"
            border_width = 4

        # ----------------------------
        # PREREQUISITE CHAIN
        # ----------------------------

        elif topic in priority_chain:

            border_color = "#6366F1"
            border_width = 2

        # ----------------------------
        # CREATE NODE
        # ----------------------------

        dot += f'''
            "{topic}" [
                label="{topic_name}\\n{percentage:.0f}% mastery",
                fillcolor="{node_color}",
                color="{border_color}",
                penwidth={border_width}
            ]
        '''

    # --------------------------------
    # CREATE CONNECTIONS
    # --------------------------------

    for topic, prerequisites in knowledge_graph.items():

        for prerequisite in prerequisites:

            if (
                topic == priority_topic
                or topic in priority_chain
                or prerequisite in priority_chain
            ):

                edge_color = "#6366F1"
                edge_width = 2.5

            else:

                edge_color = "#888888"
                edge_width = 1.5

            dot += f'''
                "{prerequisite}" -> "{topic}"
                [
                    color="{edge_color}",
                    penwidth={edge_width}
                ]
            '''

    # --------------------------------
    # CLOSE GRAPH
    # --------------------------------

    dot += """
    }
    """

    # --------------------------------
    # DISPLAY GRAPH
    # --------------------------------

    st.graphviz_chart(
        dot,
        width="stretch"
    )

    # --------------------------------
    # LEGEND
    # --------------------------------

    st.caption(
        "🟢 Strong   🔵 Good   🟡 Developing   🔴 Weak   "
        "• Purple border = AI priority/prerequisite chain"
    )



if page == "📊 Analytics":
    # --------------------------------
    # PERFORMANCE & LEARNING ANALYTICS
    # --------------------------------

    st.divider()

    st.header("📈 Learning Analytics")

    st.write(
        "The Student Twin analyzes your learning history, "
        "accuracy and mastery to understand your current "
        "learning performance."
    )

    history = student.get(
        "history",
        []
    )


    # --------------------------------
    # CALCULATE PERFORMANCE
    # --------------------------------

    if history:

        total_questions = len(history)

        correct_questions = sum(
            1
            for record in history
            if record.get("correct") is True
        )

        overall_accuracy = (
            correct_questions /
            total_questions
        )

    else:

        total_questions = 0
        correct_questions = 0
        overall_accuracy = 0


    # --------------------------------
    # MASTERY
    # --------------------------------

    if student["knowledge"]:

        overall_mastery = (
            sum(student["knowledge"].values())
            / len(student["knowledge"])
        )

    else:

        overall_mastery = 0


    # --------------------------------
    # KEY METRICS
    # --------------------------------

    st.subheader("📊 Key Performance Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🧠 Overall Mastery",
            f"{overall_mastery * 100:.1f}%"
        )

    with col2:

        st.metric(
            "🎯 Accuracy",
            f"{overall_accuracy * 100:.1f}%"
        )

    with col3:

        st.metric(
            "📝 Questions",
            total_questions
        )

    with col4:

        st.metric(
            "✅ Correct",
            correct_questions
        )


    # --------------------------------
    # OVERALL PERFORMANCE
    # --------------------------------

    st.subheader("🎯 Overall Performance")

    st.progress(
        max(
            0.0,
            min(
                1.0,
                overall_accuracy
            )
        )
    )

    st.caption(
        f"{correct_questions} correct answers "
        f"out of {total_questions} questions"
    )


    # --------------------------------
    # PERFORMANCE TREND
    # --------------------------------

    st.subheader("📈 Performance Trend")

    if history:

        cumulative_correct = 0
        trend_data = []

        for index, record in enumerate(
            history,
            start=1
        ):

            if record.get("correct") is True:

                cumulative_correct += 1

            cumulative_accuracy = (
                cumulative_correct /
                index
            )

            trend_data.append(
                cumulative_accuracy
            )

        st.line_chart(
            trend_data,
            y_label="Accuracy",
            x_label="Question"
        )

        st.caption(
            "The chart shows cumulative accuracy "
            "as more questions are answered."
        )

    else:

        st.info(
            "Performance trend will appear "
            "after you answer questions."
        )


    # --------------------------------
    # RECENT LEARNING ACTIVITY
    # --------------------------------

    st.subheader(
        "📝 Recent Learning Activity"
    )

    if history:

        recent_history = history[-5:]

        for record in reversed(
            recent_history
        ):

            topic = record.get(
                "topic",
                "Unknown"
            )

            correct = record.get(
                "correct"
            )

            question_id = record.get(
                "question_id",
                "N/A"
            )

            topic_name = (
                topic
                .replace("_", " ")
                .title()
            )

            if correct is True:

                st.success(
                    f"Question {question_id} — "
                    f"{topic_name} — ✅ Correct"
                )

            else:

                st.warning(
                    f"Question {question_id} — "
                    f"{topic_name} — ❌ Incorrect"
                )

    else:

        st.info(
            "Learning activity will appear "
            "after you answer questions."
        )


    # --------------------------------
    # LEARNING STATUS
    # --------------------------------

    st.subheader(
        "🧭 Learning Status"
    )

    if len(history) >= 10:

        previous_history = history[-10:-5]
        recent_history = history[-5:]

        previous_correct = sum(
            1
            for record in previous_history
            if record.get("correct") is True
        )

        recent_correct = sum(
            1
            for record in recent_history
            if record.get("correct") is True
        )

        previous_accuracy = (
            previous_correct /
            len(previous_history)
        )

        recent_accuracy = (
            recent_correct /
            len(recent_history)
        )

        accuracy_change = (
            recent_accuracy -
            previous_accuracy
        )


        # --------------------------------
        # STATUS MESSAGE
        # --------------------------------

        if accuracy_change >= 0.20:

            st.success(
                "🟢 Improving — your recent "
                "performance is getting better."
            )

        elif accuracy_change <= -0.20:

            st.error(
                "🔴 Declining — your recent "
                "performance has decreased."
            )

        else:

            st.info(
                "🟡 Stable — your recent "
                "performance is relatively consistent."
            )


        # --------------------------------
        # STATUS METRICS
        # --------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Previous Accuracy",
                f"{previous_accuracy * 100:.1f}%"
            )

        with col2:

            st.metric(
                "Recent Accuracy",
                f"{recent_accuracy * 100:.1f}%"
            )

        with col3:

            st.metric(
                "Change",
                f"{accuracy_change * 100:+.1f}%"
            )

    else:

        st.info(
            "Learning status will appear "
            "after at least 10 answered questions."
        )

if page == "⚙ Settings":

    st.divider()
    st.header("⚙ Settings")
    st.write("Manage how your Student Twin behaves. These controls are presentation-level and do not alter your existing learning history.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👤 Profile")
        st.text_input("Name", value=student.get("name", ""), disabled=True)
        st.text_input("Email", value=student.get("email", ""), disabled=True)
        st.text_input("Learning goal", value=student.get("profile", {}).get("goal", ""), disabled=True)
    with col2:
        st.subheader("🤖 Twin status")
        st.success("Personalization engine active")
        st.info("BKT mastery tracking active")
        st.info("Adaptive question selection active")
        st.info("AI risk and decision layer active")

    st.caption("Advanced configuration can be added later without changing the core learning engine.")
