# Color Prediction Game Script

A Python-based color prediction game script that runs in the terminal. Users can place virtual bets based on predictions and track their wallet balances. The script is designed to be both entertaining and challenging, with customizable settings for betting limits and loss streaks.

---

# Table of Contents 📑

1. **<span style="color: rgb(0, 102, 204);">About 📝</span>** - Introduction to the project
3. **<span style="color: rgb(0, 204, 204);">Features ⚙️</span>** - Key features of the game
5. **<span style="color: rgb(102, 204, 0);">Installation & Setup 💻</span>** - How to install on different platforms
   - **<span style="color: rgb(255, 102, 102);">For Termux 📱</span>** - Installation for Termux
   - **<span style="color: rgb(204, 0, 204);">For Kali Linux 🐧</span>** - Installation for Kali Linux
   - **<span style="color: rgb(255, 204, 0);">For Parrot OS 🦜</span>** - Installation for Parrot OS
7. **<span style="color: rgb(255, 0, 0);">Developer Information 👨‍💻</span>** - Developer contact and information



## About

This project provides a terminal-based color prediction game where users can bet on the prediction outcome and manage their virtual wallet. The game generates a unique period code each round, allowing users to decide if they won or lost. With a built-in loss limit, the game will automatically stop if the user reaches a 4-loss streak, providing a safe and controlled exit.

---

## Features

- **Auto Period Calculation**: Generates a unique period code for each round.
- **Easy Betting**: Allows users to input and track their bet amounts for each round.
- **Consecutive Loss Limit**: Game stops automatically after 4 consecutive losses.
- **Dynamic Wallet Management**: Deducts and adds to the wallet based on win/loss outcomes.
- **Customizable Payout Multiplier**: Set your desired payout ratio.
- **Color-Coded Output**: Uses color codes for easy reading and aesthetic appeal.
- **Input Validation**: Ensures only valid numerical inputs are accepted for wallet and bet amounts.
- **Direct Links**: Automatically opens Telegram links at the start and after 2 minutes.
- **Stop Alert on Loss Streak**: Issues a stop alert after four consecutive losses.
- **Platform Flexibility**: Compatible with Termux, Kali Linux, and Parrot OS.

---

## How to Use 🎲

### **Starting the Game:**
Once you've successfully run the script, follow these steps:

1. **Initial Setup**: You will be prompted to enter your starting wallet amount (e.g., `100`).
2. **Place Your Bet**: The game will ask you to enter the amount you wish to bet.
3. **Prediction**: The game will display a prediction — whether the outcome will be **BIG** or **SMALL**.
4. **Input Result**: After each round, you will be asked to input whether you won or lost:
   - Type `W` for win.
   - Type `L` for loss.
5. **Wallet Management**: 
   - If you win, the bet amount will be added to your wallet.
   - If you lose, the bet amount will be deducted from your wallet.
6. **Loss Streak Limit**: If you lose **4 times consecutively**, the game will stop automatically with an alert.

---

### **Example Gameplay** 💬

Here’s how the game will look when you play:

```bash
$ python3 color_prediction_game.py

Enter your starting wallet amount: 100
Welcome to Color Prediction Game!
Period Code: 20241107100010001
Enter the amount to bet: 10
Bet placed! Amount deducted: $10. Remaining Wallet: $90
Prediction: BIG
Did you win or lose? [W/L]: L
You lost! Amount lost: $10. Remaining Wallet: $80
...

```





Installation & Setup

Termux

```bash

pkg update && pkg upgrade


pkg install git


pkg install python

https://github.com/enzosrs/Color-Predict.git


cd Color-Predict


python3 Color-Predict.py

```
Kali Linux
```bash


sudo apt update && sudo apt upgrade


sudo apt install git


sudo apt install python3


https://github.com/enzosrs/Color-Predict.git


cd Color-Predict


python3 Color-Predict.py

```
Parrot OS
```bash

sudo apt update && sudo apt upgrade


sudo apt install git


sudo apt install python3


https://github.com/enzosrs/Color-Predict.git


cd Color-Predict


python3 Color-Predict.py
```


