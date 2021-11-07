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







