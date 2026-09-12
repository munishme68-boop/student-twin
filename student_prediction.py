import json

from progress import (
    calculate_recent_accuracy,
    calculate_trend
)

from knowledge_graph import (
    find_weak_prerequisites
)
from knowledge_decay import get_days_unused

from question_bank import get_questions


# --------------------------------
# PREDICT TOPIC RISK
# --------------------------------


def predict_topic_risk(student, topic):

    mastery = student["knowledge"].get(
        topic,
        0
    )

# --------------------------------
# EVIDENCE COUNT
# --------------------------------

    topic_attempts = 0

    for record in student["history"]:

        if record["topic"] == topic:

            topic_attempts += 1



    recent_accuracy = calculate_recent_accuracy(
        student,
        topic
    )

    recent_mistakes = count_recent_mistakes(
    student,
    topic
    )

    sudden_drop = detect_sudden_drop(
    student,
    topic
    )

    trend = calculate_trend(
        student,
        topic
    )

    weak_prerequisites = find_weak_prerequisites(
        student,
        topic
    )

    # --------------------------------
    # KNOWLEDGE DECAY
    # --------------------------------

    days_unused = get_days_unused(
        student,
        topic
    )

    risk_score = 0
    reasons = []


    # --------------------------------
    # MASTERY
    # --------------------------------

    if mastery < 0.40:

        risk_score += 40

        reasons.append(
            "Very low mastery"
        )

    elif mastery < 0.60:

        risk_score += 30

        reasons.append(
            "Low mastery"
        )

    elif mastery < 0.75:

        risk_score += 15

        reasons.append(
            "Moderate mastery"
        )

    
     # -------------------------------- # EVIDENCE CONFIDENCE # --------------------------------

    if topic_attempts < 3:

        reasons.append(
            "Limited practice data"
    )

    elif topic_attempts < 5:

        reasons.append(
            "Moderate amount of practice data"
    )

    # RECENT MISTAKE INFORMATION

    if recent_mistakes > 0:

        reasons.append(
            f"Recent mistakes: {recent_mistakes}"
        )


    # --------------------------------
# RECENT ACCURACY
# --------------------------------

    if topic_attempts > 0 and recent_accuracy < 0.50:

        risk_score += 30

        reasons.append(
            "Very low recent accuracy"
        )

    elif topic_attempts > 0 and recent_accuracy < 0.70:

        risk_score += 20

        reasons.append(
            "Recent accuracy below 70%"
        )


    # --------------------------------
    # PERFORMANCE TREND
    # --------------------------------

    if trend == "Declining":

        risk_score += 20

        reasons.append(
            "Performance is declining"
        )

    elif trend == "Improving":

        risk_score -= 10

        reasons.append(
            "Performance is improving"
        )
    # SUDDEN PERFORMANCE DROP

    if sudden_drop:

        risk_score += 20

        reasons.append(
            "Sudden performance drop detected"
    )    

    if recent_mistakes >= 3:

        risk_score += 20

        reasons.append(
            "Three recent mistakes detected"
        )

    elif recent_mistakes == 2:

        risk_score += 10

        reasons.append(
            "Two recent mistakes detected"
        )    
    
   
