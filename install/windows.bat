@echo off

echo "Starting install..."
git clone https://github.com/EmeraldThunder1/EmberLang

cd EmberLang

echo "Installing dependencies..."

pip install virtualenv
virtualenv EmberLang

source EmberLang/bin/activate

pip install json

set path="%path%;%cd%"

echo "Install finished, you may now close this window"