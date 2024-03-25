
#PART-A
#QUESTION 1 and 2
''' 
    A Function called Total_Combination() is a simple function that returns all possible combinations of 2 dice is created 
    It also finds the Total number of Possible combinations.

'''
def Total_Combinations():
    combinations=[]
    print("The possible Combinations are:\n")
    for die1 in range(1,7):
        for die2 in range(1,7):
            combinations.append((die1,die2))
            print("(",die1,",",die2,")", end = "    ")
        print()
    print("\nThe Total number of possible combinations =", len(combinations))
    return combinations

Combi= Total_Combinations()



#QUESTION 3
'''
The Probability_sum() function finds sum of the each element in combinations list and stores it as a dictionary called probability

'''

def Probability_sum(die1,die2):
    sum=[]      #Possible sum value is stored here
    for element in Combi:
        if element[0]+element[1] not in sum:
            sum.append(element[0]+element[1])
    
    probab=[]       #probability of each sum value is stored here
    for value in sum:
        count=0
        for comb in Combi:
            if comb[0]+comb[1]==value:
                count+=1
        p=round(count/len(Combi),4)
        probab.append(p)
    
    probability={}      #sum is mapped to corresponding probability and is stored here
    for i in range(len(sum)):
        probability[sum[i]]=probab[i]
    print("\nThe Sum value and the corresponding probablity value is" , probability)




#PART B
import random
def undoom_dice(die1,die2):
    '''
    The conditions for die_A is that it can have repeating number of spots
    It can have values not more than 4
    Therefore die_A can have any combination of numbers between 1,2,3,4.
    '''
    
    new_die_A=[1,2,3,4]
    for i in range(2):
        new_die_A.append(random.randrange(1,5))

    '''
    For new_die_B, since we are calculating the probability based off the sum, 
    the sum will be unchanged if we add the difference between the new value and the old value of first die and 
    then add it to the second die value 

    '''
        
    
    new_die_B=[]
    for i in range(6):
        d2=die1[i]-new_die_A[i]+die2[i]
        if d2>0:
            new_die_B.append(d2) 
        else:                           #To avoid negative value we change the value of new A 
            d=new_die_A[i]-die1[i]
            new_die_A[i]=d
            new_die_B.insert(i,die2[i])
    print("The new die A: ",new_die_A)
    print("The new die B: ",new_die_B)

    #checking if the probability remains unchanged
    Probability_sum(new_die_A,new_die_B)


#main program
    

die1=[1,2,3,4,5,6]
die2=[1,2,3,4,5,6]
Probability_sum(die1,die2)
print("\nThe new dice values :\n")
undoom_dice(die1,die2)


