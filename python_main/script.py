from tictactoe import *

game_entry()
cleanboard()

while game_status == True and mooves < 9:
    winchecks(player1)
    realboard()
    player_moove(player1)
    realboard()
    mooves += 1

    if mooves == 9:
        print('◄ game over ►')
        print('◄ draw ►')
        break

    winchecks(player2)
    realboard()
    player_moove(player2)
    realboard()
    mooves += 1







    
















