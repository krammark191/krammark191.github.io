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
        scout_decision_initial = input(
            print("\nPlease enter either GRAPPLE or FLARE. "))

    # Begins the GRAPPLE line.
    if scout_decision_initial.lower() == 'grapple':

        # Collect next user input.
        scout_decision_grapple = input(print("\nYou collect gold! But the gunner is grabbed by a Cave Leech!\n"
                                             "You see a chunk of Red Sugar nearby, you know it has healing properties.\n"
                                             "Do you MINE the Red Sugar, or do you SHOOT the Cave Leech? "))

        # Check input validity.
        while scout_decision_grapple.lower() != 'mine' and scout_decision_grapple.lower() != 'shoot':
            scout_decision_grapple = input(
                print("\nPlease enter either MINE or SHOOT. "))

        # Decision resulting in team failure.
        if scout_decision_grapple.lower() == 'mine':
            print("\nIn the time that you mined the Red Sugar, the Cave Leech\n"
                  "killed the Gunner and grabbed the Driller. You are now down to just\n"
                  "you and the Engineer. A Glyohid Oppressor breaks into the room,\n"
                  "you do not have enough firepower to kill it. You all die.")

        # Begins the SHOOT line.
        else:
            scout_decision_shoot = input(print("\nYou shoot the Cave Leech and kill it, unfortunately\n"
                                               "the Gunner has already been killed. As you and your team mourn the loss\n"
                                               "of your Gunner a Glyphid Oppressor appears! It's clad in thick armor\n"
                                               "but you notice a glowing green bulb on it's butt. Do you focus your\n"
                                               "fire on its HEAD or on the glowing green bulb on its BUTT? "))

            # Checks input validity.
            while scout_decision_shoot.lower() != 'head' and scout_decision_shoot.lower() != 'butt':
                scout_decision_shoot = input(
                    print("\nPlease enter either HEAD or BUTT. "))

            # Decision resulting in team failure.
            if scout_decision_shoot.lower() == 'head':
                print("\nYou and your team fire on the Glyphid Oppressor's head with everything\n"
                      "you have but to no avail, the Oppressor wipes out your remaining team members\n"
                      "and you fail.")

            # Decision resulting in success.
            else:
                print("\nYour driller shoots a wall of flame at the Glyphid Oppressor's head\n"
                      "as you and the engineer run around to the back of it. You\n"
                      "unleash everything you have on that big green bulb until the\n"
                      "Oppressor screeches its final breath and dies. Success!")

    # Begins Flare decision line.
    else:
        scout_decision_flare = input(print("\nYour flare shoots through the cave in a brilliant flash,\n"
                                           "lighting everything up along the way. When it sinks into the cave ceiling\n"
                                           "on the other side of the cave you notice a pink mass on the ceiling ahead\n"
                                           "of you. It's a Cave Leech! Do you SHOOT the Cave Leech or do you IGNORE it? "))

        # Check user input validity.
        while scout_decision_flare.lower() != 'shoot' and scout_decision_flare.lower() != 'ignore':
            scout_decision_flare = input(
                print("\nPlease enter either SHOOT or IGNORE. "))

        # Begin SHOOT line.
        if scout_decision_flare.lower() == 'shoot':
            scout_decision_shoot_2 = input(print("\nYou shoot the Cave Leech and kill it, the cave is safe!\n"
                                                 "Or so you thought. Your hear a boom as a Bulk Detonator blasts into the cave!\n"
                                                 "Bulk Detonators are notoriously difficult to kill, and they cause huge\n"
                                                 "destruction when they explode on death. Do you REGROUP with your team to\n"
                                                 "fight off the Bulk Detonator as a united team, or do you FLANK the beast\n"
                                                 "from a high point?"))

            # Check user input validity.
            while scout_decision_shoot_2.lower() != 'regroup' and scout_decision_shoot_2.lower() != 'flank':
                scout_decision_shoot_2 = input(
                    print("\nPlease enter either REGROUP or FLANK. "))

            # Success via REGROUP.
            if scout_decision_shoot_2.lower() == 'regroup':
                print("\nYou rejoin your team and you all prepare to destroy the Bulk Detonator.\n"
                      "Your team rains fire on the Detonator as it slowly thunders around\n"
                      "nearly killing your whole team on several occasions. Finally, after\n"
                      "many bullets the Bulk Detonator detonates in a spectacular explosion.\n"
                      "Your team triumphantly returns to the droppod after the mission is\n"
                      "complete. Success!")

            # Success via FLANK.
            else:
                print("\nYou grapple to a spot above the Bulk Detonator and begin raining fire\n"
                      "from above. As your team fires from all different directions\n"
                      "the Detonator goes down fast. After a brilliant flash, the\n"
                      "Bulk Detonator is gone. Your team succeeds!")

        # Failure via IGNORE.
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

    # Collect first gunner user input.
    gunner_decision_initial = input(print("\nYou exit the droppod and see the way forward\n"
                                          "has a chasm in the way. The scout zips across easily with\n"
                                          "his grapple hook, you might be able to jump it, but you could\n"
                                          "also use one of your deployable ziplines. Do you JUMP or DEPLOY\n"
                                          "a zipline? "))

    # Check input validity.
    while gunner_decision_initial.lower() != 'jump' and gunner_decision_initial.lower() != 'deploy':
        gunner_decision_initial = input(
            print("\nPlease enter either JUMP or DEPLOY. "))

    # Begins the JUMP line.
    if gunner_decision_initial.lower() == 'jump':

        # Collect next user input.
        gunner_decision_jump = input(print("\nYou leap across the chasm, barely making the jump.\n"
                                           "you go lucky, but the driller did not. The diller lands down below\n"
                                           "and takes damage but is still alive. Do you DEPLOY a zipline to his\n"
                                           "position so he can rejoin you or do you CONTINUE and let him catch\n"
                                           "up on his own? "))

        # Check input validity.
        while gunner_decision_jump.lower() != 'deploy' and gunner_decision_jump.lower() != 'continue':
            gunner_decision_jump = input(
                print("\nPlease enter either DEPLOY or CONTINUE. "))

        # Decision resulting in team failure.
        if gunner_decision_jump.lower() == 'continue':
            print("\nYou trust the driller to be able to catch up with your team, so\n"
                  "you leave him and continue onward. You make it to the next\n"
                  "room as the driller bursts out of the ground in a fit of rage.\n"
                  "\"You shouldn't have left me behind!\" the driller screams\n"
                  "as he throws C4 into the middle of the group and detonates it.\n"
                  "The whole team is dead. You all fail.\n")

        # Begins the DEPLOY line.
        else:
            gunner_decision_deploy = input(print("\nThe driller is very grateful and is able to\n"
                                                 "mine red sugar nearby and get his health back. In the next\n"
                                                 "cave your team finds a machine event. Do you ATTEMPT the\n"
                                                 "machine event for extra rewards or do you IGNORE the event? "))

            # Checks input validity.
            while gunner_decision_deploy.lower() != 'attempt' and gunner_decision_deploy.lower() != 'ignore':
                gunner_decision_deploy = input(
                    print("\nPlease enter either ATTEMPT or IGNORE. "))

            # Decision resulting in team failure.
            if gunner_decision_deploy.lower() == 'attempt':
                print("\nYou activate the machine event, unfortunately it is an O.M.E.N.\n"
                      "machine event. You stand no chance. You all get wiped out.\n")

            # Decision resulting in success.
            else:
                print("\nYou ignore the machine event when you recognize it as an\n"
                      "O.M.E.N. Modular Exterminator. These events are notoriously\n"
                      "difficult and your team is ill-prepared. Instead your team\n"
                      "finishes the mission and makes it safely back to the droppod.\n"
                      "You all succeed!\n")

        # Begins Deploy decision line.
    else:
        gunner_decision_deploy_2 = input(print("\nThe Driller and Engineer are able to cross\n"
                                               "the chasm with you. You hear a beeping noise and find out\n"
                                               "that there is a BET-C nearby. do you try to REBOOT the BET-C\n"
                                               "or do you IGNORE it and move on? "))

        # Check user input validity.
        while gunner_decision_deploy_2.lower() != 'reboot' and gunner_decision_deploy_2.lower() != 'ignore':
            gunner_decision_deploy_2 = input(
                print("\nPlease enter either REBOOT or IGNORE. "))

        # Succes via REBOOT line.
        if gunner_decision_deploy_2.lower() == 'reboot':
            print("\nYour team attempts to reboot the BET-C by destroying the\n"
                  "Xynarch Charge-Suckers. It takes your team a while\n"
                  "but with the use of your shield your team is able to\n"
                  "kill the pests and restart the BET-C. The BET-C then\n"
                  "saves your team from a seemingly unstoppable horde\n"
                  "of bugs. You are able to complete the mission and\n"
                  "return to the droppod. Success!")

        # Failure via IGNORE.
        else:
            print("\nYou ignore the BET-C, as the Xynarch Charge-Suckers make\n"
                  "for a tough battle. You move on from the BET-C but are soon\n"
                  "hit with a huge wave of bugs and are soon overwhelmed. Your\n"
                  "slowly gets picked off one by one until you are finally killed.\n")


