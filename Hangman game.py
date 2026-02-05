from random import *
def get_word():
    word_list = [
    # Animals & Nature
    "albatross", "alligator", "alpaca", "anaconda", "antelope", "aquarium", "archipelago", "armadillo", "avalanche", "baboon",
    "badger", "barracuda", "bat", "beaver", "beetle", "blizzard", "boulder", "buffalo", "butterfly", "cactus",
    "camel", "canary", "canyon", "capybara", "cataract", "chameleon", "cheetah", "chimpanzee", "chipmunk", "clover",
    "cobra", "cockatoo", "condor", "coral", "coyote", "cricket", "crocodile", "cyclone", "daffodil", "dahlia",
    "dolphin", "dragonfly", "drought", "eagle", "earthquake", "eclipse", "elephant", "falcon", "flamingo", "forest",
    "galaxy", "gazelle", "geyser", "giraffe", "glacier", "gorilla", "grasshopper", "hamster", "hedgehog", "hippopotamus",
    "horizon", "hummingbird", "hurricane", "hyena", "iceberg", "iguana", "island", "jaguar", "jungle", "kangaroo",
    "koala", "leopard", "lightning", "lizard", "lobster", "mammoth", "manatee", "meadow", "meteor", "monsoon",
    "mountain", "nebula", "nightingale", "octopus", "orchard", "ostrich", "panther", "peacock", "pelican", "penguin",
    "petunia", "pheasant", "plateau", "platypus", "porcupine", "precipice", "python", "raccoon", "rainbow", "raindrop",
    "rat", "raven", "reef", "rhinoceros", "river", "salamander", "scorpion", "seagull", "seahorse", "sequoia",
    "shark", "skeleton", "sky", "snail", "snowstorm", "sparrow", "spider", "squirrel", "starfish", "sunflower",
    "swamp", "swan", "thunder", "tiger", "tornado", "toucan", "tundra", "turtle", "twilight", "typhoon",
    "universe", "valley", "vampire", "volcano", "vulture", "walrus", "waterfall", "whale", "willow", "wolf",
    "wolverine", "wombat", "woodpecker", "zebra", "zodiac",

    # Objects & Tools
    "anchor", "anvil", "ashtray", "axe", "backpack", "balloon", "banner", "barrel", "basket", "battery",
    "beacon", "beaker", "bell", "bicycle", "binoculars", "blanket", "blueprint", "boiler", "boomerang", "bottle",
    "bracelet", "bracket", "bridge", "broom", "bucket", "buckle", "bulletin", "button", "cabinet", "calculator",
    "calendar", "camera", "candle", "canvas", "capsule", "carburetor", "carpet", "carriage", "cartridge", "cassette",
    "castle", "cauldron", "ceiling", "cellphone", "chain", "chair", "chalk", "chandelier", "chisel", "circuit",
    "clock", "closet", "clutch", "compass", "computer", "conduit", "container", "corkscrew", "cradle", "crayon",
    "crowbar", "crystal", "cupboard", "curtain", "cushion", "dagger", "dashboard", "desk", "diaper", "dictionary",
    "doorbell", "drain", "drawer", "drill", "drum", "dynamo", "earring", "easel", "engine", "envelope",
    "eraser", "faucet", "feather", "fender", "filter", "firecracker", "flashlight", "flask", "floppy", "flowerpot",
    "forklift", "fountain", "frame", "furnace", "gadget", "gasket", "gate", "gauge", "gear", "generator",
    "glasses", "glove", "goggles", "hammer", "hammock", "hanger", "harness", "harvest", "helmet", "hinge",
    "holster", "hook", "hourglass", "inkwell", "insulator", "inventory", "jacket", "jar", "jewelry", "joystick",
    "kettle", "keyboard", "keychain", "kiln", "knapsack", "knife", "knob", "ladder", "lantern", "laptop",
    "latch", "lawnmower", "ledger", "lens", "level", "lever", "lighter", "lock", "locket", "loom",
    "magnet", "magnifier", "mallet", "mantel", "marker", "mask", "mattress", "megaphone", "microscope", "mirror",
    "missile", "mixer", "monitor", "mortar", "mousepad", "muzzle", "necklace", "needle", "net", "notebook",
    "nozzle", "oar", "ornament", "outlet", "padlock", "paintbrush", "palette", "pamphlet", "paperclip", "parachute",
    "parchment", "pavement", "pedal", "pencil", "pendulum", "phone", "piano", "pillow", "pincer", "pipe",
    "piston", "pitcher", "plunger", "pocket", "portfolio", "postcard", "pottery", "propeller", "pulley", "pump",
    "puppet", "purse", "puzzle", "pyramid", "quiver", "radar", "radiator", "radio", "raft", "rail",
    "razor", "refrigerator", "remote", "reservoir", "revolver", "ribbon", "rifle", "ring", "robot", "rocket",
    "roller", "rope", "rotor", "ruler", "saddle", "safari", "safe", "sail", "satellite", "saucer",
    "scalpel", "scanner", "scarf", "scissors", "scooter", "screen", "screw", "scythe", "sensor", "shampoo",
    "shovel", "shutter", "sieve", "silo", "skateboard", "skillet", "sledge", "slipper", "snorkel", "soap",
    "socket", "sofa", "spanner", "spatula", "speaker", "spectacles", "sphere", "sponge", "spoon", "spring",
    "sprinkler", "spyglass", "statue", "stencil", "stethoscope", "sticker", "stretcher", "subway", "suitcase", "switch",
    "syringe", "table", "tablet", "tackle", "tanker", "tape", "target", "teapot", "telescope", "tent",
    "terminal", "thermometer", "thimble", "ticket", "tile", "toaster", "torch", "tower", "tractor", "trailer",
    "trampoline", "transformer", "transmitter", "tray", "trellis", "tripod", "trophy", "trowel", "truck", "trumpet",
    "tube", "tunnel", "turbine", "tweezers", "typewriter", "umbrella", "unicycle", "urn", "utensil", "vacuum",
    "valve", "vase", "vault", "vehicle", "vending", "ventilation", "vessel", "vest", "vial", "video",
    "violin", "vise", "visor", "wagon", "wallet", "wardrobe", "washer", "watch", "weapon", "wheel",
    "wheelbarrow", "whistle", "wig", "winch", "window", "windshield", "wire", "wrench", "wristband", "xylophone",
    "yacht", "yardstick", "zipper", "zither",

    # Food & Drink
    "almond", "apple", "apricot", "artichoke", "asparagus", "avocado", "bacon", "bagel", "banana", "barley",
    "basil", "bean", "beef", "beer", "berry", "biscuit", "blackberry", "blueberry", "bread", "broccoli",
    "brownie", "burger", "butter", "cabbage", "cake", "candy", "cantaloupe", "caramel", "carrot", "cashew",
    "cauliflower", "celery", "cereal", "cheese", "cherry", "chestnut", "chicken", "chili", "chocolate", "cider",
    "cinnamon", "citrus", "coconut", "coffee", "cookie", "corn", "cracker", "cranberry", "cucumber", "cupcake",
    "curry", "custard", "dairy", "date", "dessert", "donut", "dough", "dressing", "eggplant", "espresso",
    "fig", "fillet", "flour", "garlic", "ginger", "grape", "grapefruit", "gravy", "guava", "honey",
    "horseradish", "hummus", "icing", "jam", "jelly", "juice", "kebab", "ketchup", "kiwi", "lasagna",
    "lemon", "lemonade", "lentil", "lettuce", "lime", "liquorice", "macaroni", "mango", "maple", "margarine",
    "marshmallow", "melon", "milk", "mint", "muffin", "mushroom", "mustard", "noodle", "nutmeg", "oatmeal",
    "olive", "onion", "orange", "pancake", "papaya", "parsley", "pasta", "pastry", "peach", "peanut",
    "pear", "pecan", "pepper", "pickle", "pineapple", "pistachio", "pizza", "plum", "pomegranate", "popcorn",
    "potato", "pretzel", "pumpkin", "radish", "raisin", "raspberry", "ravioli", "rice", "rosemary", "salad",
    "salmon", "sandwich", "sauce", "sausage", "seafood", "shrimp", "soup", "spinach", "steak", "strawberry",
    "sugar", "syrup", "taco", "tangerine", "tea", "toast", "tofu", "tomato", "truffle", "turkey",
    "vanilla", "vinegar", "waffle", "walnut", "watermelon", "wheat", "whiskey", "yogurt", "zucchini",

    # Abstract & Jobs
    "abbey", "academy", "accent", "adventure", "agent", "alias", "alphabet", "ambassador", "amulet", "ancestor",
    "ancient", "angel", "anthem", "antique", "apprentice", "architect", "archive", "arena", "armor", "artist",
    "astronaut", "athlete", "attic", "audience", "author", "avatar", "avenue", "award", "balance", "ballad",
    "bandit", "banker", "baron", "bazaar", "beggar", "belief", "benefit", "bishop", "blessing", "boundary",
    "bravery", "brigade", "brother", "bubble", "budget", "burglar", "business", "butcher", "captain", "caravan",
    "career", "cartoon", "cathedral", "century", "champion", "chaos", "chapter", "charity", "charlatan", "charter",
    "chemist", "chess", "chieftain", "childhood", "choir", "chronicle", "cinema", "citizen", "cleric", "climate",
    "clown", "cluster", "college", "colony", "column", "comedy", "command", "commerce", "community", "company",
    "concept", "concert", "congress", "conquest", "context", "contract", "costume", "council", "courage", "cousin",
    "cowboy", "craftsman", "creature", "culture", "curiosity", "custom", "danger", "daughter", "decade", "defense",
    "dentist", "deputy", "desert", "design", "destiny", "diamond", "diploma", "director", "disaster", "discovery",
    "disease", "disguise", "distance", "district", "divinity", "doctor", "dolphin", "domain", "donation", "dragon",
    "drama", "dream", "dynasty", "economy", "editor", "education", "element", "embassy", "emperor", "empire",
    "energy", "enigma", "episode", "essence", "eternity", "evidence", "example", "exchange", "exhibit", "exile",
    "existence", "experiment", "expert", "explorer", "factory", "faculty", "failure", "fairytale", "faith", "family",
    "fantasy", "fashion", "father", "fiction", "fighter", "finance", "fireman", "flame", "flavor", "flight"
]
    word=choice(word_list)
    return word.upper()
def play(w):
    print(guess)
    letter=input()
    global tries
    global result
    if tries==0:
        print('YOU RE LOST!')
        return False
    elif guess==list(w):
        print('YOU WIN!')
    elif letter in w:
        print('You guessed!')
        n=w.count(letter)
        for i in range(n):
            ix=w.index(letter)
            guess[ix]=letter
            w=w.replace(letter,'-',1)
        print(guess)
    else:
        print('You re wrong!')
        tries-=1
        print('You have -',tries,'tries')
        return tries
def hangman(tries_count):
    if tries_count==6:
        print(''''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''')
    elif tries_count==5:
        print('''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''')
    elif tries_count==4:
        print('''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''')
    elif tries_count==3:
        print('''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',)
    elif tries_count==2:
        print('''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''')
    elif tries_count==1:
        print('''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''')
    else:
        print('''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                ''')
        



print('Hello this is a HangMan game')
word=get_word()
guess=['*']*len(word)
tries=6
result=0
while result==0:
    hangman(tries)
    print('INPUT ONLY UPPERCASE_LETTERS!')
    play(word)
print('YOU WIN!')
print('correct word-',guess)