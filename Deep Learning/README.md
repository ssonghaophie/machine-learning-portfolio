
# **Image Classification**

## Introduction
My goal for this project is to classify the facial image of two main characters from an anime called Kuroko's Basketball correctly. The question to proceed with this idea was how we can use deep learning to classify an image data accurately and effectively. As the name of the task suggests, image classification is also a classification and thus a supervised learning. It will require us to fit the model and predict the class based on how well it was trained while learning with the "true" classes.

The data I'm using to achieve this task is a custom data collected by an individual, and it includes train and test sets of different face images of Kuroko and Kagami that were cropped from the anime. I aim to train a Convolutional Neural Network (CNN) model on the data and assess its performance on predicting the character in the test data.

## Approaches
While I was proceeding, I faced challenges regarding the running time of the model fitting. One interesting phenomenon I found was that when we are computing the convolutional layer in CNN, it takes longer time if we have bigger kernel size than when we have a smaller kernel. In my case, it took 223s to run one epoch when I set kernel size to 25, while it only took 10s to run one epoch when I set it as 3. I first chose to set a big kernel size because I thought that bigger kernel will result in less number of times to compute the dot product, and thus faster. However, after thinking it twice, it makes sense that smaller kernel makes the computation faster because there are less elementwise comparison to do each time it moves down the image.

I also had confusion about why sometimes the accuracy decreased and the loss increased when one more epoch was processed compare to the result from the previous epoch. However, I think one or two fluctuations are reasonable especially when there are not a lot of data like this case.

In the end, all of the train-validation accuracy and loss started to converge into a high and low value respectively, starting at around the eighth epoch. When I continued to run more epochs, both train-validation accuracy became 100% soon and continued to be 100%. This is quite impressive accuracy because it basically means that the model can predict the character correctly for 100% of the time. As a result, it wasn't surprising to see that the model correctly classified all of the characters in the test data.

## Conclusion
It was great to complete an image classification task successfully, because presenting the image data as the matrix of numbers sounds challenging at first because it's not what we've trained to think of as. This project helped me to understand what CNN is, and how I can apply it in classifying image data. For my next project, I would like to further investigate on how other settings for CNN layers can change the model accuracy. I also want to extend on this anime character thread to explore a way to generate new image from the information gained from the image data I have, known as Generative Adversarial Networks (GAN). This backward transition from supervised learning to an unsupervised learning sounds very interesting, although generating new data yields a lot of ethical cocerns regarding copyright, portrait right, challenges in distinguishing the real data from the fake one, etc. I aknowledge that I should be aware of these and clearly understand what I'm trying to do before I enter into this field.

### Resources

1) Data Source: https://github.com/developer0hye/Custom-CNN-based-Image-Classification-in-PyTorch
2) About loading custom image data in tensorflow: https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory
3) About CNN and neural layers: Lab 22 https://colab.research.google.com/drive/15ZWa44ow2bWmQOWMfjZeHAdXJFBx_jSR?usp=sharing#scrollTo=EMguodqFISRa
4) About Tensorflow built-in methods for using CNN: https://www.tensorflow.org/tutorials/images/cnn https://www.tensorflow.org/tutorials/images/classification
5) About optimizer: https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/#:~:text=Adam%20is%20a%20replacement%20optimization,sparse%20gradients%20on%20noisy%20problems
6) About accuracy and loss: https://datascience.stackexchange.com/questions/42599/what-is-the-relationship-between-the-accuracy-and-the-loss-in-deep-learning
