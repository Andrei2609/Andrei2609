label m_new_voisin:
    call timer (0, 10) from _call_timer_18
    $ checkZone = "new_voisin_out"
    scene BG_standby
    with fondu
    nar "en cours de fabrication"
    jump map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
