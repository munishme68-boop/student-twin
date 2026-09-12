
# --------------------------------
# QUESTION BANK
# --------------------------------

import random

question_bank = [

    # =========================
    # PYTHON
    # =========================

    {
        "id": 1,
        "topic": "python",
        "difficulty": "easy",
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "function",
            "def",
            "define",
            "fun"
        ],
        "answer": 2
    },

    {
        "id": 2,
        "topic": "python",
        "difficulty": "easy",
        "question": "Which data type is used to store True or False in Python?",
        "options": [
            "String",
            "Boolean",
            "Integer",
            "List"
        ],
        "answer": 2
    },

    {
        "id": 3,
        "topic": "python",
        "difficulty": "easy",
        "question": "Which symbol is used to write a comment in Python?",
        "options": [
            "#",
            "//",
            "/* */",
            "<!-- -->"
        ],
        "answer": 1
    },

    {
        "id": 4,
        "topic": "python",
        "difficulty": "medium",
        "question": "What is the difference between a list and a tuple?",
        "options": [
            "Lists are mutable, tuples are immutable",
            "Lists are immutable, tuples are mutable",
            "Both are immutable",
            "Both are mutable"
        ],
        "answer": 1
    },

    {
        "id": 5,
        "topic": "python",
        "difficulty": "medium",
        "question": "What is a dictionary in Python?",
        "options": [
            "A collection of key-value pairs",
            "A sequence of only numbers",
            "A Python function",
            "A loop structure"
        ],
        "answer": 1
    },

    {
        "id": 6,
        "topic": "python",
        "difficulty": "medium",
        "question": "What is the purpose of a Python loop?",
        "options": [
            "To repeat a block of code",
            "To define a class",
            "To import libraries",
            "To create comments"
        ],
        "answer": 1
    },

    {
        "id": 7,
        "topic": "python",
        "difficulty": "hard",
        "question": "Explain Python decorators with an example.",
        "options": [
            "They modify or extend the behavior of functions",
            "They store variables",
            "They create loops",
            "They handle only errors"
        ],
        "answer": 1
    },

    {
        "id": 8,
        "topic": "python",
        "difficulty": "hard",
        "question": "Explain the difference between shallow copy and deep copy.",
        "options": [
            "Deep copy recursively copies nested objects",
            "Shallow copy always copies everything recursively",
            "They are exactly the same",
            "Neither creates a copy"
        ],
        "answer": 1
    },

    {
        "id": 9,
        "topic": "python",
        "difficulty": "hard",
        "question": "Explain how exception handling works in Python.",
        "options": [
            "Using try and except blocks",
            "Using only loops",
            "Using dictionaries",
            "Using comments"
        ],
        "answer": 1
    },


    # =========================
    # MACHINE LEARNING
    # =========================

    {
        "id": 10,
        "topic": "machine_learning",
        "difficulty": "easy",
        "question": "What is supervised learning?",
        "options": [
            "Learning without data",
            "Learning from labelled data",
            "Learning only from images",
            "Learning without a model"
        ],
        "answer": 2
    },

    {
        "id": 11,
        "topic": "machine_learning",
        "difficulty": "easy",
        "question": "What is a dataset?",
        "options": [
            "A collection of data used for analysis or training",
            "A programming language",
            "A neural network layer",
            "An optimizer"
        ],
        "answer": 1
    },

    {
        "id": 12,
        "topic": "machine_learning",
        "difficulty": "easy",
        "question": "What is a feature in machine learning?",
        "options": [
            "An input variable used by a model",
            "The final prediction",
            "An error message",
            "A programming language"
        ],
        "answer": 1
    },

    {
        "id": 13,
        "topic": "machine_learning",
        "difficulty": "medium",
        "question": "What is overfitting in machine learning?",
        "options": [
            "A model performs well on training data but poorly on unseen data",
            "A model has no parameters",
            "A model has no training data",
            "A model always predicts correctly"
        ],
        "answer": 1
    },

    {
        "id": 14,
        "topic": "machine_learning",
        "difficulty": "medium",
        "question": "What is the difference between classification and regression?",
        "options": [
            "Classification predicts categories, regression predicts continuous values",
            "Classification predicts only numbers",
            "Regression predicts only categories",
            "There is no difference"
        ],
        "answer": 1
    },

    {
        "id": 15,
        "topic": "machine_learning",
        "difficulty": "medium",
        "question": "Why is data preprocessing important in machine learning?",
        "options": [
            "It improves data quality and prepares data for modelling",
            "It removes the need for training",
            "It replaces the model",
            "It eliminates all features"
        ],
        "answer": 1
    },

    {
        "id": 16,
        "topic": "machine_learning",
        "difficulty": "hard",
        "question": "Explain the bias-variance tradeoff.",
        "options": [
            "It balances underfitting and overfitting",
            "It only measures dataset size",
            "It is an optimization algorithm",
            "It removes training data"
        ],
        "answer": 1
    },

    {
        "id": 17,
        "topic": "machine_learning",
        "difficulty": "hard",
        "question": "Explain how gradient descent is used to train a machine learning model.",
        "options": [
            "It updates parameters to reduce the loss",
            "It removes all parameters",
            "It only increases the loss",
            "It creates training data"
        ],
        "answer": 1
    },

    {
        "id": 18,
        "topic": "machine_learning",
        "difficulty": "hard",
        "question": "Compare bagging and boosting techniques.",
        "options": [
            "Bagging trains models independently, boosting builds models sequentially",
            "Both are identical",
            "Boosting never uses previous models",
            "Bagging always uses neural networks"
        ],
        "answer": 1
    },


    # =========================
    # NEURAL NETWORKS
    # =========================

    {
        "id": 19,
        "topic": "neural_networks",
        "difficulty": "easy",
        "question": "What is a neural network?",
        "options": [
            "A model inspired by interconnected neurons",
            "A database",
            "A programming language",
            "A sorting algorithm"
        ],
        "answer": 1
    },

    {
        "id": 20,
        "topic": "neural_networks",
        "difficulty": "easy",
        "question": "What is a neuron in a neural network?",
        "options": [
            "A computational unit that processes inputs",
            "A dataset",
            "An optimizer",
            "A programming language"
        ],
        "answer": 1
    },

    {
        "id": 21,
        "topic": "neural_networks",
        "difficulty": "easy",
        "question": "What is an input layer?",
        "options": [
            "The layer that receives input features",
            "The layer that calculates the final loss",
            "The layer that stores datasets",
            "The output prediction"
        ],
        "answer": 1
    },

    {
        "id": 22,
        "topic": "neural_networks",
        "difficulty": "medium",
        "question": "What is the purpose of an activation function?",
        "options": [
            "To introduce non-linearity into the network",
            "To store training data",
            "To remove neurons",
            "To create datasets"
        ],
        "answer": 1
    },

    {
        "id": 23,
        "topic": "neural_networks",
        "difficulty": "medium",
        "question": "What is the purpose of the loss function?",
        "options": [
            "To measure the difference between prediction and target",
            "To create neurons",
            "To store weights permanently",
            "To increase the dataset size"
        ],
        "answer": 1
    },

    {
        "id": 24,
        "topic": "neural_networks",
        "difficulty": "medium",
        "question": "What is an epoch in neural network training?",
        "options": [
            "One complete pass through the training dataset",
            "One neuron",
            "One input feature",
            "One model parameter"
        ],
        "answer": 1
    },

    {
        "id": 25,
        "topic": "neural_networks",
        "difficulty": "hard",
        "question": "Explain how backpropagation works in a neural network.",
        "options": [
            "It calculates gradients and propagates errors backward",
            "It removes all weights",
            "It creates new datasets",
            "It only performs forward propagation"
        ],
        "answer": 1
    },

    {
        "id": 26,
        "topic": "neural_networks",
        "difficulty": "hard",
        "question": "Explain the vanishing gradient problem.",
        "options": [
            "Gradients become extremely small during training",
            "Gradients always become infinite",
            "The dataset disappears",
            "Weights become exactly zero immediately"
        ],
        "answer": 1
    },

    {
        "id": 27,
        "topic": "neural_networks",
        "difficulty": "hard",
        "question": "Explain how an optimizer updates neural network weights.",
        "options": [
            "It uses gradients to adjust weights and reduce loss",
            "It removes the training dataset",
            "It changes the input features",
            "It deletes neurons"
        ],
        "answer": 1
    },


    # =========================
    # CONVOLUTION
    # =========================

    {
        "id": 28,
        "topic": "convolution",
        "difficulty": "easy",
        "question": "What is convolution in a neural network?",
        "options": [
            "An operation that applies a filter to extract features",
            "A type of dataset",
            "A loss function",
            "An optimizer"
        ],
        "answer": 1
    },

    {
        "id": 29,
        "topic": "convolution",
        "difficulty": "easy",
        "question": "What is a convolution kernel?",
        "options": [
            "A small matrix used to extract features",
            "A dataset",
            "An activation function",
            "A neural network output"
        ],
        "answer": 1
    },

    {
        "id": 30,
        "topic": "convolution",
        "difficulty": "easy",
        "question": "What is a feature map?",
        "options": [
            "The output produced after applying a filter",
            "The original dataset",
            "The optimizer",
            "The loss function"
        ],
        "answer": 1
    },

    {
        "id": 31,
        "topic": "convolution",
        "difficulty": "medium",
        "question": "What is the purpose of a convolution filter?",
        "options": [
            "To detect specific features in the input",
            "To store labels",
            "To remove the network",
            "To calculate only the final prediction"
        ],
        "answer": 1
    },

    {
        "id": 32,
        "topic": "convolution",
        "difficulty": "medium",
        "question": "What is stride in convolution?",
        "options": [
            "The number of pixels the filter moves at each step",
            "The number of neurons",
            "The learning rate",
            "The number of epochs"
        ],
        "answer": 1
    },

    {
        "id": 33,
        "topic": "convolution",
        "difficulty": "medium",
        "question": "What is padding in convolution?",
        "options": [
            "Adding pixels around the input",
            "Removing all filters",
            "Increasing the learning rate",
            "Changing the labels"
        ],
        "answer": 1
    },

    {
        "id": 34,
        "topic": "convolution",
        "difficulty": "hard",
        "question": "Explain how stride and padding affect convolution.",
        "options": [
            "They affect the spatial size of the output",
            "They only change the labels",
            "They remove the filters",
            "They replace the activation function"
        ],
        "answer": 1
    },

    {
        "id": 35,
        "topic": "convolution",
        "difficulty": "hard",
        "question": "Explain how multiple convolution filters extract different features.",
        "options": [
            "Different filters learn different patterns",
            "All filters must learn exactly the same pattern",
            "Filters only store labels",
            "Filters remove the input"
        ],
        "answer": 1
    },

    {
        "id": 36,
        "topic": "convolution",
        "difficulty": "hard",
        "question": "Derive the output size formula for a convolution operation.",
        "options": [
            "Output size depends on input size, filter size, padding and stride",
            "Output size depends only on labels",
            "Output size is always equal to the input",
            "Output size depends only on epochs"
        ],
        "answer": 1
    },


    # =========================
    # CNN
    # =========================

    {
        "id": 37,
        "topic": "cnn",
        "difficulty": "easy",
        "question": "What is the purpose of a convolution layer?",
        "options": [
            "To extract spatial features",
            "To store labels",
            "To calculate only accuracy",
            "To remove all input data"
        ],
        "answer": 1
    },

    {
        "id": 38,
        "topic": "cnn",
        "difficulty": "easy",
        "question": "What is a CNN?",
        "options": [
            "Convolutional Neural Network",
            "Computer Numerical Network",
            "Central Neural Node",
            "Convolution Number Node"
        ],
        "answer": 1
    },

    {
        "id": 39,
        "topic": "cnn",
        "difficulty": "easy",
        "question": "What type of data are CNNs commonly used for?",
        "options": [
            "Images and spatial data",
            "Only text",
            "Only audio",
            "Only numerical tables"
        ],
        "answer": 1
    },

    {
        "id": 40,
        "topic": "cnn",
        "difficulty": "medium",
        "question": "What is the role of a pooling layer in CNN?",
        "options": [
            "To reduce spatial dimensions",
            "To increase the number of labels",
            "To remove convolution",
            "To create the dataset"
        ],
        "answer": 1
    },

    {
        "id": 41,
        "topic": "cnn",
        "difficulty": "medium",
        "question": "What is the difference between max pooling and average pooling?",
        "options": [
            "Max pooling selects the maximum, average pooling calculates the average",
            "They always produce identical results",
            "Average pooling selects the maximum",
            "Max pooling calculates the average"
        ],
        "answer": 1
    },

    {
        "id": 42,
        "topic": "cnn",
        "difficulty": "medium",
        "question": "Why are CNNs useful for image classification?",
        "options": [
            "They can learn spatial and hierarchical features",
            "They cannot process images",
            "They only work with labels",
            "They do not use filters"
        ],
        "answer": 1
    },

    {
        "id": 43,
        "topic": "cnn",
        "difficulty": "hard",
        "question": "Explain how a CNN can learn hierarchical features.",
        "options": [
            "Different layers learn increasingly complex patterns",
            "Every layer learns exactly the same feature",
            "CNNs cannot learn features",
            "Only the output layer learns features"
        ],
        "answer": 1
    },

    {
        "id": 44,
        "topic": "cnn",
        "difficulty": "hard",
        "question": "Explain the complete flow of an image through a CNN.",
        "options": [
            "Convolution, activation, pooling and final classification",
            "Only pooling",
            "Only convolution",
            "Only classification"
        ],
        "answer": 1
    },

    {
        "id": 45,
        "topic": "cnn",
        "difficulty": "hard",
        "question": "Explain how CNNs reduce the number of parameters compared with fully connected networks.",
        "options": [
            "They use local connectivity and shared weights",
            "They use more parameters everywhere",
            "They remove all neurons",
            "They do not use weights"
        ],
        "answer": 1
    },
    # =========================
    # PROBABILITY
    # =========================


    {
        "id": 46,
        "topic": "probability",
        "difficulty": "easy",
        "question": "What is the probability of getting a head when a fair coin is tossed once?",
        "options": [
            "0",
            "0.25",
            "0.5",
            "1"
        ],
        "answer": 3
    },

    {
        "id": 47,
        "topic": "probability",
        "difficulty": "easy",
        "question": "What is the probability of getting a 6 when a fair die is rolled once?",
        "options": [
            "1/2",
            "1/3",
            "1/6",
            "1/12"
        ],
        "answer": 3
    },

    {
        "id": 48,
        "topic": "probability",
        "difficulty": "easy",
        "question": "A bag contains 3 red balls and 2 blue balls. What is the probability of selecting a red ball?",
        "options": [
            "2/5",
            "3/5",
            "1/2",
            "3/2"
        ],
        "answer": 2
    },

    {
        "id": 49,
        "topic": "probability",
        "difficulty": "medium",
        "question": "If P(A) = 0.4 and P(B) = 0.3, and A and B are independent, what is P(A and B)?",
        "options": [
            "0.12",
            "0.30",
            "0.40",
            "0.70"
        ],
        "answer": 1
    },

    {
        "id": 50,
        "topic": "probability",
        "difficulty": "medium",
        "question": "What is the probability of getting exactly two heads when a fair coin is tossed three times?",
        "options": [
            "1/8",
            "2/8",
            "3/8",
            "4/8"
        ],
        "answer": 3
    },

    {
        "id": 51,
        "topic": "probability",
        "difficulty": "medium",
        "question": "If P(A) = 0.5 and P(B) = 0.4, what is P(A or B) when A and B are mutually exclusive?",
        "options": [
            "0.1",
            "0.2",
            "0.9",
            "0.5"
        ],
        "answer": 3
    },

    {
        "id": 52,
        "topic": "probability",
        "difficulty": "hard",
        "question": "A fair coin is tossed four times. What is the probability of getting at least one head?",
        "options": [
            "1/16",
            "4/16",
            "11/16",
            "15/16"
        ],
        "answer": 4
    },

    {
        "id": 53,
        "topic": "probability",
        "difficulty": "hard",
        "question": "If P(A) = 0.6 and P(B|A) = 0.5, what is P(A and B)?",
        "options": [
            "0.10",
            "0.30",
            "0.50",
            "1.10"
        ],
        "answer": 2
    },

    {
        "id": 54,
        "topic": "probability",
        "difficulty": "hard",
        "question": "A box contains 5 red and 5 blue balls. Two balls are selected without replacement. What is the probability that both are red?",
        "options": [
            "1/4",
            "2/9",
            "5/18",
            "1/2"
        ],
        "answer": 2
    },
    # =========================
    # STATISTICS
    # =========================
    


        {
        "id": 55,
        "topic": "statistics",
        "difficulty": "easy",
        "question": "What is the mean of 2, 4, and 6?",
        "options": [
            "2",
            "4",
            "6",
            "12"
        ],
        "answer": 2
    },

    {
        "id": 56,
        "topic": "statistics",
        "difficulty": "easy",
        "question": "What is the median of 3, 5, and 7?",
        "options": [
            "3",
            "5",
            "6",
            "7"
        ],
        "answer": 2
    },

    {
        "id": 57,
        "topic": "statistics",
        "difficulty": "easy",
        "question": "Which measure of central tendency represents the most frequently occurring value?",
        "options": [
            "Mean",
            "Median",
            "Mode",
            "Range"
        ],
        "answer": 3
    },

    {
        "id": 58,
        "topic": "statistics",
        "difficulty": "medium",
        "question": "What is the mean of the numbers 10, 20, 30, and 40?",
        "options": [
            "20",
            "25",
            "30",
            "35"
        ],
        "answer": 2
    },

    {
        "id": 59,
        "topic": "statistics",
        "difficulty": "medium",
        "question": "What does standard deviation measure?",
        "options": [
            "The center of the data",
            "The spread of the data",
            "The largest value only",
            "The number of observations"
        ],
        "answer": 2
    },

    {
        "id": 60,
        "topic": "statistics",
        "difficulty": "medium",
        "question": "If the variance of a dataset is 25, what is its standard deviation?",
        "options": [
            "5",
            "10",
            "25",
            "50"
        ],
        "answer": 1
    },

    {
        "id": 61,
        "topic": "statistics",
        "difficulty": "hard",
        "question": "If every value in a dataset is increased by 5, what happens to the standard deviation?",
        "options": [
            "It increases by 5",
            "It decreases by 5",
            "It remains unchanged",
            "It becomes zero"
        ],
        "answer": 3
    },

    {
        "id": 62,
        "topic": "statistics",
        "difficulty": "hard",
        "question": "A dataset has a mean of 50 and a standard deviation of 10. What is the z-score of a value of 70?",
        "options": [
            "1",
            "2",
            "3",
            "4"
        ],
        "answer": 2
    },

    {
        "id": 63,
        "topic": "statistics",
        "difficulty": "hard",
        "question": "Which statement about correlation is correct?",
        "options": [
            "Correlation always proves causation",
            "Correlation measures the strength and direction of a relationship between variables",
            "Correlation can only be positive",
            "Correlation measures the mean of a dataset"
        ],
        "answer": 2
    },



        # --------------------------------
    # RNN QUESTIONS
    # --------------------------------

    {
        "id": 64,
        "topic": "rnn",
        "difficulty": "easy",
        "question": "What does RNN stand for?",
        "options": [
            "Random Neural Network",
            "Recurrent Neural Network",
            "Recursive Numeric Network",
            "Real Neural Node"
        ],
        "answer": 2
    },

    {
        "id": 65,
        "topic": "rnn",
        "difficulty": "easy",
        "question": "What type of data are RNNs especially useful for?",
        "options": [
            "Sequential data",
            "Only images",
            "Only numerical tables",
            "Static data with no order"
        ],
        "answer": 1
    },

    {
        "id": 66,
        "topic": "rnn",
        "difficulty": "easy",
        "question": "What information does an RNN hidden state carry?",
        "options": [
            "Only the current input",
            "Information from previous inputs",
            "Only the final output",
            "The learning rate"
        ],
        "answer": 2
    },

    {
        "id": 67,
        "topic": "rnn",
        "difficulty": "medium",
        "question": "Why does an RNN use the same weights across different time steps?",
        "options": [
            "To process sequences using shared parameters",
            "To remove the hidden state",
            "To make every input identical",
            "To eliminate training"
        ],
        "answer": 1
    },

    {
        "id": 68,
        "topic": "rnn",
        "difficulty": "medium",
        "question": "What is the main purpose of the hidden state in an RNN?",
        "options": [
            "To store information about previous time steps",
            "To replace the input data",
            "To calculate the dataset size",
            "To remove activation functions"
        ],
        "answer": 1
    },

    {
        "id": 69,
        "topic": "rnn",
        "difficulty": "medium",
        "question": "What is BPTT in RNN training?",
        "options": [
            "Batch Processing Through Training",
            "Backpropagation Through Time",
            "Binary Prediction Through Time",
            "Backtracking Parameter Training"
        ],
        "answer": 2
    },

    {
        "id": 70,
        "topic": "rnn",
        "difficulty": "hard",
        "question": "What major problem can occur when training a basic RNN on long sequences?",
        "options": [
            "Vanishing or exploding gradients",
            "The input becomes an image",
            "The loss function disappears",
            "The dataset becomes sorted"
        ],
        "answer": 1
    },

    {
        "id": 71,
        "topic": "rnn",
        "difficulty": "hard",
        "question": "Why can a basic RNN struggle to learn long-term dependencies?",
        "options": [
            "Gradients can become very small during backpropagation",
            "RNNs cannot process sequences",
            "RNNs have no weights",
            "RNNs cannot use hidden states"
        ],
        "answer": 1
    },

    {
        "id": 72,
        "topic": "rnn",
        "difficulty": "hard",
        "question": "How does an RNN process a sequence?",
        "options": [
            "It processes the sequence step by step while updating its hidden state",
            "It ignores the order of inputs",
            "It processes only the last input",
            "It converts every input into an image"
        ],
        "answer": 1
    },


    # --------------------------------
    # LSTM QUESTIONS
    # --------------------------------

    {
        "id": 73,
        "topic": "lstm",
        "difficulty": "easy",
        "question": "What does LSTM stand for?",
        "options": [
            "Long Short-Term Memory",
            "Long Sequential Training Model",
            "Linear Short-Term Machine",
            "Layered State Transfer Model"
        ],
        "answer": 1
    },

    {
        "id": 74,
        "topic": "lstm",
        "difficulty": "easy",
        "question": "LSTM is a specialized type of which neural network?",
        "options": [
            "CNN",
            "RNN",
            "GAN",
            "Autoencoder"
        ],
        "answer": 2
    },

    {
        "id": 75,
        "topic": "lstm",
        "difficulty": "easy",
        "question": "What is one major advantage of LSTM over a basic RNN?",
        "options": [
            "It handles long-term dependencies better",
            "It cannot process sequences",
            "It removes all parameters",
            "It only works with images"
        ],
        "answer": 1
    },

    {
        "id": 76,
        "topic": "lstm",
        "difficulty": "medium",
        "question": "Which mechanism helps an LSTM control information flow?",
        "options": [
            "Gates",
            "Pooling layers",
            "Convolution kernels",
            "Decision trees"
        ],
        "answer": 1
    },

    {
        "id": 77,
        "topic": "lstm",
        "difficulty": "medium",
        "question": "Which gate in an LSTM controls what information should be forgotten?",
        "options": [
            "Input gate",
            "Forget gate",
            "Output gate",
            "Pooling gate"
        ],
        "answer": 2
    },

    {
        "id": 78,
        "topic": "lstm",
        "difficulty": "medium",
        "question": "Which LSTM gate controls what new information is added to the cell state?",
        "options": [
            "Forget gate",
            "Input gate",
            "Output gate",
            "Loss gate"
        ],
        "answer": 2
    },

    {
        "id": 79,
        "topic": "lstm",
        "difficulty": "hard",
        "question": "What is the purpose of the cell state in an LSTM?",
        "options": [
            "To carry information across time steps",
            "To remove the hidden state",
            "To store only the input size",
            "To calculate the number of classes"
        ],
        "answer": 1
    },

    {
        "id": 80,
        "topic": "lstm",
        "difficulty": "hard",
        "question": "Why do LSTMs reduce the vanishing gradient problem?",
        "options": [
            "Their cell-state pathway and gates help preserve useful gradients",
            "They do not use gradients",
            "They do not use weights",
            "They remove backpropagation"
        ],
        "answer": 1
    },

    {
        "id": 81,
        "topic": "lstm",
        "difficulty": "hard",
        "question": "What are the three main gates in a standard LSTM?",
        "options": [
            "Input, forget, and output gates",
            "Input, pooling, and convolution gates",
            "Forget, loss, and prediction gates",
            "Hidden, weight, and bias gates"
        ],
        "answer": 1
    },


    # --------------------------------
    # NLP QUESTIONS
    # --------------------------------

    {
        "id": 82,
        "topic": "natural_language_processing",
        "difficulty": "easy",
        "question": "What does NLP stand for?",
        "options": [
            "Neural Learning Process",
            "Natural Language Processing",
            "Numeric Language Prediction",
            "Network Learning Protocol"
        ],
        "answer": 2
    },

    {
        "id": 83,
        "topic": "natural_language_processing",
        "difficulty": "easy",
        "question": "What is the main goal of NLP?",
        "options": [
            "Enable computers to process and understand human language",
            "Only classify images",
            "Only process sensor signals",
            "Build physical robots"
        ],
        "answer": 1
    },

    {
        "id": 84,
        "topic": "natural_language_processing",
        "difficulty": "easy",
        "question": "Which is an example of an NLP application?",
        "options": [
            "Machine translation",
            "Image resizing",
            "Motor control",
            "Temperature measurement"
        ],
        "answer": 1
    },

    {
        "id": 85,
        "topic": "natural_language_processing",
        "difficulty": "medium",
        "question": "What is tokenization in NLP?",
        "options": [
            "Splitting text into smaller units such as words or subwords",
            "Converting text into an image",
            "Deleting all punctuation from a computer",
            "Training a CNN"
        ],
        "answer": 1
    },

    {
        "id": 86,
        "topic": "natural_language_processing",
        "difficulty": "medium",
        "question": "What is sentiment analysis?",
        "options": [
            "Determining the emotional or opinion-based tone of text",
            "Detecting objects in images",
            "Measuring CPU temperature",
            "Sorting numerical data"
        ],
        "answer": 1
    },

    {
        "id": 87,
        "topic": "natural_language_processing",
        "difficulty": "medium",
        "question": "Why is context important in NLP?",
        "options": [
            "The meaning of a word can depend on surrounding words",
            "Context makes all words identical",
            "Context removes the need for training",
            "Context is only useful for images"
        ],
        "answer": 1
    },

    {
        "id": 88,
        "topic": "natural_language_processing",
        "difficulty": "hard",
        "question": "What is named entity recognition?",
        "options": [
            "Identifying entities such as people, places, and organizations in text",
            "Recognizing objects in images",
            "Detecting neurons in a network",
            "Finding numerical outliers"
        ],
        "answer": 1
    },

    {
        "id": 89,
        "topic": "natural_language_processing",
        "difficulty": "hard",
        "question": "What is the main challenge of understanding natural language?",
        "options": [
            "Language can be ambiguous and highly dependent on context",
            "Text always has exactly one meaning",
            "Words never depend on context",
            "Language contains no structure"
        ],
        "answer": 1
    },

    {
        "id": 90,
        "topic": "natural_language_processing",
        "difficulty": "hard",
        "question": "What is sequence-to-sequence learning commonly used for?",
        "options": [
            "Tasks such as machine translation",
            "Only image classification",
            "Only numerical sorting",
            "Only database storage"
        ],
        "answer": 1
    },


    # --------------------------------
    # TRANSFORMER QUESTIONS
    # --------------------------------

    {
        "id": 91,
        "topic": "transformers",
        "difficulty": "easy",
        "question": "What is a Transformer in deep learning?",
        "options": [
            "A neural network architecture based heavily on attention mechanisms",
            "A type of database",
            "A computer processor",
            "A traditional sorting algorithm"
        ],
        "answer": 1
    },

    {
        "id": 92,
        "topic": "transformers",
        "difficulty": "easy",
        "question": "What mechanism is central to the Transformer architecture?",
        "options": [
            "Self-attention",
            "Pooling",
            "Decision trees",
            "K-means clustering"
        ],
        "answer": 1
    },

    {
        "id": 93,
        "topic": "transformers",
        "difficulty": "easy",
        "question": "Why are Transformers effective for processing sequences?",
        "options": [
            "They can model relationships between different positions in a sequence",
            "They only process one word in total",
            "They cannot process text",
            "They remove all context"
        ],
        "answer": 1
    },

    {
        "id": 94,
        "topic": "transformers",
        "difficulty": "medium",
        "question": "What does self-attention allow a Transformer to do?",
        "options": [
            "Determine how different tokens relate to one another",
            "Remove all tokens",
            "Convert text directly into images",
            "Eliminate training"
        ],
        "answer": 1
    },

    {
        "id": 95,
        "topic": "transformers",
        "difficulty": "medium",
        "question": "Why is positional information needed in Transformers?",
        "options": [
            "Self-attention alone does not inherently encode the order of tokens",
            "It makes all tokens identical",
            "It removes the attention mechanism",
            "It replaces the vocabulary"
        ],
        "answer": 1
    },

    {
        "id": 96,
        "topic": "transformers",
        "difficulty": "medium",
        "question": "What is multi-head attention?",
        "options": [
            "Using multiple attention mechanisms to learn different relationships",
            "Using multiple datasets without training",
            "Using multiple CPUs to store data",
            "Using multiple output labels only"
        ],
        "answer": 1
    },

    {
        "id": 97,
        "topic": "transformers",
        "difficulty": "hard",
        "question": "What are the three components commonly used to compute attention?",
        "options": [
            "Query, Key, and Value",
            "Input, Hidden, and Output",
            "Mean, Median, and Mode",
            "Weight, Bias, and Loss"
        ],
        "answer": 1
    },

    {
        "id": 98,
        "topic": "transformers",
        "difficulty": "hard",
        "question": "What is the main advantage of Transformer attention compared with sequential RNN processing?",
        "options": [
            "It allows much more parallel processing across sequence positions",
            "It cannot process long sequences",
            "It removes all model parameters",
            "It requires no training data"
        ],
        "answer": 1
    },

    {
        "id": 99,
        "topic": "transformers",
        "difficulty": "hard",
        "question": "Which models are built using the Transformer architecture?",
        "options": [
            "BERT and GPT",
            "Linear Regression and KNN",
            "Decision Tree and Random Forest",
            "K-means and PCA"
        ],
        "answer": 1
    },


        # --------------------------------
    # IMAGE CLASSIFICATION
    # --------------------------------

    {
        "id": 100,
        "topic": "image_classification",
        "difficulty": "easy",
        "question": "What is image classification?",
        "options": [
            "Assigning an image to one or more predefined classes",
            "Detecting the exact location of every pixel",
            "Compressing an image",
            "Converting an image to audio"
        ],
        "answer": 1
    },

    {
        "id": 101,
        "topic": "image_classification",
        "difficulty": "easy",
        "question": "Which neural network architecture is commonly used for image classification?",
        "options": [
            "CNN",
            "RNN",
            "Decision tree",
            "K-means"
        ],
        "answer": 1
    },

    {
        "id": 102,
        "topic": "image_classification",
        "difficulty": "easy",
        "question": "What does a classification model usually predict?",
        "options": [
            "A class or category",
            "Only image dimensions",
            "Only the file size",
            "Only the number of pixels"
        ],
        "answer": 1
    },

    {
        "id": 103,
        "topic": "image_classification",
        "difficulty": "medium",
        "question": "What is the purpose of a softmax layer in multi-class image classification?",
        "options": [
            "Convert outputs into class probabilities",
            "Resize the image",
            "Detect edges",
            "Remove convolution layers"
        ],
        "answer": 1
    },

    {
        "id": 104,
        "topic": "image_classification",
        "difficulty": "medium",
        "question": "What is data augmentation in image classification?",
        "options": [
            "Creating varied training examples from existing images",
            "Deleting training images",
            "Reducing the number of classes",
            "Removing labels"
        ],
        "answer": 1
    },

    {
        "id": 105,
        "topic": "image_classification",
        "difficulty": "medium",
        "question": "Why is data augmentation useful?",
        "options": [
            "It can improve generalization and reduce overfitting",
            "It always reduces the dataset size",
            "It removes the need for labels",
            "It guarantees 100% accuracy"
        ],
        "answer": 1
    },

    {
        "id": 106,
        "topic": "image_classification",
        "difficulty": "hard",
        "question": "What is transfer learning in image classification?",
        "options": [
            "Using knowledge from a pretrained model for a new task",
            "Training every model from scratch",
            "Moving images between folders",
            "Changing image file formats"
        ],
        "answer": 1
    },

    {
        "id": 107,
        "topic": "image_classification",
        "difficulty": "hard",
        "question": "Why can pretrained CNNs be useful for image classification?",
        "options": [
            "They already contain useful learned visual features",
            "They require no input data",
            "They cannot be fine-tuned",
            "They only work with text"
        ],
        "answer": 1
    },

    {
        "id": 108,
        "topic": "image_classification",
        "difficulty": "hard",
        "question": "What is overfitting in image classification?",
        "options": [
            "The model performs well on training data but poorly on unseen data",
            "The model cannot learn the training data",
            "The image has too many pixels",
            "The model has no parameters"
        ],
        "answer": 1
    },


    # --------------------------------
    # OBJECT DETECTION
    # --------------------------------

    {
        "id": 109,
        "topic": "object_detection",
        "difficulty": "easy",
        "question": "What is object detection?",
        "options": [
            "Finding and classifying objects and their locations in an image",
            "Assigning one label to an entire dataset",
            "Compressing an image",
            "Converting text into speech"
        ],
        "answer": 1
    },

    {
        "id": 110,
        "topic": "object_detection",
        "difficulty": "easy",
        "question": "What does a bounding box represent?",
        "options": [
            "The approximate location of an object in an image",
            "The image's file size",
            "The model's learning rate",
            "The number of training epochs"
        ],
        "answer": 1
    },

    {
        "id": 111,
        "topic": "object_detection",
        "difficulty": "easy",
        "question": "How is object detection different from image classification?",
        "options": [
            "Detection identifies objects and their locations, while classification assigns image-level classes",
            "Classification always uses bounding boxes",
            "Detection cannot classify objects",
            "There is no difference"
        ],
        "answer": 1
    },

    {
        "id": 112,
        "topic": "object_detection",
        "difficulty": "medium",
        "question": "What is Intersection over Union (IoU)?",
        "options": [
            "A measure of overlap between predicted and ground-truth bounding boxes",
            "A measure of training time",
            "A measure of image brightness",
            "A measure of model size"
        ],
        "answer": 1
    },

    {
        "id": 113,
        "topic": "object_detection",
        "difficulty": "medium",
        "question": "What is Non-Maximum Suppression used for?",
        "options": [
            "Removing duplicate overlapping detections",
            "Increasing image resolution",
            "Creating training labels",
            "Increasing the learning rate"
        ],
        "answer": 1
    },

    {
        "id": 114,
        "topic": "object_detection",
        "difficulty": "medium",
        "question": "Which of the following is an object detection model family?",
        "options": [
            "YOLO",
            "K-means",
            "Linear Regression",
            "Naive Bayes"
        ],
        "answer": 1
    },

    {
        "id": 115,
        "topic": "object_detection",
        "difficulty": "hard",
        "question": "What does mean Average Precision (mAP) measure in object detection?",
        "options": [
            "Detection performance across classes and confidence thresholds",
            "Only image resolution",
            "Only training speed",
            "Only model memory usage"
        ],
        "answer": 1
    },

    {
        "id": 116,
        "topic": "object_detection",
        "difficulty": "hard",
        "question": "Why is confidence thresholding used in object detection?",
        "options": [
            "To filter out predictions with low confidence",
            "To increase image size",
            "To remove training data",
            "To change the CNN architecture"
        ],
        "answer": 1
    },

    {
        "id": 117,
        "topic": "object_detection",
        "difficulty": "hard",
        "question": "What does a detector typically predict for each detected object?",
        "options": [
            "Class, location, and confidence",
            "Only image width",
            "Only the training loss",
            "Only the learning rate"
        ],
        "answer": 1
    },


    # --------------------------------
    # WORD EMBEDDINGS
    # --------------------------------

    {
        "id": 118,
        "topic": "word_embeddings",
        "difficulty": "easy",
        "question": "What is a word embedding?",
        "options": [
            "A numerical vector representation of a word",
            "A grammar rule",
            "A database table",
            "An image representation"
        ],
        "answer": 1
    },

    {
        "id": 119,
        "topic": "word_embeddings",
        "difficulty": "easy",
        "question": "Why are word embeddings useful in NLP?",
        "options": [
            "They represent words numerically so models can process semantic relationships",
            "They remove all meaning from words",
            "They convert words directly into images",
            "They eliminate the need for training"
        ],
        "answer": 1
    },

    {
        "id": 120,
        "topic": "word_embeddings",
        "difficulty": "easy",
        "question": "Which of these is an example of a word embedding method?",
        "options": [
            "Word2Vec",
            "YOLO",
            "ResNet",
            "K-means only"
        ],
        "answer": 1
    },

    {
        "id": 121,
        "topic": "word_embeddings",
        "difficulty": "medium",
        "question": "What property can word embeddings capture?",
        "options": [
            "Semantic relationships between words",
            "Only word length",
            "Only alphabetical order",
            "Only punctuation"
        ],
        "answer": 1
    },

    {
        "id": 122,
        "topic": "word_embeddings",
        "difficulty": "medium",
        "question": "What is the main idea behind Word2Vec?",
        "options": [
            "Learn word representations from surrounding context",
            "Detect objects in images",
            "Translate images into audio",
            "Train only convolutional layers"
        ],
        "answer": 1
    },

    {
        "id": 123,
        "topic": "word_embeddings",
        "difficulty": "medium",
        "question": "What does cosine similarity commonly measure between word embeddings?",
        "options": [
            "Similarity in direction between vectors",
            "Number of characters in words",
            "Training time",
            "Vocabulary size"
        ],
        "answer": 1
    },

    {
        "id": 124,
        "topic": "word_embeddings",
        "difficulty": "hard",
        "question": "What is a contextual embedding?",
        "options": [
            "A word representation whose meaning can change based on surrounding context",
            "A fixed dictionary definition",
            "A representation that ignores surrounding words",
            "An image feature"
        ],
        "answer": 1
    },

    {
        "id": 125,
        "topic": "word_embeddings",
        "difficulty": "hard",
        "question": "Why can contextual embeddings be more powerful than traditional static embeddings?",
        "options": [
            "They can represent different meanings of a word in different contexts",
            "They always use fewer dimensions",
            "They do not require training",
            "They only represent word frequency"
        ],
        "answer": 1
    },

    {
        "id": 126,
        "topic": "word_embeddings",
        "difficulty": "hard",
        "question": "What is one limitation of static word embeddings such as traditional Word2Vec?",
        "options": [
            "A word generally receives the same representation regardless of context",
            "They cannot represent words numerically",
            "They only work for images",
            "They require no training"
        ],
        "answer": 1
    },


    # --------------------------------
    # GENERATIVE AI
    # --------------------------------

    {
        "id": 127,
        "topic": "generative_ai",
        "difficulty": "easy",
        "question": "What is Generative AI?",
        "options": [
            "AI that can generate new content such as text, images, audio, or code",
            "AI that only sorts numbers",
            "AI that only stores data",
            "AI that only detects hardware faults"
        ],
        "answer": 1
    },

    {
        "id": 128,
        "topic": "generative_ai",
        "difficulty": "easy",
        "question": "Which is an example of Generative AI?",
        "options": [
            "A model generating a paragraph of text",
            "A calculator adding two numbers",
            "A database storing a record",
            "A thermometer measuring temperature"
        ],
        "answer": 1
    },

    {
        "id": 129,
        "topic": "generative_ai",
        "difficulty": "easy",
        "question": "What is the main difference between generative and traditional discriminative models?",
        "options": [
            "Generative models can create new samples or content",
            "Generative models cannot learn from data",
            "Discriminative models always generate images",
            "There is no difference"
        ],
        "answer": 1
    },

    {
        "id": 130,
        "topic": "generative_ai",
        "difficulty": "medium",
        "question": "Which architecture is widely used in modern text generation systems?",
        "options": [
            "Transformer",
            "Decision tree",
            "K-means",
            "Linear regression"
        ],
        "answer": 1
    },

    {
        "id": 131,
        "topic": "generative_ai",
        "difficulty": "medium",
        "question": "What does text generation usually involve?",
        "options": [
            "Predicting and selecting tokens to produce a sequence",
            "Detecting image edges",
            "Sorting a database",
            "Measuring temperature"
        ],
        "answer": 1
    },

    {
        "id": 132,
        "topic": "generative_ai",
        "difficulty": "medium",
        "question": "What is a prompt in Generative AI?",
        "options": [
            "Input instructions or context given to a generative model",
            "The model's hardware",
            "A database index",
            "A convolution filter"
        ],
        "answer": 1
    },

    {
        "id": 133,
        "topic": "generative_ai",
        "difficulty": "hard",
        "question": "What is temperature in text generation?",
        "options": [
            "A parameter that influences the randomness of token selection",
            "The physical temperature of the computer",
            "The number of model layers",
            "The size of the training dataset"
        ],
        "answer": 1
    },

    {
        "id": 134,
        "topic": "generative_ai",
        "difficulty": "hard",
        "question": "What is hallucination in Generative AI?",
        "options": [
            "When a model generates information that is incorrect or unsupported",
            "When a model stops training",
            "When a GPU overheats",
            "When a dataset is deleted"
        ],
        "answer": 1
    },

    {
        "id": 135,
        "topic": "generative_ai",
        "difficulty": "hard",
        "question": "Why is evaluation important for Generative AI systems?",
        "options": [
            "Generated outputs can be fluent but still incorrect, unsafe, or irrelevant",
            "Generative models always produce perfect answers",
            "Evaluation is only needed for databases",
            "Generated content never requires checking"
        ],
        "answer": 1
    },


    # --------------------------------
    # LARGE LANGUAGE MODELS
    # --------------------------------

    {
        "id": 136,
        "topic": "large_language_models",
        "difficulty": "easy",
        "question": "What does LLM stand for?",
        "options": [
            "Large Language Model",
            "Linear Learning Machine",
            "Long Language Memory",
            "Layered Learning Model"
        ],
        "answer": 1
    },

    {
        "id": 137,
        "topic": "large_language_models",
        "difficulty": "easy",
        "question": "What type of data are LLMs primarily designed to process?",
        "options": [
            "Natural language and other token sequences",
            "Only temperature readings",
            "Only images",
            "Only audio frequencies"
        ],
        "answer": 1
    },

    {
        "id": 138,
        "topic": "large_language_models",
        "difficulty": "easy",
        "question": "Which architecture is the foundation of many modern LLMs?",
        "options": [
            "Transformer",
            "Decision tree",
            "KNN",
            "Linear regression"
        ],
        "answer": 1
    },

    {
        "id": 139,
        "topic": "large_language_models",
        "difficulty": "medium",
        "question": "What is tokenization in an LLM?",
        "options": [
            "Converting text into tokens that the model can process",
            "Converting text into images",
            "Deleting all words",
            "Changing the GPU"
        ],
        "answer": 1
    },

    {
        "id": 140,
        "topic": "large_language_models",
        "difficulty": "medium",
        "question": "What is pretraining in an LLM?",
        "options": [
            "Training a model on a large corpus to learn general language patterns",
            "Deploying the model to a server",
            "Deleting model weights",
            "Only testing the final model"
        ],
        "answer": 1
    },

    {
        "id": 141,
        "topic": "large_language_models",
        "difficulty": "medium",
        "question": "What is fine-tuning?",
        "options": [
            "Further training a pretrained model for a specific task or behavior",
            "Reducing the screen brightness",
            "Deleting the training dataset",
            "Replacing the CPU"
        ],
        "answer": 1
    },

    {
        "id": 142,
        "topic": "large_language_models",
        "difficulty": "hard",
        "question": "What is the context window of an LLM?",
        "options": [
            "The amount of token context the model can consider for a given input",
            "The size of the GPU",
            "The number of training datasets",
            "The model's physical temperature"
        ],
        "answer": 1
    },

    {
        "id": 143,
        "topic": "large_language_models",
        "difficulty": "hard",
        "question": "What is Retrieval-Augmented Generation (RAG)?",
        "options": [
            "Combining retrieval of external information with generation",
            "Training only a CNN",
            "Removing the model's context",
            "Compressing every token"
        ],
        "answer": 1
    },

    {
        "id": 144,
        "topic": "large_language_models",
        "difficulty": "hard",
        "question": "Why is RAG useful?",
        "options": [
            "It can provide a model with relevant external information at inference time",
            "It eliminates the need for any data",
            "It prevents all possible hallucinations",
            "It replaces every Transformer layer"
        ],
        "answer": 1
    },


    # --------------------------------
    # MODEL DEPLOYMENT
    # --------------------------------

    {
        "id": 145,
        "topic": "model_deployment",
        "difficulty": "easy",
        "question": "What is model deployment?",
        "options": [
            "Making a trained model available for real-world use",
            "Training a model from scratch",
            "Deleting a model",
            "Collecting only raw data"
        ],
        "answer": 1
    },

    {
        "id": 146,
        "topic": "model_deployment",
        "difficulty": "easy",
        "question": "What is an API commonly used for in model deployment?",
        "options": [
            "Allowing applications to send requests to and receive predictions from a model",
            "Increasing CPU temperature",
            "Deleting model weights",
            "Creating hardware circuits"
        ],
        "answer": 1
    },

    {
        "id": 147,
        "topic": "model_deployment",
        "difficulty": "easy",
        "question": "What is inference?",
        "options": [
            "Using a trained model to generate predictions",
            "Training the model",
            "Deleting the model",
            "Collecting electricity"
        ],
        "answer": 1
    },

    {
        "id": 148,
        "topic": "model_deployment",
        "difficulty": "medium",
        "question": "What is latency in model serving?",
        "options": [
            "The time taken to produce a response or prediction",
            "The model's accuracy",
            "The dataset size",
            "The number of classes"
        ],
        "answer": 1
    },

    {
        "id": 149,
        "topic": "model_deployment",
        "difficulty": "medium",
        "question": "Why is model serialization useful?",
        "options": [
            "It allows a trained model and its parameters to be saved and loaded later",
            "It increases the number of training examples",
            "It removes all model parameters",
            "It guarantees higher accuracy"
        ],
        "answer": 1
    },

    {
        "id": 150,
        "topic": "model_deployment",
        "difficulty": "medium",
        "question": "What is batch inference?",
        "options": [
            "Generating predictions for multiple inputs together",
            "Training with exactly one sample",
            "Deleting predictions",
            "Using only one feature"
        ],
        "answer": 1
    },

    {
        "id": 151,
        "topic": "model_deployment",
        "difficulty": "hard",
        "question": "What is model monitoring?",
        "options": [
            "Tracking model performance and behavior after deployment",
            "Changing the model every second",
            "Deleting production data",
            "Only measuring training accuracy"
        ],
        "answer": 1
    },

    {
        "id": 152,
        "topic": "model_deployment",
        "difficulty": "hard",
        "question": "What is data drift?",
        "options": [
            "A change in the distribution of input data over time",
            "A change in the model's file name",
            "A GPU hardware failure",
            "A programming syntax error"
        ],
        "answer": 1
    },

    {
        "id": 153,
        "topic": "model_deployment",
        "difficulty": "hard",
        "question": "Why is scalability important when deploying AI models?",
        "options": [
            "The system may need to handle increasing numbers of users or requests",
            "It guarantees zero errors",
            "It eliminates the need for monitoring",
            "It removes model parameters"
        ],
        "answer": 1
    },


    # --------------------------------
    # MLOPS
    # --------------------------------

    {
        "id": 154,
        "topic": "mlops",
        "difficulty": "easy",
        "question": "What does MLOps refer to?",
        "options": [
            "Practices for developing, deploying, and maintaining machine learning systems",
            "A type of neural network",
            "A programming language",
            "An image format"
        ],
        "answer": 1
    },

    {
        "id": 155,
        "topic": "mlops",
        "difficulty": "easy",
        "question": "Why is version control useful in ML projects?",
        "options": [
            "It helps track changes to code and other project artifacts",
            "It increases GPU memory",
            "It automatically guarantees accuracy",
            "It removes the need for testing"
        ],
        "answer": 1
    },

    {
        "id": 156,
        "topic": "mlops",
        "difficulty": "easy",
        "question": "What is CI/CD commonly used for?",
        "options": [
            "Automating software integration, testing, and delivery",
            "Increasing model parameters",
            "Collecting images manually",
            "Removing databases"
        ],
        "answer": 1
    },

    {
        "id": 157,
        "topic": "mlops",
        "difficulty": "medium",
        "question": "What is experiment tracking?",
        "options": [
            "Recording experiments, parameters, metrics, and model results",
            "Tracking only computer temperature",
            "Deleting failed experiments",
            "Replacing model weights manually"
        ],
        "answer": 1
    },

    {
        "id": 158,
        "topic": "mlops",
        "difficulty": "medium",
        "question": "Why are automated tests useful in ML systems?",
        "options": [
            "They help detect problems in code, data processing, and model pipelines",
            "They guarantee perfect predictions",
            "They eliminate the need for data",
            "They make all models identical"
        ],
        "answer": 1
    },

    {
        "id": 159,
        "topic": "mlops",
        "difficulty": "medium",
        "question": "What is a model registry?",
        "options": [
            "A system for managing and tracking model versions",
            "A list of Python keywords",
            "A GPU driver",
            "An image database only"
        ],
        "answer": 1
    },

    {
        "id": 160,
        "topic": "mlops",
        "difficulty": "hard",
        "question": "What is continuous training?",
        "options": [
            "Automatically retraining models when appropriate new data or conditions are available",
            "Training a model only once",
            "Removing old training data",
            "Running inference without a model"
        ],
        "answer": 1
    },

    {
        "id": 161,
        "topic": "mlops",
        "difficulty": "hard",
        "question": "Why is reproducibility important in ML?",
        "options": [
            "It helps teams reproduce experiments and understand how models were produced",
            "It prevents models from being deployed",
            "It eliminates all data",
            "It makes every model deterministic"
        ],
        "answer": 1
    },

    {
        "id": 162,
        "topic": "mlops",
        "difficulty": "hard",
        "question": "What is a typical MLOps pipeline concerned with?",
        "options": [
            "Data, training, evaluation, deployment, monitoring, and model updates",
            "Only writing Python syntax",
            "Only collecting images",
            "Only designing neural network diagrams"
        ],
        "answer": 1
    }

    
]

# --------------------------------
# SHUFFLE QUESTION OPTIONS
# --------------------------------

def shuffle_question_options():

    for question in question_bank:

        correct_answer = question["options"][
            question["answer"] - 1
        ]

        random.shuffle(
            question["options"]
        )

        question["answer"] = (
            question["options"].index(
                correct_answer
            ) + 1
        )

shuffle_question_options()        


# --------------------------------
# GET QUESTIONS BY TOPIC
# --------------------------------

def get_questions(topic):

    questions = []

    for question in question_bank:

        if question["topic"] == topic:

            questions.append(question)

    return questions

