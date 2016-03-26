#By Craig Lewin (CSLewin@gmail.com).  Written around the end of February/beginning of March 2016 as a way to learn how to use Python.

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

#roll two identical sets of dice in xdy format; return one unless they match exactly and then return reroll the second one and return both
def reroll(dicepool,sides,triggermin,triggermax): 
	trigger = range(triggermin,(triggermax + 1))
	roll1 = diceroll(dicepool,sides)
	
	if roll1 in trigger:
		roll2 = diceroll(dicepool,sides)
		while roll2 == roll1 or roll2 in trigger:
			roll2 = diceroll(dicepool,sides)
		results = [roll1, roll2]
		return results
	else:
		return [roll1]

#these are the parts that every book has (set to empty so they exist later to be filled)
book = {
	"book_type":"",
	"condition":"",
	"cover":"",
	"pages":"",
	"authors":"",
	"script":"",
	"language":"",
	"ink":"",
	"illustrations":"",
	"illustration_quality":"",
	"contents":"",
	"incantation_tradition":"",
	"incantation_rank":"",
	"special_features":""
}

tablet_form = random.choice(["clay", "wax", "wood", "stone", "the scales of a large reptile", "chitin", "bone"])
scroll_form = random.choice(["papyrus", "parchment", "vellum", "paper", "snakeskin", "scales", "living skin"])

book_type = {
	3 : "tablet made of " + tablet_form + ".",
	4 : "tablet made of " + tablet_form + ".",
    5 : "scroll made of " + scroll_form + ".",
    6 : "scroll made of " + scroll_form + ".",
    7 : "scroll made of " + scroll_form + ".",
    8 : "scroll made of " + scroll_form + ".",
    9 : "folio with ~25 pages.",
	10 : "folio with ~25 pages.",
	11 : "folio with ~25 pages.",
	12 : "folio with ~25 pages.",
	13 : "book with ~100 pages.",
	14 : "book with ~100 pages.",
	15 : "book with ~100 pages.",
	16 : "tome with ~200 pages.",
	17 : "tome with ~200 pages.",
	18 : "codex of over 500 pages."
}

condition = {
	3 : "is considerably damaged, with most pages eaten by worms, burned, or missing. Water damage has made much of it illegible.",
	4 : "is considerably damaged, with most pages eaten by worms, burned, or missing. Water damage has made much of it illegible.",
    5 : "has seen some light wear.",
    6 : "has seen some light wear.",
    7 : "has seen some light wear.",
    8 : "has seen some light wear.",
    9 : "is worn, with several bent and torn pages, scratches, and stains.",
	10 : "is worn, with several bent and torn pages, scratches, and stains.",
	11 : "is worn, with several bent and torn pages, scratches, and stains.",
	12 : "is worn, with several bent and torn pages, scratches, and stains.",
	13 : "is in poor shape, with loose components, extensive staining, and what might be burns.",
	14 : "is in poor shape, with loose components, extensive staining, and what might be burns.",
	15 : "is in poor shape, with loose components, extensive staining, and what might be burns.",
	16 : "is brand new and virtually unscathed.",
	17 : "is brand new and virtually unscathed.",
	18 : "is brand new and virtually unscathed."
}

skin = random.choice(["human skin.", "dwarf skin.", "faerie skin.", "a unrecognizable skin."])
bone = random.choice(["brittle bone.", "yellowed ivory.", "heavy horn.", "fused teeth."])
metal = random.choice(["rusted iron.", "hammer-forged steel.", "beaten bronze.", "lustrous gold."])
book_cover_lock = diceroll(1,6)
if book_cover_lock in range(1,6):
    book_cover_lock = "nowhere to be found."
elif book_cover_lock == 6:
    book_cover_lock = "within sight."
book_cover_animatedorgan = random.choice(["tongue nailed to the surface.", "penis nailed to the surface.", "eye nailed to the surface."])

cover = {
	3 : "is missing, long since torn off.",
	4 : "is made from thin wood.",
    5 : "is made from thin wood wrapped in cloth.",
    6 : "is made from thin wood wrapped in leather.",
    7 : "is made from thin wood wrapped in " + skin,
    8 : "is made from thin wood or metal covered in gold leaf.",
    9 : "is made from " + bone,
	10 : "is made from " + metal,
	11 : "is made from " + metal,
	12 : "is made from " + metal,
	13 : "is made from wood and covered in spikes.",
	14 : "is made from rough iron that bristles with blades and barbs.",
	15 : "is made from a quilt of living faces.",
	16 : "is locked, and the key is " + book_cover_lock,
	17 : "is wrapped in chains or razor wire.",
	18 : "has an animated " + book_cover_animatedorgan
}

