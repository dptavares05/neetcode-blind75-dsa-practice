class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMapping = { "}" : "{", "]" : "[", ")" : "(" } # mapp every closing parenthesis to its respective open parenthesis

        for eachCharacter in s: # for every character in the input string
            if eachCharacter in hashMapping: # check if this character is a closing parenthesis
                if stack and stack[-1] == hashMapping[eachCharacter]: # check if the stack isn't empty and the top of the stack is a closing parenthesis
                    stack.pop()
                else:# if the stack is empty or closing parenthesis doesnt match the last opening parenthesis
                    return False # then it means that the string is invalid
            else: # then its an opening parenthesis
                    stack.append(eachCharacter) # we add as many opening parenthesis as possible
        return True if not stack else False # its a valid string only if the stack is empty
                


