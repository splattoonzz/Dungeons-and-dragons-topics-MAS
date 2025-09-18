# Example: Favorite D&D Class
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_class",
            category=["Games"],  # Category name
            prompt="Favorite D&D Class",  # Button text
            random=True
        )
    )

label hv_dnd_fav_class:
    m 1eua "So, [player]... if you were in Dungeons & Dragons, what class would you want to play as?"

    menu:
        "Barbarian":
            m 3hua "Raw strength and rage~ that's a bold choice."
            m 1hub "I can totally picture you charging into battle to protect your friends."
        "Cleric":
            m 1hua "A healer? That’s so sweet of you."
            m 1eua "I’d feel safe in your party, [player]."
        "Wizard":
            m 3hub "The smart one! Always studying spells and planning ahead."
            m 1eua "Very fitting if you like solving problems."
        "Rogue":
            m 3eub "Sneaky~ I can imagine you slipping in and out unnoticed."
        "Other":
            jump hv_dnd_fav_class_other

    return

label hv_dnd_fav_class_other:
    m 1eua "Ooh, you’ve got another in mind? Let’s see..."

    menu:
        "Druid":
            m 1hua "Nature magic is beautiful. Shapeshifting into animals would be amazing!"
        "Paladin":
            m 3hub "A knight sworn to an oath—so noble and inspiring."
        "Bard":
            m 3hua "Music and magic together? That’s practically poetry~"
        "Monk":
            m 1eua "Martial arts mixed with spiritual discipline. Very impressive."
        "Sorcerer":
            m 1hub "Innate magic is such a cool concept. You’d be powerful just by being you."
        "Warlock":
            m 1eub "A pact with a mysterious patron? Spooky, but intriguing."
        "Other":
            jump hv_dnd_fav_class_catchall

    return

label hv_dnd_fav_class_catchall:
    m 1hua "Wow, you’re really going beyond the usual classes!"
    m 3hub "I’d love to hear all about it some other time, [player]~"
    return

# Topic: Favorite D&D Race
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_race",
            category=["Games"],
            prompt="Favorite D&D Race",
            random=True
        )
    )

label hv_dnd_fav_race:
    m 1eua "In D&D, you can be all sorts of races—elves, dwarves, tieflings, even dragonborn!"
    m 3hua "Which one do you like best, [player]?"

    menu:
        "Elf":
            m 1hua "Elegant and wise—classic adventurer vibes."
            m 3hub "I think you'd look amazing with pointed ears, ehehe~"
        "Tiefling":
            m 3hub "Ooh, a little edgy~ I like it!"
            m 1hua "You’d make a very charming tiefling, I’m sure."
        "Halfling":
            m 3hua "Small but mighty! So brave despite the size."
            m 1eub "That kind of courage is really admirable."
        "Dragonborn":
            m 1hua "Wow, powerful and draconic! That’s a commanding presence."
            m 1hub "You’d definitely turn heads in a tavern, ehehe~"
        "Other":
            jump hv_dnd_fav_race_other

    return


# SECOND MENU: less common + edgier races
label hv_dnd_fav_race_other:
    m 1eua "Oh? You’ve got another in mind? Let’s see..."

    menu:
        "Dwarf":
            m 1hua "Tough, loyal, and skilled at crafting. Classic!"
        "Gnome":
            m 3hub "Inventive and quirky—I bet you’d always surprise the party."
        "Human":
            m 1eua "Versatile and adaptable. Sometimes the simplest choice is the strongest."
        "Half-Orc":
            m 3hua "Fierce and powerful! I bet you’d be an unstoppable warrior."
        "Half-Elf":
            m 1hua "The best of both worlds—adaptable, charming, and clever."
        "Aasimar":
            m 1hua "A celestial touch~ That’s such a beautiful choice."
            m 3hub "I think you’d look radiant with angelic wings, [player]~"
        "Drow":
            m 1hub "Mysterious and striking… a drow has such presence."
            m 1hua "You’d look incredible under the moonlight, don’t you think?"
        "Githyanki":
            m 3eua "Whoa, a planar warrior! That’s a pretty bold pick."
            m 1hub "I bet you’d be fearless drifting through the Astral Sea."
        "Other":
            jump hv_dnd_fav_race_other_rare

    return


