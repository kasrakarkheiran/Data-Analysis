"""Take the numbers and find minimum and maximum"""

#FILE NAME
FILE_NAME = "convolution_pairs_share.txt"

#read the file
def read_file(stream):
    #buffer to read each line
    buffer = ""
    buffer = stream.readline()
    #CHECK BUFFER
    print(buffer)
    return process_buffer(buffer)

#process each buffer into different lists
def process_buffer(buffer : str):
    buffer = buffer.strip()
    #CHECK BUFFER
    print(buffer)
    main_list = buffer.split(" ")
    print(main_list)
    left_list = main_list[:8]
    right_list = main_list[8:]
    return left_list , right_list

if(__name__ == "__main__"):
    file = open(FILE_NAME)
    l1 , l2 = read_file(file)
    print(l1)
    print(l2)