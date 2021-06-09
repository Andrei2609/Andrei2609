init:
    $ ingredient_1 = ""
    $ ingredient_2 = ""
    $ ingredient_3 = ""
    $ ingredientChoix = ""
    $ mix_tour = 0
    $ smoothie =""
    $ ingredients_liste = ["cerise", "pomme", "banane", "carotte", "poivrons", "piment", "chocolat", "glace", "sperme"]

image smoothie_add = "Images/Mini-Jeux/Smoothie/smoothie_add.png"
image smoothie_cum = "Images/Mini-Jeux/Smoothie/smoothie_cum.png"
image smoothie_cum_1 = "Images/Mini-Jeux/Smoothie/smoothie_cum_1.png"

screen smoothie():
    modal True
    imagemap:
        idle "Images/Mini-Jeux/Smoothie/smoothie.png"
        hover "Images/Mini-Jeux/Smoothie/smoothie_hover.png"
        xalign 0.5
        yalign 0.5

        hotspot (36,427,93,63) action Jump("smoothie_exit")
        hotspot (203,382,168,129) action Jump("smoothie_OK")

        hotspot (31,45,100,100) action SetVariable("ingredientChoix", ingredients_liste[0]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")
        hotspot (137,45,100,100) action SetVariable("ingredientChoix", ingredients_liste[1]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")
        hotspot (243,45,100,100) action SetVariable("ingredientChoix", ingredients_liste[2]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")

        hotspot (32,151,100,100) action SetVariable("ingredientChoix", ingredients_liste[3]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")
        hotspot (138,151,100,100) action SetVariable("ingredientChoix", ingredients_liste[4]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")
        hotspot (244,151,100,100) action SetVariable("ingredientChoix", ingredients_liste[5]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")

        hotspot (32,257,100,100) action SetVariable("ingredientChoix", ingredients_liste[6]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")
        hotspot (138,257,100,100) action SetVariable("ingredientChoix", ingredients_liste[7]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")
        hotspot (244,257,100,100) action SetVariable("ingredientChoix", ingredients_liste[8]), SetVariable("mix_tour", mix_tour + 1), Jump("smoothie_img")

    frame:
        xalign 0.97
        yalign 0.05
        has vbox
        label _("Ingrédients") xalign 0.5
        text ingredient_1 xalign 0.5
        text ingredient_2 xalign 0.5
        text ingredient_3 xalign 0.5
        text _("3 ingrédients MAX") xalign 0.5

label smoothie_exit:
    $ ingredient_1 = ""
    $ ingredient_2 = ""
    $ ingredient_3 = ""
    $ ingredientChoix = ""
    $ mix_tour = 0
    return

label smoothie_img:
    hide screen smoothie
    if ingredientChoix <> "sperme":
        show smoothie_add
        with fondu
        nar ""
        hide smoothie_add
        with fondu
    elif True:
        show smoothie_cum
        with fondu
        nar ""
        hide smoothie_cum
        show smoothie_cum_1
        with flash
        nar ""
        hide smoothie_cum_1
        with fondu
    if mix_tour == 1:
        $ ingredient_1 = ingredientChoix
    elif mix_tour == 2:
        $ ingredient_2 = ingredientChoix
    elif mix_tour == 3:
        $ ingredient_3 = ingredientChoix
    call screen smoothie

label smoothie_OK:
    hide screen smoothie
    if ingredient_1 == "" and ingredient_2 == "" and ingredient_3 == "":
        $ smoothie = ""
        jump smoothie_exit
    elif ingredient_1 == "sperme" or ingredient_2 == "sperme" or ingredient_3 == "sperme":
        $ smoothie = "special L"
    elif ingredient_1 == "cerise" and ingredient_2 == "pomme" and ingredient_3 == "banane":
        $ smoothie = "fruits mix"
    elif ingredient_1 == "carotte" and ingredient_2 == "poivron" and ingredient_3 == "piment":
        $ smoothie = "legumes hot"
    elif ingredient_1 == "cerise" and ingredient_2 == "chocolat" and ingredient_3 == "glace":
        $ smoothie = "foret noire"
    elif True:
        $ smoothie = "beurk"
    user "Et voici un smoothie : [smoothie]"
    call timer (0, 30) from _call_timer_39
    jump smoothie_exit
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
