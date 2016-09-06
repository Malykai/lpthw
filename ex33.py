from sys import argv

script, stop_at = argv

def compare(stop):
    i = 0
    numbers = []

    for i in range(stop):
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += 1
        
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
    print "The numbers: "

    for num in numbers:
        print num
        

print stop_at
print compare(int(stop_at))