#Chris Jones and Anton Foretich
#ISAT 252
#Mini Project
#Python 3.6.3

#Import math and time

import math
import time

# Define universal variables
DecayConstant=0.693
DisposalConstant=37.00



#Define main function and print output
def main():
    #Define variables in main
    element=int(input("Enter 1 for phosphorus-32, Enter 2 for chromium-51, Enter 3 to quit: "))
    #Change time between each line printed
    seconds=.25
    #Give user option to quit program
    while element != 3:
        #Give user option to choose isotope
        if (element == 1 or element == 2):
            #Phosphorus-32
            if element == 1:
                isotope_half_life=14.262
                #Input variables for A0 and M
                A0=float(input("What is the value of the initial activity of the radio isotope? "))
                M=float(input("What is the mass of the radio isotope? "))
                #Define functions
                days_to_safe_level = get_days_to_safe_level(isotope_half_life, A0, M)
                safe_activity_level = get_safe_activity_level(isotope_half_life, A0, M, days_to_safe_level)
                new_isotope_activity=A0
                new_isotope_activity = get_new_isotope_activity(safe_activity_level,A0, isotope_half_life, new_isotope_activity)
                print('The safe activity level for the P isotope is ',safe_activity_level)       
                print("The days until the isotope reaches a safe activity level is ", format(days_to_safe_level, ".0f"))
                element=int(input("Enter 1 for phosphorus-32, Enter 2 for chromium-51, Enter 3 to quit: "))
            #Chromium-51
            elif element== 2:
                isotope_half_life=27.7025
                #Input variables for A0 and M
                A0=float(input("What is the value of the initial activity of the radio isotope? "))
                M=float(input("What is the mass of the radio isotope? "))
                #Define Functions
                days_to_safe_level = get_days_to_safe_level(isotope_half_life, A0, M)
                safe_activity_level = get_safe_activity_level(isotope_half_life, A0, M, days_to_safe_level)
                new_isotope_activity=A0
                new_isotope_activity = get_new_isotope_activity(safe_activity_level,A0, isotope_half_life, new_isotope_activity)
                print('The safe activity level for the P isotope is ',safe_activity_level)       
                print("The days until the isotope reaches a safe activity level is ", format(days_to_safe_level, ".0f"))
                element=int(input("Enter 1 for phosphorus-32, Enter 2 for chromium-51, Enter 3 to quit: "))
        else:
            print("Invalid Choice")
            element=int(input("Enter 1 for phosphorus-32, Enter 2 for chromium-51, Enter 3 to quit: "))
    #Input time function to change seconds between printed statements
    time.sleep(seconds)
#Define function for the days it takes to reach a safe level               
def get_days_to_safe_level(isotope_half_life, A0, M):
    days_to_safe_level = -(isotope_half_life/DecayConstant)*math.log(DisposalConstant/(A0/M))
    return days_to_safe_level

#Define function for a safe activity level
def get_safe_activity_level(isotope_half_life, A0, M, days_to_safe_level):
    safe_activity_level=A0*math.exp(-(DecayConstant*days_to_safe_level/isotope_half_life))
    return safe_activity_level

#Define function for new activity level
def get_new_isotope_activity(safe_activity_level,A0, isotope_half_life, new_isotope_activity):
    #Create variable for days
    i=0
    #Change time between each line printed
    seconds=.25
    #Create loop for activity level
    while new_isotope_activity > safe_activity_level:
        print("The activity level on day", i,"is", format(new_isotope_activity, ".4f"))
        #Input time function to change seconds between printed statements
        time.sleep(seconds)
        new_isotope_activity=new_isotope_activity*math.exp(-(DecayConstant/isotope_half_life))
        #Increment Days
        i+=1

#Call main function
main()
