import sys
from fst import FST
from fsmutils import composewords
import fsmutils

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('H')
    f.add_state('T')
    f.add_state('U')
    f.add_state('TCent')
    f.add_state('1H')
    f.add_state('29H')

    f.add_state('1')
    f.add_state('1a')
    f.add_state('1b')
    f.add_state('1c')
    f.add_state('1d')
    f.add_state('1e')
    f.add_state('2')
    f.add_state('3')
    f.add_state('4')
    f.add_state('5')
    f.add_state('6')
    f.add_state('7')
    f.add_state('71')
    f.add_state('7f')
    f.add_state('8')
    f.add_state('8a')
    f.add_state('9')
    f.add_state('9a')
    f.add_state('9b')
    f.add_state('9c')
    f.add_state('9d')
    f.add_state('9e')
    f.add_state('a')
    f.add_state('b')

    f.initial_state = 'H'

    for ii in xrange(10):
        if(ii==0):
            f.add_arc('H', 'T', [str(ii)],())
            f.add_arc('T', 'U', [str(ii)], ())
            f.add_arc('1H', 'TCent', [str(ii)], ())
            f.add_arc( 'TCent','U', [str(ii)], ())

        if(ii==1):
            f.add_arc('H', '1H', [str(ii)], [kFRENCH_TRANS[100]] )

        if(ii>1 and ii<10):
            f.add_arc('H', '29H', [str(ii)], [kFRENCH_TRANS[ii]])

        f.add_arc('U', 'U', [str(ii)], [kFRENCH_TRANS[ii]])

    for ii in xrange(1,10):   #all ten's digit numbers
        if(ii==1):
            f.add_arc('1H', '1', [str(ii)], ())
        elif(ii==7):
            f.add_arc('1H', str(ii), [str(ii)], [kFRENCH_TRANS[60]])
        elif(ii==8):
            f.add_arc('1H', str(ii), [str(ii)], [kFRENCH_TRANS[4]])
        elif(ii==9):
            f.add_arc('1H', str(ii), [str(ii)], [kFRENCH_TRANS[4]])
        else:
            f.add_arc('1H', str(ii), [str(ii)], [kFRENCH_TRANS[ii * 10]])

    for ii in xrange(1,10):
        f.add_arc('TCent', 'U', [str(ii)], [kFRENCH_TRANS[ii]])

    for ii in xrange(1,10):   #all ten's digit numbers
        if(ii==1):
            f.add_arc('T', '1', [str(ii)], ())
        elif(ii==7):
            f.add_arc('T', str(ii), [str(ii)], [kFRENCH_TRANS[60]])
        elif(ii==8):
            f.add_arc('T', str(ii), [str(ii)], [kFRENCH_TRANS[4]])
        elif(ii==9):
            f.add_arc('T', str(ii), [str(ii)], [kFRENCH_TRANS[4]])
        else:
            f.add_arc('T', str(ii), [str(ii)], [kFRENCH_TRANS[ii * 10]])

    for ii in xrange(2,10):    #all numbers 20,30,40,50,60,70,80,90
        if (ii==7):
            f.add_arc(str(ii),'7', [str(0)], [kFRENCH_TRANS[10]])
        elif (ii==8):
            dup =8
            dup+=1
            #f.add_arc(str(ii),'8a', [str(0)], [kFRENCH_TRANS[20]])  # 80 defined fully
        elif(ii!=8):
            f.add_arc(str(ii), str(ii), [str(0)], ())

    for ii in xrange(1,10): #all 21-29,31-39,41-49,51-59,61-69
        if (ii==1):
            f.add_arc(str(2), 'a', [str(1)], [kFRENCH_AND])
            f.add_arc(str(3), 'a', [str(1)], [kFRENCH_AND])
            f.add_arc(str(4), 'a', [str(1)], [kFRENCH_AND])
            f.add_arc(str(5), 'a', [str(1)], [kFRENCH_AND])
            f.add_arc(str(6), 'a', [str(1)], [kFRENCH_AND])
        else:
            f.add_arc(str(2), 'b', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc(str(3), 'b', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc(str(4), 'b', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc(str(5), 'b', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc(str(6), 'b', [str(ii)], [kFRENCH_TRANS[ii]])

    for ii in xrange(1,10):
        f.add_arc('8a', '8a',[str(ii)] , [kFRENCH_TRANS[ii]])    #81-89

    for ii in xrange(0,7):
     f.add_arc('9a', '9a', [str(ii)], [kFRENCH_TRANS[10+ii]])  # for 90-96

    f.add_arc('7', '71', [str(1)], [kFRENCH_AND])
    for ii in xrange(2,7):
     f.add_arc('7', '9a', [str(ii)], [kFRENCH_TRANS[10+ii]])  # for 90-96

    f.add_arc('9a', '9b', [str(7)], [kFRENCH_TRANS[10]])
    f.add_arc('9b', '9e', (), [kFRENCH_TRANS[7]])

    f.add_arc('9a', '9c', [str(8)], [kFRENCH_TRANS[10]])
    f.add_arc('9c', '9e', (), [kFRENCH_TRANS[8]])

    f.add_arc('9a', '9d', [str(9)], [kFRENCH_TRANS[10]])
    f.add_arc('9d', '9e', (), [kFRENCH_TRANS[9]])

    f.add_arc('7', '9b', [str(7)], [kFRENCH_TRANS[10]])
    #f.add_arc('9b', '9e', (), [kFRENCH_TRANS[7]])

    f.add_arc('7', '9c', [str(8)], [kFRENCH_TRANS[10]])
    #f.add_arc('9c', '9e', (), [kFRENCH_TRANS[8]])

    f.add_arc('7', '9d', [str(9)], [kFRENCH_TRANS[10]])
    #f.add_arc('9d', '9e', (), [kFRENCH_TRANS[9]])

    f.add_arc('29H', '1H', (), [kFRENCH_TRANS[100]])   # all epsilon transitions at last
    f.add_arc('a','b',(),[kFRENCH_TRANS[1]])
    f.add_arc('8','8a',(),[kFRENCH_TRANS[20]]) #add vingt to 8Y
    f.add_arc('71', '7f', (), [kFRENCH_TRANS[11]])

    f.add_arc('8a', '8a', [str(0)], ())  # for 80

    f.add_arc('9', '9a', (), [kFRENCH_TRANS[20]])  # add vingt to 9Y
    f.add_arc('1', '9a', (), ())


    f.set_final('U')
    f.set_final('2')
    f.set_final('3')
    f.set_final('4')
    f.set_final('5')
    f.set_final('6')
    f.set_final('7')
    f.set_final('7f')
    f.set_final('8a')
    f.set_final('b')
    f.set_final('9')
    f.set_final('9a')
    f.set_final('9e')




    return f

if __name__ == '__main__':
    string_input = raw_input()
    #string_input = "101"
    user_input = int(string_input)
    print user_input
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
        #print fsmutils.trace(f, prepare_input(user_input))
