
# FTM OTT GENIE

FTM OTT GENIE is a Telegram bot that allows users to download free videos from various OTT platforms such as JioCinema, Hotstar, SonyLIV, and Zee5. Simply send a link to the desired video, and the bot will fetch and deliver it directly to you.

## Features

- Download free videos from supported OTT platforms.
- Customized video filenames that include the uploader and disclaimer.
- Displays video duration and file size.
- Requires users to join the channel to access the bot.

## How to Use

1. Start the bot by sending the `/start` command.
2. Join our channel [@ftmmovieskiduniya](https://t.me/ftmmovieskiduniya) to access the bot features.
3. Send the link of the free video you want to download using the `/download <video_link>` command.
4. The bot will process your request and deliver the video directly to you!

## Installation

To run this project, clone the repository and install the dependencies:

```bash
git clone https://github.com/ftmdeveloperz/FTM_OTT_GENIE.git
cd FTM_OTT_GENIE
pip install -r requirements.txt
```

### Running the Bot

1. Set your TELEGRAM_BOT_API_TOKEN as an environment variable.

#### On Linux/Mac:

export TELEGRAM_BOT_API_TOKEN='your_bot_token'

#### On Windows:

set TELEGRAM_BOT_API_TOKEN='your_bot_token'


2. Run the bot:
```bash
python ftm.py
```

### Docker Setup

To deploy the bot using Docker, follow these steps:

1. Build the Docker image:
```bash
docker build -t ftm_ott_genie .
```
2. Run the Docker container:
```bash
docker run -d -e TELEGRAM_BOT_API_TOKEN='your_bot_token' ftm_ott_genie
```
### Deployment Options

#### Render
To deploy on Render, follow these steps:
1. Create a new Web Service in your Render dashboard.
2. Connect your GitHub repository containing the bot.
3. Set the build command to:
```bash
pip install -r requirements.txt
```
4. Set the start command to:
```bash
python ftm.py
```

5. Add the environment variable TELEGRAM_BOT_API_TOKEN in the settings with your bot token.

6. Click "Create Web Service" to deploy.


#### Heroku

To deploy on Heroku, follow these steps:

1. Install the Heroku CLI and log in.

2. Create a new Heroku app:
```bash
heroku create ftm-ott-genie
```

3. Set the config variable for your bot token:
```bash
heroku config:set TELEGRAM_BOT_API_TOKEN='your_bot_token'
```

4. Deploy the bot:
```bash
git push heroku main
```

5. Open your app:
```bash
heroku open
```


#### Railway

To deploy on Railway, follow these steps:

1. Go to Railway.app and create a new project.

2. Connect your GitHub repository.

3. Set the environment variable TELEGRAM_BOT_API_TOKEN in the settings with your bot token.

4. Click on "Deploy" to start the bot.

5. Monitor your deployment on the Railway dashboard.



#### Koyeb

To deploy on Koyeb, follow these steps:

1. Create a new service in your Koyeb dashboard.

2. Connect your GitHub repository.

3. Set the command to run your bot as:
```bash
python ftm.py
```

4. Add the environment variable TELEGRAM_BOT_API_TOKEN in the settings with your bot token.

5. Click "Deploy" to start the service.


#### VPS (Virtual Private Server)

To deploy on a VPS, follow these steps:

1. Access your VPS via SSH.

2. Clone the repository:
```bash
git clone https://github.com/ftmdeveloperz/FTM_OTT_GENIE.git
cd FTM_OTT_GENIE
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Set the environment variable for your bot token:
```bash
export TELEGRAM_BOT_API_TOKEN='your_bot_token'
```

5. Run the bot:
```bash
python ftm.py
```


## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
1. Fork the repository.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.



## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Special thanks to the developers of yt-dlp for making video downloading easy.
Thanks to the Telegram community for their support and resources.


## Contact

For any questions or inquiries, feel free to contact:
Telegram: @ftmdeveloperz
Email: funtoonsmultimedia@gmail.com


