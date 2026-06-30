@echo off

cd /d "%~dp0"

call .venv\Scripts\activate

pytest --browser chrome --alluredir=reports

allure generate reports --clean -o allure-report

pause