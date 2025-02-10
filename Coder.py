import string
class Coder :
    @staticmethod
    def code(x, y) :
        if x < 1 or y < 1 or x > 10 or y > 10 :
            return 'InvalidCoordinate'
        return string.ascii_uppercase[x - 1] + str(y)
    @staticmethod
    def decode(s) :
        x = string.ascii_letters.find(s[0])
        if x == -1 :
            return 'InvalidNotation'
        x = (x % 26) + 1
        if x > 10 :
            return 'InvalidNotation'
        s = s[1:]
        try:
            if int(s) < 1 or int(s) > 10 :
                return 'InvalidNotation'
            return [x, int(s)]
        except ValueError :
            return 'InvalidNotation'