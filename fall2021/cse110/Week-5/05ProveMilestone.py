import time

# Welcome statement.
print("\nWelcome to a Deep Rock Galactic typing game!\n"
      "for context, this is the title of my favorite videogame,\n"
      "so I decided to make a text-based adventure game modeled after it.\n")
time.sleep(1)
print("Allow me to set the scene. The planet is Hoxxes IV.")
time.sleep(2)

# The introduction of the story.
print("Hoxxes IV is a scorched, tidally-locked planet orbiting the blue star\n"
      "Creus, unique among the other planets in the system for its\n"
      "extraordinarily rich precious material deposits and extremely hostile\n"
      "environment. Only the mining corporation Deep Rock Galactic, known for\n"
      "a lack of safety precautions, is stubborn enough to continue mining in\n"
      "this sector, offering hefty paychecks and bonuses to those willing to\n"
      "brave the depths of Hoxxes IV.\n")
time.sleep(10)
print("The dangers include, but are not limited to: electromagnetic storms,\n"
      "gravity anomalies, tectonic instability, seas of sulfuric acid, and\n"
      "one of the most hostile ecosystems in the galaxy. The creatures of\n"
      "Hoxxes only grow more hostile and dangerous under the unending\n"
      "radiation from Creus and the biomatter and microorganisms left by\n"
      "other mining corporations. And if the pincers, teeth, tentacles, and\n"
      "altogether too many eyes of Hoxxes’ children isn’t enough to scare\n"
      "you away, rumors of even worse and much older, sinister, and alien\n"
      "things down in the deepest excavations abound.\n")
time.sleep(10)
print("For simplicity we'll be headed to Crystalline Caverns, one of the\n"
      "biomes on the planet. Let's begin the adventure.\n")
time.sleep(2)

# The adventure starts here.
dwarf_class = input(str("The mission is set, the doors to the droppod are\n"
"open, which class will you take? The high-mobility, low-firepower SCOUT?\n"
"The low-mobility, high-firepower GUNNER? The handy utilitarian ENGINEER?\n"
"Or my personal favorite, the explosive, terrain-eating DRILLER? "))
time.sleep(1)

# Set the user input to lower case.
dwarf_class = dwarf_class.lower()

# Determine the validity of the user's input.
while dwarf_class != 'scout' and dwarf_class != 'gunner' and dwarf_class != 'engineer' and dwarf_class != 'driller':
    dwarf_class = input(str(f"\n{dwarf_class.capitalize()} is not an available"
    " class, please choose one of the available classes: "))
    dwarf_class = dwarf_class.lower()
    time.sleep(1)

# Determine the path that the user is on based upon their input.
if dwarf_class == 'scout':
    print("\nYou have chosen the Scout Class!\n"
    "Your primary weapon is an automatic assault rifle, and your secondary"
    " weapon is a double-barrel shotgun.\n"
    "Your mobility tool is a rechargable grapple hook, and your misc utility"
    " is a flare gun.\n")
elif dwarf_class == 'gunner':
    print("\nYou have chosen the Gunner Class!\n"
    "Your primary weapon is a minigun, and your secondary"
    " weapon is a heavy revolver.\n"
    "Your mobility tool is a zipline gun, and your misc utility"
    " is a deployable shield.\n")
elif dwarf_class == 'engineer':
    print("\nYou have chosen the Engineer Class!\n"
    "Your primary weapon is a semi-automatic shotgun, and your secondary"
    " weapon is a propelled grenade launcher.\n"
    "Your mobility tool is a deployable platform gun, and your misc utility"
    " is a deployable sentry-turret.\n")
else:
    print("\nYou have chosen the Driller Class!\n"
    "Your primary weapon is a flamethrower, and your secondary"
    " weapon is a plasma pistol.\n"
    "Your mobility tool is a pair of drills, and your misc utility"
    " is C4.\n")