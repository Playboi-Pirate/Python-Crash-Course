#What is a list
print("What is a list SECTION")
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
#Accessing elements in a List
print("Accesing elements in a list Section")
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(f"I like {bicycles[2].title()}")
#Position starts at 0
print("Position starts at 0 Section")
print(bicycles[-1])# This command brings the last element in the list
#Using Individual Values from a list
Message=f"My first bike was a {bicycles[-1].title()} Bike"
print(Message)
#Try it Youself
print("Try it yourself Section")
#3-1
print("3-1 section")
names=['Demii','Key','Dey','Donnie','Larry']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
#3-2
print("3-2 section")
print(f"You are the coolest,{names[0]}.")
print(f"I know more about cars than you,{names[1]}.")
print(f"Want to play the game tonight,{names[2]}.")
print(f"Sorry I can't workout with you anymore,{names[3]}.")
print(f"There are some people that you would probably like,{names[4]}.")
#3-3
print("3-3 section")
Cars=['Bugatti','Lam Truck','Rolls-Royce','Miata']
Speedy=f"I want to drive a {Cars[0]} on the highway as fast as I can"
Off_Road=f"I want to drive a {Cars[1]} off road for the bumpy ride"
Luxury=f"I want to drive a {Cars[2]} through the city"
Drifting=f"I want a {Cars[3]} for drifting everywhere I go"
print(Speedy)
print(Off_Road)
print(Luxury)
print(Drifting)
#Modifying Elements in a list
print("Modifying Elements in a list")
motorcycles=['honda', 'yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'# I just switched 'honda' with 'ducati'
print(motorcycles)
#Adding Elements to a list
print("Adding Elements to a list")
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')#append adds 'ducati' at the end of the list
print(motorcycles)
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
#Inserting Elements into a List
print('Inserting Elements into a List')
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')# I used insert to put ducati at a specific position is the list
print(motorcycles)
#Removing Elements from a List
print("Removing Elements from a list")
print('Removing Items from a list using the del statement')
motorcycles=['honda', 'yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles=['honda', 'yamaha','suzuki']
del motorcycles[1]
print(motorcycles)
print('Removing Items from a list using the pop command')
# The pop is useful for keeping the value of an item after it has been removed
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
motorcycles=['honda', 'yamaha','suzuki']
last_owned=motorcycles.pop()
print(f"{last_owned.title()} was the motorcycle I loved the least.")
motorcycles=['honda', 'yamaha','suzuki']
print(motorcycles)
first_owned=motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()} Accord")
#Removing an Item by Value
print("Removing an Item by Value")
motorcycles=['honda', 'yamaha','suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles=['honda', 'yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive} is too expensive for me.")
#Try it Yourself
print("Try it Yourself Section")
#3-4 Guest List
print("3-4 Guest List Section")
Fav_People=['Jack Sparrow','Monkey.D Luffy','Theodore Rosevelt']
print(f"\nI love you calmness and chill nature as a pirate,{Fav_People[0]}. I would love if you can join my dinner party.")
print(f"\nYou are my favorite most favorite pirate, {Fav_People[1]}. I grew up watching you.I would love if you can come to my dinner party")
print(f"\n{Fav_People[2]} you are the only real person I admire, honestly. You want to come to my dinner party? ")
#3-5. Changing Guest List
print("3-5. Changing Guest List")
print(f"Sadly {Fav_People[2]} could not make it. Aww Bummer. So I am inviting someone else.")
Fav_People[2]='Roronoa Zoro'
print(Fav_People)
print(f"\n{Fav_People[0]}, I am just making sure if you are still coming, yes?")
print(f"\n{Fav_People[1]}, I just invited your right hand man,co-captain, Zoro. I can't wait to see you both!")
print(f"\n{Fav_People[2]}, I can't wait to see you and Luffy at the dinner party!! This is going to be awesome!")
#3-6.More Guests
print("3-6.More Guests")
Fav_People.insert(0,'Shanks')
Fav_People.insert(2,'Sabo')
Fav_People.append('Jonathan')
print(Fav_People)
print(f"\n{Fav_People[0]} I can't wait for you to come to my dinner party")
print(f"\n{Fav_People[1]} I just got a bigger table on the way, I invited more guests!")
print(f"\n{Fav_People[2]} I can't wait for you to come to my dinner party, your brother,Luffy is going to be there.")
print(f"\n{Fav_People[3]} I just invited your brother,Sabo. I also invited Shanks as well!")
print(f"\n{Fav_People[4]} You still coming? You might get to duel shanks to test your might as the best swords man!")
print(f"\n{Fav_People[5]} Why I invited you to the most exciting dinner party ever? I don't man. Come if you want too.")
print(f"{Fav_People} I got a new table with more seats! I am inviting more people!")
#3-7.Shrinking Guest List
print("3-7.Shrinking Guest List")
print("I can only invite 2 people from my guest list because my table has been delayed :(")
print(Fav_People)
Sorry_Jack=Fav_People.pop(1)
print(f"\n{Sorry_Jack.title()} Sorry I can't invite you to my dinner party")
print(Fav_People)
Sorry_Sabo=Fav_People.pop(1)
print(f"\n{Sorry_Sabo}, I am sorry that you won't be seeing your brother.")
print(Fav_People)
Not_Sorry=Fav_People.pop(3)
print(f"\n {Not_Sorry} I never cared if you came or not. I just ran out of people to invite. If you came you probably ruin the party anyway")
print(Fav_People)
Sorry_Zoro=Fav_People.pop(2)
print(f"\n {Sorry_Zoro} I really wanted you to come, but I can only invite 2 now")
print(Fav_People)
print(f"\n{Fav_People[0]} and {Fav_People[1]} you guys are still invited!!")
del Fav_People[0]
del Fav_People[0]
print(Fav_People)
#Organizing List
print("Organizing Lists")
#Sorting a list permanently with the Sort() Method
print('Sorting a list permanently with the Sort() Method')
cars=['bmw','audi','toyota','subaru']
cars.sort()#Changes the list in aphabetical order permanently
print(cars)
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)#Reverse Alphabetical Order permanently
print(cars)
#Sorting a List temporarily with the sorted() function
print('Sorting a list temporarily with the sorted() function')
cars=['bmw','audi','toyota','subaru']
print(f'{cars}- This is the original list')
print(f'{(sorted(cars))} - This is the sorted list')
print(f'{cars}- This is the original list again!')
#Printing a list in reverse order
print('printing in reverse order')
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
cars.reverse()# I can change it back to its original order if I use reverse again
print(cars)
#Finding the Length of a list
print('Finding the Length of a list')
cars=['bmw','audi','toyota','subaru']
Length_List=len(cars)
print(Length_List)







