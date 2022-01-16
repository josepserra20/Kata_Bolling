
class Bolos:

    def __init__(self, puntos):
        self.puntos = list(puntos)

    def spare(self, index):
            listConverter = Bolos.converter(self)
            spareScore = (10 - int(listConverter[index-1])) + int(listConverter[index + 1])
            return spareScore

    def strike(self, index):
        listConverter = Bolos.converter(self)
        strikeScore = 10 + int(listConverter[index + 1]) + int(listConverter[index + 2])
        return strikeScore
        
    def converter(self):
        converterList = []
        for index, number in enumerate(self.puntos):
            if number.isdigit():
                converterList.append(number)
            if number == '-':
                converterList.append('0')
            if number == 'X':
                converterList.append('10')
            if number == '/':
                converterList.append(10 - int((converterList[index - 1])))
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
                    finalScore += 10
                if number == '/':
                    finalScore += (10 - int(Bolos.converter(self)[index-1])) 
        return finalScore 

        
       




   