# Engineer track begins here.
def engineer_class():
    print("\nYou have chosen the Engineer Class!\n"
          "Your primary weapon is a semi-automatic shotgun, and your secondary"
          " weapon is a propelled grenade launcher.\n"
          "Your mobility tool is a deployable platform gun, and your misc utility"
          " is a deployable sentry-turret.\n")
    mission_begin()

    # Collect first scout user input.
    engineer_decision_initial = input(print("\nYou enter the cave and see some gold on the wall,\n"
                                            "but the cave is also very dark and vast, who knows what may be lurking.\n"
                                            "Do you shoot a PLATFORM on the gold so the Scout can grab it or do you\n"
                                            "BUILD a turret just in case unseen bugs are creeping around? "))

    # Check input validity.
    while engineer_decision_initial.lower() != 'platform' and engineer_decision_initial.lower() != 'build':
        engineer_decision_initial = input(
            print("\nPlease enter either PLATFORM or BUILD. "))

    # Begins the PLATFORM line.
    if engineer_decision_initial.lower() == 'platform':

        # Collect next user input.
        engineer_decision_platform = input(print("\nYou fire a platform on some gold, the scout can\n"
                                                 "collect the gold now. But the gunner gets snagged by a cave leech.\n"
                                                 "Do you LAUNCH a grenade from your PGL at the cave leech or do you\n"
                                                 "SHOOT another platform below the gunner? "))

        # Check input validity.
        while engineer_decision_platform.lower() != 'launch' and engineer_decision_platform.lower() != 'shoot':
            engineer_decision_platform = input(
                print("\nPlease enter either LAUNCH or SHOOT. "))

        # Decision resulting in team failure.
        if engineer_decision_platform.lower() == 'launch':
            print("\nThe grenade you just launch succeeds in killing the leech,\n"
                  "the gunner falls from the ceiling to his death. A Glyphid\n"
                  "Oppressor smashes through the cave wall and ambushes your\n"
                  "team. You try to defend but with no turrets set up and no\n"
                  "shields from the gunner the Oppressor wipes you all out.\n")

        # Begins the SHOOT line.
        else:
            engineer_decision_shoot = input(print("\nAs you shoot a platform underneath the gunner,\n"
                                                  "the driller and the scout shoot the leech, killing it.\n"
                                                  "The gunner falls and lands safely on the platform. Do you\n"
                                                  "SALUTE the gunner or do you TELL the scout to light up the\n"
                                                  "cave? "))

            # Checks input validity.
            while engineer_decision_shoot.lower() != 'salute' and engineer_decision_shoot.lower() != 'tell':
                engineer_decision_shoot = input(
                    print("\nPlease enter either SALUTE or TELL. "))

            # Decision resulting in success.
            if engineer_decision_shoot.lower() == 'salute':
                print("\nThe gunner salutes back and you all trudge on ahead, heads on a swivel.\n"
                      "Your team, on high-alert and with high morale, successfully\n"
                      "completes the mission.\n")

            # Decision resulting in success.
            else:
                print("\nThe scout lights up the cave, revealing more enemies but\n"
                      "also the mission objective. You, along with your team,\n"
                      "kill the bugs and collect the objective. Success!\n")

    # Begins BUILD decision line.
    else:
        engineer_decision_build = input(print("\nAs soon as you set up a turret it automatically\n"
                                              "starts shooting at a cave leech on the ceiling. Do you continue ahead and WAIT\n"
                                              "at a dirt wall or do you RUN down a different cave? "))

        # Check user input validity.
        while engineer_decision_build.lower() != 'wait' and engineer_decision_build.lower() != 'run':
            engineer_decision_build = input(
                print("\nPlease enter either WAIT or RUN. "))

        # Begin RUN line.
        if engineer_decision_build.lower() == 'run':
            engineer_decision_run = input(print("\nYou hear an explosion as the driller clears a path\n"
                                                "to a new cave, luckily, your cave ends up at the same place.\n"
                                                "Do you SALUTE your team, or do you CONTINUE on without saluting\n"
                                                "them? "))

            # Check user input validity.
            while engineer_decision_run.lower() != 'salute' and engineer_decision_run.lower() != 'continue':
                engineer_decision_run = input(
                    print("\nPlease enter either SALUTE or CONTINUE. "))

            # Success via SALUTE.
            if engineer_decision_run.lower() == 'salute':
                print("\nYou salute your team and everyone salutes you back.\n"
                      "Your team reaches the objective and completes the\n"
                      "mission with even more salutes.\n")

            # Failure via CONTINUE.
            else:
                print("\nYour driller takes offence that you did not salute when\n"
                      "everyone else did. He blows you up with C4, killing you.\n")

        # Failure via WAIT.
        else:
            print("\nYou wait at a dirt wall for the driller, he comes up and,\n"
                  "in typical fashion, throws his C4 at the dirt wall\n"
                  "and detonates it, killing you.\n")


