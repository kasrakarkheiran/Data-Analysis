import tensorflow as tf
import struct
#from ConvolutionPairs import IEEEconvert as ic
#important info: cifar10 loads data as Numpy Arrays (ndarray) and is a 4d array: (images , height, width, pixel channels)


def ConvertTuple(imageArray):
    convertedPixels = []
    redValues = []
    greenValues = []
    blueValues = []
    imageRGB = [[],[],[]]
    #go into first array
    for image in imageArray:
        #go into height of the image
        for rows in image:
            #go into the pixels of each row
            for pixel in rows:
                #Takes pixel list and turn RGB into IEEE
                convertedPixels = ValueToIEEE(pixel) 
                #print("converted values: ", convertedPixels)
                #each pixel goes into respective list
                redValues.append(convertedPixels[0])
                greenValues.append(convertedPixels[1])
                blueValues.append(convertedPixels[2])  
            #lists containing converted values are stored in matrix
            imageRGB[0].append(redValues)
            imageRGB[1].append(greenValues)
            imageRGB[2].append(blueValues)
            #Temp lists are reset
            redValues = []
            greenValues = []
            blueValues = []        

    return imageRGB



def ValueToIEEE(pixelChannels) -> list[str]:
    bitList = []
    for number in pixelChannels:
        hexConvert = struct.pack('>f',number)
        binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)
        bitList.append(binaryConvert)
    return bitList

#write elements to file
def WriteToFile(outputList):
    writeFile = open("ImageDataSet/output.txt" , "w")
    redRow = 0
    greenRow = 1
    blueRow = 2
    NUM_OF_RGB_ROWS = 3
    NUM_OF_RGB_COLS = 8
    MULTIPLYER = 3
    rgb = [redRow , greenRow , blueRow]
    #while we have not reached the final row (which is blue rgb values)
    while(rgb[2] < len(outputList)):
        #which color we are currently writing: red, blue, or green
        for rgbRow in range(len(rgb)):
            #the number of rows we are writing for that color
            for i in range(0, NUM_OF_RGB_ROWS):
                #if we have reached the end break the current loop 
                if(rgb[rgbRow] >= len(outputList)):
                    break
                #write 8 values for each line, dropping the final value
                for j in range(0, NUM_OF_RGB_COLS):
                    writeFile.write(outputList[rgb[rgbRow]][j])
                    writeFile.write(" ")
                rgb[rgbRow] += MULTIPLYER
                writeFile.write("\n")       
        #note the final 3 lines ARE IN RGB VALUE meaning line 298 is R, 299 is G and 300 is B
    return 


def FormatOutputList(inputList):
    formattedList = []    
    #index to keep track of 3*3 list
    colIndex = 0
    rowIndex = 0
    #temp list stores the 3*3 squares of pixels, then that gets stored in formatted list.
    tempList = []
    tempList1 = []
    tempList2 = []

    while(rowIndex < 30 and colIndex < 30): #Made Change to be less than not less than equal to 
        #formatting the red, blue and green value 
        for i in range(0,3):
            for j in range(0,3):
                tempList.append(inputList[0][rowIndex + i][colIndex + j]) 
                tempList1.append(inputList[1][rowIndex + i][colIndex + j])
                tempList2.append(inputList[2][rowIndex + i][colIndex + j])
        #putting temp list into formattted list and reseting temp list
        formattedList.append(tempList)
        formattedList.append(tempList1)
        formattedList.append(tempList2)
        tempList = []
        tempList1 = []
        tempList2 = []
        #if RowIndex has reached 30 and colIndex has reached 30, 
        # 3 can no longer be added to it as the list is only 32 rows and columns, so it has reached the end lists  
        if(rowIndex >= 30 and colIndex >= 30):
            break
        #if column is at the end of the row, it will go to the beginning of the row and also go to the next 3 set of rows of the squares
        if (colIndex < 30):
            colIndex += 3

        if (colIndex >= 30):
            colIndex = 0
            rowIndex += 3
        #if column is not at the end of the row then it goes to the beginning of the next set of squares

        
    return formattedList

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
    converted = ConvertTuple(testArray)
    finalFormatList = FormatOutputList(converted) #Should be 300 lists : 9r, 9g, 9b, 9r, 9g, 9b...

    WriteToFile(finalFormatList)
    #print("num rows: " , len(finalFormatList))
    
    #print("num cols: " , len(finalFormatList[0]))
    #x_test.