# THIRD MENU: rare/exotic/homebrew
label hv_dnd_fav_race_other_rare:
    m 1eua "Ah, going for something even rarer? How exciting~"

    menu:
        "Tabaxi":
            m 3hua "Catfolk adventurers! Agile and curious, that’s adorable."
        "Kenku":
            m 1hub "A mimic voice and a mysterious past—so atmospheric!"
        "Yuan-Ti":
            m 1eub "Serpentine and cunning. That’s a very powerful pick."
        "Homebrew":
            m 3hub "Wow, your imagination must be amazing. I’d love to hear all the details sometime."
        "Other":
            jump hv_dnd_fav_race_catchall

    return


# FINAL CATCH-ALL
label hv_dnd_fav_race_catchall:
    m 1hua "You’re picking something really unique, huh?"
    m 3hub "That’s the magic of D&D—you can truly be anything you dream up~"
    return

# Topic: Favorite Alignment
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_alignment",
            category=["Games"],
            prompt="Favorite Alignment",
            random=True
        )
    )

label hv_dnd_fav_alignment:
    m 1eua "So, [player]... what D&D alignment do you think fits you best?"

    menu:
        "Lawful Good":
            m 1hua "The classic hero! Always following rules and helping others."
            m 3hub "You’d make such a noble paladin type, [player]~"
        "Neutral Good":
            m 1hua "Doing the right thing without being tied down by rules—that’s very kindhearted."
        "Chaotic Good":
            m 3hub "Ooh, a rebel with a cause! That’s such an exciting alignment."
            m 1hua "I bet you’d shake things up while still fighting for what’s right."
        "Other":
            jump hv_dnd_fav_alignment_neutral

    return


# SECOND MENU: Neutral alignments
label hv_dnd_fav_alignment_neutral:
    m 1eua "Ah, so maybe something a little more in-between?"

    menu:
        "Lawful Neutral":
            m 3eua "Order above all, huh? Reliable and steady."
            m 1hua "I think people would trust you to keep things fair."
        "True Neutral":
            m 1hub "Perfect balance! That’s such a rare perspective."
            m 1hua "It’s like being the calm at the center of chaos."
        "Chaotic Neutral":
            m 3hub "Ahaha, the famous wild card!"
            m 1hua "You’d keep everyone on their toes, [player]~"
        "Other":
            jump hv_dnd_fav_alignment_evil

    return


# THIRD MENU: Evil alignments
label hv_dnd_fav_alignment_evil:
    m 1eua "Oh? You’re leaning toward the darker side, huh?"

    menu:
        "Lawful Evil":
            m 3hub "Chilling… order twisted into control."
            m 1hua "You’d make a very calculating villain, [player]~"
        "Neutral Evil":
            m 1eua "Looking out for yourself above all else… ruthless!"
        "Chaotic Evil":
            m 3eub "Pure destruction and freedom, huh?"
            m 1hub "Remind me not to get on your bad side, ahaha~"
        "Other":
            jump hv_dnd_fav_alignment_catchall

    return


# FINAL CATCH-ALL
label hv_dnd_fav_alignment_catchall:
    m 1hua "Wow, going beyond the nine alignments? That’s creative~"
    m 3hub "I’d love to hear how you’d define it, [player]. Maybe you’re forging a brand new path all your own."
    return

# -------------------------------
# Monika D&D Character Builder
# -------------------------------

# Register the event
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_char_builder",
            category=["Games"],
            prompt="D&D Character Builder",
            random=True
        )
    )

