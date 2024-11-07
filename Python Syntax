def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    x = 7
    if x in nums:
        print("should be true")
    else: 
        print("should be false")

# print("should be true", any7([1, 2, 7, 4, 5]))
# print("should be false", any7([1, 2, 4, 5]))


____________________________________________________________________________________________________________________________



def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """

    # YOUR CODE HERE
    if unit_in != 'f' and unit_in != 'c':
        return 'Invalid unit in'
    if unit_out != 'f' and unit_out != 'c':
        return 'Invalid unit out'
    if unit_in == unit_out:
        return 'Invalid units in & out'
    if type(temp) is not int:
        return 'Invalid temperature'
    if unit_in == 'f' and unit_out == 'c':
        celcius = (temp - 32) * 5 / 9
        return celcius
    if unit_in == 'c' and unit_out == 'f':
        fahrenheit = temp * 9 /5 + 32
        return fahrenheit

# print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
# print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
# print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
# print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
# print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")



____________________________________________________________________________________________________________________________



def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    extra = stop + 1
    for num in range(start, extra):
        print(num)

# count_up(5, 7)    



____________________________________________________________________________________________________________________________



def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    for num in nums:
        if lowest <= num <= highest:
            print(f"{num} fits")

# in_range([10, 20, 30, 40, 50], 15, 30)  



____________________________________________________________________________________________________________________________




def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    x = 0
    for num in nums:
        x = x + num
    return x

# print("sum_nums returned", sum_nums([1, 2, 3, 4]))



____________________________________________________________________________________________________________________________



def print_upper_words(words, letters):
    """For a list of words, print out each word on a separate line, but in all uppercase."""
    for word in words:
        if word[0] in letters:
            print(word.upper())
