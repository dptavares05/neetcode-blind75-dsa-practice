class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalizedString = ""
        for c in s:# iterate trough the string
            if c.isalnum():# clear special character and spaces
                normalizedString += c.lower() # add the letter as a lowercase for the edge case of First letter being capitalized
        reversedString = normalizedString[::-1] # reverse the normalized string
        return reversedString == normalizedString # return the boolean verification


        