# --------------------------------
# KNOWLEDGE STABILITY GAP
# --------------------------------

    if topic_attempts >= 3:

        stability_gap = mastery - recent_accuracy

        if stability_gap >= 0.50:

            risk_score += 20

            reasons.append(
                "Large gap between mastery and recent performance"
            )

        elif stability_gap >= 0.30:

            risk_score += 15

            reasons.append(
                "Moderate gap between mastery and recent performance"
            )

        elif stability_gap >= 0.15:

            risk_score += 10

            reasons.append(
                "Small gap between mastery and recent performance"
            )





    # --------------------------------
    # KNOWLEDGE DECAY
    # --------------------------------

    if days_unused >= 30:

        risk_score += 20

        reasons.append(
            "Not practiced for 30+ days"
        )

    elif days_unused >= 14:

        risk_score += 10

        reasons.append(
            "Not practiced for 14+ days"
        )

    elif days_unused >= 7:

        risk_score += 5

        reasons.append(
            "Not practiced for 7+ days"
        )


    # --------------------------------
    # PREREQUISITES
    # --------------------------------

    if weak_prerequisites:

        risk_score += 10

        prerequisite_names = []

        for prerequisite in weak_prerequisites:

            prerequisite_names.append(
                prerequisite["topic"]
            )

        reasons.append(
            "Weak prerequisite: "
            + ", ".join(prerequisite_names)
        )

        
    # --------------------------------
    # EVIDENCE-BASED RISK ADJUSTMENT
    # --------------------------------

    if topic_attempts < 3:

        risk_score = risk_score * 0.50

    elif topic_attempts < 5:

        risk_score = risk_score * 0.75


    risk_score = round(
        risk_score
    )




    # --------------------------------
    # RISK LEVEL
    # --------------------------------

    if risk_score >= 50:

        risk_level = "High"

    elif risk_score >= 25:

        risk_level = "Medium"

    else:

        risk_level = "Low"


    return {
    "topic": topic,
    "risk_score": risk_score,
    "risk_level": risk_level,
    "reasons": reasons,
    "recent_mistakes": recent_mistakes,
    "sudden_drop": sudden_drop
    }


# --------------------------------
# PREDICT ALL TOPIC RISKS
# --------------------------------

def count_recent_mistakes(
    student,
    topic,
    recent_count=3
):

    topic_records = []

    for record in student["history"]:

        if record["topic"] == topic:

            topic_records.append(
                record
            )

    if len(topic_records) == 0:
        return 0

    recent_records = topic_records[-recent_count:]

    mistakes = 0

    for record in recent_records:

        if record["correct"] == False:

            mistakes += 1

    return mistakes

def detect_sudden_drop(
    student,
    topic
):

    topic_records = []

    for record in student["history"]:

        if record["topic"] == topic:

            topic_records.append(
                record
            )

    # Need enough data to compare
    # earlier performance with recent performance

    if len(topic_records) < 4:

        return False

    midpoint = len(topic_records) // 2

    earlier_records = topic_records[:midpoint]
    recent_records = topic_records[midpoint:]

    earlier_correct = 0

    for record in earlier_records:

        if record["correct"]:

            earlier_correct += 1

    recent_correct = 0

    for record in recent_records:

        if record["correct"]:

            recent_correct += 1

    earlier_accuracy = (
        earlier_correct / len(earlier_records)
    )

    recent_accuracy = (
        recent_correct / len(recent_records)
    )

    performance_drop = (
        earlier_accuracy - recent_accuracy
    )

    if performance_drop >= 0.30:

        return True

    return False 

def predict_all_topic_risks(student):

    # --------------------------------
    # ALL AVAILABLE TOPICS
    # --------------------------------

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


    predictions = []


    # --------------------------------
    # PREDICT ASSESSED TOPICS
    # --------------------------------

    for topic in all_topics:

        if topic in student["knowledge"]:

            prediction = predict_topic_risk(
                student,
                topic
            )

            predictions.append(
                prediction
            )


    # --------------------------------
    # DETECT UNASSESSED TOPICS
    # --------------------------------

    for topic in all_topics:

        if topic not in student["knowledge"]:

            predictions.append({
                "topic": topic,
                "risk_score": 0,
                "risk_level": "Unknown",
                "reasons": [
                    "Topic has not been assessed yet"
                ]
            })


    # --------------------------------
    # SORT PREDICTIONS
    # --------------------------------

    predictions.sort(
        key=lambda x: x["risk_score"],
        reverse=True
    )


    return predictions

# --------------------------------
# TEST PREDICTION
# --------------------------------

if __name__ == "__main__":

    with open(
        "student_data.json",
        "r"
    ) as file:

        student = json.load(file)


    predictions = predict_all_topic_risks(
        student
    )


    print("\n===== STUDENT RISK PREDICTION =====")


    for prediction in predictions:

        print(
            f"\nTopic: {prediction['topic']}"
        )

        print(
            "Risk Score:",
            prediction["risk_score"]
        )

        print(
            "Risk Level:",
            prediction["risk_level"]
        )


        if prediction["reasons"]:

            print("Reasons:")

            for reason in prediction["reasons"]:

                print(
                    "-",
                    reason
                )