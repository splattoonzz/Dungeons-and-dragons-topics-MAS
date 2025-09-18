# -------------------------------
# Monika Mini Adventure (Drop-in)
# -------------------------------

label hv_dnd_mini_adventure:
    # Intro
    m 1eua "Alright, [player]! Your adventure begins now~"
    m 3hua "You, the [persistent.dnd_alignment] [persistent.dnd_race] [persistent.dnd_class], step into the mysterious Whispering Woods. The air smells like magic… and mischief."
    m 1hub "Your background as a [persistent.dnd_background] might give you an edge. Let’s see what happens!"

    jump hv_dnd_forest_fork

# -------------------------------
# First Choice: Forest Fork
label hv_dnd_forest_fork:
    m 1eua "You come to a fork in the forest path. One path is dark and tangled; the other sunlit and inviting."

    menu:
        "Take the dark path":
            if "Chaotic" in persistent.dnd_alignment:
                m 3hua "Of course! You love a little danger~"
            else:
                m 1hub "Careful… shadows can hide surprises."
            jump hv_dnd_monster_encounter
        "Take the bright path":
            if "Lawful" in persistent.dnd_alignment:
                m 3eua "Smart choice, steady and cautious."
            else:
                m 1hua "The sunlit path feels safe… maybe too safe?"
            jump hv_dnd_monster_encounter

# -------------------------------
# Monster Encounter
label hv_dnd_monster_encounter:
    m 1eua "Suddenly… a [persistent.dnd_monster_custom if persistent.dnd_monster_custom else 'Owlbear'] blocks your path!"

    if persistent.dnd_class in ["Barbarian", "Fighter", "Paladin"]:
        m 3hub "Perfect for a [persistent.dnd_class]! Time to swing your weapon~"
    elif persistent.dnd_class in ["Wizard", "Sorcerer", "Cleric", "Druid", "Bard"]:
        m 1hua "Magic time! Maybe [persistent.dnd_spell if persistent.dnd_spell else 'a spell'] will help?"
    else:
        m 3eua "You’ll need some clever thinking to get past this."

    menu:
        "Fight":
            m 1eua "You charge bravely!"
            $ fight_roll = renpy.random.randint(1,20)
            if fight_roll > 10:
                m 3hub "You defeat the [persistent.dnd_monster_custom if persistent.dnd_monster_custom else 'Owlbear']! Well done~"
            else:
                m 1hua "Oof… it hits you! But you escape with quick thinking."
        "Avoid":
            m 3eua "You try to sneak around it…"
            $ sneak_roll = renpy.random.randint(1,20)
            if sneak_roll > 8:
                m 1hub "Success! You slip past unseen."
            else:
                m 3hua "Uh-oh… it notices you! You must fight!"
        "Charm/Talk":
            if persistent.dnd_class == "Bard":
                m 1eua "You attempt to charm the creature…"
                $ charm_roll = renpy.random.randint(1,20)
                if charm_roll > 10:
                    m 3hua "It calms down! Your bardic skills are impressive."
                else:
                    m 1hub "Hmm… it didn’t work. Combat time!"
            else:
                m 1hua "Communication fails… better find another approach."

    jump hv_dnd_riddle

# -------------------------------
# Riddle / Puzzle Encounter
label hv_dnd_riddle:
    m 1eua "After the creature, you find an ancient stone door with a riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'"

    menu:
        "Echo":
            m 3hua "Correct! Clever thinking, [player]~ The door swings open."
        "Silence":
            m 1hub "Not quite… the door remains shut. Maybe try again later."
        "Other":
            m 3eua "Hmm… that’s creative, but the riddle doesn’t respond. The door stays closed."

    jump hv_dnd_treasure

# -------------------------------
# Treasure / Reward
label hv_dnd_treasure:
    m 1eua "Beyond the door, you find a small chest half-buried under roots."
    $ treasure_roll = renpy.random.randint(1,20)
    if treasure_roll > 10:
        m 3hub "Inside is a magical item! I bet it’s perfect for your [persistent.dnd_class] abilities~"
    else:
        m 1hua "The chest is empty… but surviving the adventure is treasure enough!"

    jump hv_dnd_adventure_end

# -------------------------------
# Adventure End
label hv_dnd_adventure_end:
    m 1eua "Phew! That was a short but exciting adventure, [player]~"
    m 3hua "I had so much fun adventuring with you. You’d make an amazing party member in any campaign."
    m 1hub "We could go on another adventure anytime… maybe with more monsters and puzzles next time~"
    return
