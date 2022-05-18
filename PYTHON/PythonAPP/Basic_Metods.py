import pickle
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
    def searchByID(fileName, dni):
        inp = open(fileName, 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                cont = 0
        i = 0
        answer = -1
        for st in objects:
            if st.dni == dni:
                answer = i
            i = i + 1
        return answer
    
    @staticmethod
    def searchByBookingID(fileName, id):
        inp = open(fileName, 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                cont = 0
        i = 0
        answer = -1
        for st in objects:
            if st.id == id:
                answer = i
            i = i + 1
        return answer
    
    @staticmethod
    def readFile(fileName):
        inp = open(fileName, 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                cont = 0
        for st in objects:
            print(st.toString())

    @staticmethod
    def askForFile():
        fileName = BasicMethods.askAString("Enter the file name: ")
        return fileName

    @staticmethod
    def save_objectOn_File(obj,filename):
        with open(filename, 'ab') as outp:  # Overwrites any existing file.
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
        del obj    
    
    @staticmethod
    def save_objectOn_FileWB(obj,filename):
        with open(filename, 'wb') as outp:  
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)
        del obj   
        
    @staticmethod
    def readFileToList(fileName):
        inp = open(fileName, 'rb')
        objects = []
        cont = 1
        while cont == 1:
            try:
                objects.append(pickle.load(inp))
            except EOFError:
                cont = 0
        
        return objects
    
    @staticmethod  
    def reWriteTheObjects(fileName, obj):
        count = 0
        for st in obj:
            if count == 0:
                BasicMethods.save_objectOn_FileWB(st,fileName)
            else:
                BasicMethods.save_objectOn_File(st,fileName)
            count = count + 1
