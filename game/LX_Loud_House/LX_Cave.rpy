screen cave():
    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "Images/Plans/Minis/escalier.png"
        hover "Images/Plans/Minis/escalierH_hover.png"
        action Jump("cuisine")

    imagebutton:
        xalign 0.6235
        yalign 0.747
        idle "Images/Plans/Cave/machine1.png"
        hover "Images/Plans/Cave/machine1_hover.png"
        action Jump("lave_linge")

    imagebutton:
        xalign 0.4491
        yalign 0.747
        idle "Images/Plans/Cave/machine2.png"
        hover "Images/Plans/Cave/machine2_hover.png"
        action Jump("seche_linge")

    if heure < 10 or heure > 18 and heure < 20:
        imagebutton:
            xalign 0.3
            yalign 0.9
            idle "Images/Plans/Cave/panier.png"
            hover "Images/Plans/Cave/panier_hover.png"
            action Jump("panier_linge")

    if jour == 6 and heure == 22:
        imagebutton:
            xalign 0.1
            yalign 0.8
            idle "Images/Plans/Cave/l2.png"
            hover "Images/Plans/Cave/l2_hover.png"
            action Jump("l2_fiesta")

label cave:
    scene BG_cave
    with fondu
    call screen cave()

label lave_linge:
    user "rien de bien intéressant..."
    jump cave

label seche_linge:
    user "rien de bien intéressant..."
    jump cave

label panier_linge:
    user "Beurk ! Les caleçons de papa !"
    jump cave
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
