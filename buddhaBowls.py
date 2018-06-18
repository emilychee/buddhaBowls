#
# buddhaBowls.py
#
# Emily Chatterjee
#
# user picks what type of Buddha Bowl they want to make and how many bowls.
# programs prints list of amounts of ingredients and directions
#
def pluralize(singular, plural, number):
    """Print correct form (singular or plural) of the word entered."""
    if number == 1:
        return singular

    return plural

def koreanBBQBowl():
    """Outputs ingredients and directions for Korean BBQ Bowl recipe."""
    numBowls = int(input("How many bowls do you want to make?"))

    # cups of ketchup
    KETCHUP_PER_BOWL = 0.5
    ketchupCups = KETCHUP_PER_BOWL * numBowls
    # cups of rice vinegar
    VINEGAR_PER_BOWL = 0.5
    vinegarCups = VINEGAR_PER_BOWL * numBowls
    # cups of soy sauce
    SOY_SAUCE_PER_BOWL = 0.25
    soySauceCups = SOY_SAUCE_PER_BOWL * numBowls
    # tablespoons of sugar
    SUGAR_PER_BOWL = 5.5
    sugarTablespoons = SUGAR_PER_BOWL * numBowls
    # tablespoons of sesame seeds
    SESAME_SEEDS_PER_BOWL = 1
    sesameSeedsTablespoons = SESAME_SEEDS_PER_BOWL * numBowls
    # teaspoons of yellow miso
    MISO_PER_BOWL = 2
    misoTeaspoons = MISO_PER_BOWL * numBowls
    # teaspoons of siracha
    SIRACHA_PER_BOWL = 1
    sirachaTeaspoons = SIRACHA_PER_BOWL * numBowls
    # teaspoons of black pepper
    PEPPER_PER_BOWL = 0.25
    pepperTeaspoons = PEPPER_PER_BOWL * numBowls
    # number of green onions
    ONIONS_PER_BOWL = 2
    numOnions = ONIONS_PER_BOWL * numBowls
    # pieces (1-inch) of ginger, grated
    GINGER_PER_BOWL = 1
    numGingers = GINGER_PER_BOWL * numBowls
    # cloves of garlic, minced
    GARLIC_PER_BOWL = 1
    numGarlics = GARLIC_PER_BOWL * numBowls
    # tablespoons of sesame oil
    SESAME_OIL_PER_BOWL = 3
    sesameOilTablespoons = SESAME_OIL_PER_BOWL * numBowls
    # crowns of broccoli
    BROCCOLI_PER_BOWL = 1
    numBroccolis = BROCCOLI_PER_BOWL * numBowls
    # tablespoons of water
    WATER_PER_BOWL = 1
    waterTablespoons = WATER_PER_BOWL * numBowls
    # number of zucchinis, sliced into half moons
    ZUCCHINI_PER_BOWL = 1
    numZucchinis = ZUCCHINI_PER_BOWL * numBowls
    # cups of pineapple chunks
    PINEAPPLE_PER_BOWL = 1
    pineappleCups = PINEAPPLE_PER_BOWL * numBowls
    # number of red peppers, cored and sliced
    RED_PEPPER_PER_BOWL = 1
    numPeppers = RED_PEPPER_PER_BOWL * numBowls
    # packages of 15-oz tofu
    TOFU_PER_BOWL = 1
    tofuPackages = TOFU_PER_BOWL * numBowls
    # packages of Quinoa
    QUINOA_PER_BOWL = 0.5
    quinoaPackages = QUINOA_PER_BOWL * numBowls
    # packages of shredded red cabbage
    CABBAGE_PER_BOWL = 0.25
    cabbagePackages = CABBAGE_PER_BOWL * numBowls

    print("You will need: ")
    print("--> ", ketchupCups, " cups of ketchup")
    print("--> ", vinegarCups, " cups of rice vinegar")
    print("--> ", soySauceCups, " cups of soy sauce")
    print("--> ", sugarTablespoons, " tablespoons of sugar")
    print("--> ", sesameSeedsTablespoons, " tablespoons of sesame seeds")
    print("--> ", misoTeaspoons, " teaspoons of yellow miso")
    print("--> ", sirachaTeaspoons, " teaspoons of siracha")
    print("--> ", pepperTeaspoons, " teaspoons of black pepper")
    print("--> ", numOnions, " green onions (thinly sliced)")
    print("--> ", numGarlics, " cloves of garlic (minced)")
    print("--> ", numGingers, " pieces of ginger (grated)")
    print("--> ", sesameOilTablespoons, " tablespoons of sesame oil")
    print("--> ", numBroccolis, " crowns of broccoli")
    print("--> ", numZucchinis, " zucchinis (sliced)")
    print("--> ", waterTablespoons, " tablespoons of water")
    print("--> ", pineappleCups, " cups of pineapple chunks")
    print("--> ", numPeppers, " red peppers (cored & sliced)")
    print("--> ", tofuPackages, " packages of tofu")
    print("--> ", quinoaPackages, " packages of quinoa")
    print("--> ", cabbagePackages, " packages of red cabbage")

