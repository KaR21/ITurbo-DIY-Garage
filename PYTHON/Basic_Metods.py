from tokenize import Double


class BasicMethods:
    @staticmethod
    def askAnInt(message):
        number = int(input(message))
        return number
    
    @staticmethod
    def askAnDouble(message):
        number = float(input(message))
        return number
    
    @staticmethod
    def askAString(message):
        string = input(message)
        return string

    @staticmethod
    def validateDNI(number, letter):
        letter = letter.upper()
        result = number%23
        alphabet = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        if alphabet[result] == letter:
            return True
        else:
            return False
