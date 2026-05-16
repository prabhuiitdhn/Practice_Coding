"""
https://practice.geeksforgeeks.org/problems/finding-profession3834/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

problem: we do have an family chain and needed to find the profession of family in nth level of family
starting the profession "Engineer", every profession have two child and first child always chose the profession of her/his parent and another child choose the opposite of parent's profession

level 1:   E # starting the family profession as "Engineer", It has two child and first child is following parent's profession as Engineer and second as "Doctor
level 2:  E D # in level 2, level 1 parent have 2 child by profession as Engineer, and Doctor
lecvel3:E D D E # in level 3, Each children has two children which follows parent profession and opposite of it.

Problem: needed to find the nth profession of nth level family's chain with position.
"""



# this is based on recursion and it fails for so so long level and position so, another approach is being used using setbit
def profession(level, pos):
    """
    Approach: this is simple approach
    each position will have parent in level-1 level.
    and if pos is first child of parent in level-1 level the follows the same profession else another profession.

    @param n: no of level
    @param k: in nth level, kth element in the string
    @return: return nth elements in k
    """

    if pos == 1:
        return "E"
    else:
        # choosing the parent profession
        parent = profession(level - 1, (pos + 1) // 2)
        if pos % 2 == 1:
            # first child the parent in level n-1 at position k/2
            return parent
        else:
            # second child of parent in level n-1 at position k/2+1
            if parent == "E":
                return "D"
            else:
                return "E"


# if recursion approach fails in the case of so so long level and position. set bit is being used for solving this.
# countSet bits is finding 1
def profession2(level, pos):
        # code here
        def countSetBits(n):
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count

        # no of bit require to flip to reach to the end.
        c = countSetBits(pos - 1)

        # If set bit count is odd, then doctor, else engineer
        if c % 2 == 0:
            return 'e'
        else:
            return 'd'

print(profession(5, 4))
