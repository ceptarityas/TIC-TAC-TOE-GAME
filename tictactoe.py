
papan = [' ' for x in range(10)]

def insertPapan (letter, pos) :
    papan[pos] = letter

def spaceIsFree(pos) :
    return papan[pos] == ' '

def printPapan(papan) :
    print('' + papan[1] + ' | ' + papan[2] + ' |  ' +papan[3])
    print('--------')
    print('' + papan[4] + ' | ' + papan[5] + ' |  ' +papan[6])
    print('--------')
    print('' + papan[7] + ' | ' + papan[8] + ' |  ' +papan[9])

def isWinner(bo, le) :
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))



def playerMove() :
    run = True
    while run :
        move = input('Sekarang giliran anda \'O\' pilih angka (1-9) : ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move) :
                    run = False
                    insertPapan('O', move)
                else:
                    print('Tempat ini sudah diisi')
            else:
                print('Masukan angka tanpa range(-) ')
        except:
            print('Masukan angka 1-9')
def AIMove() :
    possibleMoves = [x for x, letter in enumerate(papan) if letter == ' ' and x != 0]
    move = 0 

    for let in ['X', 'O']:
        for i in possibleMoves:
            papanCopy = papan[:]
            papanCopy[i] = let
            if isWinner(papanCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9] :
            cornersOpen.append(i)

        if len(cornersOpen) > 0:
            move = pilihAcak(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8] :
            edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move = pilihAcak(edgesOpen)

    return move
        

def pilihAcak(li) :
    import random
    ln = len(li) 
    r = random.randrange(0, ln)
    return li[r]

def isPapanPenuh(papan) :
    if papan.count(' ') > 1 :
        return False
    else :
        return True

def main() :
    print('Nama : Cepthari Ningtyas A \n' +
    'Kelas : IFX-44-02 \n'+
    'NIM : 1301208519 \n\n')
    print('==== Selamat Datang di Permainan Tic Tac Toe ====')
    print('Kamu \'O\' dan AI \'X\' ')
    printPapan(papan)

    while not(isPapanPenuh(papan)) :
        if not(isWinner(papan, 'X')) :
            playerMove()
            printPapan(papan)
        else :
            print('AI Menang, Kamu Kalah')
            break
        
        if not(isWinner(papan, 'O')):
            move = AIMove()
            if move == 0:
                print('Permainan Seri')
            else:
                insertPapan('X', move)
                print('AI menempatan sebuah "X" posisi ', move )
                printPapan(papan)
        else :
            print('Congrats! Anda Menang, AI Kalah')
            break
    if isPapanPenuh(papan) :
        print ('Permainan Seri')

main()

while True:
    answer = input('Ingin bermain lagi? (Y/N) : ')
    if answer.lower() == 'y' or answer.lower == 'yes':
        papan = [' ' for x in range(10)]
        print('--------------Permainan Baru------------')
        main()
    else:
        print('Permainan Berakhir')
        break             