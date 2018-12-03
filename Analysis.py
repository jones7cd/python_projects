def main():
    numbers = get_values()
     
    get_analysis(numbers)
    
def get_values():
    print('Please Enter A Series Of 20 Random Numbers')
    values =[]    
    for i in range(20):
        value =(int(input("Enter A Random Number " + str(i + 1) + ": ")))
        values.append(value)                 
    return values

def get_analysis (numbers):

 

    print("The Lowest Number Is:",  min(numbers))
    

    print("The Highest Number Is:", max(numbers))
    

    print("The Sum The Numbers Is:", sum(numbers))
   

    print("The Average The Numbers Is:", sum(numbers)/len(numbers))
 
main()
