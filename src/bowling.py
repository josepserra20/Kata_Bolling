
class Bolos:
    
    # Global variables
    X = 10
    DASH = 0
    SLASH = 10 

    def __init__(self, puntos):
        self.puntos = list(puntos)
        self.listConverter = Bolos.converter(self)

    def spare(self, index):
            spareScore = (Bolos.SLASH - self.listConverter[index-1]) + self.listConverter[index + 1]
            return spareScore

    def strike(self, index):
        strikeScore = Bolos.SLASH + self.listConverter[index + 1] + self.listConverter[index + 2]
        return strikeScore
        
    def converter(self):
        converterList = []
        for index, number in enumerate(self.puntos):
            if number.isdigit():
                converterList.append(int(number))
            if number == '-':
                converterList.append(Bolos.DASH)
            if number == 'X':
                converterList.append(Bolos.X)
            if number == '/':
                converterList.append(Bolos.SLASH - int((converterList[index - 1])))
        return converterList



    def score(self):

        # variables
        finalScore = 0
        frame = 0

        for index, number in enumerate(self.puntos):
            if frame < 18:
                if number.isdigit():
                    finalScore += int(number)
                    frame += 1
                if number == '/':
                    finalScore += Bolos.spare(self, index)
                    frame += 1
                if number == 'X':
                    finalScore += Bolos.strike(self, index)
                    frame += 2
                if number == '-':
                    frame += 1
            else:
                if number.isdigit():
                    finalScore += int(number)
                if number == 'X':
                    finalScore += Bolos.X
                if number == '/':
                    finalScore += (Bolos.SLASH - int(self.listConverter[index-1])) 
        return finalScore 

        
       




   