pages = {
	3 : "are made of hair, tissue, or nails.",
	4 : "are made of crackling parchment.",
    5 : "are made of crackling parchment.",
    6 : "are made of scraped vellum.",
    7 : "are made of scraped vellum.",
    8 : "are made of scraped vellum.",
    9 : "are made of bleached paper.",
	10 : "are made of bleached paper.",
	11 : "are made of bleached paper.",
	12 : "are made of bleached paper.",
	13 : "are made of translucent onionskin.",
	14 : "are made of translucent onionskin.",
	15 : "are made of translucent onionskin.",
	16 : "are made of fine metal plates.",
	17 : "are made of fine metal plates.",
	18 : "are made of delicately etched glass."
}

script = {
	3 : "is crazed and wild.",
	4 : "is scrawled and messy.",
    5 : "is scrawled and messy.",
    6 : "is small and cramped.",
    7 : "is small and cramped.",
    8 : "is small and cramped.",
    9 : "has been printed neatly.",
	10 : "has been printed neatly.",
	11 : "has been printed neatly.",
	12 : "has been printed neatly.",
	13 : "flows elegantly.",
	14 : "flows elegantly.",
	15 : "flows elegantly.",
	16 : "is big and bold.",
	17 : "is big and bold.",
	18 : "is masterfully illuminated."
}

language = {
	3 : "Dark Speech",
	4 : "Trollish",
    5 : "Trollish",
    6 : "Dwarfish", 
    7 : "Dwarfish", 
    8 : "Dwarfish", 
    9 : "Common Tongue", 
	10 : "Common Tongue", 
	11 : "Common Tongue", 
	12 : "Common Tongue", 
	13 : "High Archaic", 
	14 : "High Archaic", 
	15 : "High Archaic", 
	16 : "Elvish", 
	17 : "Elvish", 
	18 : "a secret, dead, or unknown language"
}

ink = {
	3 : "bodily fluids such as blood or urine.",
	4 : "squid ink.",
    5 : "lemon juice.",
    6 : "black oil-based ink.",
    7 : "blue oil-based ink.",
    8 : "brown oil-based ink.",
    9 : "black water-based ink.",
	10 : "black water-based ink.",
	11 : "blue water-based ink.",
	12 : "brown water-based ink.",
	13 : "yolk paints.",
	14 : "ochre paints.",
	15 : "mineral paints.",
	16 : "pure silver etched or scratched in the surface.",
	17 : "pure gold etched or scratched in the surface.",
	18 : "poison! (A living creature that comes into physical contact withthe ink must get a success on a Strength challenge roll or become poisoned for 1 minute. At the end of each round, the creature must repeat the roll, taking 1d6 damage for each failre."
}

illustrations = {
	3 : "abundant",
	4 : "some",
    5 : "some",
    6 : "sparse",
    7 : "sparse",
    8 : "sparse",
    9 : "no",
	10 : "no",
	11 : "no",
	12 : "no",
	13 : "sparse",
	14 : "sparse",
	15 : "sparse",
	16 : "some",
	17 : "some",
	18 : "abundant"
}

illustration_quality = {
	3 : "disturbing.",
	4 : "ugly.",
    5 : "ugly.",
    6 : "varied in quality, some fine, some not.",
    7 : "varied in quality, some fine, some not.",
    8 : "varied in quality, some fine, some not.",
    9 : "crude, or, at best, simple.",
	10 : "crude, or, at best, simple.",
	11 : "crude, or, at best, simple.",
	12 : "crude, or, at best, simple.",
	13 : "highly detailed.",
	14 : "highly detailed.",
	15 : "highly detailed.",
	16 : "beautiful.",
	17 : "beautiful.",
	18 : "animated!"
}

#etiquette_or_heraldry = random.choice(["Etiquette & Customs", "Heraldry"])

incantation_single = 1
incantation_1d3 = diceroll(1,3)
incantation_1d6 = diceroll(1,6)
incantation_2d6 = diceroll(2,6)

contents = {
	1 : "are filled with false or misleading information. Roll on the Academic Professions table on page 24 of Shadow of the Demon Lord. The text, when referenced, imposes 1 bane on Intellect challenge rolls made to perform a task related to its subject matter.",
	2 : "are on the subject of " + random.choice(["Architecture.", "Engineering."]),
    3 : "are on the subject of " + random.choice(["Astrology.", "Folklore."]),
    4 : "are on the subject of " + random.choice(["Etiquette & Customs.", "Heraldry."]),
    5 : "are on the subject of " + random.choice(["Geography.", "Navigation."]),
    6 : "are on the subject of " + random.choice(["History.", "Literature."]),
    7 : "are on the subject of " + random.choice(["Law.", "Politics."]),
	8 : "are on the subject of " + random.choice(["Magic.", "Occult."]),
	9 : "are on the subject of " + random.choice(["Medicine.", "Nature.", "Science."]),
	10 : "are a fictional story.",
	11 : "are a personal diary or journal.",
	12 : "are a screed or libel against " + random.choice(["a particular person.", "an organization.", "a particular nation."]),
	13 : "are pornographic.",
	14 : random.choice(["are complete gibberish.", "are entirely blank."]),
	15 : "are on the subject of " + random.choice(["Philsophy.", "Religion."]),
	16 : "are on the subject of War.",
	17 : "consist of " + str(incantation_single) + " incantation(s)!",
	18 : "consist of " + str(incantation_1d3) + " incantation(s)!",
	19 : "consist of " + str(incantation_1d6) + " incantation(s)!",
	20 : "consist of " + str(incantation_2d6) + " incantation(s)!"
}

