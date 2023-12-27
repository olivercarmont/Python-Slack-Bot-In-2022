# How to Make a Python Slack Bot in 2022 🤖💛 <br />

> **About Myself**: 🤖 I'm an aspiring ML Engineer sharing my learnings on ML/AI on [**YouTube!**](https://www.youtube.com/@olivercarmont) <br />

## - Overview -
Welcome to this step-by-step guide on creating your first Python Slack Bot! 🤖💙 If you prefer video format, check out the tutorial on [**YouTube**](https://www.youtube.com/watch?v=DyzNPAuGtcU&ab_channel=OliverCarmont) or [**Medium**](https://medium.com/@olivercarmont/how-to-make-a-simple-python-slack-bot-828d4a2f982c).
<br />

## 1 - Setting Up Your Project:
1. Go to [api.slack.com](https://api.slack.com) and click “Your apps” 📱
2. Select “Create an App” ➕ and choose “From Scratch” to name your bot 🔡
3. Hit “Bots” 🤖 and then “Review Scopes to Add” 🔭
4. Scroll down, click “Add an oAuth Scope” ➕, and select “chat:write” 💬
5. Scroll up and click “Install to Workspace” ➕

## 2 - Download This Repository
6. Download the code found in this repository onto your local desktop.

## 3 - Adding Bot Token to .env:
7. Copy the "Bot User OAuth Token" from Slack.
8. Open ".env" and paste the token as follows:
 ```python
 SLACK_BOT_TOKEN=(insert token here)
```

## 4 - Testing Your Bot:
9. Open the terminal in VS Code.
10. Run the following command:
 ```python
 python3 main.py
 ```
11. Check Slack for a notification from your bot.

### That's it! 🎊
Hope you found this tutorial useful. Make sure to subscribe to my [**YouTube channel**](https://www.youtube.com/@olivercarmont) for more updates!
