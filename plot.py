import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Define a simple MeshNet-like model (simplified for demonstration)
def build_meshnet_model(input_shape=(64, 64, 64, 1), num_classes=2):
    inputs = tf.keras.Input(shape=input_shape)
    x = tf.keras.layers.Conv3D(32, 3, padding='same', activation='relu')(inputs)
    x = tf.keras.layers.Conv3D(64, 3, padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv3D(num_classes, 3, padding='same', activation='softmax')(x)
    model = tf.keras.Model(inputs, x)
    return model

# Dice coefficient for accuracy
def dice_coefficient(y_true, y_pred):
    y_true_f = tf.keras.backend.flatten(tf.cast(y_true, 'float32'))
    y_pred_f = tf.keras.backend.flatten(tf.cast(y_pred, 'float32'))
    intersection = tf.keras.backend.sum(y_true_f * y_pred_f)
    return (2. * intersection + 1.) / (tf.keras.backend.sum(y_true_f) + tf.keras.backend.sum(y_pred_f) + 1.)

# Dice loss
def dice_loss(y_true, y_pred):
    return 1 - dice_coefficient(y_true, y_pred)

# Generate synthetic data (replace with your MRI dataset)
def generate_synthetic_data(num_samples=10, shape=(64, 64, 64)):
    X = np.random.rand(num_samples, *shape, 1)  # Simulated MRI volumes
    y = (X > 0.5).astype(np.float32)  # Simulated binary masks
    return X, y

# Main script
if __name__ == "__main__":
    # Parameters
    input_shape = (64, 64, 64, 1)
    epochs = 20
    batch_size = 2

    # Generate synthetic training and validation data
    X_train, y_train = generate_synthetic_data(8)  # 8 training samples
    X_val, y_val = generate_synthetic_data(2)      # 2 validation samples

    # Build and compile the model
    model = build_meshnet_model(input_shape)
    model.compile(optimizer='adam', loss=dice_loss, metrics=[dice_coefficient])

    # Train the model
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )

    # Plot accuracy and loss
    plt.figure(figsize=(12, 4))

    # Loss plot
    plt.subplot(1, 2, 1)
    plt.plot(history.history['loss'], label='Training Loss', color='blue')
    plt.plot(history.history['val_loss'], label='Validation Loss', color='orange')
    plt.title('Loss Over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Dice Loss')
    plt.legend()
    plt.grid(True)

    # Accuracy plot
    plt.subplot(1, 2, 2)
    plt.plot(history.history['dice_coefficient'], label='Training Dice', color='blue')
    plt.plot(history.history['val_dice_coefficient'], label='Validation Dice', color='orange')
    plt.title('Accuracy (Dice Coefficient) Over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Dice Coefficient')
    plt.legend()
    plt.grid(True)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()