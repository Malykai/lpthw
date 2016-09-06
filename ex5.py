name = 'Randy J. Sykes'
age = 32 # not a lie
height = 74 # inches
weight = 362 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall or %d cm." % (height, height * 2.54)
print "He's %d pounds heavy or %d kg or %d stones." % (weight, weight * 0.453592, weight * 0.0714286)
print "Actually thats very heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s the ones he has anyway." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)