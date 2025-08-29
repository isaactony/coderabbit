import tensorflow as tf

def custom_loss(y_true, y_pred):
    """    
    Positive cases (y_true = 1) are given higher weight to improve sensitivity.
    """
    weights = tf.where(y_true == 1, 25.0, 1.0)  # Give rare cases more importance
    return tf.reduce_mean(weights * (y_true - y_pred)**2)  # Weighted MSE loss

# Example usage in a model
model.compile(optimizer='adam', loss=custom_loss, metrics=['accuracy'])
