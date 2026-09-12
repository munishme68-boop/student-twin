from student_decision import decide_next_action
from progress import (
    calculate_recent_accuracy,
    calculate_trend
)
from knowledge_decay import get_days_unused
from knowledge_graph import find_weakest_prerequisite
from question_bank import get_questions


def get_available_difficulties(student, topic):

    questions = get_questions(topic)

    asked_question_ids = []

    for record in student["history"]:

        if "question_id" in record:

            asked_question_ids.append(
                record["question_id"]
            )


    available_difficulties = []


    # --------------------------------
    # 1. UNUSED QUESTIONS
    # --------------------------------

    for question in questions:

        if question["id"] not in asked_question_ids:

            if question["difficulty"] not in available_difficulties:

                available_difficulties.append(
                    question["difficulty"]
                )


    # --------------------------------
    # 2. PREVIOUSLY WRONG QUESTIONS
    # --------------------------------

    for question in questions:

        if question["id"] not in asked_question_ids:
            continue

        for record in reversed(student["history"]):

            if (
                record.get("question_id") == question["id"]
                and record["correct"] == False
            ):

                if question["difficulty"] not in available_difficulties:

                    available_difficulties.append(
                        question["difficulty"]
                    )

                break


    return available_difficulties

def generate_recommendation(student):

    decision = decide_next_action(student)

    if decision is None:

        return {
            "topic": None,
            "action_type": "none",
            "recommendation": (
                "No recommendation available."
            )
        }


    topic = decision["topic"]

    if topic is None:

        return {
            "topic": None,
            "action_type": "none",
            "recommendation": (
                "Continue normal learning progression."
            )
        }


    mastery = student["knowledge"].get(
        topic,
        0
    )

    recent_accuracy = calculate_recent_accuracy(
        student,
        topic
    )

    trend = calculate_trend(
        student,
        topic
    )

    days_unused = get_days_unused(
        student,
        topic
    )

    weakest_prerequisite = find_weakest_prerequisite(
        student,
        topic
    )


    # --------------------------------
    # HIGH RISK
    # --------------------------------

    if decision["risk_level"] == "High":

        if (
            weakest_prerequisite is not None
            and weakest_prerequisite["mastery"] < 0.60
        ):

            prerequisite = (
                weakest_prerequisite["topic"]
            )

            return {
                "topic": topic,
                "action_type": "prerequisite_revision",
                "recommendation": (
                    f"Revise {prerequisite} before "
                    f"continuing with {topic}. "
                    f"Your prerequisite knowledge is weak."
                )
            }


        if (
            mastery < 0.50
            and recent_accuracy < 0.50
        ):

            available_difficulties = (
                get_available_difficulties(
                    student,
                    topic
                )
            )


            if "easy" in available_difficulties:

                return {
                    "topic": topic,
                    "action_type": "foundation_practice",
                    "recommended_difficulty": "easy",
                    "recommendation": (
                        f"{topic} is currently high risk. "
                        f"Start with easy questions to rebuild "
                        f"your understanding before moving "
                        f"to harder questions."
                    )
                }


            elif "medium" in available_difficulties:

                return {
                    "topic": topic,
                    "action_type": "foundation_practice",
                    "recommended_difficulty": "medium",
                    "recommendation": (
                        f"{topic} is currently high risk. "
                        f"Easy questions have been exhausted, "
                        f"so continue with medium questions "
                        f"to rebuild your understanding."
                    )
                }


            elif "hard" in available_difficulties:

                return {
                    "topic": topic,
                    "action_type": "targeted_practice",
                    "recommended_difficulty": "hard",
                    "recommendation": (
                        f"{topic} is currently high risk, "
                        f"but easier questions are exhausted. "
                        f"Continue with the available hard "
                        f"question for targeted practice."
                    )
                }


        if trend == "Declining":

            available_difficulties = (
                get_available_difficulties(
                    student,
                    topic
                )
            )

            if "easy" in available_difficulties:

                return {
                    "topic": topic,
                    "action_type": "targeted_practice",
                    "recommended_difficulty": "easy",
                    "recommendation": (
                        f"Practice {topic} with easy questions "
                        f"because your recent performance is declining."
                    )
                }

            elif "medium" in available_difficulties:

                return {
                    "topic": topic,
                    "action_type": "targeted_practice",
                    "recommended_difficulty": "medium",
                    "recommendation": (
                        f"Practice {topic} with medium questions "
                        f"because your recent performance is declining."
                    )
                }

            else:

                return {
                    "topic": topic,
                    "action_type": "targeted_practice",
                    "recommended_difficulty": "hard",
                    "recommendation": (
                        f"Practice {topic} because your recent "
                        f"performance is declining."
                    )
                }



    # --------------------------------
    # MEDIUM RISK
    # --------------------------------

    if decision["risk_level"] == "Medium":

        if (
            weakest_prerequisite is not None
            and weakest_prerequisite["mastery"] < 0.60
        ):

            prerequisite = (
                weakest_prerequisite["topic"]
            )

            return {
                "topic": topic,
                "action_type": "prerequisite_revision",
                "recommendation": (
                    f"Revise {prerequisite} before "
                    f"continuing with {topic}. "
                    f"Your prerequisite knowledge is weak."
                )
            }


        if trend == "Declining":

            return {
                "topic": topic,
                "action_type": "targeted_practice",
                "recommendation": (
                    f"Practice {topic} because "
                    f"your performance is declining."
                )
            }


        if recent_accuracy < 0.60:

            return {
                "topic": topic,
                "action_type": "targeted_practice",
                "recommendation": (
                    f"Practice {topic} to improve "
                    f"your recent accuracy."
                )
            }


        if days_unused >= 14:

            return {
                "topic": topic,
                "action_type": "revision",
                "recommendation": (
                    f"Revise {topic} because it "
                    f"has not been practiced recently."
                )
            }


        return {
            "topic": topic,
            "action_type": "practice",
            "recommendation": (
                f"Practice {topic} to strengthen "
                f"your current understanding."
            )
        }

    # --------------------------------
    # UNKNOWN
    # --------------------------------

    if decision["risk_level"] == "Unknown":

        return {
            "topic": topic,
            "action_type": "assessment",
            "recommendation": (
                f"Assess your current knowledge "
                f"of {topic} with a few questions."
            )
        }


    # --------------------------------
    # LOW RISK
    # --------------------------------

    if mastery >= 0.90:

        return {
            "topic": topic,
            "action_type": "progression",
            "recommendation": (
                f"{topic} is strong. "
                f"Continue toward more advanced topics."
            )
        }


    return {
        "topic": topic,
        "action_type": "maintenance",
        "recommendation": (
            f"Continue practicing {topic} "
            f"to maintain your current mastery."
        )
    }

def show_recommendation(student):

    recommendation = generate_recommendation(
        student
    )

    print(
        "\n===== ADAPTIVE RECOMMENDATION ====="
    )

    print(
        "Topic:",
        recommendation["topic"]
    )

    print(
        "Action:",
        recommendation["action_type"]
    )

    print(
        "Recommendation:"
    )

    print(
        recommendation["recommendation"]
    )

    return recommendation