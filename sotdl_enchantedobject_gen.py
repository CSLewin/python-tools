import random

#roll dice in XdY format
def diceroll(dicepool,sides):
	i = dicepool
	total = 0
	while i > 0:
		roll = random.randint(1,sides)
		total = total + roll
		i -= 1
	return total

BasicMeleeWeapon = random.choice(["axe", "club", "dagger" "knife", "dart", "hammer" "hatchet", "javelin", "sickle", "spear (basic)", "staff"])
RangedWeapon = random.choice(["blowgun", "bow", "crossbow", "hand crossbow", "longbow", "sling"])
Shield = random.choice(["small shield", "large shield"])
MilitaryMeleeWeapon = random.choice(["battleaxe", "flail" "morningstar", "pick", "sword", "glaive", "halberd", "poleaxe", "lance", "mace", "bastard sword", "warhammer", "pike", "spear (military)", "trident"])
SwiftMeleeWeapon = random.choice(["chain", "cutlass", "long knife", "scourge", "small sword", "rapier", "saber", "scimitar", "whip"])
HeavyMeleeWeapon = random.choice(["greataxe", "greatsword", "maul"])

enchanted_object_form = {
	1 : "light armor: " + random.choice(["robes", "soft leather", "hard leather", "brigandine"]),
	2 : "a melee weapon: " + random.choice([BasicMeleeWeapon, Shield, MilitaryMeleeWeapon, SwiftMeleeWeapon, HeavyMeleeWeapon]),
    3 : "jewelry: " + random.choice(["ring", "necklace", "bracelet"]),
    4 : "furniture: " + random.choice(["chair", "mirror", "rug"]),
    5 : "a sculpture: " + random.choice(["statuette", "idol", "taxidermied animal (small)", "taxidermied animal (large)"]),
    6 : "a coin: " + random.choice(["copper bit", "coppy penny", "silver shilling", "gold crown", "foreign coin", "strangely-shaped coin"]),
    7 : "a tool: " + random.choice(["hammer", "scales", "wrench"]),
	8 : "clothing: " + random.choice(["hat", "cloak", "shirt", "shoes", "boots", "pants", "undergarments"]),
	9 : "an instrument: " + random.choice(["lute", "drums", "flute", "pipe", "harp", "trumpet", "large shell", "hunting horn"]),
	10 : "a container: " + random.choice(["bag", "box", "chest", "sack", "puzzle box", "wallet", "saddlebag", "pack"]),
	11 : "an inscription: " + random.choice(["tome", "scroll", "clay tablet", "wax tablet", "etched sphere"]),
	12 : "an implement: " + random.choice(["wand", "crystal ball", "athame", "runed rod", "carved bone", "bell"]),
	13 : "technology: " + random.choice(["pocket watch", "pistol", "rifle", "bomb", "blunderbuss", "clockwork curio"]),
	14 : "a game or toy: " + random.choice(["deck of cards", "single playing card", "set of dice", "single die", "doll", "wooden soldier", "child's ball", "wooden toy sword"]),
	15 : "an accessory: " + random.choice(["key", "monocle", "scabbard", "fan", "opera glasses", "cufflinks", "belt buckle", "snuff tin"]),
	16 : "a vehicle: " + random.choice(["cart", "rowboat", "wagon", "carriage", "wheelbarrow"]),
	17 : "religious: " + random.choice(["holy symbol", "holy book", "prayer beads", "minor religious relic"]),
	18 : "weird: " + random.choice(["mummified hand", "bezoar", "bejeweled skull", "small organ in resin", "blown-glass insect"]),
	19 : "a ranged weapon: " + random.choice([RangedWeapon]),
	20 : "medium/heavy armor: " + random.choice(["mail", "scale", "plate and mail", "full plate"])
}

