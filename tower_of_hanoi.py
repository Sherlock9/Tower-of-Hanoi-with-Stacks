"""
Tower of Hanoi code.
"""

def toh_stack(n):
    """ num -> None
    
    An implementation of my Tower of Hanoi code using stacks
    to store which pile currently hold which disk.
    
    Note: The disks always start on pile A.
    The disks always end on pile C.
    
    >>> toh(2)
    Pindah 1 ke B.
    Pindah 2 ke C.
    Pindah 1 ke C.
    """
    
    ## Initialize the piles. All of them begin on pile A
    pile_A = [i for i in range(n, 0, -1)]
    pile_B = []
    pile_C = []
    if n % 2:
        pointer = 1
    else:
        pointer = 0
    
    for turn in range(1, pow(2, n)):
        
        ## Always moves in the order AB, AC, BC
        ## stack_manip picks the next legal move for that pair
        if pointer == 0:
            ## Either A to B or B to A
            pile_A, pile_B, move, next_pos = stack_manip(pile_A, pile_B, 1, 2)
        elif pointer == 1:
            ## Either A to C or C to A
            pile_A, pile_C, move, next_pos = stack_manip(pile_A, pile_C, 1, 3)
        else: ## pointer == 2
            ## Either B to C or C to B
            pile_B, pile_C, move, next_pos = stack_manip(pile_B, pile_C, 2, 3)
            
        if n % 2:
            pointer = (pointer - 1) % 3
        else:
            pointer = (pointer + 1) % 3 # always 1, 2 or 3
        
        ## chr(next_pos + 64) returns either "A", "B" or "C"
        print("Pindah %d ke %s" % (move, chr(next_pos + 64)))
    
def stack_manip(first, second, pos_one, pos_two):
    """ (list, list, num, num) -> (list, list, num, num)

    A step in a Tower of Hanoi game, i.e. moving one token from
    one pile to another, using the only legal move between the two
    piles, first and second provided in the parameters.

    pos_one and pos_two are used to help with the printing of the
    next move when the functions returns to toh_stack(n).

    >>> stack_manip([3, 2, 1], [], 0, 1)
    ([3, 2], [1], 1, 1)
    >>> stack_manip([1, 5], [3, 4], 1, 2)
    ([5], [1, 3, 4], 1, 2)
    """
    
    ## If one of the piles is empty, move a disk from the non-empty pile
    ## Note that if two piles are empty, it can only be because all of the 
    ## disks are on the third pile, i.e. that the puzzle is solved.
    if len(first) == 0:
        move = second.pop()
        first.append(move)
        next_pos = pos_one
    elif len(second) == 0:
        move = first.pop()
        second.append(move)
        next_pos = pos_two
    ## If both piles have disks, pop the disks at the top of each pile
    ## compare them, and move the smaller disk on top of the larger disk
    else:
        a = first.pop()
        b = second.pop()
        if a < b:
            move = a
            second.append(b)
            second.append(move)
            next_pos = pos_two
        else:
            move = b
            first.append(a)
            first.append(move)
            next_pos = pos_one
            
    ## Return the current state of the two piles
    ## the number of the disk that was moved,
    ## and the pile onto which the disk was moved
    return first, second, move, next_pos

def main_menu():
    num = input("Masukkan berapa disk untuk tumpukan? ")
    num = int(num)
    toh_stack(num)
    
main_menu()