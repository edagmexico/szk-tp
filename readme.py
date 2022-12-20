
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result = ""
        result_list=[]
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
        div=div/26
        print("temp: {}, result {}, div {}".format(temp, result_list, div))
        if (div>0 and div <= 26):
            result_list.append(equivalence_dict[temp-1])
            result_list.append(equivalence_dict[div-1])
            #result=equivalence_dict[div-1]+equivalence_dict[temp-1]
        else:
            result_list.append(equivalence_dict[temp-1])
            #result=equivalence_dict[temp-1]
        
        counter=0
        while div > 26:
            temp=div % 26
            div=div/26
            if (div>0 and div <= 26):
                result_list.append(equivalence_dict[temp-1])
                result_list.append(equivalence_dict[div-1])
                #result=equivalence_dict[div-1]+equivalence_dict[temp-1]
            else:
                result_list.append(equivalence_dict[temp-1])
            #if (div>0 and div <= 26):
            #    result+=equivalence_dict[div-1]+equivalence_dict[temp-1]
            #else:
            #    result+=equivalence_dict[temp-1]
            
            print("counter {}, temp {}, div {}, result {}".format(counter, temp, div, result_list))
            counter+=1
        #result =  result_list.reverse()
        result = result_list[::-1]
        return ''.join(result)
