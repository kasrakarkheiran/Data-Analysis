import struct

def convertTo754(convertValue:float):
    return struct.pack('>f',convertValue)
    
testFloat = 0.53493253
hexConvert = convertTo754(testFloat)
binaryConvert = ''
binaryConvert = ''.join(f'{byte:08b}' for byte in hexConvert)

print(binaryConvert)