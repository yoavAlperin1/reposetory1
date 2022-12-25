
#global varibles

player1 =['x',[]]
#
player2 =['o',[]]
#
mooves = 0
#
game_status = True
#
b = [
    '','','','','','','','',''
    # b = board
    ]
#
wins_arr = [
    [b[0],b[1],b[2]],
    [b[3],b[4],b[5]],
    [b[6],b[7],b[8]],
    [b[0],b[3],b[6]],
    [b[1],b[4],b[7]],
    [b[2],b[5],b[8]],
    [b[0],b[4],b[8]],
    [b[2],b[4],b[6]]
    ]

#global varibles




#functions

def player_moove(player_number):
    # sy = symbol (x or o)
    y =  input("choose a number batween 1-9")
    player_number[1].append(y)
#
def endgame(whowin):
    if whowin == player1:
        print("player 1 win")
        return
    if whowin == player2:
        print("player 2 win")
        return
    if mooves == 9 :
        print("draw")
        return
#
def winchecks(player_number):
    for i in wins_arr:
        counter = 0
        for j in i:
            if j in player_number[1] == True:
                counter += 1
        if counter == 3:
            endgame(player_number)
#
def game_entry():
    
    print('▓▓▓▓▓▓▓▓▓▓▓▓▓')
    print('▓tic tac toe▓')
    print('▓▄▄▄▄▄▄▄▄▄▄▄▓')
    print('             ')
    player1_name = input("◄ choose your name ►")
    print('                                   ')
    player2_name = input("◄ choose your name ►")
    print('                                   ')
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print(player1_name + ' vs '+player2_name   )
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
    print(player1_name + ' start')
    print('▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')
#
def cleanboard():
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('▓          ▓          ▓          ▓')
    print('▓      7   ▓     8    ▓     9    ▓')
    print('▓          ▓          ▓          ▓')
    print('▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓')
    print('▓          ▓          ▓          ▓')
    print('▓    4     ▓    5     ▓     6    ▓')
    print('▓          ▓          ▓          ▓')
    print('▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓')
    print('▓          ▓          ▓          ▓')
    print('▓  1       ▓   2      ▓   3      ▓')
    print('▓          ▓          ▓          ▓')
    print('▓          ▓          ▓          ▓')
    print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
#
def realboard():
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('▓          ▓          ▓          ▓')
    print('▓'+ b[6] +'▓'+ b[7] +'▓'+ b[8] +'▓')
    print('▓          ▓          ▓          ▓')
    print('▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓')
    print('▓          ▓          ▓          ▓')
    print('▓'+ b[3] +'▓'+ b[4] +'▓'+ b[5] +'▓')
    print('▓          ▓          ▓          ▓')
    print('▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓▬▬▬▬▬▬▬▬▬▬▓')
    print('▓          ▓          ▓          ▓')
    print('▓'+ b[0] +'▓'+ b[1] +'▓'+ b[2] +'▓')
    print('▓          ▓          ▓          ▓')
    print('▓          ▓          ▓          ▓')
    print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
#


#functions