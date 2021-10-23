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

# Universal mission begin statement for all classes.
def mission_begin():
    print("\nThe mission begins, the droppod lands in a dark cavern.\n"
    "As your team disembarks the droppod its engines roar to life and\n"
    "it leaves you and your team alone. Let the mission begin.\n")

# Scout track begins here.
def scout_class():
    print("\nYou have chosen the Scout Class!\n"
    "Your primary weapon is an automatic assault rifle, and your secondary"
    " weapon is a double-barrel shotgun.\n"
    "Your mobility tool is a rechargable grapple hook, and your misc utility"
    " is a flare gun.\n")
    mission_begin()
    
    # Collect first scout user input.
    scout_decision_initial = input(print("\nIn the dark cave you see a faint glow,\n"
    "you've found gold! Do you GRAPPLE to the gold or do you shoot a FLARE? "))

    # Check input validity.
    while scout_decision_initial.lower() != 'grapple' and scout_decision_initial.lower() != 'flare':
        scout_decision_initial = input(print("\nPlease enter either GRAPPLE or FLARE. "))

    if scout_decision_initial.lower() == 'grapple':

        # Collect next user input.
        scout_decision_grapple = input(print("\nYou collect gold! But the gunner is grabbed by a Cave Leech!\n"
        "You see a chunk of Red Sugar nearby, you know it has healing properties.\n"
        "Do you MINE the Red Sugar, or do you SHOOT the Cave Leech? "))

        # Check input validity.
        while scout_decision_grapple.lower() != 'mine' and scout_decision_grapple.lower() != 'shoot':
            scout_decision_grapple = input(print("\nPlease enter either MINE or SHOOT. "))
        
        # Decision resulting in team failure.
        if scout_decision_grapple.lower() == 'mine':
            print("\nIn the time that you mined the Red Sugar, the Cave Leech\n"
            "killed the Gunner and grabbed the Driller. You are now down to just\n"
            "you and the Engineer. A Glyohid Oppressor breaks into the room,\n"
            "you do not have enough firepower to kill it. You all die.")
        else:
            scout_decision_shoot = input(print("\nYou shoot the Cave Leech and kill it, unfortunately\n"
            "the Gunner has already been killed. As you and your team mourn the loss\n"
            "of your Gunner a Glyphid Oppressor appears! It's clad in thick armor\n"
            "but you notice a glowing green bulb on it's butt. Do you focus your\n"
            "fire on its HEAD or on the glowing green bulb on its BUTT? "))

            while scout_decision_shoot.lower() != 'head' and scout_decision_shoot.lower() != 'butt':
                scout_decision_shoot = input(print("\nPlease enter either HEAD or BUTT. "))
            
            if scout_decision_shoot.lower() == 'head':
                print("\nYou and your team fire on the Glyphid Oppressor's head with everything\n"
                "you have but to no avail, the Oppressor wipes out your remaining team members\n"
                "and you fail.")
            else:
                print("\nYour driller shoots a wall of flame at the Glyphid Oppressor's head\n"
                "as you and the engineer run around to the back of it. You\n"
                "unleash everything you have on that big green bulb until the\n"
                "Oppressor screeches its final breath and dies. Success!")
    else:
        scout_decision_flare = input(print("\nYour flare shoots through the cave in a brilliant flash,\n"
        "lighting everything up along the way. When it sinks into the cave ceiling\n"
        "on the other side of the cave you notice a pink mass on the ceiling ahead\n"
        "of you. It's a Cave Leech! Do you SHOOT the Cave Leech or do you IGNORE it? "))

        while scout_decision_flare.lower() != 'shoot' and scout_decision_flare.lower() != 'ignore':
            scout_decision_flare = input(print("\nPlease enter either SHOOT or IGNORE. "))
        
        if scout_decision_flare.lower() == 'shoot':
            scout_decision_shoot_2 = input(print("\nYou shoot the Cave Leech and kill it, the cave is safe!\n"
            "Or so you thought. Your hear a boom as a Bulk Detonator blasts into the cave!\n"
            "Bulk Detonators are notoriously difficult to kill, and they cause huge\n"
            "destruction when they explode on death. Do you REGROUP with your team to\n"
            "fight off the Bulk Detonator as a united team, or do you FLANK the beast\n"
            "from a high point?"))

            while scout_decision_shoot_2.lower() != 'regroup' and scout_decision_shoot_2.lower() != 'flank':
                scout_decision_shoot_2 = input(print("\nPlease enter either REGROUP or FLANK. "))
            
            if scout_decision_shoot_2.lower() == 'regroup':
                print("\nYou rejoin your team and you all prepare to destroy the Bulk Detonator.\n"
                "Your team rains fire on the Detonator as it slowly thunders around\n"
                "nearly killing your whole team on several occasions. Finally, after\n"
                "many bullets the Bulk Detonator detonates in a spectacular explosion.\n"
                "Your team triumphantly returns to the droppod after the mission is\n"
                "complete. Success!")
            
            else:
                print("\nYou grapple to a spot above the Bulk Detonator and begin raining fire\n"
                "from above. As your team fires from all different directions\n"
                "the Detonator goes down fast. After a brilliant flash, the\n"
                "Bulk Detonator is gone. Your team succeeds!")
        
        else:
            print("\nYou ignore the Cave Leech on the ceiling and go about your exploration.\n"
            "SNAP! You've been grabbed by the Cave Leech! You're lifted high above\n"
            "the ground and the Leech starts eating you. Your teammates shoot the\n"
            "Leech and kill it just before it kills you, but the fall from all the\n"
            "way up is enough to finish you off. You are killed.\n")


# Gunner track begins here.
def gunner_class():
    print("\nYou have chosen the Gunner Class!\n"
    "Your primary weapon is a minigun, and your secondary"
    " weapon is a heavy revolver.\n"
    "Your mobility tool is a zipline gun, and your misc utility"
    " is a deployable shield.\n")
    mission_begin()

# Engineer track begins here.
def engineer_class():
    print("\nYou have chosen the Engineer Class!\n"
    "Your primary weapon is a semi-automatic shotgun, and your secondary"
    " weapon is a propelled grenade launcher.\n"
    "Your mobility tool is a deployable platform gun, and your misc utility"
    " is a deployable sentry-turret.\n")
    mission_begin()

# Driller track begins here.
def driller_class():
    print("\nYou have chosen the Driller Class!\n"
    "Your primary weapon is a flamethrower, and your secondary"
    " weapon is a plasma pistol.\n"
    "Your mobility tool is a pair of drills, and your misc utility"
    " is C4.\n")
    mission_begin()


# Determine the path that the user is on based upon their input.
if dwarf_class == 'scout':
    scout_class()
elif dwarf_class == 'gunner':
    gunner_class()
elif dwarf_class == 'engineer':
    engineer_class()
else:
    driller_class()