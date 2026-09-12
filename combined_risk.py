import joblib

from student_prediction import (
    predict_topic_risk
)

from student_ml_model import (
    predict_mistake_probability
)



# --------------------------------
# COMBINE RULE + ML RISK
# --------------------------------

def calculate_combined_risk(
    student,
    topic,
    difficulty="medium"
):

    # --------------------------------
    # RULE-BASED RISK
    # --------------------------------

    rule_prediction = predict_topic_risk(
        student,
        topic
    )

    rule_score = rule_prediction[
        "risk_score"
    ]

    # --------------------------------
    # COUNT TOPIC ATTEMPTS
    # --------------------------------

    topic_attempts = 0

    for record in student["history"]:

        if record["topic"] == topic:

            topic_attempts += 1

    # --------------------------------
# NOT ENOUGH ML DATA
# --------------------------------

    if topic_attempts < 3:

        if topic not in student["knowledge"]:

            return {
                "topic": topic,
                "rule_score": rule_score,
                "ml_probability": None,
                "combined_score": rule_score,
                "risk_level": "Unknown",
                "reasons": (
                    rule_prediction["reasons"]
                    + [
                        "No mastery estimate available",
                        "Insufficient ML evidence",
                        f"Only {topic_attempts} attempt(s)"
                    ]
                )
            }

    # Mastery exists, but there is not enough
    # history for a reliable ML prediction.

        if rule_score >= 60:
            risk_level = "High"

        elif rule_score >= 30:
            risk_level = "Medium"

        else:
            risk_level = "Low"

        return {
            "topic": topic,
            "rule_score": rule_score,
            "ml_probability": None,
            "combined_score": rule_score,
            "risk_level": risk_level,
            "reasons": (
                rule_prediction["reasons"]
                + [
                    "Insufficient ML evidence",
                    f"Only {topic_attempts} attempt(s)"
                ]
            )
        }

    # --------------------------------
    # LOAD SAVED ML MODEL
    # --------------------------------

    try:

        model = joblib.load(
            "student_ml_model.pkl"
        )

    except FileNotFoundError:

        return {
            "topic": topic,
            "rule_score": rule_score,
            "ml_probability": None,
            "combined_score": rule_score,
            "risk_level": rule_prediction[
                "risk_level"
            ],
            "reasons": rule_prediction[
                "reasons"
            ]
        }

    # --------------------------------
    # ML PREDICTION
    # --------------------------------

    ml_probability = predict_mistake_probability(
        model,
        student,
        topic,
        difficulty
    )

    ml_score = ml_probability * 100

    # --------------------------------
    # COMBINE SCORES
    # --------------------------------

    combined_score = (
        rule_score * 0.70
        + ml_score * 0.30
    )

    # --------------------------------
    # DETERMINE RISK LEVEL
    # --------------------------------

    if combined_score >= 60:

        risk_level = "High"

    elif combined_score >= 30:

        risk_level = "Medium"

    else:

        risk_level = "Low"

    # --------------------------------
    # RETURN RESULT
    # --------------------------------

    return {
        "topic": topic,
        "rule_score": rule_score,
        "ml_probability": ml_probability,
        "combined_score": combined_score,
        "risk_level": risk_level,
        "reasons": rule_prediction[
            "reasons"
        ]
    }

def calculate_all_combined_risks(
    student
):

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

    # --------------------------------
    # LOAD SAVED ML MODEL
    # --------------------------------

    try:

        model = joblib.load(
            "student_ml_model.pkl"
        )

    except FileNotFoundError:

        print(
            "ML model not found."
        )

        return []

    predictions = []

    for topic in all_topics:

        result = calculate_combined_risk(
            student,
            topic,
            "medium"
        )

        predictions.append(
            result
        )

    # --------------------------------
    # RISK PRIORITY ORDER
    # --------------------------------

    risk_priority = {
        "High": 3,
        "Medium": 2,
        "Unknown": 1,
        "Low": 0
    }

    predictions.sort(
        key=lambda x: (
            risk_priority[
                x["risk_level"]
            ],
            x["combined_score"]
        ),
        reverse=True
    )

    return predictions


# --------------------------------
# TEST
# --------------------------------

if __name__ == "__main__":

    import json

    with open(
        "student_data.json",
        "r"
    ) as file:

        student = json.load(file)

    predictions = calculate_all_combined_risks(
        student
    )

    print(
        "\n===== ALL COMBINED STUDENT RISKS ====="
    )

    for prediction in predictions:

        print(
            prediction["topic"],
            "->",
            f"{prediction['combined_score']:.2f}",
            "|",
            prediction["risk_level"]
        )