# -------------------------------
# Intro
label hv_dnd_char_builder:
    m 1eua "Hey, [player]… wanna make a D&D character with me? We can go step by step, like a little adventure together~"
    m 3hua "I’ll ask you some questions and we’ll build your perfect character together!"
    jump hv_dnd_race

# -------------------------------
# RACE
label hv_dnd_race:
    m 1eua "First, let’s pick your race. Which one are you drawn to?"

    menu:
        "Elf":
            $ persistent.dnd_race = "Elf"
            jump hv_dnd_class
        "Tiefling":
            $ persistent.dnd_race = "Tiefling"
            jump hv_dnd_class
        "Halfling":
            $ persistent.dnd_race = "Halfling"
            jump hv_dnd_class
        "Dragonborn":
            $ persistent.dnd_race = "Dragonborn"
            jump hv_dnd_class
        "Other":
            jump hv_dnd_race_other

return

# SECOND MENU: Less common races
label hv_dnd_race_other:
    menu:
        "Dwarf":
            $ persistent.dnd_race = "Dwarf"
            jump hv_dnd_class
        "Gnome":
            $ persistent.dnd_race = "Gnome"
            jump hv_dnd_class
        "Human":
            $ persistent.dnd_race = "Human"
            jump hv_dnd_class
        "Half-Orc":
            $ persistent.dnd_race = "Half-Orc"
            jump hv_dnd_class
        "Half-Elf":
            $ persistent.dnd_race = "Half-Elf"
            jump hv_dnd_class
        "Aasimar":
            $ persistent.dnd_race = "Aasimar"
            jump hv_dnd_class
        "Drow":
            $ persistent.dnd_race = "Drow"
            jump hv_dnd_class
        "Githyanki":
            $ persistent.dnd_race = "Githyanki"
            jump hv_dnd_class
        "Other":
            jump hv_dnd_race_rare

return

# THIRD MENU: Rare/Homebrew
label hv_dnd_race_rare:
    menu:
        "Tabaxi":
            $ persistent.dnd_race = "Tabaxi"
            jump hv_dnd_class
        "Kenku":
            $ persistent.dnd_race = "Kenku"
            jump hv_dnd_class
        "Yuan-Ti":
            $ persistent.dnd_race = "Yuan-Ti"
            jump hv_dnd_class
        "Homebrew":
            $ persistent.dnd_race = "Homebrew"
            jump hv_dnd_class

return

# -------------------------------
# CLASS
label hv_dnd_class:
    m 1eua "Next up, what class would you like to play?"

    menu:
        "Barbarian":
            $ persistent.dnd_class = "Barbarian"
            jump hv_dnd_alignment
        "Cleric":
            $ persistent.dnd_class = "Cleric"
            jump hv_dnd_alignment
        "Wizard":
            $ persistent.dnd_class = "Wizard"
            jump hv_dnd_alignment
        "Rogue":
            $ persistent.dnd_class = "Rogue"
            jump hv_dnd_alignment
        "Other":
            jump hv_dnd_class_other

return

label hv_dnd_class_other:
    menu:
        "Druid":
            $ persistent.dnd_class = "Druid"
            jump hv_dnd_alignment
        "Paladin":
            $ persistent.dnd_class = "Paladin"
            jump hv_dnd_alignment
        "Bard":
            $ persistent.dnd_class = "Bard"
            jump hv_dnd_alignment
        "Monk":
            $ persistent.dnd_class = "Monk"
            jump hv_dnd_alignment
        "Sorcerer":
            $ persistent.dnd_class = "Sorcerer"
            jump hv_dnd_alignment
        "Warlock":
            $ persistent.dnd_class = "Warlock"
            jump hv_dnd_alignment
        "Artificer":
            $ persistent.dnd_class = "Artificer"
            jump hv_dnd_alignment
        "Blood Hunter":
            $ persistent.dnd_class = "Blood Hunter"
            jump hv_dnd_alignment
        "Homebrew":
            $ persistent.dnd_class = "Homebrew"
            jump hv_dnd_alignment

