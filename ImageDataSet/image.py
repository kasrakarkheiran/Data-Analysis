import tensorflow as tf
import struct
#from ConvolutionPairs import IEEEconvert as ic
#important info: cifar10 loads data as Numpy Arrays (ndarray) and is a 4d array: (images , height, width, pixel channels)


def ConvertTuple(imageArray):
    convertedValues = []
    #go into first array
    for image in imageArray:
        #go into height of the image
        for rows in image:
            #go into the pixels of each row
            for pixel in rows:
                convertedValues.extend(ValueToIEEE(pixel))      
    return convertedValues



def ValueToIEEE(pixelChannels) -> list[str]:
    bitList = []
    for number in pixelChannels:
        hexConvert = struct.pack('>f',number)
        binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)
        bitList.append(binaryConvert)
    return bitList

#write elements to file
def WriteToFile(outputList : list[str]):
    writeFile = open("ImageDataSet/output.txt" , "w")
    for index , string in enumerate(outputList):
        writeFile.write(string + " ")
        if((index + 1) % 9 == 0):
            writeFile.write("\n")
    return 

if(__name__ == "__main__"):
    print("test")
    # Load the CIFAR-10 dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    print(type(x_train))
    # Check the shapes of the data
    print(f"Training data shape: {x_train.shape}, Training labels shape: {y_train.shape}")
    print(f"Data of one training data image: {x_train[0][0][0]}")
    print(f"Test data shape: {x_test.shape}, Test labels shape: {y_test.shape}")
    hexConvert = struct.pack('>f',x_train[0][0][0][0])
    binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)
    print(binaryConvert)
    print(type(binaryConvert))
    testArray = []
    testArray.append(x_train[0])
    converted = ConvertTuple(testArray)
    print(converted[0])
    print(type(converted[0]))
    WriteToFile(converted)
    #x_test.