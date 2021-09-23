# Beginning of MadLib.py, the following inputs are the prompts for the user that will feed the madlib machine.
print("Welcome to MadLib.py! Please answer the following prompts")

# adj = adjective
# ani = animal
# ver = verb
# exc = exclamation
# adv = adverb
# famper = famous person
# plunou = plural noun
adj1 = input("Please enter an adjective: ")
ani1 = input("Please enter an animal: ")
ver1 = input("Please enter a verb: ")
exc1 = input("Please enter an exclamation: ")
ver2 = input("Please enter another verb: ")
ver3 = input("Please enter another verb: ")
# This is the end of the story provided by the assignment.

# This is the beginning of my own story.
adj2 = input("Please enter another adjective: ")
adv1 = input("Please enter an adverb: ")
adj3 = input("Please enter another adjective: ")
famper1 = input("Please enter the name of a famous person, dead or alive: ")
ver4 = input("Please enter another verb: ")
adv2 = input("Please enter another adverb: ")
ver5 = input("Please enter another verb: ")
plunou1 = input("Please enter a plural noun: ")
# At this point all of the user input has been collected.

# The following code prints the story with the user input embedded in the story.
# The user input is formatted such that it will look nice.
print("\nThe other day, I was really in trouble. It all started when I saw a very\n"
    f"{adj1.lower()} {ani1.lower()} {ver1.lower()} down the hallway. \"{exc1.capitalize()}!\" I yelled. But all\n"
    f"I could think to do was to {ver2.lower()} over and over. Miraculously,\n"
    f"that caused it to stop, but not before it tried to {ver3.lower()}\n"
    "right in front of my family.\n"
    f"What happened next was completely {adj2.lower()}. A {adv1} {adj3} {famper1.title()} "
    "decided to grace me with their presence.\n"
    f"They {ver4.lower()}ed {adv2.lower()} and then {ver5.lower()}"
    f"ed right at me. I tried to move but my legs were stuck in {plunou1.lower()}.\n")

# End of code, thanks for playing!