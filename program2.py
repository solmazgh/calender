'''Write a program using lists and functions that allows the user to select a month and then displays how many days are in that month.  It does this by "looking up" information it has stored in the Lists.'''
monthname=["JANUARY","FEBRUARY","MARCH", "APRIL", "MAY","JUNE","JULY", "AUGUST","SEPTEMBER","OCTOBER","NOVEMBER",
"DECEMBER"]  
monthday=[31,28,31,30,31,30,31,31,30,31,30,31];
month=input("please enter the month: ")
for i in monthname:
    if month.upper()==i:
        print("You have chosen the month" , month )
        
    
if month.upper() == "JANUARY":
        day= 31
        
        print("This month has "+str(monthday[0])+" days")
elif month== "FEBRUARY":
        day =28
        
        print("This month has "+str(monthday[1])+" days")
elif month.upper()== "MARCH":
        day=31
         
        print("This month has "+str(monthday[2])+" days")
elif month.upper()=="APRIL":
        day=30
        
        print("This month has "+str(monthday[3])+" days")
elif month.upper()=="MAY":
        day=31
        
        print("This month has "+str(monthday[4])+" days")
elif month.upper() == "JUNE":
        day=30
        
        print("This month has "+str(monthday[5])+" days")
elif month.upper() =="JULY":
        day=31
        
        print("This month has "+str(monthday[6])+" days")
elif month.upper() == "AUGUST":
        day=31
        
        print("This month has "+str(monthday[7])+" days")
elif month.upper()== "SEPTEMBER":
        day= 30
        
        print("This month has "+str(monthday[8])+" days")
elif month.upper()== "OCTOBER":
        day =31
        
        print("This month has "+str(monthday[9])+" days")
elif month.upper()=="NOVEMBER":
        day=30
        
        print("This month has "+str(monthday[10])+" days")
elif month.upper()=="DECEMBER":
        day=31
        
        print("This month has"+str(monthday[11])+" days")