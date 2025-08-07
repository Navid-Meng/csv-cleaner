@echo off
REM CSV Cleaner Batch Script
REM Usage: clean_csv.bat file1.csv file2.csv ...
REM Or: clean_csv.bat *.csv

echo CSV Cleaner - Batch Processing
echo ================================

if "%1"=="" (
    echo Usage: %0 file1.csv file2.csv ...
    echo Or: %0 *.csv
    echo.
    echo This will clean CSV files by removing empty rows and trailing commas.
    echo Cleaned files will be saved with "_cleaned" suffix.
    pause
    exit /b 1
)

python csv_cleaner.py %*

echo.
echo Batch cleaning completed!
pause