### Key Features:

- **Separate Sections** for **Termux**, **Kali Linux**, and **Parrot OS**: Each platform has its own set of installation commands.
- **Step-by-Step Usage Instructions**: Clear instructions on how to start and play the game.
- **Example Gameplay**: Shows what the user will see while playing.
- **User-Friendly Format**: Commands and instructions are presented in a readable, easy-to-follow format.

This setup should provide clear instructions for users to install and use the script on **Termux**, **Kali Linux**, and **Parrot OS** in a **user-friendly** way!


<div style="display: flex; align-items: center;">
  <!-- Programming Languages and Technologies section -->
  <div style="flex: 1;">
    <h2>Developer Info</h2>
    <p>Hello! I'm Enzo, a passionate Web Developer, Android App Developer, Expert Telegram Bot Creator, and Script Maker. I specialize in creating seamless applications, dynamic web platforms, powerful automation solutions, and custom scripts. My goal is to provide exceptional, user-centric experiences that seamlessly integrate functionality with the latest technological advancements</p>
    <h3>🛠️ Programming Languages</h3>
    <ul>
      <li><img src="https://img.icons8.com/color/48/000000/html-5.png" width="20"/> HTML</li>
      <li><img src="https://img.icons8.com/color/48/000000/css3.png" width="20"/> CSS</li>
      <li><img src="https://img.icons8.com/color/48/000000/javascript--v1.png" width="20"/> JavaScript</li>
      <li><img src="https://img.icons8.com/color/48/000000/python--v1.png" width="20"/> Python</li>
      <li><img src="https://img.icons8.com/color/48/000000/react-native.png" width="20"/> React JS</li>
      <li><img src="https://img.icons8.com/color/48/000000/php.png" width="20"/> PHP</li>
    </ul>
  </div>

  <!-- GIF section placed on the right side -->
  <div style="flex-shrink: 0; margin-left: 20px;">
    <img src="https://camo.githubusercontent.com/5046cb083418fd1922b7f5990e594c3bb06f5d87e5516cd8839ae0aa48b3aec4/68747470733a2f2f696d616765732e73717561726573706163652d63646e2e636f6d2f636f6e74656e742f76312f3537363966633430316236333162616231616464623261622f313534313538303631313632342d5445363451474b524a4738535741495553374e532f6b6531375a77644742546f6464493870446d34386b506f73776c7a6a53564d4d2d53784f703743563539425a772d7a505067646e346a557756634a45315a7657515578776b6d794578676c4e714770304976544a5a616d574c49327a76595748384b332d735f3479737a63703272795449304871544f6161556f68724938504936465879386339505774426c7141566c555335697a7064634958445a71445976707252715a32395077306f2f636f64696e672d667265616b2e676966" width="200" />
  </div>
</div>





### 📞 Contact Me

<a href="https://t.me/enzosrs" target="_blank" style="text-decoration: none;">
    <img src="https://img.icons8.com/color/48/000000/telegram-app.png" width="24" /> @enzosrs
</a><br>
<a href="https://t.me/+bq8xzmz_CoE2Yzc1" target="_blank" style="text-decoration: none;">
    <img src="https://img.icons8.com/color/48/000000/telegram-app.png" width="24" /> Channel
</a><br>

<a href="https://www.instagram.com/sanam.ux?igsh=MWNtNzNsMGRsYWNsbw==" target="_blank" style="text-decoration: none;">
    <img src="https://img.icons8.com/fluency/48/000000/instagram-new.png" width="24" />  @sanam.ux
</a><br>

<a href="https://github.com/enzosrs" target="_blank" style="text-decoration: none;">
    <img src="https://img.icons8.com/fluency/48/000000/github.png" width="24" /> Enzo's GitHub
</a><br>

<a href="enzosrs@gmail.com" target="_blank" style="text-decoration: none;">
    <img src="https://img.icons8.com/fluency/48/000000/email.png" width="24" /> enzosrs@gmail.com
</a>

