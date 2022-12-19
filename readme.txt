step 1:
git clone https://github.com/edagmexico/szk-tp.git

git add readme.txt

git commit -m "Added first commit to szk project"

git push

step 2: 
create a branch

afgjherwghsgafsdmDXCFVGYIBHOJNKML

step 3:
demo for jhu zie work
git branch forJhuZie

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        x = columnNumber/26
        number = columnNumber%26
        columnName = []
        while(x > 26):
            columnName.append(char(x%26))
            x = int(columnNumber/26)
            number = x%26

        columnName.append(char(x%26))

        for i in range(len(columnName)):
            columnStr = columnStr + columnName[-1-i]

        return columnStr