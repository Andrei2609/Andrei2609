
image BG_dentiste = "Images/Backgrounds/job_rita.png"
image BG_dentiste_hall = "Images/Backgrounds/job_rita_hall.png"

screen dentiste():
    imagebutton:
        xalign 0.01
        yalign 0.99
        idle "Images/Plans/Minis/flecheBG.png"
        hover "Images/Plans/Minis/flecheBG_hover.png"
        action Jump("map")

    imagebutton:
        xalign 0.99
        yalign 0.4
        idle "Images/Plans/Minis/porte.png"
        hover "Images/Plans/Minis/porte_hover.png"
        action Jump("rita_job_in")

label dentiste_in:
    $ checkZone = "dent_hall"
    scene BG_dentiste_hall
    with fondu
    call screen dentiste

label dentiste:
    if heure >= 8 and heure < 18 and jour < 6:
        call timer (0, 10) from _call_timer_26
        jump dentiste_in
    elif True:
        nar "c'est fermé..."
        jump map

label rita_job_in:
    $ checkZone = "dent_room"
    scene BG_dentiste
    show screen Actor1("mom", "job", "normal", "sh_1", "sb_1", "job", "boucle_1", "", "", "Neutre", "P")
    with fondu
    mom "Lincoln, je travaille là !"
    hide screen Actor1
    with fondu
    jump dentiste_in
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
