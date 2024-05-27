def sum_of_digits(n):
        if n < 10: #base case: if n is a single-digit number, return n
                return n 
        else:   # recursive case: calculate the sum of the digits
                last_digit = n % 10   # get the last digit of n
                remaining_digits = n // 10   # get the remaining digits by integerdivision with 10

                return last_digit + sum_of_digits(remaining_digits)   # recursively call the function with the remaining digits 
                                                                      # and add the last digit to the result


print(sum_of_digits(123))