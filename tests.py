import unittest
from soundex import letters_to_numbers, truncate_to_three_digits, add_zero_padding
from french_count import french_count, prepare_input
from morphology import generate

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.f1 = letters_to_numbers()
        self.f2 = truncate_to_three_digits()
        self.f3 = add_zero_padding()

        self.french = french_count()

    def test_letters(self):
        s = []
        try: self.assertEqual("".join(self.f1.transduce(x for x in "washington")), "w25235")
        except: s.append(1)
        try: self.assertEqual("".join(self.f1.transduce(x for x in "jefferson")), "j1625")
        except: s.append(2)
        try: self.assertEqual("".join(self.f1.transduce(x for x in "adams")), "a352")
        except: s.append(3)
        try: self.assertEqual("".join(self.f1.transduce(x for x in "bush")), "b2")
        except: s.append(4)

        print '\nNumber of failed letters tests:', str(len(s))
        if len(s)!=0: print 'Failed letters tests:', ','.join([str(x) for x in s])

    def test_truncation(self):
        s = []
        try: self.assertEqual("".join(self.f2.transduce(x for x in "a33333")), "a333")
        except: s.append(1)
        try: self.assertEqual("".join(self.f2.transduce(x for x in "123456")), "123")
        except: s.append(2)
        try: self.assertEqual("".join(self.f2.transduce(x for x in "11")), "11")
        except: s.append(3)
        try: self.assertEqual("".join(self.f2.transduce(x for x in "5")), "5")
        except: s.append(4)

        print '\nNumber of failed truncation tests:', str(len(s))
        if len(s)!=0: print 'Failed truncation tests:', ','.join([str(x) for x in s])

    def test_padding(self):
        s = []
        try: self.assertEqual("".join(self.f3.transduce(x for x in "3")), "300")
        except: s.append(1)
        try: self.assertEqual("".join(self.f3.transduce(x for x in "b56")), "b560")
        except: s.append(2)
        try: self.assertEqual("".join(self.f3.transduce(x for x in "c111")), "c111")
        except: s.append(3)

        print '\nNumber of failed padding tests:', str(len(s))
        if len(s)!=0: print 'Failed padding tests:', ','.join([str(x) for x in s])

    def test_numbers(self):
        s = []
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(1))), "un")
        except: s.append(1)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(100))), "cent")
        except: s.append(2)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(31))), "trente et un")
        except: s.append(3)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(99))), "quatre vingt dix neuf")
        except: s.append(4)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(300))), "trois cent")
        except: s.append(5)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(555))), "cinq cent cinquante cinq")
        except: s.append(6)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(101))), "cent un")
        except: s.append(7)
        try: self.assertEqual(" ".join(self.french.transduce(prepare_input(19))), "dix neuf")
        except: s.append(8)

        print '\nNumber of failed numbers tests:', str(len(s))
        if len(s)!=0: print 'Failed numbers tests:', ','.join([str(x) for x in s])

    def test_morphology(self):
        s = []
        try: self.assertEqual(generate("pack+s"), "packs")
        except: s.append(1)
        try: self.assertEqual(generate("ice+ing"), "icing")
        except: s.append(2)
        try: self.assertEqual(generate("frolic+ed"), "frolicked")
        except: s.append(3)
        try: self.assertEqual(generate("pace+ed"), "paced")
        except: s.append(4)
        try: self.assertEqual(generate("ace+ed"), "aced")
        except: s.append(5)
        try: self.assertEqual(generate("traffic+ing"), "trafficking")
        except: s.append(6)
        try: self.assertEqual(generate("lilac+ing"), "lilacking")
        except: s.append(7)
        try: self.assertEqual(generate("lick+ed"), "licked")
        except: s.append(8)

        print '\nNumber of failed morphology tests:', str(len(s))
        if len(s)!=0: print 'Failed morphology tests:', ','.join([str(x) for x in s])

if __name__ == '__main__':
    unittest.main()
