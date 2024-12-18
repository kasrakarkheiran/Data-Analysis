"""Take the numbers and find minimum and maximum"""

#FILE NAME
FILE_NAME = "convolution_pairs_share.txt"
#num multiplyer (may not be needed)
NUMBER_MULTIPLIER = 10000

#read the file
def read_file(stream):
    #buffer to read each line
    total_sum = 0
    left_min = 1000
    right_min = 1000
    right_max = -1000
    left_max= -1000
    count = 0
    buffer = ""
    list1 = []
    list2 = []
#while True:
    buffer = stream.readline()
    l1 , l2, left_min, left_max, right_min, right_max, sum1, count1 = process_buffer(buffer, right_min, right_max, left_min, left_max)
    total_sum += sum1
    count += count1
    list1.extend(l1)
    list2.extend(l2)
    #CHECK BUFFER
    #print(buffer)
    return list1 , list2, right_min, right_max, left_min, left_max, total_sum, count

#process each buffer into different lists
def process_buffer(buffer : str, right_min : float, right_max : float, left_min : float, left_max : float ):
    count = 0
    total = 0
    buffer = buffer.strip()

    main_list = buffer.split(" ")

    left_list = main_list[:8]
    right_list = main_list[8:]
    
    for i in range(len(left_list)):
        left_list[i] = float(left_list[i])
        total += left_list[i]
        if(left_list[i] > left_max):
            left_max = left_list[i]
        if(left_list[i] < left_min):
            left_min = left_list[i]
        count += 1
                
    for i in range(len(right_list)):
        right_list[i] = float(right_list[i])
        total += right_list[i]
        if(right_list[i] > right_max):
            right_max = right_list[i]
        if(right_list[i] < right_min):
            right_min = right_list[i]
        count += 1
        
    return left_list , right_list, right_min, right_max, left_min, left_max, total, count


if(__name__ == "__main__"):
    #sum

    file = open(FILE_NAME , "rt")
    l1 , l2, right_min, right_max, left_min, left_max, total_final, count = read_file(file)
    print(f"Left List : {l1}")
    print(f"Right List : {l2}")
    print(f"Right Max : {right_max}")
    print(f"Right Min : {right_min}")
    print(f"Left Max : {left_max}")
    print(f"Left Min : {left_min}")
    print(f"Total : {total_final}")
    print(f"Count : {count}")
    