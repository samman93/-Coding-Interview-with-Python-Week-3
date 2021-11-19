class Solution:
    def isNumber(self, s: str) -> bool:
        
        def sign(s):
            if s[0] in '+-':
                if s.count('+') + s.count('-') > 1 or len(s) == 1:
                    return ''
                s = s[1:]
            return s
        
        def checkDigits(s):
            for i in s:
                if not i.isdigit():
                    return False
            return True
        
        def checkInt(s):
            if not s:
                return False
            s = sign(s)
            if not s:
                return False
            return checkDigits(s)
        
        def decimal(s):
            if not s:
                return False
            s = sign(s)
            if not s:
                return False
            dot_count = s.count('.')
            if dot_count > 1 or dot_count == 1 and len(s) == 1:
                return False
            s = s.replace('.','')
            return checkDigits(s)
        
        x = s.split('e')
        if len(x) == 1:
            x = x[0].split('E')
        if len(x) > 2:
            return False
        elif len(x) == 2:
            return (checkInt(x[0]) or decimal(x[0])) and checkInt(x[1])
        else:
            return (checkInt(x[0]) or decimal(x[0]))
            
                
            
            
        