import sys
#==================================
my_output = open("my_output.txt", "r")
correct_output = open("correct_output.txt", "r")
line = 0
wrong_list = []
while True:
    
    try:
        line += 1
        true = correct_output.readline()
        my = my_output.readline()
        if my != true:
            wrong_list.append(line)
        if true=="\n":
            break
        
    except:
        print("Error!")
        break
    

if wrong_list:
    print(f"Wrong Answer Exists at line", end =' ')
    for _ in wrong_list:
        print(_, end=", ")
    print()
else:
    print("Correct!")
my_output.close()
correct_output.close()