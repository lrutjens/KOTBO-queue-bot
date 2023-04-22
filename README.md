# KOTBO-queue-bot
This is a bot for queuing in the knights of the blood oath zenith guild
## Setup
1. change `example.env` to `.env`
**In the .env file**
2. You need to set `TOKEN` to your discord bot token
3. Set `RAID_QUEUE_CHANNEL_ID_1` to the channel id of your tier 1 raid queue channel
4. Set `RAID_QUEUE_CHANNEL_ID_2` to the channel id of your tier 2 raid queue channel
5. Set `DUNGEON_QUEUE_CHANNEL_ID` to the channel id of your dungeon queue channel
6. Set `ROULETTE_QUEUE_LEVELING` to the channel id of your leveling roulette queue channel
7. Set `ROULETTE_QUEUE_RAID` to the channel id of your raid roulette queue channel
8. Set `ROULETTE_QUEUE_EXPERT` to the channel id of your expert roulette queue channel


**Python**
Make sure you have python installed
Make sure you have pycord and python-dotenv installed (`pip install pycord` and `pip install python-dotenv`)

**The roles HAVE to be named `Tier 1 Raid Queue`, `Tier 2 Raid Queue`, `Dungeon Queue`, `Leveling Roulette Queue`, `Raid Roulette Queue` and `Expert Roulette Queue`**

**You need to make sure the KOTBO bot role has grester permissions/is higher up on the list for it to be able to add and remove the roles, and that the bot has access to the queue channels**

**The queue channels should not be visible to the general server unless the have a queue role**

Made by ___**@Angry Fool#2653**___
