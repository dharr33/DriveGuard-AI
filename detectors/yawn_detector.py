import cv2
import numpy as np
import tensorflow as tf

IMG_SIZE = 224

# Recreate model architecture
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False

x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(128, activation="relu")(x)
x = tf.keras.layers.Dropout(0.4)(x)
output = tf.keras.layers.Dense(1, activation="sigmoid")(x)

model = tf.keras.Model(inputs=base_model.input, outputs=output)

# Load trained weights
model.load_weights("models/yawn_detection_model4.keras")

def detect_yawn(frame, face):

    x, y, w, h = face

    x = max(0, x)
    y = max(0, y)

    # Mouth region
    mouth = frame[y + h//2 : y + h, x : x + w]

    if mouth.size == 0:
        return "NO_YAWN"

    mouth = cv2.resize(mouth, (IMG_SIZE, IMG_SIZE))
    mouth = mouth.astype("float32") / 255.0
    mouth = np.expand_dims(mouth, axis=0)

    prediction = model.predict(mouth, verbose=0)

    if prediction[0][0] > 0.5:
        return "YAWN"
    else:
        return "NO_YAWN"