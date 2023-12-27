# How to Make a Python Slack Bot in 2022 🤖💛 <br />
### - Overview -
Welcome to this step-by-step guide on creating your first Python Slack Bot! 🤖💙 If you prefer video format, check out the tutorial on [**YouTube**](https://www.youtube.com/watch?v=DyzNPAuGtcU&ab_channel=OliverCarmont) or [**Medium**](https://medium.com/@olivercarmont/how-to-make-a-simple-python-slack-bot-828d4a2f982c).
<br />
> **About Myself**: 🤖 I'm an aspiring ML Engineer sharing my learnings on ML/AI on [**YouTube!**](https://www.youtube.com/@olivercarmont) 🎥❤️ 
<br />
### 1 - Setting Up Your Project:
1. Go to [api.slack.com](https://api.slack.com) and click “Your apps” 📱
2. Select “Create an App” ➕ and choose “From Scratch” to name your bot 🔡
3. Hit “Bots” 🤖 and then “Review Scopes to Add” 🔭
4. Scroll down, click “Add an oAuth Scope” ➕, and select “chat:write” 💬
5. Scroll up and click “Install to Workspace” ➕

### 2 - Creating Project Files:
6. In VS Code, create a new folder for your project.
7. Inside the folder, create two files: "main.py" and ".env"

### 3 - Adding Bot Token to .env:**
8. Copy the "Bot User OAuth Token" from Slack.
9. Open ".env" and paste the token as follows:
 ```
 SLACK_BOT_TOKEN=(insert token here)
```

### 4 - Installing Dependencies:
10. Open your terminal and navigate to your project folder.
11. Run the following commands:
 ```
 pip3 install slackclient
 pip3 install python-dotenv
 ```

### 5- Running Your Bot:
12. Open "main.py" in VS Code.
13. Add the necessary imports at the beginning of the file.
14. Save your changes.

### 6 - Testing Your Bot:
15. Open the terminal in VS Code.
16. Run the following command:
 ```
 python3 main.py
 ```
17. Check Slack for a notification from your bot.

### That's it! 🎊
Hope you found this tutorial useful. Make sure to subscribe to my YouTube channel for more updates!
