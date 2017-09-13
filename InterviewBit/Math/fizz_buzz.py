"""
Given a positive integer N, print all the integers from 1 to N. But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. Also for number which are multiple of 3 and 5, prints “FizzBuzz”.

Example

N = 5
Return: [1 2 Fizz 4 Buzz]
Note: Instead of printing the answer, you have to return it as list of strings.
"""

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        result = []
        for each in  xrange(1, A+1):
            if each %3 == 0 and each % 5 ==0:
                result.append('FizzBuzz')
            elif each %3 == 0:
                result.append('Fizz')
            elif each %5 ==0:
                result.append('Buzz')
            else:
                result.append(each)

        return result
