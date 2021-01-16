colors = ["red", "blue", "yellow", "Black"]
print(colors)
print(colors[0])
print(colors[-1])

#Extracting the exam date and print it out.
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

name = input("who are you? ")
print("hello %s" % (name,))

#Program accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)