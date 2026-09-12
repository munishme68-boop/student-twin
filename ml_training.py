import json

from progress import (
    calculate_recent_accuracy
)


# --------------------------------
# LOAD STUDENT DATA
# --------------------------------

def load_student(
    file_path="student_data.json"
):

    with open(
        file_path,
        "r"
    ) as file:

        student = json.load(file)

    return student

# --------------------------------
# COUNT TOPIC ATTEMPTS
# --------------------------------

def count_topic_attempts(
    student,
    topic
):

    count = 0

    for record in student["history"]:

        if record["topic"] == topic:

            count += 1

    return count


# --------------------------------
# COUNT RECENT MISTAKES
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

    recent_records = topic_records[
        -recent_count:
    ]

    mistakes = 0

    for record in recent_records:

        if record["correct"] == False:

            mistakes += 1

    return mistakes


# --------------------------------
# BUILD TRAINING DATA
# --------------------------------

def build_training_data(
    student
):

    from bkt import update_mastery
    from datetime import datetime
    from progress import calculate_trend

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

    X = []
    y = []

    mastery_state = {}
    topic_history = {}

    for record in student["history"]:

        topic = record["topic"]

        # --------------------------------
        # PREVIOUS MASTERY
        # --------------------------------

        previous_mastery = mastery_state.get(
            topic,
            0
        )

        # --------------------------------
        # PREVIOUS HISTORY
        # --------------------------------

        previous_records = topic_history.get(
            topic,
            []
        )

        previous_attempts = len(
            previous_records
        )

        # --------------------------------
        # RECENT ACCURACY
        # --------------------------------

        recent_records = previous_records[-3:]

        if len(recent_records) == 0:

            recent_accuracy = 0

        else:

            correct_count = 0

            for previous_record in recent_records:

                if previous_record["correct"]:

                    correct_count += 1

            recent_accuracy = (
                correct_count /
                len(recent_records)
            )

        # --------------------------------
        # RECENT MISTAKES
        # --------------------------------

        recent_mistakes = 0

        for previous_record in recent_records:

            if previous_record["correct"] == False:

                recent_mistakes += 1

        # --------------------------------
        # DIFFICULTY
        # --------------------------------

        difficulty_map = {
            "easy": 1,
            "medium": 2,
            "hard": 3
        }

        difficulty = difficulty_map.get(
            record.get(
                "difficulty",
                "medium"
            ),
            2
        )

        # --------------------------------
        # HISTORICAL DAYS UNUSED
        # --------------------------------

        if len(previous_records) == 0:

            days_unused = 0

        else:

            previous_timestamp = previous_records[-1].get(
                "timestamp"
            )

            current_timestamp = record.get(
                "timestamp"
            )

            if (
                previous_timestamp is not None
                and current_timestamp is not None
            ):

                previous_time = datetime.fromisoformat(
                    previous_timestamp
                )

                current_time = datetime.fromisoformat(
                    current_timestamp
                )

                time_difference = (
                    current_time -
                    previous_time
                )

                days_unused = (
                    time_difference.total_seconds()
                    / 86400
                )

            else:

                days_unused = 0

        # --------------------------------
        # CREATE FEATURES
        # --------------------------------

        

        topic_value = topic_map.get(
            topic,
            0
        )

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

        features = [
            previous_mastery,
            recent_accuracy,
            recent_mistakes,
            previous_attempts,
            difficulty,
            days_unused,
            topic_value,
            trend_value
        ]

        X.append(
            features
        )

        # --------------------------------
        # TARGET
        # --------------------------------

        if record["correct"] == False:

            target = 1

        else:

            target = 0

        y.append(
            target
        )

        # --------------------------------
        # UPDATE MASTERY
        # --------------------------------

        mastery_state[topic] = update_mastery(
            previous_mastery,
            record["correct"],
            record.get(
                "difficulty",
                "medium"
            )
        )

        # --------------------------------
        # UPDATE TOPIC HISTORY
        # --------------------------------

        if topic not in topic_history:

            topic_history[topic] = []

        topic_history[topic].append(
            record
        )

    return X, y


# --------------------------------
# MAIN
# --------------------------------

def main():

    student = load_student()

    X, y = build_training_data(
        student
    )

    print(
        "\n===== ML TRAINING DATA ====="
    )

    print(
        "Number of samples:",
        len(X)
    )

    print(
        "Number of features:",
        len(X[0])
        if len(X) > 0
        else 0
    )

    print(
        "\nFeatures:"
    )

    print(
        "[previous_mastery, "
        "recent_accuracy, "
        "recent_mistakes, "
        "previous_attempts, "
        "difficulty]"
    )

    print(
        "\nFirst 10 feature rows:"
    )

    for row in X[:10]:

        print(row)

    print(
        "\nFirst 10 targets:"
    )

    print(
        y[:10]
    )


if __name__ == "__main__":

    main()