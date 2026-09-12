
# --------------------------------
# GET TOPIC PROGRESS
# --------------------------------

def get_topic_progress(student, topic):

    progress = []

    for record in student["history"]:

        if record["topic"] == topic:

            progress.append({
                "correct": record["correct"],
                "difficulty": record.get("difficulty", "unknown")
            })

    return progress


# --------------------------------
# CALCULATE TOPIC ACCURACY
# --------------------------------

def calculate_accuracy(student, topic):

    progress = get_topic_progress(student, topic)

    if len(progress) == 0:
        return 0

    correct_answers = 0

    for record in progress:

        if record["correct"]:
            correct_answers += 1

    accuracy = correct_answers / len(progress)

    return accuracy


# --------------------------------
# CALCULATE LEARNING TREND
# --------------------------------

def calculate_trend(student, topic):

    progress = get_topic_progress(
        student,
        topic
    )

    # Need enough data to calculate a trend
    if len(progress) < 4:
        return "Not enough data"

    midpoint = len(progress) // 2

    earlier_progress = progress[:midpoint]
    recent_progress = progress[midpoint:]

    earlier_correct = 0

    for record in earlier_progress:
        if record["correct"]:
            earlier_correct += 1

    recent_correct = 0

    for record in recent_progress:
        if record["correct"]:
            recent_correct += 1

    earlier_accuracy = (
        earlier_correct / len(earlier_progress)
    )

    recent_accuracy = (
        recent_correct / len(recent_progress)
    )

    difference = (
        recent_accuracy - earlier_accuracy
    )

    # Significant improvement
    if difference >= 0.20:
        return "Improving"

    # Significant decline
    elif difference <= -0.20:
        return "Declining"

    # Small difference
    else:
        return "Stable"

# --------------------------------
# CALCULATE OVERALL MASTERY
# --------------------------------

def calculate_overall_mastery(student):

    knowledge = student["knowledge"]

    if len(knowledge) == 0:
        return 0

    total_mastery = 0

    for topic, mastery in knowledge.items():

        total_mastery += mastery

    overall_mastery = total_mastery / len(knowledge)

    return overall_mastery


# --------------------------------
# FIND WEAK TOPICS
# --------------------------------

def find_weak_topics(student, threshold=0.60):

    weak_topics = []

    for topic, mastery in student["knowledge"].items():

        if mastery < threshold:

            weak_topics.append({
                "topic": topic,
                "mastery": mastery
            })

    return weak_topics


# --------------------------------
# FIND STRONG TOPICS
# --------------------------------

def find_strong_topics(student, threshold=0.70):

    strong_topics = []

    for topic, mastery in student["knowledge"].items():

        if mastery >= threshold:

            strong_topics.append({
                "topic": topic,
                "mastery": mastery
            })

    return strong_topics


# --------------------------------
# CALCULATE RECENT ACCURACY
# --------------------------------

def calculate_recent_accuracy(
    student,
    topic,
    recent_count=3
):

    progress = get_topic_progress(
        student,
        topic
    )

    if len(progress) == 0:
        return 0

    recent_progress = progress[-recent_count:]

    correct_answers = 0

    for record in recent_progress:

        if record["correct"]:
            correct_answers += 1

    return correct_answers / len(recent_progress)