table1 = {
	1 : "You make challenge rolls with 1 boon to avoid becoming diseased or recover from disease. You take half damage from disease.",
	2 : "You make challenge rolls with 1 boon to avoid becoming poisoned or to remove the poisoned affliction. You take half damage from poison.",
    3 : "You take half damage from fire.",
    4 : "You do not become fatigued from exposure to extreme heat or cold.",
    5 : "You can use an action to cause the object to shed light in a 2-yard radius around it until you use a triggered action on your turn to end the effect.",
    6 : "When brought within 100 yards of a demon, the object slightly darkens the shadows surrounding the demon, negating the creature's horrifying trait.",
    7 : "You can speak one additional language, determined by the object's creator.",
    8 : "You always float 1 inch above the ground, though you still take damage on landing from a fall.",
    9 : "When you move, you can choose to do so without making a sound, regardless of the surface.",
    10 : "You can use an action to damp light in a 2-yard radius around the object. If lit, the area becomes shadows; if shadows, it becomes darkness.",
    11 : "When you attempt to climb, you make the Strength challenge roll with 1 boon.",
    12 : "When you attempt to swim, you make the Strength challenge roll with 1 boon.",
    13 : "You learn one additional profession, as determined by the object's creator.",
    14 : "Your Perception increases by 1.",
    15 : "Others cannot use magic to read your thoughts or communicate with you against your will.",
    16 : "If the object is a container, it can hold up to four times its apparent volume. Otherwise, when the object is placed inside a container, it multiplies the container's volume by four.",
    17 : "Neither you nor the object ever gets dirty.",
    18 : "You always know the exact time.",
    19 : "You always know which way is north.",
    20 : "The object has legs and acts as a compelled construct of its Size."
}

table2 = {
	1 : "The object warms a cold area within a 5-yard radius around it until the temperature is just above freezing.",
	2 : "When placed in a liquid, the object sinks and freezes the liquid around it in a 1-yard radius. Removing the frozen ball from the liquid deactivates the object, and the frozen material thaws as normal.",
    3 : "You can use an action to place the object on any flat surface no more than 6 inches thick that you can reach. The object and the surface it covers become transparent until it is removed from the surface.",
    4 : "You can use an action to cause flames to swirl around the object for as long as you concentrate, up to 1 minute. The flames shed light as a torch and deal 1d6 damage to anything they touch other than the creature wielding the object. The object has three uses. You regain expended uses once each day when you place the object in a fire.",
    5 : "The object is poisonous. Any living creature that comes into contact with it takes 1d6 damage from poison unless it gets a success on a Strength challenge roll.",
    6 : "The object radiates menace. Creatures within 5 yards of it make Will challenge rolls with 1 bane to resist being frightened.",
    7 : "You can use an action to place the object on any surface you can reach. The object stays there, no matter what, until you touch it and use an action to pick it up.",
	8 : "The object changes color to match its surroundings perfectly.",
	9 : "The object vibrates slightly when within 100 yards of a troll or giant.",
	10 : "You can use an action to extinguish all flames within 10 yards of you. The object has three uses. You regain expended uses once each day when you douse the object with water.",
	11 : "The object turns green when within 10 yards of a poison or a poisonous creature.",
	12 : "You can use an action to cause all doors, containers, and other objects that can be closed or opened within 10 yards of you to close or open as you decide. The object has three uses.",
	13 : "The object emits a field in a 10-yard-radius sphere around it that keeps out normal insects.",
	14 : "You can use a triggered action when you heal damage to heal twice the normal amount of damage. The object has one use.",
	15 : "You can use a triggered action on your turn to become invisible for 1 minute. You immediately become visible if you make an attack or cast a spell that deals damage. The object has one use.",
	16 : "You can use an action to choose one target creature or object within 10 yards of you. Make an Agility attack roll against the target's Agility. On a success, the target takes 2d6 damage from one of the following sources: acid, cold, fire, lightning, thunder, or something else of the GM's choice. The object has three uses.",
	17 : "You can use an action to choose one target living creature within 10 yards of you. Make a Will attack roll against the target's Will. On a success, the target becomes charmed for 1 minute or until it takes damage. The object has three uses. ",
	18 : "You can use an action to gain a +10 bonus to your Speed for 1 minute. After this time, you become fatigued for 1 minute. The object has three uses.",
	19 : "You can use an action to fly up to 100 yards and then land safely. The object has three uses.",
	20 : "You can use an action to toss the object onto an open space on the ground within 20 yards of you. The object disappears and a compelled small animal appears in the space. It serves you for 1 minute or until it becomes incapacitated. When the effect ends, the animal disappears and the object reappears in the space it left. The object has one use."
}

