import streamlit as st
import plotly.express as px

def app():
    st.image('./Streamlit_UI/Header.gif', use_column_width=True)

    st.subheader("💡 Abstract:")

    inspiration = '''
    Deep learning has had a lot of success with Generative Adversarial Networks (GANs) in recent times which are used to generate high-quality outputs that are comparable to the original inputs. GANs have been widely utilised to create new realistic pictures and to improve existing ones. On the other hand, GANs may be used to fool individuals by generating false data. Fake faces made by GANs, for example, may deceive not only humans but also machine learning classifiers. Synthetic photographs for identification and authentication purposes, for example, can be used maliciously.
    
    Furthermore, advanced picture editing software such as Adobe Photoshop allows for the alteration of complicated input photographs as well as the creation of high-quality new images. These techniques have improved to the point that they can now build realistic and intricate false pictures that are difficult to distinguish from the genuine thing. YouTube has step-by-step directions and tutorials for making these sorts of fictitious graphics. As a result, these technologies have the potential to be utilised for defamation, impersonation, and factual distortion. Furthermore, with social media, fraudulent material may be swiftly and extensively shared on the Internet.
    '''

    st.write(inspiration)

    st.subheader("👨🏻‍💻 What our Project Does?")

    what_it_does = '''
    Deforgify is a tool that utilizes the power of Deep Learning to distinguish Real images from the Fake ones. For instance, if someone takes your original image and inserts your face into a murder scene or photoshops it onto someone else's body, Deforgify will tag it as fake reducing the chances of it being used to smear you. <br>
    Simply submit the image, and the machine learning model will evaluate it and provide a response in a fraction of a second.'''

    st.markdown(what_it_does, unsafe_allow_html=True)

    stats, buff, graph = st.columns([2, 0.5, 2])

    stats.subheader("🧠 ML Process")

    stats.markdown("<h5> 📊 Getting the Data and EDA Process </h5>", unsafe_allow_html=True)

    stats.markdown("*The dataset was taken from Kaggle and you can find it [here](https://www.kaggle.com/hamzaboulahia/hardfakevsrealfaces).*")

    stats.markdown('''The Dataset contains 1288 faces out of which
    <li> 589 are Real </li> 
    <li> 700 are Fake </li>
    ''', unsafe_allow_html=True) 

    fig = px.bar(x=['Real', 'Fake'], y=[589, 700], height=400)
    graph.plotly_chart(fig, use_container_width=True)

    st.write('The "fake" faces collected in this dataset are generated using the StyleGAN2, which present a harder challenge to classify them correctly even for the human eye.')

    st.image('./Streamlit_UI/faces_1.png', use_column_width=True)
    st.image('./Streamlit_UI/faces_2.png', use_column_width=True)

    st.subheader("⚙️ Model Architecture")

    st.image('./Streamlit_UI/model.png', use_column_width=True)

    ml_process = f'''
- We designed a Sequential Model having 5 Convolutional Layers and 4 Dense Layers.
- The first layer started with 32 filters and kernel of 2x2.
- The number of filters are doubled at every next layer and kernel is is incremented by 1.
- We introduced some Max Pooling Layers after Convolutional Layers to avoid over-fitting and reduce Computational Costs.
- The Output from Covolutional Layer is Flattened and passed over to Dense Layers.
- We started with 512 neurons in the first Dense layer and reduced them to half over the next two Dense layers.
- Some Dropout Layers were also introduced throught the model to randomly ignore some of the neurons and reduce over-fitting.
- We used ReLU activation in all layers except output layer to reduce computation cost and introduce non-linearity.
- Finally the Output Layer was constructed containing 2 neurons (1 for each class) and softmax activation.
'''
    st.write(ml_process)

    results = f'''
    - The model with least Validation Loss was saved during the training and reloaded before obtaining the final results.
    - The model was able to classify all of the samples correctly.
    '''
    loss, buff, acc = st.columns([2, 0.4, 2])

    loss.image('./Streamlit_UI/loss.png', use_column_width=True)
    acc.image('./Streamlit_UI/accuracy.png', use_column_width=True)

    st.subheader("📈 Results")
    st.markdown(results, unsafe_allow_html=True)

    st.write("Classification Report:")
    
    cfr = '''
 Report Title     precision    recall  f1-score   support

        Real       1.00      1.00      1.00        59
        Fake       1.00      1.00      1.00        70

    accuracy                           1.00       129
   macro avg       1.00      1.00      1.00       129
weighted avg       1.00      1.00      1.00       129
'''
    st.code(cfr)

    st.write(" ")

    st.write("*Try it out now by clicking on Classify Image button on the Sidebar*")

    
