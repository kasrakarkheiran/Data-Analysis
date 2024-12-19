"""Take the numbers and find minimum and maximum"""
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import IEEEconvert as convert
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
    left_list = []
    right_list = []
#while True:
    buffer = stream.readline()
    while buffer:
        l1 , l2, left_min, left_max, right_min, right_max, sum1, sum2, count1 = process_buffer(buffer, right_min, right_max, left_min, left_max)
        left_total_sum += sum1
        right_total_sum += sum2
        count += count1
        left_list.extend(l1)
        right_list.extend(l2)
        #CHECK BUFFER
        buffer = stream.readline()
        #print(buffer)
    return left_list , right_list, right_min, right_max, left_min, left_max, left_total_sum, right_total_sum, count

#process each buffer into different lists
def process_buffer(buffer : str, right_min : float, right_max : float, left_min : float, left_max : float ):
    count = 0
    left_total = 0
    right_total = 0
    buffer = buffer.strip()

    main_list = buffer.split(" ")

    left_list = main_list[:8]
    right_list = main_list[8:]
    
    #convert each element to float
    #calculate sum, min and max of the array
    for i in range(len(left_list)):
        left_list[i] = float(left_list[i])
        left_total += left_list[i]
        if(left_list[i] > left_max):
            left_max = left_list[i]
        if(left_list[i] < left_min):
            left_min = left_list[i]
        count += 1
    #convert each element to float
    #calculate sum, min and max of the array
    for i in range(len(right_list)):
        right_list[i] = float(right_list[i])
        right_total += right_list[i]
        if(right_list[i] > right_max):
            right_max = right_list[i]
        if(right_list[i] < right_min):
            right_min = right_list[i]
        count += 1
        
    return left_list , right_list, left_min, left_max, right_min, right_max, left_total, right_total, count

    #combine the left and right lists into 1 list in the correct format (8 from the left, 8 from the right)
def combine_lists(left : list , right : list) -> list:
    combinedList = []
    index = 0;
    while index <= len(left):
        combinedList.extend(left[index:index+8])
        combinedList.extend(right[index:index+8])
        index += 8;
    
    return combinedList

if(__name__ == "__main__"):
    #sum

    #file = open(FILE_NAME , "rt")
    file = open("test.txt" , "rt")
    left , right, right_min, right_max, left_min, left_max, left_total_final, right_total_final, count = read_file(file)
    left_avg = float(left_total_final)/ float(count/2)
    right_avg = float(right_total_final) / float(count/2)
    
   #print(f"Left List : {l1}")
   #print(f"Right List : {l2}")
    print(f"Right Max : {right_max}")
    print(f"Right Min : {right_min}")
    print(f"Left Max : {left_max}")
    print(f"Left Min : {left_min}")
    print(f"Left Total : {left_total_final}")
    print(f"Right Total : {right_total_final}")
    print(f"Left Average : {left_avg}")
    print(f"Right Average : {right_avg}")   
    print(f"Count : {count}")
    
    #test1 = ["r","r","r","r","r","r","r","r","r","r","r","r","r","r","r","r"]
    #test2 = ["l","l","l","l","l","l","l","l","l","l","l","l","l","l","l","l"]
    
    #Combines left list and right list for conversion to IEEE
    combinedList = combine_lists(left , right)
    #converts to IEEE format
    bitList = convert.convertTo754(combinedList)
    #writes to file
    convert.test(bitList)

    pltList = []
    pltList.append(left)
    pltList.append(right)
    #print(len(pltList))
    plt.boxplot(pltList)
    plt.show()

    box = go.Figure()
    box.add_trace(go.Box(y = left, name = "Image Data"))
    box.add_trace(go.Box(y = right, name = "Weights Data"))
    box.update_layout(
        xaxis_title = "Categories", yaxis_title = "Values"
    )
    box.show()