def thaiBowlPeanutSauce():
    pass

def eggVeggieBrkfstBowl():
    """Outputs ingredients and directions for Egg and Veggie Breakfast
    Bowl recipe."""
    numBowls = int(input("How many bowls do you want to make?"))

    # pounds of brussel sprouts
    BRUSSELS_PER_BOWL = 0.25
    brusselPounds = BRUSSELS_PER_BOWL * numBowls
    # tabelspoons of olive oil
    OLIVE_OIL_PER_BOWL = 0.375
    oliveOilTablespoons = OLIVE_OIL_PER_BOWL * numBowls
    # number of eggs
    EGGS_PER_BOWL = 1
    numEggs = EGGS_PER_BOWL * numBowls
    # tablespoons of apple cider vinegar
    ACV_PER_BOWL = 0.75
    acvTablespoons = ACV_PER_BOWL * numBowls
    # pounds of sweet potato
    POTATO_PER_BOWL = 0.25
    potatoPounds = POTATO_PER_BOWL * numBowls
    # cups of spinach
    SPINACH_PER_BOWL = 0.5
    spinachCups = SPINACH_PER_BOWL * numBowls
    # tablespoons of harissa
    HARISSA_PER_BOWL = 0.5
    harissaTablespoons = HARISSA_PER_BOWL * numBowls
    # packages of rice
    RICE_PER_BOWL = 0.5
    ricePackages = RICE_PER_BOWL * numBowls

    print("You will need: ")
    print("--> ", brusselPounds, pluralize("pound", "pounds", brusselPounds),
          "of brussel sprouts")
    print("--> ", oliveOilTablespoons,
          pluralize("tablespoon", "tablespoons", oliveOilTablespoons),
          "of olive oil")
    print("--> ", numEggs, pluralize("egg", "eggs", numEggs))
    print("--> ", acvTablespoons,
          pluralize("tablespoon", "tabelspoons", acvTablespoons),
          "of apple cider vinegar")
    print("--> ", potatoPounds, pluralize("pound", "pounds", potatoPounds),
          "of sweet potato")
    print("--> ", spinachCups, pluralize("cup", "cups", spinachCups),
          "of spinach")
    print("--> ", harissaTablespoons,
          pluralize("tablespoon", "tabelspoons", harissaTablespoons),
          "of harissa")

def cubanQuinoaBowl():
    pass

def roastedVeggieBowl():
    pass

def winterHarvestBowl():
    pass

def veganBuddhaBowl():
    pass

def kaowBowl():
    pass

def cauliflowerRiceBowl():
    pass

def springRollBowl():
    pass

def sweetPotatoBowl():
    pass

def spicyPolentaBowl():
    pass

def order():
    """Takes the order of the user."""
    print("Recipes: ")
    print("1) Korean BBQ Bowl")
    print("2) Thai Bowl w/ Peanut Sauce")
    print("3) Egg and Veggie Breakfast Bowl")
    print("4) Cuban Quinoa Bowl")
    print("5) Roasted Veggie Bowl")
    print("6) Winter Harvest Bowl")
    print("7) Vegan Buddha Bowl")
    print("8) Kale, Avocado, Orange, and Wild Rice Bowl")
    print("9) Cauliflower Rice Bowl")
    print("10) Spring Roll Bowl")
    print("11) Sweet Potato Bowl")
    print("12) Spicy Barbeuc Polenta Bowl")

    orderNumber = int(input("What type of bowl do you want to make?"))

    if orderNumber == 1:
        koreanBBQBowl()
    elif orderNumber == 2:
        thaiBowlPeanutSauce()
    elif orderNumber == 3:
        eggVeggieBrkfstBowl()
    elif orderNumber == 4:
        cubanQuinoaBowl()
    elif orderNumber == 5:
        roastedVeggieBowl()
    elif orderNumber == 6:
        winterHarvestBowl()
    elif orderNumber == 7:
        veganBuddhaBowl()
    elif orderNumber == 8:
        kaowBowl()
    elif orderNumber == 9:
        cauliflowerRiceBowl()
    elif orderNumber == 10:
        springRollBowl()
    elif orderNumber == 11:
        sweetPotatoBowl()
    elif orderNumber == 12:
        spicyPolentaBowl()

if __name__ == '__main__':
    order()
