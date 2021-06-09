label m_joy:
    call timer (0, 10) from _call_timer_6
    $ checkZone = "joy_out"
    scene BG_standby
    with fondu
    nar "en cours de fabrication"
    jump map
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
