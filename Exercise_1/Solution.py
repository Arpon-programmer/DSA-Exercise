print('First>>>>')
Expense={'January':2200,'February':2350,'March':2600,'April':2130,'May':2190}

#1. In Feb, how many dollars you spent extra compare to January?
print('Question 1.')
for month in Expense:
    if Expense[month] > Expense['January']:
        print(f"In {month} I spent {Expense[month]-Expense['January']} extra compare to January.")


#2. Find out your total expense in first quarter (first three months) of the year.
print('\nQuestion 2.')
print(f"My total expense in first quater is {Expense['January']+Expense['February']+Expense['March']}.")

#3. Find out if you spent exactly 2000 dollars in any month
print('\nQuestion 3.')
for month in Expense:
    if Expense[month] == 2000:
        print(f"I spent exactly 2000 dollars in {month}.")

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print('\nQuestion 4.')
Expense['June']=1980
print(Expense['June'])

#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
print('\nQuestion 5.')
Expense['April']=Expense['April']-200
print(f"Corrected Expense of April {Expense['April']}")

print('\nSecond>>>>')
heros=['spider man','thor','hulk','iron man','captain america']
#1. Length of the list
print('Question 1.')
print(f"Length of the list is {len(heros)}.")
#2. Add 'black panther' at the end of this list
heros.append('black panther')
print('\nQuestion 2.')
print(heros)
#3. You realize that you need to add 'black panther' after 'hulk'.so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print('\nQuestion 3.')
print(heros)
#4. Now you don't like thor and hulk because they get angry easily :)
       #So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       #Do that with one line of code.
heros[1:3]=['doctor strange']
print('\nQuestion 4.')
print(heros)
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
print('\nQuestion 5.')
heros.sort()
print(heros)


print('\nThird>>>>')
#3. Create a list of all odd numbers between 1 and a max number.
    #Max number is something you need to take from a user using input() function
n=int(input('Give the length : '))
odd_list=[]
for i in range(1,n+1):
    if i%2!=0:
        odd_list.append(i)
print(odd_list)