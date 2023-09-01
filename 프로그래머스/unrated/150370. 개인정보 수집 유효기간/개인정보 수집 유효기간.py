
def solution(today, terms, privacies):
    
    answer = []
    termDict = dict()
    
    for term in terms:
        temp = term.split()
        termDict[temp[0]] = int(temp[1])
        
    for i in range(len(privacies)):
        temp = privacies[i].split()
        tempDate = Date()
        tempDate.setDate(temp[0],termDict[temp[1]])
        tempDate.cal()
        if tempDate.check(today) == 0:
            answer.append(i+1)
    
    return answer

class Date:
    def setDate(self,date,remains):
        temp = date.split(".")
        self.year = int(temp[0])
        self.month = int(temp[1])
        self.day = int(temp[2])
        self.remains = remains
        
    def cal(self):
        
        self.day -= 1
        if self.day == 0:
            self.day = 28
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1
                
        self.month += self.remains
        if self.month > 12:
            temp = self.month // 12
            self.month = self.month % 12
            if self.month == 0:
                self.month = 12
                self.year -=1
            self.year += temp
        print(self.year,self.month,self.day)   
        
    def check(self,today):
        temp = today.split(".")
        bool = 1
        todayYear = int(temp[0])
        todayMonth = int(temp[1])
        todayDay = int(temp[2])
        if todayYear > self.year:
            bool = 0
        if todayYear == self.year and todayMonth > self.month:
            bool = 0
        if todayYear == self.year and todayMonth == self.month and todayDay > self.day:
            bool = 0
        return bool           
        
        