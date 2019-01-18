class fizz_buzz():

    def fizz_buzz_str(self, n=100):
        dict = fizz_buzz.fizz_buzz_dict(n)
        return str(dict.values())
        print(str(dict.values()))

    def fizz_buzz_dict(self, n=100):
        i = 1
        dict = {}
        while i < n:
            if i % 3 == 0 and not i % 5 == 0:
                dict[i] = "Fizz"
                print("Fizz")
                if i == 100:
                    break
                else:
                    i+=1
            if i % 5 == 0 and not i % 3 == 0:
                dict[i] = "Buzz"
                print ("Buzz")
                if i == 100:
                    break
                else:
                    i+=1
            if i % 3 == 0 and i % 5 == 0:
                dict[i] = "FizzBuzz"
                print("FizzBuzz")
                if i == 100:
                    break
                else:
                    i+=1
            else:
                dict[i] = str(i)
                print (i)
                if i == 100:
                    break
                else:
                    i+=1

        return(dict)
