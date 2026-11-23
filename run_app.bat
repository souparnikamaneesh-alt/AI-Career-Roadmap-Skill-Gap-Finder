@echo off
cd /d "%~dp0"
title AI Career Roadmap & Skill Gap Finder
echo ======================================================================
echo   Starting AI Career Roadmap & Skill Gap Finder...
echo   Opening in your default browser at http://localhost:8501
echo ======================================================================
echo.

set "PYTHON_PATH=C:\Users\D E L L\AppData\Local\Python\bin\python.exe"

if exist "%PYTHON_PATH%" (
    "%PYTHON_PATH%" -m streamlit run app.py
) else (
    python -m streamlit run app.py
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred while launching Streamlit.
    echo Press any key to exit...
    pause >nul
)
