# Telegram Bot with Schedule and Spam Control

This repository contains a Python script for a Telegram bot that sends scheduled messages to users. The bot allows users to start or stop the spam messages using inline buttons.

## Features

- **Start and Stop Spam:** Users can control whether they want to receive spam messages using "yes" and "no" buttons.
- **Threading:** The script uses threading to run the message schedule in the background without blocking the bot's other functionalities.
- **Environment Variables:** The bot token is securely managed using an `.env` file, ensuring that sensitive information is not hardcoded in the script.

## Prerequisites

- Python 3.7 or higher
- Telegram bot token (you can create a bot and obtain a token using [BotFather](https://core.telegram.org/bots#botfather))

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sademban/teligram-bot-test.git
   cd telegram-bot-test
