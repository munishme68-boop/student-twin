
# --------------------------------
# KNOWLEDGE GRAPH
# --------------------------------

knowledge_graph = {

    # --------------------------------
    # FOUNDATIONS
    # --------------------------------

    "python": [],

    "probability": [],

    "statistics": [],


    # --------------------------------
    # MACHINE LEARNING
    # --------------------------------

    "machine_learning": [
        "python",
        "probability",
        "statistics"
    ],


    # --------------------------------
    # DEEP LEARNING
    # --------------------------------

    "neural_networks": [
        "machine_learning"
    ],

    "convolution": [
        "neural_networks"
    ],

    "cnn": [
        "convolution"
    ],

    "rnn": [
        "neural_networks"
    ],

    "lstm": [
        "rnn"
    ],


    # --------------------------------
    # COMPUTER VISION
    # --------------------------------

    "image_classification": [
        "cnn"
    ],

    "object_detection": [
        "cnn",
        "image_classification"
    ],


    # --------------------------------
    # NLP
    # --------------------------------

    "natural_language_processing": [
        "machine_learning"
    ],

    "word_embeddings": [
        "natural_language_processing"
    ],

    "transformers": [
        "word_embeddings",
        "neural_networks"
    ],


    # --------------------------------
    # GENERATIVE AI
    # --------------------------------

    "generative_ai": [
        "transformers"
    ],

    "large_language_models": [
        "transformers",
        "generative_ai"
    ],


    # --------------------------------
    # AI ENGINEERING
    # --------------------------------

    "model_deployment": [
        "machine_learning"
    ],

    "mlops": [
        "model_deployment",
        "machine_learning"
    ],

        # --------------------------------
    # MECHANICAL / ROBOTICS
    # --------------------------------

    "thermodynamics": [],

    "fluid_mechanics": [],

    "ros": [
        "python"
    ]
}


# --------------------------------
# GET DIRECT PREREQUISITES
# --------------------------------

def get_prerequisites(topic):

    return knowledge_graph.get(topic, [])


# --------------------------------
# FIND WEAK DIRECT PREREQUISITES
# --------------------------------

def find_weak_prerequisites(
    student,
    topic,
    threshold=0.60
):

    prerequisites = get_prerequisites(topic)

    weak_topics = []

    for prerequisite in prerequisites:

        mastery = student["knowledge"].get(
            prerequisite,
            0
        )

        if mastery < threshold:

            weak_topics.append({
                "topic": prerequisite,
                "mastery": mastery
            })

    return weak_topics


# --------------------------------
# FIND ALL PREREQUISITES
# --------------------------------

def get_all_prerequisites(topic):

    all_prerequisites = []

    def collect_prerequisites(current_topic):

        for prerequisite in get_prerequisites(
            current_topic
        ):

            if prerequisite not in all_prerequisites:

                all_prerequisites.append(
                    prerequisite
                )

                collect_prerequisites(
                    prerequisite
                )

    collect_prerequisites(topic)

    return all_prerequisites
# --------------------------------
# FIND WEAKEST PREREQUISITE
# --------------------------------

def find_weakest_prerequisite(
    student,
    topic
):

    prerequisites = get_all_prerequisites(topic)

    if not prerequisites:

        return None

    weakest_topic = None
    weakest_mastery = 1.0

    for prerequisite in prerequisites:

        mastery = student["knowledge"].get(
            prerequisite,
            0
        )

        if mastery < weakest_mastery:

            weakest_mastery = mastery
            weakest_topic = prerequisite

    return {
        "topic": weakest_topic,
        "mastery": weakest_mastery
    }

