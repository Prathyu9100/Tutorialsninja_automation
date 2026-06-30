@echo off
cd /d "%~dp0"

python -m pip install -r requirements.txt
python -m pytest --browser chrome --alluredir=reports
allure generate reports --clean -o allure-report