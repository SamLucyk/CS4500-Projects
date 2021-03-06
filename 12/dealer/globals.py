### TraitCard
CARNIVORE = "carnivore"
AMBUSH = "ambush"
BURROWING = "burrowing"
CLIMBING = "climbing"
COOPERATION = "cooperation"
FATTISSUE = "fat-tissue"
FERTILE = "fertile"
FORAGING = "foraging"
HARDSHELL = "hard-shell"
HERDING = "herding"
HORNS = "horns"
LONGNECK = "long-neck"
PACKHUNTING = "pack-hunting"
SCAVENGER = "scavenger"
SYMBIOSIS = "symbiosis"
WARNINGCALL = "warning-call"

TRAITS_LIST = [CARNIVORE, AMBUSH, BURROWING, CLIMBING, COOPERATION, FATTISSUE, FERTILE, FORAGING,
               HARDSHELL, HERDING, HORNS, LONGNECK, PACKHUNTING, SCAVENGER, SYMBIOSIS,  WARNINGCALL]

CARN_FOOD_MIN = -8
CARN_FOOD_MAX = 8
HERB_FOOD_MIN = -3
HERB_FOOD_MAX = 3

### Species
MIN_FOOD = 0
MAX_FOOD = 7
MIN_POP = 1
MAX_POP = 7
MIN_BODY = 0
MAX_BODY = 7
MIN_FATFOOD = 0
MAX_TRAITS = 3
HARD_SHELL_DIFF = 4

### Player
MIN_PLAYER_ID = 1
MIN_FOOD_BAG = 0

### Dealer
MIN_WATERING_HOLE = 0
LOP_MIN = 3
LOP_MAX = 8
LOC_MAX = 122
FEED_QUANTITY = 1
KILL_QUANTITY = 1
HERB_FEED_LENGTH = 2
CARN_FEED_LENGTH = 3
EXTINCTION_CARD_AMOUNT = 2
DEAL_AMOUNT = 3
SCORE_TEMPLATE = "%d player id: %d score: %d"

### JSON messages
## Length
CONFIG_LENGTH = 3
FEEDING_LENGTH = 3
PLAYER_LENGTH = 3
PLAYER_PLUS_LENGTH = 4
SPECIES_LENGTH = 4
SPECIES_FAT_LENGTH = 5
CARD_LENGTH = 2

## Labels
# Player
ID = "id"
SPECIES = "species"
BAG = "bag"
CARDS = "cards"
# Species
FOOD = "food"
BODY = "body"
POPULATION = "population"
TRAITS = "traits"
FATFOOD = "fat-food"

### Actions
GROW_POP_AMOUNT = 1
GROW_BODY_AMOUNT = 1

# Changes
CHANGE_TEMPLATE = "[%s, %s->%s]"
CARD_TEMPLATE = "[%s, %d]"
