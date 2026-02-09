from son_topish import *

def play(x = 10):
    retro = True
    while retro:
        ts_user = son_top(x)
        ts_pc = son_top_pc(x)

        if ts_pc > ts_user:
            print('Siz yutdingiz!')
        elif ts_pc < ts_user:
            print('Men yutdim!')
        elif ts_pc == ts_user:
            print('Durrang!')
        retro = int(input("Yana o'ynaysizmi? Ha(1), yo'q(0): "))

play()