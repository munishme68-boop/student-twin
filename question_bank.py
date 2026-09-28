
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
    },

        # =========================
    # THERMODYNAMICS
    # =========================

    {
        "id": 163,
        "topic": "thermodynamics",
        "difficulty": "easy",
        "question": "What is the SI unit of temperature?",
        "options": ["Celsius", "Kelvin", "Fahrenheit", "Joule"],
        "answer": 2
    },

    {
        "id": 164,
        "topic": "thermodynamics",
        "difficulty": "easy",
        "question": "Which law of thermodynamics deals with conservation of energy?",
        "options": [
            "Zeroth law",
            "First law",
            "Second law",
            "Third law"
        ],
        "answer": 2
    },

    {
        "id": 165,
        "topic": "thermodynamics",
        "difficulty": "easy",
        "question": "What is the SI unit of pressure?",
        "options": ["Newton", "Joule", "Pascal", "Watt"],
        "answer": 3
    },

    {
        "id": 166,
        "topic": "thermodynamics",
        "difficulty": "easy",
        "question": "Which property does not depend on the amount of substance?",
        "options": [
            "Mass",
            "Volume",
            "Specific volume",
            "Total energy"
        ],
        "answer": 3
    },

    {
        "id": 167,
        "topic": "thermodynamics",
        "difficulty": "easy",
        "question": "What is heat transfer from a hotter body to a colder body?",
        "options": [
            "Work",
            "Heat transfer",
            "Mass transfer",
            "Compression"
        ],
        "answer": 2
    },

    {
        "id": 168,
        "topic": "thermodynamics",
        "difficulty": "medium",
        "question": "For an ideal gas, which equation relates pressure, volume, temperature and amount of gas?",
        "options": [
            "PV = mgh",
            "PV = nRT",
            "P = ρgh",
            "Q = mc"
        ],
        "answer": 2
    },

    {
        "id": 169,
        "topic": "thermodynamics",
        "difficulty": "medium",
        "question": "What happens to the temperature of an ideal gas during an isothermal process?",
        "options": [
            "It remains constant",
            "It always increases",
            "It always decreases",
            "It becomes zero"
        ],
        "answer": 1
    },

    {
        "id": 170,
        "topic": "thermodynamics",
        "difficulty": "medium",
        "question": "In an adiabatic process, which quantity is zero?",
        "options": [
            "Pressure",
            "Temperature",
            "Heat transfer",
            "Work"
        ],
        "answer": 3
    },

    {
        "id": 171,
        "topic": "thermodynamics",
        "difficulty": "medium",
        "question": "What does entropy measure in thermodynamics?",
        "options": [
            "Only pressure",
            "Energy disorder or energy dispersal",
            "Only volume",
            "Mass of a system"
        ],
        "answer": 2
    },

    {
        "id": 172,
        "topic": "thermodynamics",
        "difficulty": "medium",
        "question": "Which thermodynamic process occurs at constant pressure?",
        "options": [
            "Isochoric",
            "Isothermal",
            "Isobaric",
            "Adiabatic"
        ],
        "answer": 3
    },

    {
        "id": 173,
        "topic": "thermodynamics",
        "difficulty": "hard",
        "question": "For a reversible process, the change in entropy can be expressed as:",
        "options": [
            "dS = δQ_rev / T",
            "dS = T / δQ_rev",
            "dS = P dV",
            "dS = V dP"
        ],
        "answer": 1
    },

    {
        "id": 174,
        "topic": "thermodynamics",
        "difficulty": "hard",
        "question": "For an ideal gas, internal energy is primarily a function of:",
        "options": [
            "Pressure only",
            "Volume only",
            "Temperature only",
            "Pressure and volume independently"
        ],
        "answer": 3
    },

    {
        "id": 175,
        "topic": "thermodynamics",
        "difficulty": "hard",
        "question": "What does the second law of thermodynamics establish?",
        "options": [
            "Conservation of mass only",
            "Direction of natural processes and entropy behavior",
            "Absolute zero temperature",
            "The ideal gas equation"
        ],
        "answer": 2
    },

    {
        "id": 176,
        "topic": "thermodynamics",
        "difficulty": "hard",
        "question": "The coefficient of performance of a refrigerator is defined as:",
        "options": [
            "Work input / refrigeration effect",
            "Refrigeration effect / work input",
            "Heat rejected / work output",
            "Work output / heat supplied"
        ],
        "answer": 2
    },

    {
        "id": 177,
        "topic": "thermodynamics",
        "difficulty": "hard",
        "question": "For a Carnot engine operating between temperatures T_H and T_L, its thermal efficiency is:",
        "options": [
            "1 - T_L/T_H",
            "1 - T_H/T_L",
            "T_H/T_L",
            "T_L/T_H"
        ],
        "answer": 1
    },


    # =========================
    # FLUID MECHANICS
    # =========================

    {
        "id": 178,
        "topic": "fluid_mechanics",
        "difficulty": "easy",
        "question": "What is the SI unit of dynamic viscosity?",
        "options": [
            "Pa·s",
            "N",
            "m/s",
            "J"
        ],
        "answer": 1
    },

    {
        "id": 179,
        "topic": "fluid_mechanics",
        "difficulty": "easy",
        "question": "What is density defined as?",
        "options": [
            "Mass per unit volume",
            "Volume per unit mass",
            "Force per unit area",
            "Mass per unit area"
        ],
        "answer": 1
    },

    {
        "id": 180,
        "topic": "fluid_mechanics",
        "difficulty": "easy",
        "question": "Which instrument is commonly used to measure pressure?",
        "options": [
            "Thermometer",
            "Manometer",
            "Hygrometer",
            "Calorimeter"
        ],
        "answer": 2
    },

    {
        "id": 181,
        "topic": "fluid_mechanics",
        "difficulty": "easy",
        "question": "A fluid at rest is called a:",
        "options": [
            "Dynamic fluid",
            "Static fluid",
            "Ideal gas",
            "Turbulent fluid"
        ],
        "answer": 2
    },

    {
        "id": 182,
        "topic": "fluid_mechanics",
        "difficulty": "easy",
        "question": "What does pressure represent?",
        "options": [
            "Force per unit area",
            "Mass per unit volume",
            "Energy per unit mass",
            "Velocity per unit time"
        ],
        "answer": 1
    },

    {
        "id": 183,
        "topic": "fluid_mechanics",
        "difficulty": "medium",
        "question": "What does the continuity equation represent for steady incompressible flow?",
        "options": [
            "Conservation of mass",
            "Conservation of temperature",
            "Conservation of viscosity",
            "Conservation of entropy"
        ],
        "answer": 1
    },

    {
        "id": 184,
        "topic": "fluid_mechanics",
        "difficulty": "medium",
        "question": "Bernoulli's equation is based primarily on conservation of:",
        "options": [
            "Mass",
            "Energy",
            "Temperature",
            "Viscosity"
        ],
        "answer": 2
    },

    {
        "id": 185,
        "topic": "fluid_mechanics",
        "difficulty": "medium",
        "question": "What does Reynolds number help determine?",
        "options": [
            "Fluid color",
            "Flow regime",
            "Fluid temperature",
            "Pipe material"
        ],
        "answer": 2
    },

    {
        "id": 186,
        "topic": "fluid_mechanics",
        "difficulty": "medium",
        "question": "In a horizontal pipe, if the flow velocity increases, the pressure generally:",
        "options": [
            "Increases",
            "Decreases",
            "Always becomes zero",
            "Remains exactly unchanged"
        ],
        "answer": 2
    },

    {
        "id": 187,
        "topic": "fluid_mechanics",
        "difficulty": "medium",
        "question": "Which force is mainly responsible for surface tension?",
        "options": [
            "Gravitational force",
            "Cohesive molecular forces",
            "Magnetic force",
            "Centrifugal force"
        ],
        "answer": 2
    },

    {
        "id": 188,
        "topic": "fluid_mechanics",
        "difficulty": "hard",
        "question": "For incompressible steady one-dimensional flow, the continuity equation is:",
        "options": [
            "A₁V₁ = A₂V₂",
            "P₁V₁ = P₂V₂",
            "P₁/A₁ = P₂/A₂",
            "V₁/V₂ = A₁A₂"
        ],
        "answer": 1
    },

    {
        "id": 189,
        "topic": "fluid_mechanics",
        "difficulty": "hard",
        "question": "What is the Reynolds number defined as?",
        "options": [
            "ρVD/μ",
            "μVD/ρ",
            "ρμ/VD",
            "VD/ρμ"
        ],
        "answer": 1
    },

    {
        "id": 190,
        "topic": "fluid_mechanics",
        "difficulty": "hard",
        "question": "For fully developed laminar flow through a circular pipe, the velocity profile is:",
        "options": [
            "Uniform",
            "Parabolic",
            "Sinusoidal",
            "Exponential"
        ],
        "answer": 2
    },

    {
        "id": 191,
        "topic": "fluid_mechanics",
        "difficulty": "hard",
        "question": "What does cavitation occur when local fluid pressure falls below?",
        "options": [
            "Atmospheric pressure only",
            "Vapor pressure of the liquid",
            "Critical pressure of air",
            "Zero pressure"
        ],
        "answer": 2
    },

    {
        "id": 192,
        "topic": "fluid_mechanics",
        "difficulty": "hard",
        "question": "In Bernoulli's equation, pressure head has the dimensions of:",
        "options": [
            "Velocity",
            "Length",
            "Mass",
            "Time"
        ],
        "answer": 2
    },


    # =========================
    # ROS 2
    # =========================

    {
        "id": 193,
        "topic": "ros",
        "difficulty": "easy",
        "question": "What does ROS stand for?",
        "options": [
            "Robot Operating System",
            "Robotic Output Service",
            "Remote Operating Software",
            "Robot Object Structure"
        ],
        "answer": 1
    },

    {
        "id": 194,
        "topic": "ros",
        "difficulty": "easy",
        "question": "What is a node in ROS 2?",
        "options": [
            "A physical sensor only",
            "A process that performs a specific task",
            "A type of battery",
            "A robot wheel"
        ],
        "answer": 2
    },

    {
        "id": 195,
        "topic": "ros",
        "difficulty": "easy",
        "question": "Which communication mechanism is commonly used for continuous data streams in ROS 2?",
        "options": [
            "Topics",
            "Passwords",
            "Files only",
            "Serial numbers"
        ],
        "answer": 1
    },

    {
        "id": 196,
        "topic": "ros",
        "difficulty": "easy",
        "question": "Which language is commonly supported for ROS 2 programming?",
        "options": [
            "Python",
            "HTML only",
            "SQL only",
            "CSS only"
        ],
        "answer": 1
    },

    {
        "id": 197,
        "topic": "ros",
        "difficulty": "easy",
        "question": "What is a ROS 2 package?",
        "options": [
            "A collection of ROS-related files and software",
            "A physical box for a robot",
            "A type of sensor",
            "A battery management system"
        ],
        "answer": 1
    },

    {
        "id": 198,
        "topic": "ros",
        "difficulty": "medium",
        "question": "In ROS 2, what does a publisher do?",
        "options": [
            "Sends messages to a topic",
            "Only receives messages",
            "Compiles Python",
            "Controls battery voltage"
        ],
        "answer": 1
    },

    {
        "id": 199,
        "topic": "ros",
        "difficulty": "medium",
        "question": "In ROS 2, what does a subscriber do?",
        "options": [
            "Sends messages to a topic",
            "Receives messages from a topic",
            "Creates a Linux kernel",
            "Builds hardware circuits"
        ],
        "answer": 2
    },

    {
        "id": 200,
        "topic": "ros",
        "difficulty": "medium",
        "question": "Which ROS 2 command lists available topics?",
        "options": [
            "ros2 topic list",
            "ros2 node show",
            "ros2 package build",
            "ros2 topic create"
        ],
        "answer": 1
    },

    {
        "id": 201,
        "topic": "ros",
        "difficulty": "medium",
        "question": "Which ROS 2 command lists active nodes?",
        "options": [
            "ros2 node list",
            "ros2 topic list",
            "ros2 run list",
            "ros2 package list"
        ],
        "answer": 1
    },

    {
        "id": 202,
        "topic": "ros",
        "difficulty": "medium",
        "question": "What is the purpose of a ROS 2 service?",
        "options": [
            "Request-response communication",
            "Only continuous sensor streaming",
            "Storing images permanently",
            "Compiling the operating system"
        ],
        "answer": 1
    },

    {
        "id": 203,
        "topic": "ros",
        "difficulty": "hard",
        "question": "What is the main difference between a ROS 2 service and an action?",
        "options": [
            "An action supports long-running tasks with feedback and a result",
            "A service can only use Python",
            "An action cannot communicate between nodes",
            "A service always provides continuous feedback"
        ],
        "answer": 1
    },

    {
        "id": 204,
        "topic": "ros",
        "difficulty": "hard",
        "question": "Which tool is commonly used to build ROS 2 workspaces?",
        "options": [
            "colcon",
            "pip",
            "npm",
            "gcc-only"
        ],
        "answer": 1
    },

    {
        "id": 205,
        "topic": "ros",
        "difficulty": "hard",
        "question": "Which Python client library is commonly used to create ROS 2 nodes?",
        "options": [
            "rclpy",
            "numpy",
            "flask",
            "pandas"
        ],
        "answer": 1
    },

    {
        "id": 206,
        "topic": "ros",
        "difficulty": "hard",
        "question": "What is the purpose of a ROS 2 launch file?",
        "options": [
            "Start and configure multiple ROS nodes and related components",
            "Format a hard drive",
            "Train a neural network automatically",
            "Change the robot's physical dimensions"
        ],
        "answer": 1
    },

    {
        "id": 207,
        "topic": "ros",
        "difficulty": "hard",
        "question": "What is DDS primarily used for in ROS 2?",
        "options": [
            "Underlying data communication between ROS 2 nodes",
            "Computer graphics rendering",
            "Battery charging",
            "Mechanical manufacturing"
        ],
        "answer": 1
    },

    {
        "id": 208,
        "topic": 'python',
        "difficulty": 'easy',
        "question": 'Which data type stores an ordered, changeable collection in Python?',
        "options": [
            'List',
            'Tuple',
            'Set',
            'String',
        ],
        "answer": 1
    },

    {
        "id": 209,
        "topic": 'python',
        "difficulty": 'easy',
        "question": 'Which function returns the number of items in a Python collection?',
        "options": [
            'size()',
            'count()',
            'len()',
            'length()',
        ],
        "answer": 3
    },

    {
        "id": 210,
        "topic": 'python',
        "difficulty": 'medium',
        "question": 'What is the main purpose of a Python dictionary?',
        "options": [
            'Store key-value pairs',
            'Store only numbers',
            'Create loops',
            'Define classes',
        ],
        "answer": 1
    },

    {
        "id": 211,
        "topic": 'python',
        "difficulty": 'medium',
        "question": 'What does a list comprehension primarily provide?',
        "options": [
            'A compact way to create lists',
            'A way to compile Python',
            'A database connection',
            'A method for installing packages',
        ],
        "answer": 1
    },

    {
        "id": 212,
        "topic": 'python',
        "difficulty": 'hard',
        "question": 'What does the `try`/`except` structure handle?',
        "options": [
            'Exceptions',
            'Loops',
            'Imports',
            'Comments',
        ],
        "answer": 1
    },

    {
        "id": 213,
        "topic": 'python',
        "difficulty": 'hard',
        "question": 'What is the difference between `==` and `is` in Python?',
        "options": [
            '`==` compares values; `is` checks object identity',
            'Both always check identity',
            '`==` checks types only',
            '`is` performs arithmetic',
        ],
        "answer": 1
    },

    {
        "id": 214,
        "topic": 'machine_learning',
        "difficulty": 'easy',
        "question": 'Which type of learning uses labeled input-output examples?',
        "options": [
            'Supervised learning',
            'Unsupervised learning',
            'Reinforcement learning',
            'Random search',
        ],
        "answer": 1
    },

    {
        "id": 215,
        "topic": 'machine_learning',
        "difficulty": 'easy',
        "question": 'What is a feature in a machine-learning dataset?',
        "options": [
            'An input variable used by a model',
            'The final prediction only',
            'A model parameter after training',
            'A software license',
        ],
        "answer": 1
    },

    {
        "id": 216,
        "topic": 'machine_learning',
        "difficulty": 'medium',
        "question": 'Why is a validation set commonly used?',
        "options": [
            'To tune choices without using the final test set',
            'To replace all training data',
            'To store model code',
            'To increase the number of classes',
        ],
        "answer": 1
    },

    {
        "id": 217,
        "topic": 'machine_learning',
        "difficulty": 'medium',
        "question": 'What does regularization generally try to reduce?',
        "options": [
            'Overfitting',
            'Data collection',
            'Number of features to zero',
            'Training labels',
        ],
        "answer": 1
    },

    {
        "id": 218,
        "topic": 'machine_learning',
        "difficulty": 'hard',
        "question": 'Why can a decision tree overfit when it becomes very deep?',
        "options": [
            'It can memorize noise and specific training examples',
            'It cannot split data',
            'It always has high bias',
            'It ignores every feature',
        ],
        "answer": 1
    },

    {
        "id": 219,
        "topic": 'machine_learning',
        "difficulty": 'hard',
        "question": 'What is the purpose of cross-validation?',
        "options": [
            'Estimate generalization performance across multiple train-validation splits',
            'Guarantee 100% test accuracy',
            'Remove all missing values automatically',
            'Convert classification into regression',
        ],
        "answer": 1
    },

    {
        "id": 220,
        "topic": 'neural_networks',
        "difficulty": 'easy',
        "question": 'What is a weight in a neural network?',
        "options": [
            'A learned parameter multiplying an input',
            'A dataset row',
            'A loss value only',
            'A class label',
        ],
        "answer": 1
    },

    {
        "id": 221,
        "topic": 'neural_networks',
        "difficulty": 'easy',
        "question": 'What does a bias term allow a neuron to do?',
        "options": [
            'Shift its activation independently of the weighted inputs',
            'Store the training dataset',
            'Remove all nonlinearities',
            'Set the batch size',
        ],
        "answer": 1
    },

    {
        "id": 222,
        "topic": 'neural_networks',
        "difficulty": 'medium',
        "question": 'Why are nonlinear activation functions used?',
        "options": [
            'They let networks represent nonlinear relationships',
            'They remove the need for data',
            'They guarantee no overfitting',
            'They make all outputs binary',
        ],
        "answer": 1
    },

    {
        "id": 223,
        "topic": 'neural_networks',
        "difficulty": 'medium',
        "question": 'What is an epoch?',
        "options": [
            'One complete pass through the training data',
            'One neuron',
            'One test example',
            'One gradient value',
        ],
        "answer": 1
    },

    {
        "id": 224,
        "topic": 'neural_networks',
        "difficulty": 'hard',
        "question": 'Why can very large gradients be a problem?',
        "options": [
            'Updates can become unstable or excessively large',
            'The model cannot read labels',
            'The loss becomes exactly zero',
            'The input dimension becomes zero',
        ],
        "answer": 1
    },

    {
        "id": 225,
        "topic": 'neural_networks',
        "difficulty": 'hard',
        "question": 'What does backpropagation compute?',
        "options": [
            'Gradients of the loss with respect to parameters',
            'Only the final class label',
            'The number of training samples',
            'The test-set accuracy directly',
        ],
        "answer": 1
    },

    {
        "id": 226,
        "topic": 'convolution',
        "difficulty": 'easy',
        "question": 'In a convolution operation, what is a kernel?',
        "options": [
            'A small set of learnable weights applied locally',
            'A dataset name',
            'A training epoch',
            'A class label',
        ],
        "answer": 1
    },

    {
        "id": 227,
        "topic": 'convolution',
        "difficulty": 'easy',
        "question": 'What does stride control in convolution?',
        "options": [
            'How far the kernel moves between positions',
            'The number of classes',
            'The learning rate',
            'The loss function',
        ],
        "answer": 1
    },

    {
        "id": 228,
        "topic": 'convolution',
        "difficulty": 'medium',
        "question": 'What is padding used for in convolution?',
        "options": [
            'To control spatial size and border handling',
            'To increase the learning rate',
            'To remove channels',
            'To label images',
        ],
        "answer": 1
    },

    {
        "id": 229,
        "topic": 'convolution',
        "difficulty": 'medium',
        "question": 'If stride increases while other settings stay fixed, what usually happens to output spatial size?',
        "options": [
            'It decreases',
            'It always doubles',
            'It becomes infinite',
            'It stays exactly the same in every case',
        ],
        "answer": 1
    },

    {
        "id": 230,
        "topic": 'convolution',
        "difficulty": 'hard',
        "question": 'Why do convolutional filters help image models?',
        "options": [
            'They learn local spatial patterns using shared weights',
            'They assign a unique weight to every image pixel independently',
            'They remove all spatial information',
            'They require no training',
        ],
        "answer": 1
    },

    {
        "id": 231,
        "topic": 'convolution',
        "difficulty": 'hard',
        "question": 'What is receptive field in a convolutional network?',
        "options": [
            'The region of the input that can influence a unit',
            'The number of output classes',
            'The optimizer learning rate',
            'The number of epochs',
        ],
        "answer": 1
    },

    {
        "id": 232,
        "topic": 'cnn',
        "difficulty": 'easy',
        "question": 'What does CNN stand for?',
        "options": [
            'Convolutional Neural Network',
            'Continuous Neural Node',
            'Computed Network Number',
            'Central Numeric Network',
        ],
        "answer": 1
    },

    {
        "id": 233,
        "topic": 'cnn',
        "difficulty": 'easy',
        "question": 'Which type of data is a CNN especially suited for?',
        "options": [
            'Images and spatial grid data',
            'Only tabular salaries',
            'Only text labels',
            'Only scalar constants',
        ],
        "answer": 1
    },

    {
        "id": 234,
        "topic": 'cnn',
        "difficulty": 'medium',
        "question": 'What is pooling commonly used for in a CNN?',
        "options": [
            'Downsampling feature maps',
            'Increasing image file size',
            'Generating labels',
            'Replacing all convolutions',
        ],
        "answer": 1
    },

    {
        "id": 235,
        "topic": 'cnn',
        "difficulty": 'medium',
        "question": 'What does a feature map represent?',
        "options": [
            'Activations produced by filters over spatial locations',
            'The original image filename',
            'The training history only',
            'A list of class names',
        ],
        "answer": 1
    },

    {
        "id": 236,
        "topic": 'cnn',
        "difficulty": 'hard',
        "question": 'Why can pooling improve computational efficiency?',
        "options": [
            'It reduces spatial dimensions',
            'It increases every feature map dimension',
            'It removes all learned parameters',
            'It doubles image resolution',
        ],
        "answer": 1
    },

    {
        "id": 237,
        "topic": 'cnn',
        "difficulty": 'hard',
        "question": 'Why can CNNs generalize useful visual patterns across locations?',
        "options": [
            'Convolution uses shared filter weights across spatial positions',
            'Each pixel gets a completely unrelated model',
            'Pooling stores the original image',
            'The output has no spatial structure',
        ],
        "answer": 1
    },

    {
        "id": 238,
        "topic": 'probability',
        "difficulty": 'easy',
        "question": 'What is the probability of a certain event?',
        "options": [
            '1',
            '0',
            '-1',
            '2',
        ],
        "answer": 1
    },

    {
        "id": 239,
        "topic": 'probability',
        "difficulty": 'easy',
        "question": 'What is the probability of an impossible event?',
        "options": [
            '0',
            '1',
            '-1',
            '0.5',
        ],
        "answer": 1
    },

    {
        "id": 240,
        "topic": 'probability',
        "difficulty": 'medium',
        "question": 'If two events cannot occur together, what are they called?',
        "options": [
            'Mutually exclusive',
            'Independent',
            'Identical',
            'Continuous',
        ],
        "answer": 1
    },

    {
        "id": 241,
        "topic": 'probability',
        "difficulty": 'medium',
        "question": 'For independent events A and B, how is their joint probability computed?',
        "options": [
            'P(A)P(B)',
            'P(A)+P(B)',
            'P(A)-P(B)',
            'P(A)/P(B)',
        ],
        "answer": 1
    },

    {
        "id": 242,
        "topic": 'probability',
        "difficulty": 'hard',
        "question": 'What does conditional probability P(A|B) describe?',
        "options": [
            'Probability of A given that B has occurred',
            'Probability of B never occurring',
            'Probability of A and B being impossible',
            'Probability of A without any condition',
        ],
        "answer": 1
    },

    {
        "id": 243,
        "topic": 'probability',
        "difficulty": 'hard',
        "question": 'What does Bayes theorem allow you to compute?',
        "options": [
            'A posterior probability from related prior and likelihood information',
            'Only an arithmetic mean',
            'Only a variance',
            'Only a sample size',
        ],
        "answer": 1
    },

    {
        "id": 244,
        "topic": 'statistics',
        "difficulty": 'easy',
        "question": 'What does the mean represent?',
        "options": [
            'The arithmetic average',
            'The largest value',
            'The smallest value',
            'The middle value only',
        ],
        "answer": 1
    },

    {
        "id": 245,
        "topic": 'statistics',
        "difficulty": 'easy',
        "question": 'What does the median represent?',
        "options": [
            'The middle ordered value or midpoint of two middle values',
            'The most frequent value only',
            'The total of all values',
            'The range',
        ],
        "answer": 1
    },

    {
        "id": 246,
        "topic": 'statistics',
        "difficulty": 'medium',
        "question": 'Which quantity is measured by standard deviation?',
        "options": [
            'Spread of values around the mean',
            'Number of observations only',
            'The maximum value',
            'The sample label',
        ],
        "answer": 1
    },

    {
        "id": 247,
        "topic": 'statistics',
        "difficulty": 'medium',
        "question": 'What does a correlation coefficient near zero indicate?',
        "options": [
            'Little linear association',
            'Perfect positive linear association',
            'Perfect negative linear association',
            'Equal means',
        ],
        "answer": 1
    },

    {
        "id": 248,
        "topic": 'statistics',
        "difficulty": 'hard',
        "question": 'Why is a sample used instead of a population in many studies?',
        "options": [
            'The whole population may be too large or costly to measure',
            'A sample always contains every individual',
            'A sample has no uncertainty',
            'Population data are always invalid',
        ],
        "answer": 1
    },

    {
        "id": 249,
        "topic": 'statistics',
        "difficulty": 'hard',
        "question": 'What does a confidence interval communicate?',
        "options": [
            'A range produced by a statistical procedure to reflect uncertainty about a population parameter',
            'The exact value of every observation',
            'A guarantee that the parameter is inside',
            'Only the sample maximum',
        ],
        "answer": 1
    },

    {
        "id": 250,
        "topic": 'rnn',
        "difficulty": 'easy',
        "question": 'Which expansion is correct for the acronym RNN?',
        "options": [
            'Recurrent Neural Network',
            'Random Numeric Network',
            'Recursive Normal Node',
            'Reduced Neural Number',
        ],
        "answer": 1
    },

    {
        "id": 251,
        "topic": 'rnn',
        "difficulty": 'easy',
        "question": 'What is a key idea in an RNN?',
        "options": [
            'Using a hidden state to carry information across sequence steps',
            'Ignoring previous inputs',
            'Using no trainable parameters',
            'Processing only unordered data',
        ],
        "answer": 1
    },

    {
        "id": 252,
        "topic": 'rnn',
        "difficulty": 'medium',
        "question": 'RNNs are commonly applied to which kind of data?',
        "options": [
            'Sequences',
            'Only static images',
            'Only database schemas',
            'Only isolated constants',
        ],
        "answer": 1
    },

    {
        "id": 253,
        "topic": 'rnn',
        "difficulty": 'medium',
        "question": 'What difficulty can basic RNNs face over long sequences?',
        "options": [
            'Vanishing or exploding gradients',
            'No input values',
            'Too many image channels',
            'No hidden state',
        ],
        "answer": 1
    },

    {
        "id": 254,
        "topic": 'rnn',
        "difficulty": 'hard',
        "question": 'Why does an RNN hidden state matter?',
        "options": [
            'It provides a representation influenced by earlier sequence elements',
            'It stores only the final label',
            'It replaces the optimizer',
            'It removes sequence order',
        ],
        "answer": 1
    },

    {
        "id": 255,
        "topic": 'rnn',
        "difficulty": 'hard',
        "question": 'What is truncated backpropagation through time used for?',
        "options": [
            'Limiting the number of time steps used for gradient propagation',
            'Increasing image resolution',
            'Removing recurrent connections',
            'Changing labels into features',
        ],
        "answer": 1
    },

    {
        "id": 256,
        "topic": 'lstm',
        "difficulty": 'easy',
        "question": 'Which expansion is correct for the acronym LSTM?',
        "options": [
            'Long Short-Term Memory',
            'Long Sequence Training Model',
            'Linear State Transfer Machine',
            'Local Short Tensor Method',
        ],
        "answer": 1
    },

    {
        "id": 257,
        "topic": 'lstm',
        "difficulty": 'easy',
        "question": 'Why was LSTM designed?',
        "options": [
            'To help neural networks retain useful information over longer sequences',
            'To classify only static images',
            'To remove all memory from an RNN',
            'To replace datasets',
        ],
        "answer": 1
    },

    {
        "id": 258,
        "topic": 'lstm',
        "difficulty": 'medium',
        "question": 'Which component helps an LSTM control information flow?',
        "options": [
            'Gates',
            'Pooling layers',
            'Decision trees',
            'Kernels only',
        ],
        "answer": 1
    },

    {
        "id": 259,
        "topic": 'lstm',
        "difficulty": 'medium',
        "question": 'What does the forget gate mainly control?',
        "options": [
            'What information from the cell state should be discarded',
            'The number of classes',
            'The image size',
            'The optimizer type',
        ],
        "answer": 1
    },

    {
        "id": 260,
        "topic": 'lstm',
        "difficulty": 'hard',
        "question": 'What does the input gate help control?',
        "options": [
            'What new information is written to the cell state',
            'Which test examples are removed',
            'The batch count only',
            'The vocabulary size directly',
        ],
        "answer": 1
    },

    {
        "id": 261,
        "topic": 'lstm',
        "difficulty": 'hard',
        "question": 'Why can LSTM reduce the vanishing-gradient problem compared with a basic RNN?',
        "options": [
            'Its gated cell-state pathway can preserve information and gradients over longer spans',
            'It has no nonlinearities',
            'It never uses gradients',
            'It has no recurrent connections',
        ],
        "answer": 1
    },

    {
        "id": 262,
        "topic": 'natural_language_processing',
        "difficulty": 'easy',
        "question": 'Which expansion is correct for the acronym NLP?',
        "options": [
            'Natural Language Processing',
            'Neural Learning Program',
            'Numeric Language Prediction',
            'Natural Logic Protocol',
        ],
        "answer": 1
    },

    {
        "id": 263,
        "topic": 'natural_language_processing',
        "difficulty": 'easy',
        "question": 'What is tokenization?',
        "options": [
            'Splitting text into smaller units such as words or subwords',
            'Deleting every word',
            'Translating text to images',
            'Sorting documents alphabetically',
        ],
        "answer": 1
    },

    {
        "id": 264,
        "topic": 'natural_language_processing',
        "difficulty": 'medium',
        "question": 'What is named entity recognition used for?',
        "options": [
            'Identifying entities such as people, places, and organizations',
            'Counting only punctuation',
            'Generating random text',
            'Removing all nouns',
        ],
        "answer": 1
    },

    {
        "id": 265,
        "topic": 'natural_language_processing',
        "difficulty": 'medium',
        "question": 'What is part-of-speech tagging?',
        "options": [
            'Assigning grammatical categories to tokens',
            'Encrypting text',
            'Counting documents',
            'Creating images',
        ],
        "answer": 1
    },

    {
        "id": 266,
        "topic": 'natural_language_processing',
        "difficulty": 'hard',
        "question": 'Why is text normalization useful?',
        "options": [
            'It makes textual forms more consistent for downstream processing',
            'It guarantees perfect translation',
            'It removes all meaning',
            'It always increases vocabulary size',
        ],
        "answer": 1
    },

    {
        "id": 267,
        "topic": 'natural_language_processing',
        "difficulty": 'hard',
        "question": 'What is word sense disambiguation?',
        "options": [
            'Choosing the intended meaning of a word from its context',
            'Splitting words into characters only',
            'Removing stopwords only',
            'Counting word frequency',
        ],
        "answer": 1
    },

    {
        "id": 268,
        "topic": 'word_embeddings',
        "difficulty": 'easy',
        "question": 'Which statement best describes a word embedding?',
        "options": [
            'A numerical vector representation of a word or token',
            'A grammar rule only',
            'An image file',
            'A database password',
        ],
        "answer": 1
    },

    {
        "id": 269,
        "topic": 'word_embeddings',
        "difficulty": 'easy',
        "question": 'What is a useful property of many word embeddings?',
        "options": [
            'Semantically related words can have similar vector representations',
            'Every word must have the same vector',
            'They contain no numerical values',
            'They work only for punctuation',
        ],
        "answer": 1
    },

    {
        "id": 270,
        "topic": 'word_embeddings',
        "difficulty": 'medium',
        "question": 'What does Word2Vec learn?',
        "options": [
            'Vector representations from word-context relationships',
            'Only document lengths',
            'Only punctuation positions',
            'Image filters',
        ],
        "answer": 1
    },

    {
        "id": 271,
        "topic": 'word_embeddings',
        "difficulty": 'medium',
        "question": 'What is a limitation of basic static word embeddings?',
        "options": [
            'A word generally has one vector even when its meaning changes by context',
            'They cannot be stored numerically',
            'They always require images',
            'They contain no semantic information',
        ],
        "answer": 1
    },

    {
        "id": 272,
        "topic": 'word_embeddings',
        "difficulty": 'hard',
        "question": 'Why are embeddings useful as model inputs?',
        "options": [
            'They convert discrete tokens into continuous numerical representations',
            'They remove the need for any model',
            'They guarantee correct predictions',
            'They eliminate sequence order',
        ],
        "answer": 1
    },

    {
        "id": 273,
        "topic": 'word_embeddings',
        "difficulty": 'hard',
        "question": 'How do contextual embeddings differ from static embeddings?',
        "options": [
            'Their representation can depend on surrounding context',
            'They cannot represent words numerically',
            'They are always one-hot vectors',
            'They contain only word length',
        ],
        "answer": 1
    },

    {
        "id": 274,
        "topic": 'transformers',
        "difficulty": 'easy',
        "question": 'What is a key component of the Transformer architecture?',
        "options": [
            'Self-attention',
            'Decision trees',
            'Pooling only',
            'K-means clustering',
        ],
        "answer": 1
    },

    {
        "id": 275,
        "topic": 'transformers',
        "difficulty": 'easy',
        "question": 'What does self-attention help a token do?',
        "options": [
            'Use information from other tokens in the sequence',
            'Ignore all other tokens',
            'Change the dataset labels',
            'Remove the vocabulary',
        ],
        "answer": 1
    },

    {
        "id": 276,
        "topic": 'transformers',
        "difficulty": 'medium',
        "question": 'Why are positional encodings or position information used?',
        "options": [
            'To provide information about token order',
            'To reduce all tokens to one number',
            'To label images',
            'To calculate accuracy',
        ],
        "answer": 1
    },

    {
        "id": 277,
        "topic": 'transformers',
        "difficulty": 'medium',
        "question": 'In a Transformer, what is meant by multi-head attention?',
        "options": [
            'Several attention mechanisms operating in parallel with different learned projections',
            'Several datasets merged without learning',
            'Multiple loss functions added randomly',
            'A method that removes token order',
        ],
        "answer": 1
    },

    {
        "id": 278,
        "topic": 'transformers',
        "difficulty": 'hard',
        "question": 'Why can Transformers process sequence tokens in parallel during training more readily than standard RNNs?',
        "options": [
            'Self-attention does not require processing tokens strictly one step after another',
            'Transformers have no parameters',
            'RNNs cannot process text',
            'Transformers use no matrix operations',
        ],
        "answer": 1
    },

    {
        "id": 279,
        "topic": 'transformers',
        "difficulty": 'hard',
        "question": 'What is the purpose of a Transformer feed-forward sublayer?',
        "options": [
            'To apply learned nonlinear transformations independently to each position after attention',
            'To store the entire dataset permanently',
            'To replace all attention heads',
            'To perform database indexing',
        ],
        "answer": 1
    },

    {
        "id": 280,
        "topic": 'image_classification',
        "difficulty": 'easy',
        "question": 'Which task is called image classification?',
        "options": [
            'Assigning an image to one or more predefined classes',
            'Detecting every object location only',
            'Compressing an image file',
            'Changing image brightness',
        ],
        "answer": 1
    },

    {
        "id": 281,
        "topic": 'image_classification',
        "difficulty": 'easy',
        "question": 'What is a label in image classification?',
        "options": [
            'The target class associated with an image',
            'The image width',
            'The optimizer',
            'A convolution kernel',
        ],
        "answer": 1
    },

    {
        "id": 282,
        "topic": 'image_classification',
        "difficulty": 'medium',
        "question": 'What is data augmentation?',
        "options": [
            'Creating varied training examples through transformations of existing data',
            'Deleting training images',
            'Changing labels randomly every time',
            'Removing all pixels',
        ],
        "answer": 1
    },

    {
        "id": 283,
        "topic": 'image_classification',
        "difficulty": 'medium',
        "question": 'Why is a separate test set used?',
        "options": [
            'To evaluate performance on data not used for fitting or tuning',
            'To increase training labels',
            'To guarantee perfect accuracy',
            'To store model weights',
        ],
        "answer": 1
    },

    {
        "id": 284,
        "topic": 'image_classification',
        "difficulty": 'hard',
        "question": 'What does top-1 accuracy measure?',
        "options": [
            'Whether the highest-scoring predicted class matches the true class',
            'Whether any class appears in the dataset',
            'The number of layers',
            'The training time',
        ],
        "answer": 1
    },

    {
        "id": 285,
        "topic": 'image_classification',
        "difficulty": 'hard',
        "question": 'Why can class imbalance affect image classification?',
        "options": [
            'A model may be biased toward classes with many training examples',
            'All classes become equally represented automatically',
            'Images lose their pixels',
            'The optimizer stops working',
        ],
        "answer": 1
    },

    {
        "id": 286,
        "topic": 'object_detection',
        "difficulty": 'easy',
        "question": 'Which task is called object detection?',
        "options": [
            'Finding objects and their locations in an image',
            'Assigning one label to an entire dataset',
            'Removing image backgrounds only',
            'Compressing images',
        ],
        "answer": 1
    },

    {
        "id": 287,
        "topic": 'object_detection',
        "difficulty": 'easy',
        "question": 'In object detection, what does a bounding box specify?',
        "options": [
            'The location and extent of a detected object',
            'The model learning rate',
            'A class vocabulary',
            'The image file size',
        ],
        "answer": 1
    },

    {
        "id": 288,
        "topic": 'object_detection',
        "difficulty": 'medium',
        "question": 'What does IoU compare?',
        "options": [
            'Overlap between predicted and ground-truth bounding boxes',
            'Training and test accuracy',
            'Two learning rates',
            'Two class names',
        ],
        "answer": 1
    },

    {
        "id": 289,
        "topic": 'object_detection',
        "difficulty": 'medium',
        "question": 'Why is non-maximum suppression used?',
        "options": [
            'To reduce multiple overlapping detections of the same object',
            'To increase the number of duplicate boxes',
            'To normalize image colors',
            'To train word embeddings',
        ],
        "answer": 1
    },

    {
        "id": 290,
        "topic": 'object_detection',
        "difficulty": 'hard',
        "question": 'What is a confidence score in object detection?',
        "options": [
            'A model-estimated confidence that a detection corresponds to an object/class',
            'The exact physical size of the object',
            'The image resolution',
            'The number of training epochs',
        ],
        "answer": 1
    },

    {
        "id": 291,
        "topic": 'object_detection',
        "difficulty": 'hard',
        "question": 'Why can small objects be difficult to detect?',
        "options": [
            'Their visual features may occupy very few pixels and be lost during downsampling',
            'They always have no labels',
            'They cannot be represented by CNNs',
            'They have infinite resolution',
        ],
        "answer": 1
    },

    {
        "id": 292,
        "topic": 'generative_ai',
        "difficulty": 'easy',
        "question": 'What is generative AI designed to do?',
        "options": [
            'Generate new content such as text, images, audio, or code',
            'Only sort databases',
            'Only detect objects',
            'Only calculate averages',
        ],
        "answer": 1
    },

    {
        "id": 293,
        "topic": 'generative_ai',
        "difficulty": 'easy',
        "question": 'Which is an example of generative AI output?',
        "options": [
            'A newly generated paragraph',
            'A fixed database schema',
            'A temperature sensor reading',
            'A manually entered ID',
        ],
        "answer": 1
    },

    {
        "id": 294,
        "topic": 'generative_ai',
        "difficulty": 'medium',
        "question": 'What does a generative model learn to represent?',
        "options": [
            'Patterns or distributions that can be used to produce new samples',
            'Only the names of users',
            'Only hardware temperatures',
            'Only file extensions',
        ],
        "answer": 1
    },

    {
        "id": 295,
        "topic": 'generative_ai',
        "difficulty": 'medium',
        "question": 'What is a common risk when generative models produce plausible but false information?',
        "options": [
            'Hallucination or factual error',
            'Guaranteed correctness',
            'Zero variability',
            'Automatic source verification',
        ],
        "answer": 1
    },

    {
        "id": 296,
        "topic": 'generative_ai',
        "difficulty": 'hard',
        "question": 'What does temperature commonly control in text generation?',
        "options": [
            'Randomness or diversity of token selection',
            'The physical CPU temperature',
            'The vocabulary size only',
            'The model parameter count',
        ],
        "answer": 1
    },

    {
        "id": 297,
        "topic": 'generative_ai',
        "difficulty": 'hard',
        "question": 'Why can retrieval-augmented generation improve factual grounding?',
        "options": [
            'It supplies retrieved external information to the generation process',
            'It removes all model parameters',
            'It guarantees every retrieved source is correct',
            'It prevents any generation',
        ],
        "answer": 1
    },

    {
        "id": 298,
        "topic": 'large_language_models',
        "difficulty": 'easy',
        "question": 'Which expansion is correct for the acronym LLM?',
        "options": [
            'Large Language Model',
            'Long Learning Machine',
            'Language Logic Module',
            'Large Linear Memory',
        ],
        "answer": 1
    },

    {
        "id": 299,
        "topic": 'large_language_models',
        "difficulty": 'easy',
        "question": 'What is an LLM primarily trained to model?',
        "options": [
            'Patterns in sequences of language tokens',
            'Only image edges',
            'Only database tables',
            'Only sensor voltages',
        ],
        "answer": 1
    },

    {
        "id": 300,
        "topic": 'large_language_models',
        "difficulty": 'medium',
        "question": 'What is a token in an LLM?',
        "options": [
            'A unit of text processed by the model',
            'A hardware component',
            'A database table',
            'A class label only',
        ],
        "answer": 1
    },

    {
        "id": 301,
        "topic": 'large_language_models',
        "difficulty": 'medium',
        "question": 'What is pretraining?',
        "options": [
            'Learning general patterns from a large corpus before later task-specific adaptation',
            'Testing only on one example',
            'Deleting model weights',
            'Manually writing every response',
        ],
        "answer": 1
    },

    {
        "id": 302,
        "topic": 'large_language_models',
        "difficulty": 'hard',
        "question": 'In machine learning, what is fine-tuning?',
        "options": [
            'Further training a pretrained model on a targeted dataset or task',
            'Compressing a model into a zip file',
            'Removing all attention layers',
            'Changing only the user interface',
        ],
        "answer": 1
    },

    {
        "id": 303,
        "topic": 'large_language_models',
        "difficulty": 'hard',
        "question": 'Why can LLMs require substantial computing resources?',
        "options": [
            'They can contain many parameters and process large amounts of data',
            'They contain no numerical operations',
            'They never use matrix multiplication',
            'They work only on paper',
        ],
        "answer": 1
    },

    {
        "id": 304,
        "topic": 'model_deployment',
        "difficulty": 'easy',
        "question": 'What does model deployment mean?',
        "options": [
            'Making a trained model available for use in a real application',
            'Training a model without data',
            'Deleting a trained model',
            'Only changing a model name',
        ],
        "answer": 1
    },

    {
        "id": 305,
        "topic": 'model_deployment',
        "difficulty": 'easy',
        "question": 'In model deployment, what is an API commonly used for?',
        "options": [
            'Allowing software to send inputs to and receive outputs from a model service',
            'Storing images only',
            'Replacing the operating system',
            'Calculating exam marks manually',
        ],
        "answer": 1
    },

    {
        "id": 306,
        "topic": 'model_deployment',
        "difficulty": 'medium',
        "question": 'In a deployed model, what is inference?',
        "options": [
            'Using a trained model to produce predictions on new inputs',
            'Training from scratch only',
            'Deleting predictions',
            'Collecting labels manually',
        ],
        "answer": 1
    },

    {
        "id": 307,
        "topic": 'model_deployment',
        "difficulty": 'medium',
        "question": 'Why is input validation important in a deployed ML service?',
        "options": [
            'It helps reject malformed or unexpected inputs before model processing',
            'It guarantees perfect predictions',
            'It increases the model parameter count',
            'It removes the need for monitoring',
        ],
        "answer": 1
    },

    {
        "id": 308,
        "topic": 'model_deployment',
        "difficulty": 'hard',
        "question": 'What is model latency?',
        "options": [
            'The time taken to produce a response or prediction',
            'The number of model classes',
            'The training dataset size',
            'The model accuracy',
        ],
        "answer": 1
    },

    {
        "id": 309,
        "topic": 'model_deployment',
        "difficulty": 'hard',
        "question": 'Why is model monitoring needed after deployment?',
        "options": [
            'Data and model behavior can change over time, affecting performance',
            'A deployed model never changes context',
            'Monitoring replaces all testing',
            'It guarantees zero failures',
        ],
        "answer": 1
    },

    {
        "id": 310,
        "topic": 'mlops',
        "difficulty": 'easy',
        "question": 'What does MLOps combine?',
        "options": [
            'Machine learning practices with software engineering and operations',
            'Only hardware repair',
            'Only data entry',
            'Only UI design',
        ],
        "answer": 1
    },

    {
        "id": 311,
        "topic": 'mlops',
        "difficulty": 'easy',
        "question": 'What is version control used for in ML projects?',
        "options": [
            'Tracking changes to code and other project artifacts',
            'Increasing GPU memory',
            'Replacing model evaluation',
            'Removing all datasets',
        ],
        "answer": 1
    },

    {
        "id": 312,
        "topic": 'mlops',
        "difficulty": 'medium',
        "question": 'In MLOps, what is the purpose of a model registry?',
        "options": [
            'A system for storing and managing model versions and metadata',
            'A list of programming keywords',
            'A GPU driver',
            'A database of keyboard shortcuts',
        ],
        "answer": 1
    },

    {
        "id": 313,
        "topic": 'mlops',
        "difficulty": 'medium',
        "question": 'Why are reproducible ML pipelines valuable?',
        "options": [
            'They make data processing, training, and evaluation more repeatable',
            'They guarantee the same real-world data forever',
            'They remove the need for testing',
            'They prevent model updates',
        ],
        "answer": 1
    },

    {
        "id": 314,
        "topic": 'mlops',
        "difficulty": 'hard',
        "question": 'In MLOps, what does data drift mean?',
        "options": [
            'A change in the distribution of input data over time',
            'A change in Python syntax',
            'A faster GPU',
            'A reduction in model file size',
        ],
        "answer": 1
    },

    {
        "id": 315,
        "topic": 'mlops',
        "difficulty": 'hard',
        "question": 'What is CI/CD useful for in MLOps?',
        "options": [
            'Automating integration, testing, and delivery/deployment workflows',
            'Only labeling images manually',
            'Replacing all monitoring',
            'Increasing model randomness',
        ],
        "answer": 1
    },
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

