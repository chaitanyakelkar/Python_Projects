checkerboard = {'1': ' ', '2': ' ', '3': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '7': ' ', '8': ' ', '9': ' ', }
board_backup = []
for key in checkerboard:
    board_backup.append(key)


def game():
    turn = 'X'
    count = 0
    for i in range(10):
        i += 1
        print("\t\t" + checkerboard['1'] + '|' + checkerboard['2'] + '|' + checkerboard['3'])
        print("\t\t" + '-----')
        print("\t\t" + checkerboard['4'] + '|' + checkerboard['5'] + '|' + checkerboard['6'])
        print("\t\t" + '-----')
        print("\t\t" + checkerboard['7'] + '|' + checkerboard['8'] + '|' + checkerboard['9'])
        print("\t\t" + '-----')
        
        while True:
            print('It is ' + turn + "'s Turn Where you want to place?")
            user_input = input('> ')
            if not user_input.isnumeric():
                print('Invalid alphabet input! Print nos 1 to 9')
                print("\t\t" + checkerboard['1'] + '|' + checkerboard['2'] + '|' + checkerboard['3'])
                print("\t\t" + '-----')
                print("\t\t" + checkerboard['4'] + '|' + checkerboard['5'] + '|' + checkerboard['6'])
                print("\t\t" + '-----')
                print("\t\t" + checkerboard['7'] + '|' + checkerboard['8'] + '|' + checkerboard['9'])
                print("\t\t" + '-----')
            else:
                break
        if int(user_input) > 9:
            print('Invalid number input! Print nos 1 to 9')
            continue
        else:
            if checkerboard[user_input] != ' ':
                print('That place is already filled')
                continue
            else:
                checkerboard[user_input] = turn
                count += 1
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

                if checkerboard['1'] == checkerboard['2'] == checkerboard['3'] != ' ':
                    print("********* " + checkerboard['1'] + "'s Player Won *********")
                    break
                if checkerboard['4'] == checkerboard['5'] == checkerboard['6'] != ' ':
                    print("********* " + checkerboard['4'] + "'s Player Won *********")
                    break
                if checkerboard['7'] == checkerboard['8'] == checkerboard['9'] != ' ':
                    print("********* " + checkerboard['7'] + "'s Player Won *********")
                    break
                if checkerboard['1'] == checkerboard['4'] == checkerboard['7'] != ' ':
                    print("********* " + checkerboard['1'] + "'s Player Won *********")
                    break
                if checkerboard['2'] == checkerboard['5'] == checkerboard['8'] != ' ':
                    print("********* " + checkerboard['2'] + "'s Player Won *********")
                    break
                if checkerboard['3'] == checkerboard['6'] == checkerboard['9'] != ' ':
                    print("********* " + checkerboard['3'] + "'s Player Won *********")
                    break
                if checkerboard['1'] == checkerboard['5'] == checkerboard['9'] != ' ':
                    print("********* " + checkerboard['1'] + "'s Player Won *********")
                    break
                if checkerboard['3'] == checkerboard['5'] == checkerboard['7'] != ' ':
                    print("********* " + checkerboard['3'] + "'s Player Won *********")
                    break
                if count >= 9:
                    print("It's a Tie")
                    break


game()
