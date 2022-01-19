
class Bolos:
    
    # Global variables
    X = 10
    DASH = 0

    def __init__(self, puntos):
        self.puntos = list(puntos)
        self.listConverter = Bolos.converter(self)

    def spare(self, index):
        return (Bolos.X - self.listConverter[index - 1]) + self.listConverter[index + 1]

    def strike(self, index):
        return Bolos.X + self.listConverter[index + 1] + self.listConverter[index + 2]
        
        
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
                converterList.append(Bolos.X - int((converterList[index - 1])))
        return converterList

    def score(self):

        # variables
        finalScore = 0
        roll = 0

        for index, number in enumerate(self.puntos):
            if roll < 18:
                if number.isdigit():
                    finalScore += int(number)
                    roll += 1
                if number == '/':
                    finalScore += Bolos.spare(self, index)
                    roll += 1
                if number == 'X':
                    finalScore += Bolos.strike(self, index)
                    roll += 2
                if number == '-':
                    roll += 1
            else:
                if number.isdigit():
                    finalScore += int(number)
                if number == 'X':
                    finalScore += Bolos.X
                if number == '/':
                    finalScore += (Bolos.X - int(self.listConverter[index-1])) 
        return finalScore 

        
       




   



