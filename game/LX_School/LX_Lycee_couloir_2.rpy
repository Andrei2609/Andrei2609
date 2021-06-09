screen school_couloir():
    imagebutton:
        xalign 0.009
        yalign 0.5
        idle "Images/Plans/Minis/flecheG.png"
        hover "Images/Plans/Minis/flecheG_hover.png"
        action Jump("hall")

    if heure < 13 and heure >= 10:
        imagebutton:
            xalign 0.2
            yalign 0.76
            idle "Images/Plans/Lycee/EVENT/chloe.png"
            hover "Images/Plans/Lycee/EVENT/chloe_hover.png"
            action Jump("school_chloe")

    if heure < 13 and heure >= 10:
        imagebutton:
            xalign 0.4
            yalign 0.7
            idle "Images/Plans/Lycee/EVENT/emma.png"
            hover "Images/Plans/Lycee/EVENT/emma_hover.png"
            action Jump("school_emma")

    if jour == 5 and heure < 10 or heure < 13 and heure >= 10:
        imagebutton:
            xalign 0.8
            yalign 0.9
            idle "Images/Plans/Lycee/EVENT/joy.png"
            hover "Images/Plans/Lycee/EVENT/joy_hover.png"
            action Jump("school_joy")

    frame:
        xalign 0.99
        yalign 0.99
        has vbox
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Minis/urgence.png"
            hover "Images/Plans/Minis/urgence_hover.png"
            action Jump("infirmerie")
        text _("Infirmerie") xalign 0.5
        imagebutton:
            xalign 0.5
            idle "Images/Plans/Minis/bureau.png"
            hover "Images/Plans/Minis/bureau_hover.png"
            action Jump("principal")
        text _("Principal") xalign 0.5


label school_couloir_2:
    $ checkZone = "school_couloir_2"
    scene BG_lycee_casiers_2
    with fondu
    call screen school_couloir
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
