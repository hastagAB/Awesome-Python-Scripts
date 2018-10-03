#Importing Libraries
import numpy as np
import tensorflow as tf
import tensorflow.contrib.learn as learn
import tensorflow.contrib.metrics as metrics

#Importing Dataset
mnist = learn.datasets.load_dataset('mnist')

#Training Datasets
data = mnist.train.images
labels = np.asarray(mnist.train.labels, dtype=np.int32)
test_data = mnist.test.images
test_labels = np.asarray(mnist.test.labels, dtype=np.int32)
feature_columns = learn.infer_real_valued_columns_from_input(data)

#Applying Classifiers
classifier = learn.DNNClassifier(feature_columns=feature_columns, n_classes=10,hidden_units=[1024,512,256])
classifier.fit(data, labels, batch_size=100, steps=1000)

#Evaluating the Results 
classifier.evaluate(test_data, test_labels)                                      
accuracy_score = classifier.evaluate(test_data, test_labels)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))