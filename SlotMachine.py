MAX_LINES = 3   #liczba linii którą można obstawić w jednorękim bandycie
                #capsami = wartość 
MAX_BET = 100
MIN_BET = 1                

#collecting user input
def deposit():
    while True:
        amount = input('Wprowadź depozyt: $')
        if amount.isdigit():    #sprawdza czy wprowadzony tekts to liczba
            amount = int(amount)    #jeśli wprowadzony tekst to liczba to jest teraz zamieniana w integer'a
            if amount > 0:
                break            #jeśli numer jest >0 to break zamyka loop'a
            else:
                print('Wartość musi być większa niż 0.')
        else:
            print('Proszę wprowadzić numer.')
    return amount

def get_number_of_lines():
    while True:
        lines = input('Ile linii chcesz obstawić (1-' + str(MAX_LINES) + ')?')
        if lines.isdigit():    #sprawdza czy wprowadzony tekts to liczba
            lines = int(lines)    #jeśli wprowadzony tekst to liczba to jest teraz zamieniana w integer'a
            if 1 <= lines <= MAX_LINES:
                break            #jeśli numer jest >0 to break zamyka loop'a
            else:
                print('Wprowadź poprawną ilość linii (1-' + str(MAX_LINES) + ')?')        
        else:
            print('Proszę wprowadzić numer.')
    return lines          

def get_bet():
    while True:
        amount = input('Ile chcesz obstawić? $')
        if amount.isdigit():    #sprawdza czy wprowadzony tekts to liczba
            amount = int(amount)    #jeśli wprowadzony tekst to liczba to jest teraz zamieniana w integer'a
            if MIN_BET <= amount <= MAX_BET:
                break            #jeśli numer jest >0 to break zamyka loop'a
            else:
                print(f'Wprowadź ilość między ${MIN_BET} - ${MAX_BET}.')    
                #inny sposób sprowadzania liczb do stringa     
        else:
            print('Proszę wprowadzić numer.')
    return amount


def main():                     #funkcja która uruchomi gre
    balance = deposit()    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f'Nie masz wystarczających środków. Masz ${balance}.')
        else:
            break            
    print(
        f'Obstawiasz ${bet} na {lines} linie. Cały zakład to {total_bet}.')

main()    