return

# -------------------------------
# ALIGNMENT
label hv_dnd_alignment:
    m 1eua "What alignment do you think fits your character best?"

    menu:
        "Lawful Good":
            $ persistent.dnd_alignment = "Lawful Good"
            jump hv_dnd_background
        "Neutral Good":
            $ persistent.dnd_alignment = "Neutral Good"
            jump hv_dnd_background
        "Chaotic Good":
            $ persistent.dnd_alignment = "Chaotic Good"
            jump hv_dnd_background
        "Other":
            jump hv_dnd_alignment_neutral

return

label hv_dnd_alignment_neutral:
    menu:
        "Lawful Neutral":
            $ persistent.dnd_alignment = "Lawful Neutral"
            jump hv_dnd_background
        "True Neutral":
            $ persistent.dnd_alignment = "True Neutral"
            jump hv_dnd_background
        "Chaotic Neutral":
            $ persistent.dnd_alignment = "Chaotic Neutral"
            jump hv_dnd_background
        "Other":
            jump hv_dnd_alignment_evil

return

label hv_dnd_alignment_evil:
    menu:
        "Lawful Evil":
            $ persistent.dnd_alignment = "Lawful Evil"
            jump hv_dnd_background
        "Neutral Evil":
            $ persistent.dnd_alignment = "Neutral Evil"
            jump hv_dnd_background
        "Chaotic Evil":
            $ persistent.dnd_alignment = "Chaotic Evil"
            jump hv_dnd_background
        "Other":
            $ persistent.dnd_alignment = "Homebrew"
            jump hv_dnd_background

return

# -------------------------------
# BACKGROUND
label hv_dnd_background:
    m 1eua "Alright, now let’s pick a background. What’s your character’s story?"

    menu:
        "Acolyte":
            $ persistent.dnd_background = "Acolyte"
        "Criminal":
            $ persistent.dnd_background = "Criminal"
        "Folk Hero":
            $ persistent.dnd_background = "Folk Hero"
        "Noble":
            $ persistent.dnd_background = "Noble"
        "Hermit":
            $ persistent.dnd_background = "Hermit"
        "Sage":
            $ persistent.dnd_background = "Sage"
        "Soldier":
            $ persistent.dnd_background = "Soldier"
        "Other":
            $ persistent.dnd_background = "Homebrew"

    jump hv_dnd_extras

# -------------------------------
# EXTRAS (weapon, familiar, spell)
label hv_dnd_extras:
    m 1eua "Do you want to pick a favorite weapon for your character?"

    menu:
        "Yes":
            $ persistent.dnd_weapon = renpy.input("Type your weapon of choice:")
        "No":
            $ persistent.dnd_weapon = "None"

    m 1eua "Do you want your character to have a companion or familiar?"

    menu:
        "Yes":
            $ persistent.dnd_familiar = renpy.input("Type your companion/familiar:")
        "No":
            $ persistent.dnd_familiar = "None"

    m 1eua "Any favorite spell or special ability?"

    menu:
        "Yes":
            $ persistent.dnd_spell = renpy.input("Type your favorite spell or ability:")
        "No":
            $ persistent.dnd_spell = "None"

    jump hv_dnd_summary

# -------------------------------
# SUMMARY
label hv_dnd_summary:
    m 1eua "Alright, [player]! Here's your full character:"
    m 3hua "[persistent.dnd_alignment] [persistent.dnd_race] [persistent.dnd_class] with a background as [persistent.dnd_background]."
    m 1hub "Weapon: [persistent.dnd_weapon], Familiar: [persistent.dnd_familiar], Favorite Spell/Ability: [persistent.dnd_spell]."
    m 3eua "You’d make an amazing adventurer! I can already imagine you in a party with me~"
    return

# Topic: Favorite Spell
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_spell",
            category=["Games"],
            prompt="Favorite Spell",
            random=True
        )
    )

