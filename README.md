# That-Random-Discord-Bot-Hotswap
This is another version of the TRDB discord bot. The only difference is that the user can determine if they want a self bot or a verified bot in the same file. 

# Link to server bot:
https://discord.com/api/oauth2/authorize?client_id=1076895961432989777&permissions=8&scope=bot

(I am not responsible for any use cases of this bot. I am supplying this for educational purposes only)

#Updates
If I were to update the TRDB bot series, I will probably only update this repositopry for convenience.

# Setup
This is the self and server bot version of the TRDB( that random discord bot). You can add this to servers and private group chats in discord.
1. Get the token to the account you want to add the bot to. To do this, create a bookmark and set the url to : javascript:(function()%7Blocation.reload()%3Bvar i %3D document.createElement('iframe')%3Bdocument.body.appendChild(i)%3Balert(i.contentWindow.localStorage.token)%7D)() 
2. copy the token string to the token variable on the line under the if(selfBot) statment. The variable is located in main.py
3. Go to the link: https://discord.com/developers/applications and create a new application. Then you want to add a new bot to that application. You should set the permissions to Administrator and set the application type to bot.
4. Copy your bot token in the dev portal. After you have your bot token, replace the empty string("") next to the variable token(the variable under the else: statment) with your bot token. The variable is located in main.py

If you want to run the bot 24/7 for free:
5.Copy all of the lines of code and put the code in replit. When you run the code, replit should install the dependincies. After that, a small window will pop up above the console. At the top of the window, there is a link. Copy the Link

6. Go to https://uptimerobot.com and create a free account. Next, click add monitor. In that section, select https and put the url that you copied. You can keep all of the remaining settings the same (you may want to put your email to see when the bot is down)

7. enjoy the bot!
