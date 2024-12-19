import struct

#convert elements to IEEE
def convertTo754(convertList : list[float]) -> list[str]:
    bitList = []
    for number in convertList:
        hexConvert = struct.pack('>f',number)
        binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)
        bitList.append(binaryConvert)
    return bitList

#write elements to file
def WriteToFile(combinedList : list[str]):
    writeFile = open("convolution_pairs_IEEE.txt" , "w")
    for i in range(len(combinedList)):
        string = combinedList[i]
        #goes to next line after 16 elements
        if((i + 1) % 16 == 0):
            writeFile.write(string + "\n")
        else:
            writeFile.write(string + " ")
    return 


if(__name__ == "__main__"):    
    testFloat = 0.53493253
    hexConvert = struct.pack(">f" , testFloat)
    binaryConvert = ''
    binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)
    print(type(hexConvert))
    print(type(binaryConvert))