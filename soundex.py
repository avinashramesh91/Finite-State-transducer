from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start') #handle no input

    f1.add_state('next')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.initial_state = 'start'

    # Set all the final states

    f1.set_final('start') #handle no input

    f1.set_final('next')
    f1.set_final('1')
    f1.set_final('2')
    f1.set_final('3')
    f1.set_final('4')
    f1.set_final('5')
    f1.set_final('6')

    group0 = ['a','A','e','E','h','H','i','I','o','O','u','U','w','W','y','Y']
    group1 = ['b','B', 'f','F', 'p','P', 'v','V']
    group2 = ['c','C', 'g','G', 'j','J', 'k','K', 'q','Q', 's','S', 'x','X', 'z','Z']
    group3 = ['d','D', 't','T']
    group4 = ['l','L']
    group5 = ['m','M', 'n','N']
    group6 = ['r','R']
    # Add the rest of the arcs
    for letter in string.ascii_letters:
        f1.add_arc('start', 'next', (letter), (letter)) #first letter retained

        if(letter in group0):
          f1.add_arc('next', 'next', (letter), ())  #successive vowels

          f1.add_arc('6', 'next', (letter), ()) #vowels from other states
          f1.add_arc('5', 'next', (letter), ())
          f1.add_arc('4', 'next', (letter), ())
          f1.add_arc('3', 'next', (letter), ())
          f1.add_arc('2', 'next', (letter), ())
          f1.add_arc('1', 'next', (letter), ())

        else:
         if(letter in group1):
          f1.add_arc('next', '1', (letter), ('1')) #first group1 letter

          f1.add_arc('1', '1', (letter), ()) #successive group1 letters

          f1.add_arc('2', '1', (letter), ('1')) #group1 letters from other states
          f1.add_arc('3', '1', (letter), ('1'))
          f1.add_arc('4', '1', (letter), ('1'))
          f1.add_arc('5', '1', (letter), ('1'))
          f1.add_arc('6', '1', (letter), ('1'))
         if(letter in group2):
          f1.add_arc('next', '2', (letter), ('2')) #first group2 letter

          f1.add_arc('2', '2', (letter), ()) #successive group2 letters

          f1.add_arc('1', '2', (letter), ('2')) #group2 letters from other states
          f1.add_arc('3', '2', (letter), ('2'))
          f1.add_arc('4', '2', (letter), ('2'))
          f1.add_arc('5', '2', (letter), ('2'))
          f1.add_arc('6', '2', (letter), ('2'))
         if(letter in group3):
          f1.add_arc('next', '3', (letter), ('3')) #first group3 letter

          f1.add_arc('3', '3', (letter), ()) #successive group3 letters

          f1.add_arc('1', '3', (letter), ('3')) #group3 letters from other states
          f1.add_arc('2', '3', (letter), ('3'))
          f1.add_arc('4', '3', (letter), ('3'))
          f1.add_arc('5', '3', (letter), ('3'))
          f1.add_arc('6', '3', (letter), ('3'))
         if(letter in group4):
          f1.add_arc('next', '4', (letter), ('4')) #first group4 letter

          f1.add_arc('4', '4', (letter), ()) #successive group4 letters

          f1.add_arc('1', '4', (letter), ('4')) #group4 letters from other states
          f1.add_arc('2', '4', (letter), ('4'))
          f1.add_arc('3', '4', (letter), ('4'))
          f1.add_arc('5', '4', (letter), ('4'))
          f1.add_arc('6', '4', (letter), ('4'))
         if(letter in group5):
          f1.add_arc('next', '5', (letter), ('5')) #first group5 letter

          f1.add_arc('5', '5', (letter), ()) #successive group5 letters

          f1.add_arc('1', '5', (letter), ('5')) #group5 letters from other states
          f1.add_arc('2', '5', (letter), ('5'))
          f1.add_arc('3', '5', (letter), ('5'))
          f1.add_arc('4', '5', (letter), ('5'))
          f1.add_arc('6', '5', (letter), ('5'))
         if(letter in group6):
          f1.add_arc('next', '6', (letter), ('6')) #first group6 letter

          f1.add_arc('6', '6', (letter), ()) #successive group6 letters

          f1.add_arc('1', '6', (letter), ('6')) #group6 letters from other states
          f1.add_arc('2', '6', (letter), ('6'))
          f1.add_arc('3', '6', (letter), ('6'))
          f1.add_arc('4', '6', (letter), ('6'))
          f1.add_arc('5', '6', (letter), ('6'))

    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')


    f2.initial_state = '1'

    f2.set_final('1')  #handle no input

    f2.set_final('1')
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('1', '1', (letter), (letter))

    for n in range(10): # 1st number
        f2.add_arc('1', '2', (str(n)), (str(n)))

    for n in range(10): #2nd number
        f2.add_arc('2', '3', (str(n)), (str(n)))

    for n in range(10): #3rd number
        f2.add_arc('3', '4', (str(n)), (str(n)))

    for n in range(10):
        f2.add_arc('4', '4', (str(n)), ())

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('2')
    f3.add_state('3')
    f3.add_state('4')
    f3.add_state('5')
    f3.add_state('6')
    f3.add_state('7')
    f3.add_state('8')
    f3.add_state('9')
    f3.add_state('10')
    
    f3.initial_state = '1'

    f3.set_final('1')  #handle no input

    f3.set_final('4') #has to have 3 numbers
    f3.set_final('10')
    f3.set_final('6')
    f3.set_final('7')

    for letter in string.letters:   #retain first letter
        f3.add_arc('1', '1', (letter), (letter))

    for number in range(1,10):  #transition for the 3 numbers
        f3.add_arc('1', '2', (str(number)), (str(number)))
        f3.add_arc('2', '3', (str(number)), (str(number)))
        f3.add_arc('3', '4', (str(number)), (str(number)))

    f3.add_arc('1', '8', (), ('0'))
    f3.add_arc('8', '9', (), ('0'))
    f3.add_arc('9', '10', (), ('0'))

    f3.add_arc('2', '5', (), ('0'))
    f3.add_arc('5', '6', (), ('0'))

    f3.add_arc('3', '7', (), ('0'))










    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))

    #print composechars(tuple("jurafsky"),f1)
    #print composechars(tuple("washington"),f1)
    print trace(f3,tuple("b2"))
    #print f3.transduce(tuple("j61"))


