import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, accuracy_score, precision_recall_fscore_support
import numpy as np

def create_model():
    model = Sequential()

    # Convolutional layers
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(400, 400, 3), name='conv2d_12'))
    model.add(MaxPooling2D((2, 2), name='max_pooling2d_12'))

    model.add(Conv2D(32, (3, 3), activation='relu', name='conv2d_13'))
    model.add(MaxPooling2D((2, 2), name='max_pooling2d_13'))

    model.add(Conv2D(16, (3, 3), activation='relu', name='conv2d_14'))
    model.add(MaxPooling2D((2, 2), name='max_pooling2d_14'))

    model.add(Conv2D(16, (3, 3), activation='relu', name='conv2d_15'))
    model.add(MaxPooling2D((2, 2), name='max_pooling2d_15'))

    # Flatten the feature map for the dense layers
    model.add(Flatten(name='flatten_3'))

    # Dense layers
    model.add(Dense(128, activation='relu', name='dense_12'))
    model.add(Dropout(0.5, name='dropout_6'))

    model.add(Dense(96, activation='relu', name='dense_13'))
    model.add(Dropout(0.5, name='dropout_7'))

    model.add(Dense(64, activation='relu', name='dense_14'))
    model.add(Dense(8, activation='softmax', name='dense_15'))

    # Compile the model
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Create the model
model = create_model()

# Training Data
train_datagen = ImageDataGenerator(rescale=1./255,validation_split=0.2)  # Normalize pixel values
train_data = train_datagen.flow_from_directory(
    'data',
    target_size=(400, 400),
    batch_size=32,
    class_mode='categorical',
    subset='training'
)
#Testing Data
test_data = train_datagen.flow_from_directory(
    'data',
    target_size=(400, 400),
    batch_size=32,
    class_mode='categorical',
    subset='validation',
    shuffle=False
)

# Training the model
epochs =3
model.fit(train_data, epochs=epochs)

# Saving the model with trained weights
model.save('cnn_model.h5')

#Printing Accuracy
test_loss, test_accuracy = model.evaluate(test_data)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# Prediction
predictions = model.predict(test_data)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = test_data.classes
class_labels = list(test_data.class_indices.keys())

# Classification report
print("\nClassification Report:")
print(classification_report(true_classes, predicted_classes, target_names=class_labels))
precision, recall, f1_score, support = precision_recall_fscore_support(true_classes, predicted_classes, average=None)

print("\nDetailed Metrics per Class:")
for i, label in enumerate(class_labels):
    print(f"Class '{label}':")
    print(f"  Precision: {precision[i]:.2f}")
    print(f"  Recall: {recall[i]:.2f}")
    print(f"  F1-Score: {f1_score[i]:.2f}")
    print(f"  Support: {support[i]}")

# Overall accuracy
overall_accuracy = accuracy_score(true_classes, predicted_classes)
print(f"\nOverall Test Accuracy: {overall_accuracy * 100:.2f}%")
