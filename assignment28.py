# Write a Python script to print the following status of a file:
# a. Whether a file is read only
# b. Whether a file is closed or not
# c. Which file opening mode is used
# d. Name of the file
# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.
# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on
# the console.
# 4. Write a Python script to store a list of city names in a file ‘cities.txt’
# 5. Write a Python script to append list of city names in a file ‘cities.txt’
# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or
# not
# 7. Write a Python script to count the number of Python keywords occurring in a python
# source file.
# 8. Write a Python script to create a copy of a file.
# 9. Write a Python script to store book data in a file. Book data is in the form of a
# dictionary in which book name is the key and price is its value. Use pickle to store
# data into a file (say bookfile


# 1) ...............................................
# which file opening mode is used

# 2) ...........................................
# f=open('myfile.txt','w')
# f.write('hey how are you ?')
# f.close()

# 3) ........................................
# f=open('myfile.txt','r')
# read_text=f.read()
# print(read_text)
# f.close()

# # 4) .........................................
# f=open('cities.txt','w')
# f.write(' ["Agra","Varansi","lucknow","azamgarh"] ')
# f.close()

# 5) ............................................. 
# x=open('cities.txt','a')
# x.write(' ["haridwar","kanpur","gorakhpur","agarala"] ')
# x.close
# 
# 6) ..........................................
# from fileinput import filename
# def search(filename,word):
#     f=open(filename,'r')
#     count_line=0
#     for line in f.readlines():
#         count_line+=1
#         list1=line.split(" ")
#         word_count=0
#         for w in list1:
#             word_count+=1
#             if word==w:
#                 print(count_line,word_count)           
#     f.close()  
# search('cities.txt','lucknow')


# 7) ............................................
# from keyword import kwlist


# f=open('keyword.txt','w')
# c=0
# for keyword in kwlist:
#     f.write()
#     c+=1
# print(c)
# f.close()


# 8) .............................................
# import os
# os.rename('dfg.txt','keyword.txt')


# 9) ..........................................
f=open("book.txt","w")

