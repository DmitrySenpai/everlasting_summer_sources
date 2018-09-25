label prologue:

    $ set_mode_adv()
    $ persistent.sprite_time = "day"
    play music music_list["a_promise_from_distant_days"] fadein 2
    scene anim prolog_1 with fade3
    show un shy pioneer at center with dissolve
    window show
    un "Привет!"
    window hide
    scene bg ext_square_day
    show un smile pioneer at center
    with dissolve
    $ day_time()
    window show
    un "Это тестовый сценарий."
    me "Это всё?"
    un "Да."
    "На этом всё."
    window hide
    stop music fadeout 2
    scene bg black with fade3
    pause 0.5
    return