label hv_dnd_fav_spell:
    m 1eua "Spells are so much fun! Which one would you say is your favorite?"

    menu:
        "Fireball":
            m 3hua "Boom! Classic choice. Explosions everywhere~"
        "Charm Person":
            m 1hub "Ooh, sneaky~ Trying to charm me too, [player]? 😉"
        "Mage Armor":
            m 1eua "Protective and practical, I like it."
        "Healing Word":
            m 3hub "Nice! Always keeping your friends alive… very thoughtful."
        "Other":
            $ persistent.dnd_spell_custom = renpy.input("Which spell is your favorite?")
            m 1hua "Ah, [persistent.dnd_spell_custom]! That’s a very interesting choice."

    return

# Topic: Favorite Campaign Setting
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_setting",
            category=["Games"],
            prompt="Favorite Campaign Setting",
            random=True
        )
    )

label hv_dnd_fav_setting:
    m 1eua "Campaign settings can really set the mood! Which world do you like best?"

    menu:
        "Forgotten Realms":
            m 3hua "Classic! So many epic stories take place there."
        "Ravenloft":
            m 1hub "Dark and spooky… I’d love to explore that with you~"
        "Eberron":
            m 3eua "Steampunk magic? Count me in!"
        "Homebrew":
            m 1hua "Your imagination must be amazing. Tell me all about it someday."
        "Other":
            $ persistent.dnd_setting_custom = renpy.input("Which campaign setting?")
            m 1hua "[persistent.dnd_setting_custom]? Ooh, that’s unique!"

    return

# Topic: Favorite Monster
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_monster",
            category=["Games"],
            prompt="Favorite Monster",
            random=True
        )
    )

label hv_dnd_fav_monster:
    m 1eua "Monsters make adventures exciting! Which one is your favorite?"

    menu:
        "Owlbear":
            m 3hua "Of course! The classic terrifyingly cute hybrid~"
        "Dragon":
            m 1hub "Powerful and majestic… scary and amazing at the same time."
        "Beholder":
            m 3eua "Eyeballs everywhere! That’s a fun choice."
        "Mind Flayer":
            m 1hua "Creepy and intelligent… very intimidating."
        "Other":
            $ persistent.dnd_monster_custom = renpy.input("Which monster?")
            m 3hua "[persistent.dnd_monster_custom]? That’s such an interesting pick!"

    return

# Topic: Favorite Dice
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_fav_dice",
            category=["Games"],
            prompt="Favorite Dice",
            random=True
        )
    )

label hv_dnd_fav_dice:
    m 1eua "Dice are so satisfying to roll… which one’s your favorite?"

    menu:
        "d20":
            m 3hua "The classic hero’s choice~"
        "d12":
            m 1hub "Ooh, the underrated one!"
        "d10":
            m 3eua "Perfect for percentiles and chaos~"
        "d8":
            m 1hua "Balanced and versatile, I like it."
        "d6":
            m 3hua "Good old standard die!"
        "d4":
            m 1hub "Tiny but mighty, hehe~"
        "Other":
            $ persistent.dnd_dice_custom = renpy.input("Which dice?")
            m 3hua "[persistent.dnd_dice_custom]? Fancy choice!"

    return

# Topic: Party Role
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_dnd_party_role",
            category=["Games"],
            prompt="Party Role",
            random=True
        )
    )

label hv_dnd_party_role:
    m 1eua "Every adventurer has a role in the party. Which do you usually play?"

    menu:
        "Leader":
            m 3hua "Taking charge, I like it!"
        "Damage Dealer":
            m 1hub "All the flashy moves, I love it~"
        "Support/Healer":
            m 3eua "Caring for the team, so reliable!"
        "Trickster":
            m 1hua "Mischief and cleverness, fun!"
        "Other":
            $ persistent.dnd_party_role_custom = renpy.input("Which role?")
            m 3hua "[persistent.dnd_party_role_custom]? That’s unique!"

    return


