


import contentFile

# print( contentFile.variable )


with open("contentFile.py", "r" ) as file:

    # when you read a File using read() method the returned value will be String, which will read the file exactly including New Lines white spaces.
    data = file.read()

    print( data )
    print( type(data))


print("""



""")







