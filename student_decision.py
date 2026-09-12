import json

from student_prediction import (
    predict_all_topic_risks
)

from goal_recommendation import (
    get_next_goal_topic
)

from knowledge_decay import (
    get_days_unused
)

from combined_risk import (
    calculate_all_combined_risks
)

# --------------------------------
# DECIDE NEXT ACTION
# --------------------------------


def decide_next_action(student):

    predictions = calculate_all_combined_risks(
    student
    )
     

    if not predictions:
        return None

    next_goal_topic = get_next_goal_topic(
    student
    )

    decay_priority = {}

    for topic in student["knowledge"]:

        days_unused = get_days_unused(
            student,
            topic
        )

        if days_unused >= 14:

            decay_priority[topic] = days_unused

    avoided_topics = []

    for topic in student["knowledge"]:

        mastery = student["knowledge"][topic]

        if mastery < 0.60:

            topic_attempts = 0

            for record in student["history"]:

                if record["topic"] == topic:

                    topic_attempts += 1

            if topic_attempts >= 3:

                days_unused = get_days_unused(
                    student,
                    topic
                )

                if days_unused >= 7:

                    avoided_topics.append(topic)        

    unassessed_topics = []

    for prediction in predictions:

        if prediction["risk_level"] == "Unknown":

            unassessed_topics.append(
                prediction["topic"]
            )                


    # --------------------------------
    # HIGH RISK TOPICS
    # --------------------------------

    high_risk_topics = []

    for prediction in predictions:

        if prediction["risk_level"] == "High":

            high_risk_topics.append(
                prediction
            )

    if high_risk_topics:

        top_prediction = high_risk_topics[0]

        topic = top_prediction["topic"]
        risk_score = top_prediction["combined_score"]
        ml_probability = top_prediction["ml_probability"]
        risk_level = top_prediction["risk_level"]
        reasons = top_prediction["reasons"]

        recent_mistakes = top_prediction.get(
            "recent_mistakes",
            0
        )

        sudden_drop = top_prediction.get(
            "sudden_drop",
            False
        )


        # Check for weak prerequisite

        weak_prerequisite = None

        for reason in reasons:

            if reason.startswith(
                "Weak prerequisite:"
            ):

                weak_prerequisite = reason.replace(
                    "Weak prerequisite:",
                    ""
                ).strip()

                break


        if weak_prerequisite:

            action = (
                "Repair the prerequisite "
                + weak_prerequisite
                + " before practicing "
                + topic
                + "."
            )

        elif sudden_drop:

            action = (
                "Immediately revise "
                + topic
                + " because a sudden performance drop was detected."
            )

        elif recent_mistakes >= 2:

            action = (
                "Perform targeted practice on "
                + topic
                + " because repeated mistakes were detected."
            )

        else:

            action = (
                "Practice "
                + topic
                + " immediately before moving to advanced topics."
            )


        return {
            "topic": topic,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "ml_probability": ml_probability,
            "reasons": reasons,
            "action": action
       }


    # --------------------------------
    # MEDIUM RISK TOPICS
    # --------------------------------

    medium_risk_topics = []

    for prediction in predictions:

        if prediction["risk_level"] == "Medium":

            medium_risk_topics.append(
                prediction
            )

    if medium_risk_topics:

        top_prediction = medium_risk_topics[0]

        topic = top_prediction["topic"]
        risk_score = top_prediction["combined_score"]
        ml_probability = top_prediction["ml_probability"]
        risk_level = top_prediction["risk_level"]
        reasons = top_prediction["reasons"]

        recent_mistakes = top_prediction.get(
            "recent_mistakes",
            0
        )

        sudden_drop = top_prediction.get(
            "sudden_drop",
            False
        )


        # Check for weak prerequisite

        weak_prerequisite = None

        for reason in reasons:

            if reason.startswith(
                "Weak prerequisite:"
            ):

                weak_prerequisite = reason.replace(
                    "Weak prerequisite:",
                    ""
                ).strip()

                break


        if topic == next_goal_topic:

            action = (
                "Prioritize "
                + topic
                + " because it is the next topic required for your goal."
            )

        elif topic in decay_priority:

            action = (
                "Revise "
                + topic
                + " because it has not been practiced for "
                + f"{decay_priority[topic]:.1f} days."
            )

        elif topic in avoided_topics:

            action = (
                "Return to "
                + topic
                + " because it appears to be a weak topic "
                + "that has not been practiced recently."
            )

        elif topic in unassessed_topics:

            action = (
                "Assess "
                + topic
                + " to determine your current knowledge level "
                + "before continuing to advanced topics."
            )

        elif weak_prerequisite:

            action = (
                "Strengthen the prerequisite "
                + weak_prerequisite
                + " before continuing with "
                + topic
                + "."
            )

        elif sudden_drop:

            action = (
                "Revise "
                + topic
                + " immediately because a sudden performance drop was detected."
            )

        elif recent_mistakes >= 2:

            action = (
                "Perform targeted practice on "
                + topic
                + " because repeated mistakes were detected."
            )

        elif "Performance is declining" in reasons:

            action = (
                "Revise "
                + topic
                + " and practice it again soon because performance is declining."
            )

        elif "Recent accuracy below 70%" in reasons:

            action = (
                "Practice "
                + topic
                + " with additional questions to improve recent accuracy."
            )

        elif "Very low recent accuracy" in reasons:

            action = (
                "Practice "
                + topic
                + " immediately because recent performance is very weak."
            )

        else:

            action = (
                "Revise "
                + topic
                + " and monitor performance."
            )


        return {
            "topic": topic,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "ml_probability": ml_probability,
            "reasons": reasons,
            "action": action
       }


    # --------------------------------
