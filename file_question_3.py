sizes = [4, 6, 8]
import numpy as np
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

for size in image_sizes:
    resized_images = [resize(image, (size, size)) for image in images]

    X_train, X_temp, y_train, y_temp = train_test_split(
        resized_images, labels, train_size=0.7, random_state=42)
    X_dev, X_test, y_dev, y_test = train_test_split(
        X_temp, y_temp, test_size=0.2, random_state=42)

    train_acc = accuracy_score(y_train, model.predict(X_train))
    dev_acc = accuracy_score(y_dev, model.predict(X_dev))
    test_acc = accuracy_score(y_test, model.predict(X_test))


    print(size)
