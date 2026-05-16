'''
problem:
given two string s1, s2, check whether s2 is rotation of s1 or not?
return:
True if s2 is rotation of s1, and False
'''

def areRotations(s1, s2):
    if s1 == s2:
        return True
    else:
        if len(s1) == len(s2):
            for i in range(1, len(s1)):
                # modified_str = s1[-i:] + s1[i:]
                modified_str = s1[i:] + s1[:i]
                if modified_str == s2:
                    return True
            return False
        else:
            return False

# s1 = "mightandmagic"
# s2 = "andmagicmigth"

# s1 = "geeksforgeeks"
# s2 = "forgeeksgeeks"

s1 = "rvvsvczyczqjojiovkpokdbaeggkqbchwxzucasgzlpquzeplvfvygxepdofftmdsnxunscpdthxslpdgub"
s2 = "vsvczyczqjojiovkpokdbaeggkqbchwxzucasgzlpquzeplvfvygxepdofftmdsnxunscpdthxslpdgubrv"
print(areRotations(s1, s2))