# UNASSESSED TOPICS
# --------------------------------


    unknown_topics = []

    for prediction in predictions:

        if prediction["risk_level"] == "Unknown":

            unknown_topics.append(
                prediction
            )

    if unknown_topics:

        top_prediction = unknown_topics[0]

        topic = top_prediction["topic"]
        risk_score = 0
        risk_level = top_prediction["risk_level"]
        ml_probability = None
        reasons = top_prediction["reasons"]

        action = (
           "Assess "
            + topic
            + " to determine your current knowledge level."
        )

        return {
            "topic": topic,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "ml_probability": ml_probability,
            "reasons": reasons,
            "action": action
        }


# --------------------------------
# NO SIGNIFICANT RISK
# --------------------------------

    return {
        "topic": None,
        "risk_score": 0,
        "risk_level": "Low",
        "ml_probability": None,
        "reasons": [],
        "action": (
            "Continue normal learning progression."
        )
}

# --------------------------------
# DISPLAY DECISION
# --------------------------------

def show_next_action(student):

    decision = decide_next_action(
        student
    )


    print(
        "\n===== STUDENT TWIN DECISION ====="
    )


    if decision is None:

        print(
            "No decision available."
        )

        return None


    print(
        "\nPriority topic:",
        decision["topic"]
    )


    print(
        "Risk score:",
        decision["risk_score"]
    )


    print(
        "Risk level:",
        decision["risk_level"]
    )
    if decision["ml_probability"] is not None:

        print(
            "ML mistake probability:",
            f"{decision['ml_probability'] * 100:.2f}%"
        )

    else:

        print(
            "ML mistake probability:",
            "Not available"
        )

    print(
        "\nWhy:"
    )


    for reason in decision["reasons"]:

        print(
            "-",
            reason
        )


    print(
        "\nRecommended action:"
    )


    print(
        decision["action"]
    )


    return decision


# --------------------------------
# TEST
# --------------------------------

if __name__ == "__main__":

    with open(
        "student_data.json",
        "r"
    ) as file:

        student = json.load(file)


    show_next_action(student)