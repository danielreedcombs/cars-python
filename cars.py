#Create an empty set named showroom.
#Add four of your favorite car model names to the set.
#Print the length of your set.
#Pick one of the items in your show room and add it to the set again.
#Print your showroom. Notice how there's still only one instance of that model in there.
#Using update(), add two more car models to your showroom with another set.
#You've sold one of your cars. Remove it from the set with the discard() method.

show_room = set(["lambo", "toyota", "honda", "blue"])
new_cars = set(["fast car","slow car"])
print(len(show_room))
show_room.add("toyota")
print(show_room)
show_room.update(new_cars)
print(show_room)

#Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set,
junk_yard = set(["scrappy" , "broken" , "zac's impounded car"])

#add some different cars, but also add a few that are the same as in the show_room set.
junk_yard.add("lambo")
print(junk_yard)
junk_yard.add("chop shop impala")
print(junk_yard)

#Use the intersection method to see which cars exist in both the show_room and that junkyard.
print(show_room.intersection(junk_yard))

#Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your show_room.
new_junk_yard= junk_yard.union(show_room)
print(new_junk_yard)

#Use the discard() method to remove any cars that you acquired from the junkyard that you want in your show_room.
print(new_junk_yard.discard(junk_yard))
