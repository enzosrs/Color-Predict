import random
import math
import time
import webbrowser
from datetime import datetime
from threading import Timer

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "pink": "\033[95m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "end_color": "\033[0m"
}

def show_second_url():
    print(f"{colors['cyan']}Visit this link: https://t.me/+tEjnt4Dh_3QyYzE1{colors['end_color']}")
    webbrowser.open("https://t.me/+tEjnt4Dh_3QyYzE1")  

def get_initial_wallet():
    print(f"{colors['red']}Enter your current wallet amount:{colors['end_color']}")
    while True:
        try:
            wallet = float(input())
            if wallet > 0:
                return wallet
            else:
                print(f"{colors['blue']}Please enter a positive amount.{colors['end_color']}")
        except ValueError:
            print(f"{colors['green']}Invalid input. Please enter a numeric value.{colors['end_color']}")

def calculate_auto_period():
    current_date = datetime.utcnow()
    period_date = current_date.strftime('%Y%m%d')
    total_minutes = current_date.hour * 60 + current_date.minute
    period_number = str(10001 + total_minutes)
    auto_period = f"{period_date}1000{period_number}"
    return auto_period

def calculate_prediction(auto_period):
    last_four_digits = auto_period[-4:]
    last_four_total = int(last_four_digits)
    final_result = last_four_total % 10

    big_numbers = [0, 9, 4, 5, 6]
    small_numbers = [1, 3, 7, 8, 2]

    if final_result in big_numbers:
        return "Bɪɢ"
    elif final_result in small_numbers:
        return "Sᴍᴀʟʟ"
    else:
        return "Error"

def color_prediction_game():
   
    print(f"{colors['yellow']}Visit this link: https://t.me/+bq8xzmz_CoE2Yzc1{colors['end_color']}")
    webbrowser.open("https://t.me/+bq8xzmz_CoE2Yzc1")  
    Timer(120, show_second_url).start()  

    wallet = get_initial_wallet()
    payout_multiplier = 1.96  
    loss_streak = 0  

    print(f"{colors['pink']}Welcome to the Color Prediction Game!{colors['end_color']}")

    while wallet > 0:
        auto_period = calculate_auto_period()
        print(f"\n{colors['cyan']}Period Code: {auto_period}{colors['end_color']}")

        while True:
            print(f"{colors['blue']}Enter the amount to bet:{colors['end_color']}")
            try:
                current_bet = float(input())
                if 0 < current_bet <= wallet:
                    wallet -= current_bet  
                    print(f"{colors['pink']}Bet placed! Amount deducted: ${current_bet:.2f}. Remaining Wallet: ${wallet:.2f}{colors['end_color']}")
                    break
                else:
                    print(f"{colors['pink']}Enter a valid bet amount within your wallet balance.{colors['end_color']}")
            except ValueError:
                print(f"{colors['green']}Invalid input. Please enter a numeric value.{colors['end_color']}")

        prediction = calculate_prediction(auto_period)
        print(f"{colors['red']}Prediction: {prediction}{colors['end_color']}")

        user_result = input(f"{colors['yellow']}Did you win or lose? [W/L]:{colors['end_color']} ").strip().upper()

        if user_result == 'W':
            win_amount = current_bet * payout_multiplier
            wallet += win_amount
            print(f"{colors['green']}You win! Amount received: ${win_amount:.2f}. New Wallet: ${wallet:.2f}{colors['end_color']}")
            loss_streak = 0  
        elif user_result == 'L':
            print(f"{colors['red']}You lose! Amount lost: ${current_bet:.2f}. Remaining Wallet: ${wallet:.2f}{colors['end_color']}")
            loss_streak += 1
            if loss_streak >= 4:
                print(f"{colors['red']}You have lost 4 times in a row. Game Over.{colors['end_color']}")
                break
        else:
            print(f"{colors['cyan']}Invalid input. Please enter 'W' or 'L'.{colors['end_color']}")

        if wallet <= 0:
            print(f"{colors['pink']}You have run out of money! Game Over.{colors['end_color']}")
            break

color_prediction_game()
