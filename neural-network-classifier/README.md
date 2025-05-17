## [Neural Network from Scratch](Basic_neural.ipynb)

This Project/Assignment was given to me by "__TuteDude__". This project demonstrate the implementation of a __Neural Network from scratch__ using only "__NumpY__" and "__Matplotlib__", without any external machine learning libraries like TensorFLow or PyTorch. The network is trained to classify pixel-based bainary patterns representing the characters A, B,and C on a 5x6 grid. This project soldifies understanding of core neural network concepts such as forward propagation, back propagation, gradient descent, and weight optimization.

📌 __Project Overview__

- Implemented a 2-Layer neural network using NumPy to classify the letters A, B, and C bssed on pixel data.
- Images are represented as flattened 1D arrays from 5x6 grid (30 pixels).
- The model is trained through custom backpropagation logic.
- Sigmoid activation function is used for non-linearity.
- Optimized weights using gradient descent.
- Tracked loss reduction and accuracy improvement over epochs.

📝 __Approach and Methodology__

1. #### __Data Representation__
  - Each letter (A, B, C) is represented in a 5x6 grid as binary pixel patterns.
  - These pixel patterns are flattened into 1d arrays of size 30 to be fed into the neural network.

2. #### __Neural Network Architecture__
  - A simple 2-Layer network:
     - __input layer__ : 30 neurons(representing 30 pixels)
     - __Hidden Layer__: 15 neurons(chosen experimentally)
     - __Output Layer__: 3 neurons (one for each class A, B, C)

3. #### __Forward Propagation__
  - Input is multiplied by weights and passed through the sigmoid activation to introduce non-linearity.(Explaining the sigmoid in simple terms, the weighted values can come in any form of number but  what we need is to have a number that is betweeen the numbers 0 and 1, and the sigmoid funtion just does that. It sqiushes the whole number line in between the number 0 and 1 , the negative values are closer to 0 where as positive values are closer to 1).
  - The network computes intermediate values at the hidden layer and final values at the output layer.

4. #### __Backpropagation and Weight Updates__
  - Calculated the error between the prodicted output and actual labels.
  - Gradient of the loss were computed using the chain rule.
  - Weigths and biases were adjusted using the learning rate to minimize the loss.

5. #### __Loss Tracking and Visualization__
  - The loss was recorded at each epoch to monitor convergence.
  - Plotted loss vs. epochs to visualize the learning progress.
 
📊 __Analysis and Process__

- The neural network was able to distinguish between the letters A, B, and C with increasing accuracy over epochs.
- The sigmoid activation function helpled in mapping non-linear relationships effectively.
- Gradient descent successfully minimized the error, although carrful tuning of the learning rate was crucial.
- Overfitting was not an issue due to the simplicity of the dataset, but generalization to more characters would require adjustments.

🔍 __Key Findings__ 

- Learning Rate Sensitivity : Too high, and the model divergies; too low, and convergence is slow.
- Hidden Layer Neurons: Experimenting with the numbers of neurons layers impacted the speed of learning.
- Sigmoid Activation's Role : Allowed the network to learn non-linear mappings efficiently.
- Backpropagation Efficiency: Successfully adjusted weights to reduce loss consistently.

🚀 __Future Improvements__

- Extend the network to recognize more characters(D,E,F,etc.).
- Visualze weight adjustments and decision boundaries for deeper understanding.
