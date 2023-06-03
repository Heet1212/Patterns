"""

Sample Input:

5
Sample Output:

    *
   ***
  *****
 *******
*********
"""

def star_pattern(n):
    '''input: n = An Integer value defines number of rows
       output: print triangle star pattern'''
    # YOUR CODE GOES HERE
    for i in range(n-1,-1,-1):

            for j in range(1,i+1):

                print(" ",end="")
            for k in range(1,2*(n-i)):
                print("*",end="")    

            print(end="\n")
