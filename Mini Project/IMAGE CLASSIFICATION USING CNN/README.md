# 🚗 Vehicle Type Recognition Using Deep Learning 🚌

Welcome to the **Vehicle Type Recognition** project! This project leverages the power of deep learning to identify various vehicle types such as cars, trucks, buses, and motorcycles from images. Whether you're interested in traffic monitoring, toll collection, or automated parking systems, this project showcases a practical implementation of intelligent transportation systems.

## 🌟 Project Highlights

### Introduction
Vehicle type recognition is a crucial technology for modern intelligent transportation systems. By using images captured by cameras, our deep learning model can accurately identify the type of vehicle, which has numerous real-world applications.

### Technologies Used
- **TensorFlow**: 🧠 An open-source machine learning framework used to build and train the neural network.
- **OpenCV**: 👀 A library for real-time computer vision used for image processing.
- **Python**: 🐍 The programming language used to implement the project.
- **NVIDIA GPU**: 🚀 Utilized for accelerating the training process.

### Dataset Information
- **Source**: [Vehicle Type Recognition Dataset on Kaggle](https://www.kaggle.com/datasets/kaggleashwin/vehicle-type-recognition)
- **Classes**: Bus, Car, Truck, Motorcycle
- **Total Images**: 400
- **Training Set**: 200 images
- **Validation Set**: 200 images
- **Image Size**: 256x256 pixels

### Methodology
1. **Data Collection and Cleaning**: 📂
   - Images were collected and stored in respective class folders.
   - Dodgy images (unsupported formats or corrupted files) were removed.

2. **Data Preprocessing**: 🔄
   - Images were resized to 256x256 pixels.
   - Normalization was performed to scale pixel values to the range [0, 1].

3. **Model Building**: 🏗️
   - A Convolutional Neural Network (CNN) with multiple Conv2D and MaxPooling2D layers was designed.
   - The model was compiled using the Adam optimizer and sparse categorical cross-entropy loss.

4. **Training and Validation**: 🎓
   - The model was trained on the training dataset for 20 epochs.
   - Validation was performed on a separate validation set to tune hyperparameters.

5. **Testing**: 🧪
   - The trained model was evaluated on the test dataset to measure its performance.

### Results and Discussion
- **Training Accuracy**: The model achieved high training accuracy, indicating it learned the patterns well.
- **Validation Accuracy**: The validation accuracy was slightly lower than the training accuracy, suggesting a good generalization.
- **Test Accuracy**: The model's performance on the test set was satisfactory.
- **Precision, Recall, and F1-Score**: Evaluated to measure the model's effectiveness in predicting each class accurately.

### Conclusion
The project successfully implemented a deep learning model to recognize vehicle types from images. The model demonstrated good accuracy and generalization capabilities. Future work could involve improving the dataset size and diversity, experimenting with different model architectures, and deploying the model in a real-time system.

## 📁 What's Included
- **Code**: The complete code for the project.
- **Report**: A detailed project report.
- **Presentation**: A PowerPoint presentation summarizing the project.


