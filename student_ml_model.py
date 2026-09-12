from ml_training import (
    load_student,
    build_training_data
)

from sklearn.model_selection import (
    train_test_split
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

from sklearn.model_selection import cross_val_score

from knowledge_decay import get_days_unused

import joblib

# --------------------------------
# TRAIN MODEL
# --------------------------------

def train_model():

    student = load_student(
        "student_data_before_full_test.json"
    )

    X, y = build_training_data(
        student
    )

        # --------------------------------
    # TRAINING DATA DIAGNOSTICS
    # --------------------------------

    total_samples = len(y)

    correct_samples = 0
    mistake_samples = 0

    for target in y:

        if target == 1:

            mistake_samples += 1

        else:

            correct_samples += 1

    print(
        "\n===== TRAINING DATA DIAGNOSTICS ====="
    )

    print(
        "Total samples:",
        total_samples
    )

    print(
        "Correct answers:",
        correct_samples
    )

    print(
        "Mistakes:",
        mistake_samples
    )

    print(
    "Correct-to-mistake ratio:",
    f"{correct_samples}:{mistake_samples}"
    )

    if mistake_samples > 0:

        print(
            "Mistake class proportion:",
            f"{mistake_samples / total_samples * 100:.2f}%"
        )

    if total_samples > 0:

        mistake_percentage = (
            mistake_samples /
            total_samples
        ) * 100

        print(
            "Mistake percentage:",
            f"{mistake_percentage:.2f}%"
        )

    print(
        "\nFeatures used:"
    )

    print("1. Previous mastery")
    print("2. Recent accuracy")
    print("3. Recent mistakes")
    print("4. Previous attempts")
    print("5. Difficulty")
    print("6. Days unused")
    print("7. Topic")
    print("8. Performance trend")

    if len(X) < 10:

        print(
            "Not enough training data."
        )

        return None

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )
    )

    model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
    )
    

    model.fit(
        X_train,
        y_train
    )

    cv_scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="accuracy"
    )

    print(
    "\n===== CROSS-VALIDATION RESULTS ====="
    )

    for i, score in enumerate(
        cv_scores,
        start=1
    ):

        print(
            f"Fold {i}:",
            f"{score * 100:.2f}%"
        )

    print(
        "Mean:",
        f"{cv_scores.mean() * 100:.2f}%"
    )

    print(
        "Standard deviation:",
        f"{cv_scores.std() * 100:.2f}%"
    )

    joblib.dump(
        model,
        "student_ml_model.pkl"
    )

    predictions = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        "\n===== STUDENT ML MODEL ====="
    )

    print(
        "Training samples:",
        len(X_train)
    )

    print(
        "Testing samples:",
        len(X_test)
    )

    print(
        "Model accuracy:",
        f"{accuracy * 100:.2f}%"
    )

    print(
        "\nClassification Report:"
    )

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    return model

def predict_mistake_probability(
    model,
    student,
    topic,
    difficulty="medium"
):

    from progress import (
        calculate_recent_accuracy
    )

    # --------------------------------
    # PREVIOUS MASTERY
    # --------------------------------

    previous_mastery = student[
        "knowledge"
    ].get(
        topic,
        0
    )

    # --------------------------------
    # RECENT ACCURACY
    # --------------------------------

    recent_accuracy = calculate_recent_accuracy(
        student,
        topic
    )

    # --------------------------------
    # RECENT MISTAKES
    # --------------------------------

    topic_records = []

    for record in student["history"]:

        if record["topic"] == topic:

            topic_records.append(
                record
            )

    recent_records = topic_records[-3:]

    recent_mistakes = 0

    for record in recent_records:

        if record["correct"] == False:

            recent_mistakes += 1

    # --------------------------------
    # PREVIOUS ATTEMPTS
    # --------------------------------

    previous_attempts = len(
        topic_records
    )

    # --------------------------------
    # DIFFICULTY
    # --------------------------------

    difficulty_map = {
        "easy": 1,
        "medium": 2,
        "hard": 3
    }

    difficulty_value = difficulty_map.get(
        difficulty,
        2
    )

    # --------------------------------
    # CREATE FEATURE VECTOR
    # --------------------------------

    days_unused = get_days_unused(
        student,
        topic
    )

    topic_map = {
        "python": 1,
        "machine_learning": 2,
        "neural_networks": 3,
        "convolution": 4,
        "cnn": 5,
        "probability": 6,
        "statistics": 7,
        "rnn": 8,
        "lstm": 9,
        "natural_language_processing": 10,
        "transformers": 11,
        "image_classification": 12,
        "object_detection": 13,
        "word_embeddings": 14,
        "generative_ai": 15,
        "large_language_models": 16,
        "model_deployment": 17,
        "mlops": 18
    }

    topic_value = topic_map.get(
        topic,
        0
    )

    from progress import calculate_trend

    trend = calculate_trend(
        student,
        topic
    )

    trend_map = {
        "Improving": 1,
        "Stable": 0,
        "Declining": -1,
        "Not enough data": 0
    }

    trend_value = trend_map.get(
        trend,
        0
    )

    features = [[
        previous_mastery,
        recent_accuracy,
        recent_mistakes,
        previous_attempts,
        difficulty_value,
        days_unused,
        topic_value,
        trend_value
    ]]

    # --------------------------------
    # PREDICT PROBABILITY
    # --------------------------------

    probabilities = model.predict_proba(
        features
    )

    mistake_probability = probabilities[
        0
    ][1]

    return mistake_probability

def predict_all_ml_risks(
    model,
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

    predictions = []

    for topic in all_topics:

        # --------------------------------
        # COUNT ATTEMPTS
        # --------------------------------

        topic_attempts = 0

        for record in student["history"]:

            if record["topic"] == topic:

                topic_attempts += 1

        # --------------------------------
        # NOT ENOUGH DATA
        # --------------------------------

        if topic_attempts < 3:

            predictions.append({
                "topic": topic,
                "mistake_probability": None,
                "confidence": "Low",
                "attempts": topic_attempts
            })

            continue

        # --------------------------------
        # ML PREDICTION
        # --------------------------------

        probability = predict_mistake_probability(
            model,
            student,
            topic,
            "medium"
        )

        predictions.append({
            "topic": topic,
            "mistake_probability": probability,
            "confidence": "High",
            "attempts": topic_attempts
        })

    # --------------------------------
    # SORT
    # --------------------------------

    predictions.sort(
        key=lambda x: (
            x["mistake_probability"]
            if x["mistake_probability"] is not None
            else -1
        ),
        reverse=True
    )

    return predictions


# --------------------------------
# MAIN
# --------------------------------

if __name__ == "__main__":

    student = load_student()

    model = train_model()

    if model is not None:

        predictions = predict_all_ml_risks(
            model,
            student
        )

        print(
            "\n===== ML RISK PREDICTIONS ====="
        )

        for prediction in predictions:

            if prediction["mistake_probability"] is None:

                print(
                    prediction["topic"],
                    "->",
                    "Unknown",
                    f"(Attempts: {prediction['attempts']},",
                    f"Confidence: {prediction['confidence']})"
            )

            else:

                print(
                    prediction["topic"],
                    "->",
                    f"{prediction['mistake_probability'] * 100:.2f}%",
                    f"(Attempts: {prediction['attempts']},",
                    f"Confidence: {prediction['confidence']})"
            )