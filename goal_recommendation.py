def get_goal_topics(student):

    goal = student["profile"]["goal"].lower()

    if "ai engineer" in goal:

        return [

            # Foundations
            "python",
            "probability",
            "statistics",

            # Machine Learning
            "machine_learning",

            # Deep Learning
            "neural_networks",
            "convolution",
            "cnn",
            "rnn",
            "lstm",

            # NLP
            "natural_language_processing",
            "word_embeddings",
            "transformers",

            # Computer Vision
            "image_classification",
            "object_detection",

            # Generative AI
            "generative_ai",
            "large_language_models",

            # AI Engineering
            "model_deployment",
            "mlops"
        ]

    elif "data scientist" in goal:

        return [
            "python",
            "probability",
            "statistics",
            "machine_learning"
        ]

    elif "computer vision" in goal:

        return [
            "python",
            "neural_networks",
            "convolution",
            "cnn",
            "image_classification",
            "object_detection"
        ]

    else:

        return []

def get_next_goal_topic(student):

    topics = get_goal_topics(student)

    for topic in topics:

        mastery = student["knowledge"].get(
            topic,
            0
        )

        if mastery < 0.60:
            return topic

    return None