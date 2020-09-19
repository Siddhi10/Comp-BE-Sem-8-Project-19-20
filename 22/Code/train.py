from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import SGD

# Initializing the CNN
from keras.applications.vgg16 import VGG16
vgg = Sequential()
vgg.add(Convolution2D(64,[3,3],strides=1,padding='same',activation='relu',
                        input_shape=(128, 128, 1)))
_vgg = VGG16(weights='imagenet', include_top=False)
counter=0
for layer in _vgg.layers:
    layer.trainable = False
    counter+=1
print("VGG's ", counter , " layers are not added to the layer")
vgg.add(_vgg)
print("done")
vgg.add(Flatten())

vgg.add(Dense(512,activation='relu'))
vgg.add(Dense(28,activation="softmax"))
from keras.optimizers import SGD
SGD(lr=0.001, momentum=0.9, nesterov=False)
vgg.compile(loss='categorical_crossentropy',
              optimizer='SGD',
              metrics=['accuracy'])
bs = 5
epoch  = 15
train_datagen = idg(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    #width_shift_range=0.2,
    #height_shift_range=0.2,
    #horizontal_flip=True,
    )
    
traincomplete_datagen = idg(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    #width_shift_range=0.2,
    #height_shift_range=0.2,
    #horizontal_flip=True,
    )

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(128, 128),
    batch_size=bs,
    color_mode="grayscale",
    class_mode='categorical')

validation_generator = train_datagen.flow_from_directory(
    'data/test',
    target_size=(128, 128),
    batch_size=bs,
    color_mode="grayscale",
    class_mode='categorical')

history= vgg.fit_generator(
    train_generator,
    steps_per_epoch=2000*28/5,
    epochs=epoch,
    validation_data=validation_generator,
    validation_steps=500*28/5)		




#saving
model_json=classifier.to_json()
with open("model-bw.json","w")as json_file:
	json_file.write(model_json)
classifier.save_weights('model-bw.h5')
