# KOTBO-queue-bot
This is a bot for queuing in the knights of the blood oath zenith guild
## Setup
1. change `example.env` to `.env`
**In the .env file**
2. You need to set `TOKEN` to your discord bot token
3. Set `RAID_QUEUE_CHANNEL_ID` to the channel id of your raid queue channel
4. Set `DUNGEON_QUEUE_CHANNEL_ID` to the channel id of your dungeon queue channel
5. Set `ROULETTE_QUEUE_CHANNEL_ID` to the channel id of your roulette queue channel
**Python**
Make sure you have python installed
Make sure you have pycord and python-dotenv installed (`pip install pycord` and `pip install python-dotenv`)

**The roles should preferably be name `Raid Queue`, `Dungeon Queue`, and `Roulette Queue`**

**You need to make sure the KOTBO bot role has grester permissions/is higher up on the list for it to be able to add and remove the roles, and that the bot a=has access to the queue channels**

**The queue channels should not be visible to the general server unless the have a queue role**

Made by @Angry Fool#2653
