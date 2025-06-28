# Valid parenthesis


class Solution:

    def is_valid(self,str):
        self.st=[]

        if len(str)%2!=0:
            return False
        
        for ch in list(str):
            if ch == '(' or ch == '{' or ch == '[':
                self.st.append(ch)
            
            else:
                if len(self.st)==0:
                    return False
            
                top=self.st.pop()
                if ch == ')' and top!='(':
                    return False
                
                elif ch == ']' and top!='[':
                    return False
                
                elif ch == '}' and top!='{':
                    return False         

        if len(self.st)==0:
            return True
        else:
            return False
        

s = Solution()


print(s.is_valid("()"))         # True
print(s.is_valid("([{}])"))     # True
print(s.is_valid("({[)]}"))     # False
print(s.is_valid("((("))        # False

