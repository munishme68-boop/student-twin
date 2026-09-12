
# --------------------------------
# ADAPTIVE QUESTION SYSTEM
# --------------------------------

from sympy import python

from bkt import update_knowledge

from knowledge_graph import (
    find_weakest_prerequisite
)

from question_bank import (
    get_questions
)

from progress import (
    find_weak_topics,
    calculate_recent_accuracy
)


# --------------------------------
# CHOOSE DIFFICULTY
# --------------------------------


def choose_difficulty(
    mastery,
    recent_accuracy=None
):

    # --------------------------------
    # LOW MASTERY
    # --------------------------------

    if mastery < 0.40:
        return "easy"

    # --------------------------------
    # MEDIUM MASTERY
    # --------------------------------

    elif mastery < 0.70:

        if recent_accuracy is not None:

            if recent_accuracy >= 0.80:
                return "medium"

            else:
                return "easy"

        return "medium"

    # --------------------------------
    # HIGH MASTERY
    # --------------------------------

    else:

        if recent_accuracy is not None:

            if recent_accuracy >= 0.80:
                return "hard"

            elif recent_accuracy >= 0.60:
                return "medium"

            else:
                return "easy"

        return "medium"


def get_next_difficulty(
    current_difficulty,
    correct,
    session_question_number
):

    # --------------------------------
    # FIRST TWO QUESTIONS
    # Always use Medium for baseline
    # assessment.
    # --------------------------------

    if session_question_number < 1:

        return "medium"


    # --------------------------------
    # AFTER TWO QUESTIONS
    # Adapt difficulty based on answer.
    # --------------------------------

    if correct:

        if current_difficulty == "easy":

            return "medium"

        elif current_difficulty == "medium":

            return "hard"

        else:

            # Hard + Correct → stay Hard
            return "hard"


    else:

        if current_difficulty == "hard":

            return "medium"

        elif current_difficulty == "medium":

            return "easy"

        else:

            # Easy + Wrong → stay Easy
            return "easy"



# --------------------------------
# FIND BEST TOPIC
# --------------------------------

def find_best_topic(student):

    # --------------------------------
    # CHECK AI DECISION
    # --------------------------------

    try:

        from student_decision import decide_next_action

        decision = decide_next_action(student)

        if decision is not None:

            decision_topic = decision.get(
                "topic"
            )

            risk_level = decision.get(
                "risk_level"
            )

            # Use Decision Engine for
            # High, Medium, and Unknown topics

            if (
                decision_topic is not None
                and risk_level in [
                    "High",
                    "Medium",
                    "Unknown"
                ]
            ):

                return decision_topic

    except Exception:

        pass


    # --------------------------------
    # FALLBACK TO EXISTING LOGIC
    # --------------------------------
    # --------------------------------
# FALLBACK TO EXISTING LOGIC
# --------------------------------

    weak_topics = find_weak_topics(
        student,
        threshold=0.60
    )

    if len(weak_topics) == 0:
        all_topics = [
            "python",
            "machine_learning",
            "neural_networks",
            "convolution",
            "cnn",
            "probability",
            "statistics",
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
            "mlops"
        ]

        # First check for unassessed topics

        for topic in all_topics:

            if topic not in student["knowledge"]:

                questions = get_questions(topic)

                if len(questions) > 0:

                    return topic

        # If every topic has been assessed,
        # continue practicing the weakest topic.

        weakest_topic = min(
            all_topics,
            key=lambda topic: student["knowledge"].get(
                topic,
                0
            )
        )

        return weakest_topic

    return weakest_topic

    weakest_topic = min(
        weak_topics,
        key=lambda x: x["mastery"]
    )["topic"]


    weakest_prerequisite = find_weakest_prerequisite(
        student,
        weakest_topic
    )


    if weakest_prerequisite is not None:

        if weakest_prerequisite["mastery"] < 0.60:

            return weakest_prerequisite["topic"]


    return weakest_topic

# --------------------------------
# GET NEXT QUESTION
# --------------------------------

