server:
	poetry run python -m src.server.main

bot:
	echo "Sudo is required beacuse of keyboard.py"; sudo python3 -m src.api.bot
