# Pongdej Masodee
# This program will keep track of balance and monthly Income/Expense  ,
# Program will separate into a function,

#main()
def main(): 
    file_name = input("Enter the file that you want to read: ")

    ReadFile(file_name)
    data = ReadFile(file_name)
    
    #Let user choose the choice
    while True:
        
       choice = Menu()
       if choice == 1:
         CheckBalance(data["Balance"]) 
      
       elif choice== 2:
         income=AddIncome(data)
         data['Balance'] += income # Income + balance = Updated balannce
       elif choice == 3:
         expense = AddExpense(data)
         data['Balance'] -= expense # Income - balance = Updated balannce
       elif choice == 4:
         MonthlyTotal(data)
       elif choice == 5:
         PrintStatement(data)
       elif choice == 6:
         StatementToFile(data)
         
       elif choice == 7:
         data['Month'] = NewMonth(data['Month'], data)  
       elif choice == 8:
         data["Name"]= ChangeName()   
       elif choice == 9:
         SaveToFile(data,file_name)
         break
      
def ReadFile(file_name):
   data_file = open(file_name,'r') 
   data_dict = {"Name":"","Balance":0,"Month":"","Expense":{},"Income":{} } # Create a nested dict. 
   count = 0 
   for lines in data_file: 
       data = lines.split() # Make a list
       s = lines.split("$")
       
       for _ in data:
        if count == 0:
          name = data[0]+" "+data[-1] 
          data_dict["Name"] = name # Assign value = name into a key["Name"]
        elif count == 1:
          balance = data[0]
          data_dict["Balance"] = float(balance)  #Assign value = balance into a key["Balance"]
        elif count == 2:
          month = data[0]+" "+data[-1]
          data_dict["Month"] = month #Assign month = balance into a key["Month"]
        elif count > 2 :
            for _ in range(len(s)):
              num = float(s[-1])
              if num > 0:
                
                 data_dict["Income"][s[0].strip()]= float(s[-1])#Nested dictionary.
              else:
                 data_dict["Expense"][s[0].strip()]= float(s[-1])#Nested dictionary.
            
       count +=1 #Count the line and increased the value by 1. 
    
   data_file.close() 
   return(data_dict)
   
def Menu():

 print("""\nThe available operations are:\n 
1. Check balance
2. Add income
3. Add an expense
4. Check monthly total
5. View monthly statement
6. Save monthly statement to file
7. Change to a new Month
8. Change Name
9. Exit \n""")
 choice = int(input("Choose one from the options above: "))
 return choice

def CheckBalance(balance):   # Check balance without changing any value yet. 
     
  print("Your balance is : $%0.2f" % balance)
   
def AddIncome(data): #User can add income into the nested dictionary. 
   source = input("Enter the source of income: ")
   amount = int(input("Enter the amount of income : "))
   if source in data["Income"]:
       data["Income"][source] += amount
   else:
       data["Income"][source] = amount
   return  amount
 
def AddExpense(data): #User can add expense into the nested dictionary. 
   source = input("Enter the expense: ")
   amount = int(input("Enter the expense amount : "))
   if source in data["Expense"]:
       data["Expense"][source] -= amount
   else:
       data["Expense"][source] = -amount
   return amount
def MonthlyTotal(data):  #Calculate monthly total. 
   expense_total = 0
   income_total = 0
   for i in data["Expense"]:
       expense_total += data["Expense"][i] 
   for i in data["Income"]:   
       income_total += data["Income"][i] 
   total = expense_total + income_total
   print("Your total amount is : $%0.2f" % total)
    
def PrintStatement(data): #Print staetment to display.
    print("\n"+data["Name"]+"                           "+data["Month"]) 
    print("\n\nMonthly Statement")      
    print("\n---------------------------------------------------------------------------")
    print("Name","-----------------------------------------------------------","Amount")
    print("---------------------------------------------------------------------------")
    for (key,value) in data["Expense"].items():  
     print ("%-50s%10s" % (key,value))
    for (key,value) in data["Income"].items():  
     print ("%-50s%10s" % (key,value))
    print("\n\nYour total balance is : $%0.2f" % data["Balance"])
    
def StatementToFile(data): #Save statement to file.
    monthly_slip = input("\n Enter file name : ") 
    bank_file = open(monthly_slip, 'w')
    bank_file.write("\n"+data["Name"]+"                 "+data["Month"])
    bank_file.write("\n\nMonthly Statement")     
    bank_file.write("\n---------------------------------------------------------------------------")
    bank_file.write("\nName"+"-----------------------------------------------------------"+"Amount")
    bank_file.write("\n---------------------------------------------------------------------------")
    for (key,value) in data["Expense"].items():  
      bank_file.write("\n%-50s%10s" % (key,value))
    for (key,value) in data["Income"].items():  
      bank_file.write ("\n%-50s%10s" % (key,value))
    bank_file.write("\n\nYour total balance is : $%0.2f" % data["Balance"])
   
    bank_file.close() 

def NewMonth(month, data): # Change to the new month, save the file, clear the data, start the new one.
    bank_file = open(month+'.txt','w')
    bank_file.write("\n"+data["Name"]+"                 "+data["Month"])
    bank_file.write("\n\nMonthly Statement")     
    bank_file.write("\n---------------------------------------------------------------------------")
    bank_file.write("\nName"+"-----------------------------------------------------------"+"Amount")
    bank_file.write("\n---------------------------------------------------------------------------")
    for (key,value) in data["Expense"].items():  
      bank_file.write(key+value)
    for (key,value) in data["Income"].items():  
      bank_file.write(key+value)
    bank_file.write("\n\nYour total balance is : $%0.2f" % data["Balance"])
   
    bank_file.close()
    months = ["January","February","March","April","May","June","July","August",
   "September","October","November","December"]
    for i in range(len(months)): #Loop through the list. 
       if months[i] in data["Month"]:#Compare which month = the ending month
           new_month = months[i+1] #Set the new month, according to last month array position.
    data["Income"].clear()
    data["Expense"].clear()
    return(new_month)
    
     
      
def ChangeName(): # Change the name.
   new_name = input("\nEnter new name: ")
   return new_name
  
def SaveToFile(data,file_name): # Save the file before exit.
       
    bank_file = open(file_name, 'w')
    data["Name"]= ChangeName()
    bank_file.write(data["Name"]+'\n')
    bank_file.write(str(data["Balance"])+'\n')
    bank_file.write(data["Month"]+'\n')
   
    bank_file.close() 
   
if __name__ == "__main__":
   main()
