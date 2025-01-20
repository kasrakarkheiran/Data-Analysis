import tensorflow as tf
import image as img

if(__name__ == "__main__"):
    print("test")
    # Load the CIFAR-10 dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    print(type(x_train))
    # Check the shapes of the data
    print(f"Training data shape: {x_train.shape}, Training labels shape: {y_train.shape}")
    print(f"pixel data : {x_train[0][0][0]}")
    print(f"Test data shape: {x_test.shape}, Test labels shape: {y_test.shape}")
    
    testArray = []
    testArray.append(x_train[0])
    convertedImagePixels = img.ConvertTuple(testArray)
    
    
    print("Length: " , len(convertedImagePixels))
    
    
    
    print("amount of red pixel Rows: " , len(convertedImagePixels[0]))
    print("amount of green pixel Rows: " , len(convertedImagePixels[1]))
    print("amount of blue pixel Rows: " , len(convertedImagePixels[2]))
    
    
    print("lenght of red pixel Rows: " , len(convertedImagePixels[0][0]))
    print("length of green pixel Rows: " , len(convertedImagePixels[1][0]))
    print("length of blue pixel Rows: " , len(convertedImagePixels[2][0]))
    
    for i in convertedImagePixels[0][1]:
        print(i , ", ")

    
    
    
    
    
    """
    hexConvert = struct.pack('>f',x_train[0][0][0][0])
    binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)
    print(binaryConvert)
    print(type(binaryConvert))
    testArray = []
    """