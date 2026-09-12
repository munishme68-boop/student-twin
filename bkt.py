
# --------------------------------
# BAYESIAN KNOWLEDGE TRACING
# --------------------------------
from datetime import datetime
def update_mastery(
    mastery,
    correct,
    difficulty="medium",
    learning_probability=0.03,
    guess_probability=0.20,
    slip_probability=0.20
):

    # Difficulty affects the learning rate
    if difficulty == "easy":
        learning_probability = 0.03
    elif difficulty == "medium":
        learning_probability = 0.03
    elif difficulty == "hard":
        learning_probability = 0.04
    # --------------------------------
    # STEP 1: UPDATE BELIEF
    # --------------------------------

    if correct:

        numerator = mastery * (1 - slip_probability)

        denominator = (
            numerator
            + (1 - mastery) * guess_probability
        )

    else:

        numerator = mastery * slip_probability

        denominator = (
            numerator
            + (1 - mastery) * (1 - guess_probability)
        )

    probability_known = numerator / denominator

    # --------------------------------
    # STEP 2: LEARNING AFTER ANSWER
    # --------------------------------

    new_mastery = (
        probability_known
        + (1 - probability_known)
        * learning_probability
    )


# Limit mastery change from a single question
    max_change = 0.10

    if new_mastery > mastery + max_change:
        new_mastery = mastery + max_change

    elif new_mastery < mastery - max_change:
        new_mastery = mastery - max_change


    new_mastery = max(0, min(1, new_mastery))

    return new_mastery


def update_knowledge(
    student,
    topic,
    correct,
    difficulty
):

    old_mastery = student["knowledge"].get(
        topic,
        0
    )

    new_mastery = update_mastery(
        old_mastery,
        correct,
        difficulty
    )

    student["knowledge"][topic] = new_mastery

    student["history"].append({
      "topic": topic,
      "correct": correct,
      "difficulty": difficulty,
      "timestamp": datetime.now().isoformat()
    })
    return new_mastery
