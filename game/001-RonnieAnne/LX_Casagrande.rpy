label casagrande:
    if permis == True:
        $ checkZone = "casagrande_out"
        $ time_car = 10
        $ cpt_car += 1
        call screen conduite("ville")
    elif True:
        scene BG_ville
        with fondu
        nar "C'est trop loin pour y aller à pied... Il te faut Vanzilla !"
        jump map

label casagrande_ext:
    call timer (2, 0) from _call_timer_32
    scene BG_casagrande
    with fondu
    user "Bizarre... Personne n'est là !?"
    user "Il ne me reste plus qu'a rentré !"
    jump map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