def get_next_question(
    student,
    session_topic=None,
    recommended_difficulty=None,
    session_question_ids=None,
    force_difficulty=None
):
    if session_question_ids is None:
        session_question_ids = []


    if session_topic is None:
        topic = find_best_topic(student)
    else:
        topic = session_topic


    if topic is None:
        return None


    mastery = student["knowledge"].get(
        topic,
        0
    )


    recent_accuracy = calculate_recent_accuracy(
        student,
        topic
    )


    if recommended_difficulty is not None:

        preferred_difficulty = recommended_difficulty

    else:

        preferred_difficulty = choose_difficulty(
            mastery,
            recent_accuracy
        )


    questions = get_questions(topic)

        # --------------------------------
    # FORCE A SPECIFIC DIFFICULTY
    # --------------------------------

    if force_difficulty is not None:

        for question in questions:

            if (
                question["difficulty"] == force_difficulty
                and question["id"] not in session_question_ids
            ):

                return question

        return None


    # --------------------------------
    # FIND QUESTIONS ALREADY ASKED
    # --------------------------------

    asked_question_ids = []

    for record in student["history"]:

        if "question_id" in record:

            asked_question_ids.append(
                record["question_id"]
            )


    # --------------------------------
    # DIFFICULTY ORDER
    # --------------------------------

    if recommended_difficulty == "easy":

        difficulty_order = [
            "easy",
            "medium",
            "hard"
        ]

    elif recommended_difficulty == "medium":

        difficulty_order = [
            "medium",
            "easy",
            "hard"
        ]

    elif recommended_difficulty == "hard":

        difficulty_order = [
            "hard",
            "medium",
            "easy"
        ]

    else:

        difficulty_order = [
            "easy",
            "medium",
            "hard"
        ]


    # --------------------------------
    # 1. TRY PREFERRED DIFFICULTY
    #    UNUSED IN HISTORY AND SESSION
    # --------------------------------

    for question in questions:

        if question["difficulty"] != preferred_difficulty:
            continue

        if question["id"] in asked_question_ids:
            continue

        if question["id"] in session_question_ids:
            continue

        return question


    # --------------------------------
    # 2. REUSE PREVIOUSLY WRONG QUESTION
    #    BUT NEVER IN CURRENT SESSION
    # --------------------------------

    for question in questions:

        if question["difficulty"] != preferred_difficulty:
            continue

        if question["id"] not in asked_question_ids:
            continue

        if question["id"] in session_question_ids:
            continue

        for record in reversed(student["history"]):

            if (
                record.get("question_id") == question["id"]
                and record["correct"] == False
            ):

                return question


    # --------------------------------
# 3. REUSE PREVIOUSLY WRONG
#    QUESTIONS FROM EASIER DIFFICULTIES
# --------------------------------

    for difficulty in difficulty_order:

        if difficulty == "hard":
            continue

        for question in questions:

            if question["difficulty"] != difficulty:
                continue

            if question["id"] not in asked_question_ids:
                continue

            if question["id"] in session_question_ids:
                continue

            for record in reversed(student["history"]):

                if (
                    record.get("question_id") == question["id"]
                    and record["correct"] == False
                ):

                    return question


# --------------------------------
# 4. TRY OTHER DIFFICULTIES
#    UNUSED IN HISTORY AND SESSION
# --------------------------------

    for difficulty in difficulty_order:

        if difficulty == preferred_difficulty:
            continue

        for question in questions:

            if question["difficulty"] != difficulty:
                continue

            if question["id"] in asked_question_ids:
                continue

            if question["id"] in session_question_ids:
                continue

            return question



    # 5 reuse any previously wrong question
    # outside the current session
    for question in questions:

        if question["id"] in session_question_ids:
            continue

        if question["id"] not in asked_question_ids:
            continue

        for record in reversed(student["history"]):

            if (
                record.get("question_id") == question["id"]
                and record["correct"] == False
            ):

                return question


    # 6 FINAL SESSION FALLBACK
    # If all questions have been asked historically,
    # allow reuse of any question that is NOT already
    # part of the current session.
    for question in questions:

        if question["id"] not in session_question_ids:

            return question


    return None


# --------------------------------
# ANSWER QUESTION
# --------------------------------

def answer_question(
    student,
    question,
    correct
):

    topic = question["topic"]

    difficulty = question["difficulty"]


    old_mastery = student["knowledge"].get(
        topic,
        0
    )


    # Update mastery
    update_knowledge(
        student,
        topic,
        correct,
        difficulty
    )


    # Add question ID to latest history record
    student["history"][-1]["question_id"] = (
        question["id"]
    )


    new_mastery = student["knowledge"][topic]


    print("\nAnswer recorded.")

    print(
        "Topic:",
        topic
    )

    print(
        "Correct:",
        correct
    )

    print(
        "Previous mastery:",
        f"{old_mastery * 100:.2f}%"
    )

    print(
        "New mastery:",
        f"{new_mastery * 100:.2f}%"
    )
