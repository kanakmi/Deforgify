# Deforgify

## 💡 Inspiration
Deep learning has had a lot of success with Generative Adversarial Networks (GANs) in recent times which are used to generate high-quality outputs that are comparable to the original inputs. GANs have been widely utilised to create new realistic pictures and to improve existing ones. On the other hand, GANs may be used to fool individuals by generating false data. Fake faces made by GANs, for example, may deceive not only humans but also machine learning classifiers. Synthetic photographs for identification and authentication purposes, for example, can be used maliciously.

Furthermore, advanced picture editing software such as Adobe Photoshop allows for the alteration of complicated input photographs as well as the creation of high-quality new images. These techniques have improved to the point that they can now build realistic and intricate false pictures that are difficult to distinguish from the genuine thing. YouTube has step-by-step directions and tutorials for making these sorts of fictitious graphics. As a result, these technologies have the potential to be utilised for defamation, impersonation, and factual distortion. Furthermore, with social media, fraudulent material may be swiftly and extensively shared on the Internet.


## 💻 What it does
Deforgify is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones. For instance, if someone takes your original image and inserts your face into a murder scene or photoshops it onto someone else's body, Deforgify will tag it as fake reducing the chances of it being used to smear you. <br>
Simply submit the image, and the machine learning model will evaluate it and provide a response in a fraction of a second.

## 🤖 Machine Learning Process

<img src="https://user-images.githubusercontent.com/54859521/156918096-1516ea9b-59c4-4ab6-a774-d6e660d76a84.png" align="right"  width="28%"/>
<h3> 📊 Getting the Data and EDA Process </h3>

*The dataset was taken from Kaggle and you can find it [here](https://www.kaggle.com/hamzaboulahia/hardfakevsrealfaces).* <br>

The Dataset contains 1288 faces out of which 
- 589 are Real 
- 700 are Fake

<br>

The "fake" faces collected in this dataset are generated using the StyleGAN2, which present a harder challenge to classify them correctly even for the human eye.

![image](https://user-images.githubusercontent.com/54859521/156918357-a2c60191-24f4-4bf1-a054-fb005f397968.png)
![image](https://user-images.githubusercontent.com/54859521/156918366-6a5e35e5-7f09-4784-978a-7e7db51649a1.png)

### ⚙️ Model Architecture

![image](https://user-images.githubusercontent.com/54859521/156918839-2a2f7296-5a9b-4700-8c60-e46b5edf4e87.png)

- We designed a Sequential Model having 5 Convolutional Layers and 4 Dense Layers.
- The first layer started with 32 filters and kernel of 2x2.
- The number of filters are doubled at every next layer and kernel is is incremented by 1.
- We introduced some Max Pooling Layers after Convolutional Layers to avoid over-fitting and reduce Computational Costs.
- The Output from Covolutional Layer is Flattened and passed over to Dense Layers.
- We started with 512 neurons in the first Dense layer and reduced them to half over the next two Dense layers.
- Some Dropout Layers were also introduced throught the model to randomly ignore some of the neurons and reduce over-fitting.
- We used ReLU activation in all layers except output layer to reduce computation cost and introduce non-linearity.
- Finally the Output Layer was constructed containing 3 neurons (1 for each class) and softmax activation.

### 🤩 Results
- The model with least Validation Loss was saved during the training and reloaded before obtaining the final results.
- The model was able to classify all of the samples correctly.

## 🧠 Challenges we ran into
After achieving 96% accuracy on the testing data initially, we were releaved thinking we have built something great that can correctly classify most of the fake images online. We decided to put it to the test by downloading more test images from Google, but the results were utterly unexpected. Six of the ten photos we evaluated were incorrectly categorised. We were so disappointed with the outcome that we decided to start over with a fresh dataset and a little different strategy, and it worked like magic.

## 🏅 Accomplishments that we're proud of
- Completing the Project in such short time frame
- Achieving a 100% accuracy on the test set (and 90% on different images from google)

## 📖 What we learned

## 🚀 What's next for Deforgify

## 🏃🏻‍♂️ Installing and Running Locally