incantation_tradition = {
	1 : "Air",
	2 : "Alchemy",
	3 : "Alteration",
	4 : "Arcana",
    5 : "Battle",
    6 : "Celestial", 
    7 : "Chaos", 
    8 : "Conjuration",
    9 : "Curse",
	10 : "Death",
	11 : "Demonology",
	12 : "Destruction",
	13 : "Divination",
	14 : "Earth",
	15 : "Enchantment",
	16 : "Fire",
	17 : "Forbidden",
	18 : "Illusion",
	19 : "(GM's Choice)",
	20 : "(GM's Choice)",
	21 : "Life",
	22 : "Nature",
	23 : "Necromacy",
	24 : "Primal",
    25 : "Protection",
    26 : "Rune",
    27 : "Shadow",
    28 : "Song",
    29 : "Spiritualism",
	30 : "Storm",
	31 : "Technomancy",
	32 : "Telekinesis",
	33 : "Telepathy",
	34 : "Teleportation",
	35 : "Theurgy",
	36 : "Time",
	37 : "Transformation",
	38 : "Water",
	39 : "(GM's Choice)",
	40 : "(GM's Choice)"
}

incantation_rank = {
	3 : "4",
	4 : "3",
    5 : "3",
    6 : "1",
    7 : "1",
    8 : "1",
    9 : "0",
	10 : "0",
	11 : "0",
	12 : "0",
	13 : "2",
	14 : "2",
	15 : "2",
	16 : "5",
	17 : "5",
	18 : "6 or higher!"
}

strangereading = random.choice(["in a mirror.", "by the light of the moon.", "in total darkness."])
strangebinding = random.choice(["thread-like worms.", "tiny, clutching hands.", "perfect rows of miniscule teeth."])
strangecompartment = random.choice(["poisonous gas that billows out when opened, forcing each living, breathing creature within short range to make a Strength challenge roll. On a failure, the creature takes 3d6 damage and becomes poisoned for 1 hour. This trap can be triggered only once.", "a hand-written letter.", "nothing.", "1d6 silver shillings.", "an enchanted object!"])

special_features = {
	3 : "The writing stains the soul of any creature that reads it. A creature reading the words must get a success on a Will challenge roll with 1d3 banes or gain 1 Corruption.",
	4 : "The text is unreadable unless read " + strangereading,
    5 : "The text is unreadable unless read " + strangereading,
    6 : "The binding is utterly bizarre, the pages held in place by " + strangebinding,
    7 : "The binding is utterly bizarre, the pages held in place by " + strangebinding,
    8 : "The binding is utterly bizarre, the pages held in place by " + strangebinding,
    9 : "The book has a secret compartment containing " + strangecompartment,
	10 : "The book has a secret compartment containing " + strangecompartment,
	11 : "The book has a secret compartment containing " + strangecompartment,
	12 : "The book has a secret compartment containing " + strangecompartment,
	13 : "The writing inspires madness. When a creature reads the text, it must make a Will challenge roll with 1d3 banes. On a failure, the creature must read the book for 1d6 hours unless prevented in some way, in which case the creature becomes impaired until the effect ends. At the end of each hour, the creature must repeat the Will challenge roll, gaining 1 Insanity on a failure.",
	14 : "The writing inspires madness. When a creature reads the text, it must make a Will challenge roll with 1d3 banes. On a failure, the creature must read the book for 1d6 hours unless prevented in some way, in which case the creature becomes impaired until the effect ends. At the end of each hour, the creature must repeat the Will challenge roll, gaining 1 Insanity on a failure.",
	15 : "The book is infested with toothy parasites! A creature that opens the book must get a success on an Agility challenge roll with 1d3 banes or take 1d6 damage from the burrowing parasites. At the end of each round, the creature must get a success on a Strength challenge roll with 1 bane or take 1d6 damage. After three successes or the affected creature takes 10 damage or more from fire, the effect ends.",
	16 : "The book is infested with toothy parasites! A creature that opens the book must get a success on an Agility challenge roll with 1d3 banes or take 1d6 damage from the burrowing parasites. At the end of each round, the creature must get a success on a Strength challenge roll with 1 bane or take 1d6 damage. After three successes or the affected creature takes 10 damage or more from fire, the effect ends.",
	17 : "The book bears a magical trap! Finding the trap requires a success on a Perception challenge roll with 3 banes. A creature with an academic profession involving magical knowledge makes the roll with 1 boon. Reading any words in the book causes it to explode in flames. The book and everything within short range of it takes 3d6 damage. A creature that gets a success on an Agility challenge roll takes half the damage instead.",
	18 : "The book is alive (as a small construct that has teeth in place of an appendage) and attacks any creature that handles it."
}

