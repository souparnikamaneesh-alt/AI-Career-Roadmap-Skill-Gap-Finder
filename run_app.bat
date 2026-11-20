@echo off
echo ========================================================
echo   Starting AI Career Roadmap & Skill Gap Finder App...
echo ========================================================
echo.

set PYTHON_PATH="C:\Users\D E L L\AppData\Local\Python\bin\python.exe"

if exist %PYTHON_PATH% (
    %PYTHON_PATH% -m streamlit run app.py
) else (
    python -m streamlit run app.py
)

pause
