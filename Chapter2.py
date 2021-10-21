#Variables and Simple Data Types

#Variables
message="Hello Python World"
print(message)
message1="Welcome to my World Python!"
print(message1)

#Changing Case in a String with Methods
name="kitty cat warrior_1"
print(name.title())
name2="kitty cat warrior_2"
print(name2.upper())
name3="KITTY cat warrior_3"
print(name3.lower())

#Using Variables in Strings
first_name="Kitty"
middle_name='Cat'
last_name='Warrior_4'
full_name=f"{first_name} {middle_name} {last_name}"
print(full_name)
print(f"Hello,{full_name}.Welcome to my World")
Welcome_messsage=(f"{full_name} your goal for this world is to become the greatest")
print(Welcome_messsage)

#Adding Whitespace to Strings with tabs or Newlines
print("Bag")
print("\tInventory\tQuest Book\tMap")
print("Inventory:\nStick\nFish\nPants")

#Stripping Whitespace
Meow="'  language   '"
print(Meow)
Meow.rstrip()
print(Meow)

#Try it Yourself

#2-3
Jack_Sparrow="Hello Jack,would you like to go on an adventure with me today?"
#2-4
Pirate="Jack Sparrow"
print(Pirate.title())
print(Pirate.upper())
print(Pirate.lower())
#2-5
Famous_Quote1='Billy once said,"If my wife ever cheats on me, I will shoot her,the kids, and myself"'
#2-6
Famous_Person="I LOVE YOU BILLY.I AM YOUR BIGGEST FAN!"
message2=f"{Famous_Person}"
print(message2)
#2-7
Crazy_Duo="\n\tJack Sparrow\n\tBilly Magnum"
print(Crazy_Duo)
print(Crazy_Duo.rstrip())
print(Crazy_Duo.lstrip())
print(Crazy_Duo.strip())

#Integers


