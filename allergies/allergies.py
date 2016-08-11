import collections

class Allergies:
    lst = []
    def __init__(self, allergyScore):
        self.lst = []
        allergyList = collections.OrderedDict()
        allergyList['cats'] = 128
        allergyList['pollen'] = 64
        allergyList['chocolate'] = 32
        allergyList['tomatoes'] = 16
        allergyList['strawberries'] = 8
        allergyList['shellfish'] = 4
        allergyList['peanuts'] = 2
        allergyList['eggs'] = 1

        for allergy in allergyList:
            if ((allergyScore-allergyList[allergy]) >= 0):
                print allergy
                allergyScore -= allergyList[allergy]
                self.lst.append(allergy)
                print self.lst

    def is_allergic_to(self, allergy):
        if (allergy in self.lst):
            return True
        else:
            return False