table3 = {
	1 : "You can use an action to cause the object to emit soft music until you use a triggered action at any time to silence it.",
	2 : "You can use a triggered action at any time to grant 1 boon on the next roll you make before the end of the round. The object has one use.",
    3 : "You can use a triggered action on your turn to change your appearance so you look like someone else. The effect lasts for 1 hour or until you take any damage. Suspicious creatures can make Perception challenge rolls to see through the disguise. The object has three uses.",
    4 : "You can use an action to cause fog to spread out 10 yards around the object. The fog remains for 1 minute or until dispersed by wind and partially obscures its area. The object has three uses. ",
    5 : "You can use an action to choose one target object you can see. You learn one true thing about the target. The object has three uses. ",
    6 : "You can use an action to choose a point on the ground within 20 yards of you. Grass, thick vines, and other growth spreads across the ground from that spot in a 5-yard-radius circle. The ground in the area is difficult terrain. The object has one use.",
    7 : "You can use an action to regain one casting of a rank 1 spell you know. The object has one use.",
	8 : "You can use an action to transform the object into a different object worth no more than 1 ss. The new form cannot have any magical properties. The object retains this shape until used again. The object has one use. ",
	9 : "You can use an action to create 1 gallon of pure, clean water. The object has one use.",
	10 : "You can use an action to create a permeable, opaque hemisphere with a radius of 5 yards centered on the object. The hemisphere remains in place for 8 hours. The object has one use.",
	11 : "You can use a triggered action on your turn to teleport to an open space you can see within 100 yards of you. The object has one use.",
	12 : "You can use an action to choose a point within 100 yards of you. You can hear from that spot as if you were there for as long as you concentrate, up to 1 minute. The object has three uses.",
	13 : "You can use a triggered action on your turn to communicate telepathically with any willing creature that knows at least one language and is within 20 yards of you. The effect lasts for 1 minute. The object has three uses.",
	14 : "You move at full speed across difficult terrain.",
	15 : "You can breathe normally when submerged in liquid.",
	16 : "You can use an action to grant 1 boon on all challenge rolls you make for 1 minute. The object has one use.",
	17 : "You can use an action to clear away vapors, gases, fog, smoke, or mist within 10 yards of the object. The object has one use.",
	18 : "You can use an action to reduce by 1d3 (to a minimum of 0) the number of banes on attack rolls and challenge rolls you make for 1 minute. The object has one use.",
	19 : "You can use an action to cause the object to vanish into an extradimensional space. At any time thereafter, you can use a triggered action to call the object back to hand.",
	20 : "You can use an action to grant 2 boons on the next roll you make before the end of the round. The object has one use.",
}

table4 = {
	1 : "You make challenge rolls with 1 boon to see Illusions for what they are.",
	2 : "You can use a triggered action on your turn to jump forward in time. You disappear and reappear at the end of the round in the same space or the open space nearest to it if it is occupied. The object has three uses.",
    3 : "You can use a triggered action when you make an attack roll with a spell you cast to grant 1 boon on that roll. The object has one use.",
    4 : "Each hour you rest, roll a d6. On a 6, you heal 2d6 damage.",
    5 : "You cannot be surprised.",
    6 : "Your jumping distance is doubled.",
    7 : "You can move across and stand on liquid surfaces as if they were solid ground.",
	8 : "You can use a triggered action on your turn to become insubstantial until the end of the round. While insubstantial, you take half damage from weapons, can move through solid objects and other creatures, and ignore the effects of moving across difficult terrain. If you end your movement inside a solid object, you die instantly. The object has three uses.",
	9 : "This object is a suit of armor with no Strength requirement.",
	10 : "This object is a weapon or a piece of ammunition that can never break or be lost. When you succeed on an attack roll using this weapon, you can use a triggered action to fill the target of the attack with dread. The target becomes frightened for 1 round unless it gets a success on a Will challenge roll.",
	11 : "The object glows whenever someone within 5 yards of it knowingly speaks a lie. ",
	12 : "You gain shadowsight.",
	13 : "You increase your healing rate by an amount equal to your level.",
	14 : "When you get a failure on a challenge roll required by a spell, you can use a triggered action to turn the failure into a success. The object has one use.",
	15 : "You can use an action to transform the object into a 10-foot-long ladder. The object remains in this form until you use an action to transform it back.",
	16 : "You can use an action to transform into a tiny animal. You remain in that form for up to 1 hour, until you become unconscious, or until you use a triggered action on your turn to return to your normal form. The object has one use.",
	17 : "You can use an action to instantly and safely transport yourself and up to five other willing creatures within your reach to a destination chosen by the GM. The destination can be the same each time you use the object or a different one. The object has one use. ",
	18 : "You can use a triggered action when a creature gets a failure on an attack roll with a melee weapon to teleport to an open space within 1 yard of the triggering creature. ",
	19 : "You can use an action to touch the object. The object disappears and becomes a tattoo on your body, where it remains until you use a triggered action on your turn to retrieve it. Once retrieved, the object appears in your hand or in an open space within your reach.",
	20 : "You can use an action to protect yourself from magic for 1 round. Until the effect ends, you make challenge rolls required by spells or other magical effects with 1 boon. As well, creatures make attack rolls with 1 bane when attacking you with spells. The object has one use."
}

