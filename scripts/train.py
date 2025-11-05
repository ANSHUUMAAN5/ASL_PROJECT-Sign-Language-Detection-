import json, os
from pathlib import Path

import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Input
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam

DATA_DIR = "data/asl_dataset"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "asl_model.h5")
LABELS_PATH = os.path.join(MODEL_DIR, "labels.json")
IMG_SIZE = (128, 128)
BATCH_SIZE = 32
EPOCHS = 6
LR = 1e-4

def main():
    Path(MODEL_DIR).mkdir(parents=True, exist_ok=True)

    datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        validation_split=0.2,
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
    )

    train_gen = datagen.flow_from_directory(
        DATA_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="training",
        shuffle=True
    )

    val_gen = datagen.flow_from_directory(
        DATA_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False
    )

    num_classes = train_gen.num_classes
    print("Classes:", train_gen.class_indices)

    
    idx2label = {v: k for k, v in train_gen.class_indices.items()}
    with open(LABELS_PATH, "w") as f:
        json.dump(idx2label, f)

    base = MobileNetV2(include_top=False, weights="imagenet",
                       input_tensor=Input(shape=(IMG_SIZE[0], IMG_SIZE[1], 3)))
    x = base.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.25)(x)
    out = Dense(num_classes, activation="softmax")(x)
    model = Model(inputs=base.input, outputs=out)

    for layer in base.layers[:-40]:
        layer.trainable = False

    model.compile(optimizer=Adam(learning_rate=LR),
                  loss="categorical_crossentropy",
                  metrics=["accuracy"])

    callbacks = [
        EarlyStopping(patience=3, restore_best_weights=True, monitor="val_accuracy"),
        ModelCheckpoint(MODEL_PATH, monitor="val_accuracy", save_best_only=True)
    ]

    model.fit(
        train_gen,
        validation_data=val_gen,
        epochs=EPOCHS,
        callbacks=callbacks
    )

    print(f"✅ Model saved: {MODEL_PATH}")
    print(f"✅ Labels saved: {LABELS_PATH}")

if __name__ == "__main__":
    main()
