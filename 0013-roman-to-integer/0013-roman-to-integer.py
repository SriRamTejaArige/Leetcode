class Solution:
    def romanToInt(self, s: str) -> int:
        data={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        su=0
        pr=0
        for i in s:
            if(data[i]<pr):
                su+=data[i]
            elif(data[i]==pr):
                su+=data[i]    
            else:
                su+=data[i]-pr-pr
                
            pr=data[i]
        return su   
            