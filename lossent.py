import tensorflow as tf

def custom_loss(y_true, y_pred):

    weights = tf.where(y_true == 1, 25.0, 1.0)  
    return tf.reduce_mean(weights * (y_true - y_pred)**2)  # Weighted MSE loss

model.compile(optimizer='adam', loss=custom_loss, metrics=['accuracy'])
