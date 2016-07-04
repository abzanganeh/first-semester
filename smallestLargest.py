largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num=int(num)
    except:
        print "Please enter an invalid integer number or 'done' to see results"
        continue
    if num < smallest or smallest is None:
        smallest=num
    elif num > largest:
        largest = num
print "Maximum is ", largest
print "Minimum is ", smallest