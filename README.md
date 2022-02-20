<h1 align="center">
  <b>Save Restricted Content Bot</b>
</h1> 

- works for both public and private channels
- Custom thumbnail support for Pvt medias
- supports text and webpage media messages
- Faster speed
- Forcesubscribe available 
- `/batch` - (For owner only) Use this command to save upto 100 files from a pvt or public restricted channel at once.
- Time delay is added to avoid FloodWait and keep user account safe. 

# Variables

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT TOKEN` 
- `OWNER_ID` - Owner user id
- `CHUSERNAME` - Public channel username without '@'. Don't forget to add bot in channel as administrator. 

# Deploy
  
- Fork the repo, and star it
- create app in heroku
- go to settings of app>> config vars>> add all variables
- add buildpacks
- connect to github and deploy
- turn on dynos
  
Buildpacks for manual deploy:

- `heroku/python`
- `https://github.com/FriDayXD/heroku-buildpack-ffmpeg-latest.git`

# CREDITS
`BLAZE` 
`STARK`
Special Thank To `TeamDrone`
