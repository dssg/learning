import os
import cPickle as pickle
import time
import sys

def demo_pickling():
    #Pretend that this function spent a lot of time calculating something
    def compute_tricky_thing():
        toR = []
        for i in range(5):
            toR.append(i)
            time.sleep(1)

        return toR

    def run_demo():
        print "Computing tricky thing..."; sys.stdout.flush()
        tricky_thing = compute_tricky_thing()
        print "Computed!"; sys.stdout.flush()

        #After computing the tricky thing, we save it to disk (to read it in later).
        dump_file = open("demo_tricky_thing.pkl", "wb")
        pickle.dump(tricky_thing, dump_file)
        dump_file.close()

        #Now that it's later, let's read in the object from the file.
        in_file = open("demo_tricky_thing.pkl")
        print "Loading tricky thing..."; sys.stdout.flush()
        tricky_thing_2 = pickle.load(in_file)
        print "Loaded!"; sys.stdout.flush()
    run_demo()










def demo_list_comprehensions():
    #A simple recursive quick-sort implementation.
    def qsort(L):
        if L == []:
            return []
        left = [x for x in L if x < L[0]]
        '''This is equivalent to:
        left = []
        for x in L:
            if x < L[0]:
               left.append(x)
            else:
               pass
        '''
        right = [x for x in L if x > L[0]]
        return qsort(left) + [L[0]] + qsort(right)

    def run_demo():
        mylist = [6, 1, 5, 2, 7, 3, 9, 4]
        print "Original list:", mylist
        sorted = qsort(mylist)
        print "Sorted list:", sorted

    run_demo()
















def demo_justify():
    names = ["Bob", "Sir Williams", "Kenneth", "Jo"]
    animals = ["Fish", "Cat", "Platypus", "Canadian Tree Frog"]

    #Let's print things in a silly way
    def without_just():
        for name in names:
            print name,
        print "\n",
        for animal in animals:
            print animal,
        print "\n",
                    
    def with_just():
        lspace = 15
        for name in names:
            print name.ljust(lspace),
        print "\n",

        for animal in animals:
            print animal.ljust(lspace),
        print "\n",

    def run_demo():
        print "Without justification:"
        without_just()
        print "\n"

        print "With justification:"
        with_just()
        
    run_demo()













def demo_kwargs():
    
    def describe_person_1(name, age, weight, height, personality, enroll_date):
        print name, "is", age, "years old."
        print name, "is", height, "feet tall and weighs", weight, "pounds."
        print name, "has been", personality, "ever since", enroll_date
        
    def describe_person_kwargs(name, **kwargs):
        if "age" in kwargs:
            print name, "is", kwargs["age"], "years old."
        if "height" in kwargs and "weight" in kwargs:
            print name, "is", kwargs["height"], "feet tall and weighs", kwargs["weight"], "pounds."
        if "personality" in kwargs and "enroll_date" in kwargs:
            print name, "has been", kwargs["personality"], "ever since", kwargs["enroll_date"]


    def run_demo():
        describe_person_1("Joe", 20, 6, 210, "January 12th", "happy")
        print "\n"
        print "Enter any key to continue",
        sys.stdout.flush()
        raw_input()
        describe_person_kwargs("Joe", age = 20, weight = 210, height = 6, personality = "happy", enroll_date = "January 12th")
        print "\nEnter any key to continue",
        sys.stdout.flush()
        raw_input()
        
        print "\n"
        describe_person_1("Joe", height = 6, personality = "happy", enroll_date = "January 12th", weight = 210, age = 20)
        
    run_demo()










def demo_unpacking():
    def get_mag(x, y):
        return x**2 + y**2

    def run_demo():
        my_xs = [1, 5, 7, 2, 3]
        my_ys = [2, 3, 4, 1, 2]
        my_points = zip(my_xs, my_ys)
        print "My points are:"
        print my_points
        print "Their mags are:"
        for p in my_points:
            print get_mag(*p),
        print "\n",
    run_demo()













def demo_error_handling():
    def divide(a, b):
        try: #This code may raise an exception
            print "Dividing:", a, " and ", b 
            result = a / b
        except ZeroDivisionError: #If it does, we catch it here
            print "no." #and print this
        else:
            print "The result is:", result #If it instead throws no exception, we do this
        finally:
            print "So there you go."#No matter what, we do this.
    
    def run_demo():
        divide(1.4, 2.0)
        print "\n"
        divide (1.0, 0)
    run_demo()
















def demo_generators():
    def faulty_function():
        for i in range(10): #Useless loop -- this function always returns 0
            return i 

    def gen():
        for i in range(10):
            yield i #This bit is the key. We 'yield' i, rather than returning it 

    def run_demo():
        for i in range(3):
            print "From faulty function:", faulty_function()
        mygen = gen()
        for i in range(3):
            print "From generator:", mygen.next()
        for i in mygen:
            print "And again:", i
            
    run_demo()











def demo_decorators():    
    #A decorator takes a function as an argument.
    #It returns a function (in this case, toR).
    #Calling foo(a, b, c), when foo is decorated with bar, is equivalent to calling:
    #   bar(foo)(a, b, c)
    def dec_data_writer(f):
        def toR(*args, **kwargs):
            foutn = args[-1]
            if os.path.exists(foutn):
                print "File [" + foutn + "] already exists"
                pass
            else:
                return f(*args, **kwargs)
        return toR

    @dec_data_writer #The @ symbol is how to decorate make_data_1 with dec_data_writer
    def make_data_1(a, b, foutn):
        fout = open(foutn, "wb")
        fout.write(str(a + b))
        fout.write("\n")
    
    @dec_data_writer
    def make_data_2(a, b, c, d, foutn):
        fout = open(foutn, "wb")
        fout.write(str(a + b + c + d))
        fout.write("\n")


    def run_demo():
        make_data_1(1, 2, "out1.txt")
        make_data_2(3, 4, 5, 6,  "out2.txt")
    run_demo()


if __name__ == "__main__":    
    myswitch = {"p": demo_pickling,\
                    "l": demo_list_comprehensions,\
                    "j": demo_justify,\
                    "k": demo_kwargs,\
                    "u": demo_unpacking,\
                    "e": demo_error_handling,\
                    "d": demo_decorators,\
                    "g": demo_generators}
    while (True):
        print "--------------------------------------------"
        print "Please Enter A Command:"
        print "\tp: Pickling Demo"
        print "\tl: List Comprehension Demo"
        print "\tj: Justification Demo"
        print "\tk: Keyword Arguments Demo"
        print "\tu: Arugment Unpacking Demo"
        print "\te: Error Handling Demo"
        print "\tg: Generators Demo"
        print "\td: Decorators Demo"
        print "\tq: Exit"
        print "--------------------------------------------"
        
        print "Your command: ", 
        sys.stdout.flush()
        cmd = raw_input()
        
        if cmd == "q":
            exit()
        elif cmd in myswitch.keys():
            myswitch[cmd]()
            sys.stdout.flush()
        else:
            print "Command not Recognized"
            sys.stdout.flush()
