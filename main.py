"""Take the numbers and find minimum and maximum"""
import matplotlib.pyplot as plt

#FILE NAME
FILE_NAME = "convolution_pairs_share.txt"
#num multiplyer (may not be needed)
NUMBER_MULTIPLIER = 10000

#read the file
def read_file(stream):
    #buffer to read each line
    left_total_sum = 0
    right_total_sum = 0
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
    while buffer:
        l1 , l2, left_min, left_max, right_min, right_max, sum1, sum2, count1 = process_buffer(buffer, right_min, right_max, left_min, left_max)
        left_total_sum += sum1
        right_total_sum += sum2
        count += count1
        list1.extend(l1)
        list2.extend(l2)
        #CHECK BUFFER
        buffer = stream.readline()
        #print(buffer)
    
    
    return list1 , list2, right_min, right_max, left_min, left_max, left_total_sum, right_total_sum, count

#process each buffer into different lists
def process_buffer(buffer : str, right_min : float, right_max : float, left_min : float, left_max : float ):
    count = 0
    left_total = 0
    right_total = 0
    buffer = buffer.strip()

    main_list = buffer.split(" ")

    left_list = main_list[:8]
    right_list = main_list[8:]
    
    for i in range(len(left_list)):
        left_list[i] = float(left_list[i])
        left_total += left_list[i]
        if(left_list[i] > left_max):
            left_max = left_list[i]
        if(left_list[i] < left_min):
            left_min = left_list[i]
        count += 1
                
    for i in range(len(right_list)):
        right_list[i] = float(right_list[i])
        right_total += right_list[i]
        if(right_list[i] > right_max):
            right_max = right_list[i]
        if(right_list[i] < right_min):
            right_min = right_list[i]
        count += 1
        
    return left_list , right_list, left_min, left_max, right_min, right_max, left_total, right_total, count


if(__name__ == "__main__"):
    #sum

    file = open(FILE_NAME , "rt")
    l1 , l2, right_min, right_max, left_min, left_max, left_total_final, right_total_final, count = read_file(file)
    left_avg = float(left_total_final)/ float(count/2)
    right_avg = float(right_total_final) / float(count/2)
    
   # print(f"Left List : {l1}")
   # print(f"Right List : {l2}")
    print(f"Right Max : {right_max}")
    print(f"Right Min : {right_min}")
    print(f"Left Max : {left_max}")
    print(f"Left Min : {left_min}")
    print(f"Left Total : {left_total_final}")
    print(f"Right Total : {right_total_final}")
    print(f"Left Average : {left_avg}")
    print(f"Right Average : {right_avg}")   
    print(f"Count : {count}")
    
    plt.boxplot(l1)
    plt.boxplot(l2)
    plt.show()