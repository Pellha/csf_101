class Solution:
    def game (self, N, sur, des, aux):
        # sur == source, des == destination, aux == auxillary
        # Base case: If there is only one disk to move, move it directly from 'sur' to 'des'
        if N == 1:
          print("move disk " + str(N) + " from rod " + str(sur) + " to rod " + str(des))
          print("\n")
          return 1
        # Return 1 move made

        # Recursive case: Move N-1 disks from 'sur' to 'aux',using 'des' as an auxiliary rod
        moves = 0
        moves += self.game(N - 1, sur, aux, des) # Recursive call
        moves += 1 # Increment the total moves count for the current step
            # Move the remaining largest disk from 'sur' to 'des'
        print("move disk " + str(N) + " from rod " + str(sur) + "to rod " + str(des))
            # Recursive call: Move the N-1 disks from 'aux' to 'des', using 'sur' as an auxiliary rod 
        moves += self.game(N - 1, aux, des, sur) # Recursive call
        return moves # Return the total moves made for this step and all recursive steps
  
s = Solution()
print(s.game(3, 1, 3, 2))


#Time Complexity: O(2^N)
#Space Complexity: O(N)|
def tower_of_hanoi(n, source, target, auxillary): # lets say, n is number of desk, soucre is the place of desk, target is place where u will put the desk, auxillary is middle rod
    if n > 0:                                      # actually there are three rod, first one is source, middle is auxillary, last is target
                                              # n is greater than zero means that the function needs to moves or is operate recursive function. the function will keeping on operating untill the n become zero 
        tower_of_hanoi(n-1, source, auxillary,target)

        print("move disk", n-1, "from rod", source, "to rod", target )

        tower_of_hanoi(n-1, auxillary, target, source)

x = 3
tower_of_hanoi(x,1, 2, 3)