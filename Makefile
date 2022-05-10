install:
	sudo apt install ./driver/google-chrome-stable_current_amd64.deb -y
	cd driver; unzip *.zip
	pip install termcolor