###
#####
####### Start actually generating and printing the details of the book
#####	\/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ \/ 
###		


#roll the book's physical type (tablet, scroll, book)
def check_book_type():
	global book
	roll = diceroll(3,6)
	return book_type[roll]

print ""
print "This is a", check_book_type()

#Roll the physical condition of the work
def check_book_condition():
	global book
	roll = diceroll(3,6)
	return condition[roll]

print "The work", check_book_condition()

#Roll the details of the cover
def check_book_cover():
	global book
	book_cover = reroll(3,6,16,18)
	if len(book_cover) == 2:
		return str(cover[book_cover[0]]) + " The material of the cover " + str(cover[book_cover[1]]) #display the text result of the first and second roll
	else:
		return cover[book_cover[0]] #display the associated text result of the first roll

print "Tablets have no cover. Otherwise, the scroll case or cover", check_book_cover()

#Roll the details of the pages.  Later on, figure out a way to only roll this for books, not tablets or scrolls.
def check_book_pages():
	global book
	roll = diceroll(3,6)
	return pages[roll]

print "Tablets and scrolls lack pages, but if this is a book, the pages", check_book_pages()

#Roll the number of authors and the script of each. This is kind of messy, but it's functional!
def check_book_authors_and_scripts():
	global book
	author_check = diceroll(1,3)
	if author_check < 3:
		scriptroll = diceroll(3,6)
		languageroll = diceroll(3,6)
		inkroll = diceroll(3,6)
		return "There is a single author. Their writing " + str(script[scriptroll]) + " Their words are in " + str(language[languageroll]) + " and have been written using " + str(ink[inkroll])
	else:
		number_of_authors = (diceroll(1,3) + 1)
		print "There are", number_of_authors, "authors:"
		i = number_of_authors
		author_list = ""
		while i > 0:
			scriptroll = diceroll(3,6)
			languageroll = diceroll(3,6)
			inkroll = diceroll(3,6)
			author_list += ("One author's writing " + str(script[scriptroll]) + " Their words are in " + str(language[languageroll]) + " and have been written using " + str(ink[inkroll])) + " "
			i -= 1
		return author_list

print str(check_book_authors_and_scripts())

#Determine if the book contains illustrations. If there are any, describe their quality.
def check_book_illustrations():
	global book
	roll = diceroll(3,6)
	return illustrations[roll]

illustration_presence = check_book_illustrations()

def check_book_illustration_quality():
	global book
	roll = diceroll(3,6)
	return illustration_quality[roll]

print "The work offers", illustration_presence, "illustrations."
if illustration_presence != "no":
	print "The illustrations are each", check_book_illustration_quality()

#Determine what the book is actually about.
def check_book_contents():
	global book
	roll = diceroll(1,20)
	return contents[roll]

contents = check_book_contents()
print "The work's contents", contents

#If incantations are present, identify how many appear from earlier results as well as the tradition and rank of each one.
def check_book_incantation_tradition():
	global book
	roll = diceroll(1,40)
	return incantation_tradition[roll]
	
if contents[-15:] == "incantation(s)!":
	incantation_count = int(contents[-18:-15])
	i = incantation_count
	incantation_list = "The incantations are "
	while i > 0:
		roll = diceroll(3,6)
		incantation_level = incantation_rank[roll]
		incantation_list += check_book_incantation_tradition() + " (Rank " + str(incantation_level) + "); "
		i -= 1
	print incantation_list

#roll a d6
#if the result is 1, roll 1d6-3.  If THAT result is less than 1, set it to 1.
#Print a number of special feaures equal to the final result of the second roll.

def check_book_special_features():
	global book
	roll = diceroll(1,6)
	if roll != 1:
		return "The work displays no other special features."
	else:
		roll2 = diceroll(1,6) - 3
		i = max(roll2, 1)
		while i > 0:
			roll3 = diceroll(3,6)
			special_feature_list = ""
			special_feature_list += special_features[roll3]
			i -= 1
		return special_feature_list

print check_book_special_features()

print ""