# Driller track begins here.
def driller_class():
    print("\nYou have chosen the Driller Class!\n"
          "Your primary weapon is a flamethrower, and your secondary"
          " weapon is a plasma pistol.\n"
          "Your mobility tool is a pair of drills, and your misc utility"
          " is C4.\n")
    mission_begin()

    # Collect first scout user input.
    driller_decision_initial = input(print("\nYou have chosen the driller. No terrain stands in your way.\n"
                                           "Your team starts traversing the caves like complete plebs.\n"
                                           "You have already won, you have explosives and drills for arms.\n"
                                           "You are mole incarnate. You are the superior miner. You need\n"
                                           "not worry about anything now, you are a source of fiery and\n"
                                           "explosive pain to all bug-kind. Your choices lay before you:\n"
                                           "Will you explode a horde of BUGS or will you explode your TEAM? "))

    # Check input validity.
    while driller_decision_initial.lower() != 'bugs' and driller_decision_initial.lower() != 'team':
        driller_decision_initial = input(
            print("\nPlease enter either BUGS or TEAM. "))

    # Begins the BUGS line.
    if driller_decision_initial.lower() == 'bugs':

        # Collect next user input.
        driller_decision_bugs = input(print("\nYou destroy an entire horde of bugs in one spectacular\n"
                                            "display of pyrotechnics. Your teammates bow at your feet. Do you\n"
                                            "SALUTE them or do you go out with a BANG? "))

        # Check input validity.
        while driller_decision_bugs.lower() != 'salute' and driller_decision_bugs.lower() != 'bang':
            driller_decision_bugs = input(
                print("\nPlease enter either SALUTE or BANG. "))

        # Decision resulting in team failure, but your success.
        if driller_decision_bugs.lower() == 'bang':
            print("\nYou're high on life. You've never felt so alive. You throw a C4\n"
                  "in the middle of your team and detonate it, taking all of you\n"
                  "out in a stunning blaze of glory.\n")

        # Begins the SALUTE line.
        else:
            driller_decision_salute = input(print("\nYou and your teammates press on, cowering behind you when\n"
                                                  "a Glyphid Pretorian shows up. Do you ENCOURAGE your team to fight together\n"
                                                  "or do you BLOW up the pretorian all by your self? "))

            # Checks input validity.
            while driller_decision_salute.lower() != 'encourage' and driller_decision_salute.lower() != 'blow':
                driller_decision_salute = input(
                    print("\nPlease enter either ENCOURAGE or BLOW. "))

            # Decision resulting in success.
            if driller_decision_salute.lower() == 'encourage':
                print("\nYou and your teammates fight the praetorian, swiftly destroying it.\n"
                      "Your team completes the objective and succeeds.\n")

            # Decision resulting in success.
            else:
                print("\nYou blow up the Praetorian in an explosion of epic proportions.\n"
                      "Your team completes the objective and succeeds.\n")

    # Begins TEAM decision line.
    else:
        driller_decision_team = input(print("\nYou disintigrate your entire team in one glorious explosion!\n"
                                            "How will you celebrate this magnificant feat? will you\n"
                                            "destroy as much terrain as possible and then FINISH the\n"
                                            "mission in solo glory, or will you DIG to the bottom of\n"
                                            "the map? "))

        # Check user input validity.
        while driller_decision_team.lower() != 'finish' and driller_decision_team.lower() != 'dig':
            driller_decision_team = input(
                print("\nPlease enter either FINISH or DIG. "))

        # Success via FINISH.
        if driller_decision_team.lower() == 'finish':
            print("\nAfter laying waste to all bug-kind and torching the entire\n"
                  "planet, you return to the droppod with a satisfied\n"
                  "smile on your face. The world is yours to destroy.\n")

        # Success via DIG.
        else:
            print("\nYou reach the bottom of the map and run out of fuel in your\n"
                  "drills. The droppod leaves, but it's ok, you're in your happy place.\n")


# Determine the path that the user is on based upon their input.
if dwarf_class == 'scout':
    scout_class()
elif dwarf_class == 'gunner':
    gunner_class()
elif dwarf_class == 'engineer':
    engineer_class()
else:
    driller_class()
