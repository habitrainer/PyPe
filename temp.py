
filename = 'getfromcommanbdline.exe'
def main ():
    print ("Hello World!")
    with open(filename, 'rb') as byte_reader:
        print (byte_reader.read(2)) # magic - MZ - 0x5a4d
        print (byte_reader.read(2)) # cblp
        print (byte_reader.read(2)) # cp
        print (byte_reader.read(2)) # crlc
        print (byte_reader.read(2)) # cparhdr
        print (byte_reader.read(2)) # minalloc
        print (byte_reader.read(2)) # maxalloc
        print (byte_reader.read(2)) # ss
        print (byte_reader.read(2)) # sp
        print (byte_reader.read(2)) # csum
        print (byte_reader.read(2)) # ip
        print (byte_reader.read(2)) # cs
        print (byte_reader.read(2)) # lfarlc
        print (byte_reader.read(2)) # ovno
        print (byte_reader.read(2)) # res
        print (byte_reader.read(2)) # oemid
        print (byte_reader.read(2)) # oeminfo
        print (byte_reader.read(2)) # res2
        print (byte_reader.read(2)) # lfanew pointer to the NT header
        ## Wil the windos loader let me put random stuff here
        #move read head to the NT header
        print (byte_reader.read(0)) #read the dos stub
        
        print (byte_reader.read(2)) # #Signature 0x5045
        
        
        
if __name__ == "__main__":
    main()