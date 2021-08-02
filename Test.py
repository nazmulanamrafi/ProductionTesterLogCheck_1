import os
#the following loop is setting the same condition as "lambda" function in line 10
def check_if_text(filename):
    return filename.endswith(".txt")


path = "C:/Users/rafi.nazmul/Documents/Test_log_22.06.2021"
os.chdir(path)
all_files = os.listdir(path)
txt_files = list(filter(check_if_text, all_files))
#print(all_files)
OK_files = list(filter(lambda fname: 'OK' in fname, txt_files))
#print(OK_files)
# to store your important text files.
# this list stores your important text line (2nd line) in each file
texts = []
for file in OK_files:
    with open(os.path.join(path, file)) as f:
        #texts = texts + f.readlines()
        texts.append(f.readlines())
#print(texts)
final_data = []
#file_data in the following line is a variable
for file_data in texts:
    #print(file_data)
    for row in file_data: #(?)
        #splits each row of the file data into two parts (position 0 is assigned to the first and 1 to the second part)
        parts = row.split(" : ")
        parts1 = row.split(" ( ")
        #if the lenth of the splitted parts is less than 1, meaning no text after the :, continues from the beginning of the for loop
        if len(parts) < 1: #(?)
            continue

        if "Current" in parts[1]: #(?)
            final_data.append(parts[1])
        elif "-> voltage" in parts[1]:
            final_data.append(parts[1])
        elif "Serial:" in parts[1]:
            if "MCU_SN" in parts[1]:
                final_data.append(parts[1])
        elif  "FF Lite SN:" in parts[1]:
            final_data.append(parts[1])
    final_data.append("\n")

#print(final_data)


# to print each important line
filepath1 = "C:/Users/rafi.nazmul/Documents/Test_log_22.06.2021/Output.txt"
#if multiple copies needed at different directories
#filepath2 = "C:/Users/rafi.nazmul/Documents/Loki board/Output.txt"

with open(filepath1,'w+') as file:
    for text in final_data:
        file.write(text)
        #print(text)
#with open(filepath2,'w+') as file:
    #for text in final_data:
        #file.write(text)