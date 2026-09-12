
# --------------------------------
# KNOWLEDGE DECAY
# --------------------------------

from datetime import datetime


def apply_decay(
    mastery,
    days_unused,
    decay_rate=0.01
):

    new_mastery = mastery * (
        (1 - decay_rate) ** days_unused
    )

    # Mastery should never go below 0
    new_mastery = max(
        0,
        new_mastery
    )

    return new_mastery

def get_days_unused(
    student,
    topic
):

    topic_records = []

    for record in student["history"]:

        if record["topic"] == topic:

            if "timestamp" in record:

                topic_records.append(
                    record["timestamp"]
                )

    # No timestamp available
    if not topic_records:
        return 0

    last_timestamp = topic_records[-1]

    last_practice = datetime.fromisoformat(
        last_timestamp
    )

    current_time = datetime.now()

    time_difference = (
        current_time - last_practice
    )

    days_unused = time_difference.total_seconds() / 86400

    return days_unused


def apply_decay_to_student(student):

    current_time = datetime.now()

    # Create last_decay storage if it doesn't exist
    student.setdefault(
        "last_decay",
        {}
    )

    for topic in student["knowledge"]:

        # Find the last time this topic was practiced
        days_unused = get_days_unused(
            student,
            topic
        )

        # If no usable timestamp exists
        if days_unused <= 0:
            continue

        # Check when decay was last applied
        last_decay_timestamp = student["last_decay"].get(topic)

        if last_decay_timestamp is not None:

            last_decay_time = datetime.fromisoformat(
                last_decay_timestamp
            )

            # Calculate only the NEW unused time
            new_unused_time = (
                current_time - last_decay_time
            )

            days_unused = (
                new_unused_time.total_seconds() / 86400
            )

        if days_unused <= 0:
            continue

        old_mastery = student["knowledge"][topic]

        new_mastery = apply_decay(
            old_mastery,
            days_unused
        )

        student["knowledge"][topic] = new_mastery

        # Record when decay was applied
        student["last_decay"][topic] = (
            current_time.isoformat()
        )

    return student