attribute = random.choice(["Strength", "Agility", "Intellect", "Willpower"])

table5 = {
	1 : "You make Will challenge rolls with 1 boon to avoid gaining Insanity.",
	2 : "You make challenge rolls with 1 boon to break down doors, open chests, and lift heavy weights.",
    3 : "You can use an action to cause the object to emit a deafening noise in a 10-yard radius around it for 1 minute. During that time, all creatures in the area are deafened while they remain in the area, and creatures within 100 yards of the object make Perception challenge rolls to listen with 1 bane. The object has three uses.",
    4 : "You can use a triggered action on your turn to deal 1d6 extra damage with all attacks you make for 1 round. The object has three uses. ",
    5 : "The object is buoyant and never sinks. It always floats back to the surface of any liquid into which it is placed.",
    6 : "The object is possessed by a tiny demon. When you become incapacitated, you immediately heal damage equal to your healing rate and become controlled by the demon for 1 minute. See Demonic Possession in Chapter 10.",
    7 : "The object is invisible in light.",
	8 : "The object is a weapon. You reduce by 1 the number of banes imposed on rolls you make to attack with it (to a minimum of 0).",
	9 : "When you cast a rank 1 or 2 spell, roll a d6. On a 1, you gain 1 Insanity. On a 6, you regain the casting of that spell. On any other number, there is no effect. ",
	10 : "You do not need to breathe.",
	11 : "You make all attack rolls in social settings with 1 boon.",
	12 : "When you move, you either leave no tracks or your tracks look like they were left by a creature you choose.",
	13 : "Areas of shadows caused by demons within 100 yards of you become lit, and you are immune to the creatures' horrifying trait.",
	14 : "You do not need to eat or drink.",
	15 : "You cannot become frightened.",
	16 : "The object makes a chiming noise whenever it is brought within 20 yards of a trap.",
	17 : "The object contains a rank 1 spell of the GM's choice. You can cast the spell from the object regardless of your Power. This spell has one casting, which is regained once each day at dawn.",
	18 : "Your " + attribute + " score and modifier increases by 1.",
	19 : "The object has two properties.  Roll two more objects and add their properties to this one!  Maybe code this in later, yeah?",
	20 : "The object has three properties.  Roll three more objects and add their properties to this one!  Maybe code this in later, yeah?",
}

tableroll = diceroll(1,20)

enchanted_object_properties = {
	1 : table1[tableroll],
	2 : table2[tableroll],
	3 : table3[tableroll],
	4 : table4[tableroll],
	5 : table5[tableroll]
}

def roll_enchanted_object():
	roll = diceroll(1,20)
	return enchanted_object_form[roll]

def roll_enchanted_object_property():
	roll = diceroll(1,5)
	return enchanted_object_properties[roll]

print ""
print "The form of the enchanted object is " + roll_enchanted_object()
print "The magical property of the object: " + roll_enchanted_object_property()
print ""