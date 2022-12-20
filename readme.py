
Hola mundo
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        equivalence_dict={}
        alphabet = list(string.ascii_uppercase)
        print("alphabet: {}".format(alphabet))
        print("len_ alphabet {}".format(len(alphabet)))
        for key in range(len(alphabet)):
            equivalence_dict[key] = alphabet[key]
        print("equivalence_dict: {}".format(equivalence_dict))
        print("columnNumber: {}".format(columnNumber))
        div=columnNumber
        temp=columnNumber % 26
        print("temp: {}".format(temp))
        counter=0
        while temp != 0:
            div=div / 26
            temp=div % 26
            print("counter {}, temp {}, div {}".format(counter, temp, div))
            counter+=1
        return "AA"
