#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV Cleaner Script
Cleans CSV files by removing empty rows, trailing commas, and formatting issues.
Preserves UTF-8 encoding for Khmer text.
"""

import csv
import os
import sys
from pathlib import Path

def clean_csv_file(input_file_path, output_file_path=None):
    """
    Clean a CSV file by removing empty rows and trailing commas.
    
    Args:
        input_file_path (str): Path to the input CSV file
        output_file_path (str): Path to the output CSV file (optional)
    
    Returns:
        str: Path to the cleaned file
    """
    input_path = Path(input_file_path)
    
    # If no output path specified, create one with _cleaned suffix
    if output_file_path is None:
        output_path = input_path.parent / f"{input_path.stem}_cleaned{input_path.suffix}"
    else:
        output_path = Path(output_file_path)
    
    # Check if input file exists
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    cleaned_rows = []
    header_row = None
    
    print(f"Cleaning file: {input_path}")
    
    # Read the CSV file with UTF-8 encoding
    try:
        with open(input_path, 'r', encoding='utf-8', newline='') as infile:
            # Read all lines first to handle trailing commas
            lines = infile.readlines()
            
            for i, line in enumerate(lines):
                # Strip whitespace and trailing commas
                cleaned_line = line.strip().rstrip(',')
                
                # Skip completely empty lines
                if not cleaned_line:
                    continue
                
                # Split by comma to check for empty rows
                fields = [field.strip() for field in cleaned_line.split(',')]
                
                # Skip rows that are all empty or just commas
                if all(field == '' for field in fields):
                    continue
                
                # Store header row (first non-empty row)
                if header_row is None:
                    header_row = fields
                    cleaned_rows.append(fields)
                else:
                    # Only keep rows that have at least one non-empty field
                    if any(field != '' for field in fields):
                        # Ensure row has same number of columns as header
                        while len(fields) < len(header_row):
                            fields.append('')
                        # Trim extra columns if any
                        fields = fields[:len(header_row)]
                        cleaned_rows.append(fields)
    
    except UnicodeDecodeError:
        print(f"Warning: UTF-8 decode error. Trying with different encoding...")
        # Try with different encodings if UTF-8 fails
        for encoding in ['utf-8-sig', 'cp1252', 'latin1']:
            try:
                with open(input_path, 'r', encoding=encoding, newline='') as infile:
                    lines = infile.readlines()
                    # Process lines same as above...
                    break
            except UnicodeDecodeError:
                continue
        else:
            raise UnicodeDecodeError(f"Could not decode file with any common encoding: {input_file_path}")
    
    # Write cleaned CSV
    with open(output_path, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)
    
    rows_removed = len(lines) - len(cleaned_rows)
    print(f"✓ Cleaned file saved: {output_path}")
    print(f"  Original rows: {len(lines)}")
    print(f"  Cleaned rows: {len(cleaned_rows)}")
    print(f"  Rows removed: {rows_removed}")
    
    return str(output_path)

def clean_multiple_files(file_patterns, output_dir=None):
    """
    Clean multiple CSV files matching the given patterns.
    
    Args:
        file_patterns (list): List of file paths or glob patterns
        output_dir (str): Directory to save cleaned files (optional)
    
    Returns:
        list: List of cleaned file paths
    """
    cleaned_files = []
    
    for pattern in file_patterns:
        # Handle glob patterns
        if '*' in pattern or '?' in pattern:
            from glob import glob
            files = glob(pattern)
        else:
            files = [pattern]
        
        for file_path in files:
            if not file_path.endswith('.csv'):
                continue
                
            try:
                if output_dir:
                    output_path = Path(output_dir) / f"{Path(file_path).stem}_cleaned.csv"
                    output_dir_path = Path(output_dir)
                    output_dir_path.mkdir(exist_ok=True)
                else:
                    output_path = None
                
                cleaned_file = clean_csv_file(file_path, output_path)
                cleaned_files.append(cleaned_file)
                
            except Exception as e:
                print(f"Error cleaning {file_path}: {e}")
    
    return cleaned_files

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python csv_cleaner.py input_file.csv [output_file.csv]")
        print("  Multiple files: python csv_cleaner.py file1.csv file2.csv file3.csv")
        print("  Glob pattern: python csv_cleaner.py '*.csv'")
        print("  With output directory: python csv_cleaner.py input.csv --output-dir cleaned/")
        return
    
    # Parse arguments
    files = []
    output_dir = None
    
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == '--output-dir' and i + 1 < len(sys.argv):
            output_dir = sys.argv[i + 1]
            i += 2
        else:
            files.append(sys.argv[i])
            i += 1
    
    if not files:
        print("No input files specified.")
        return
    
    # Clean the files
    if len(files) == 1 and output_dir is None and len(sys.argv) == 3:
        # Single file with specific output
        clean_csv_file(files[0], sys.argv[2])
    else:
        # Multiple files or use default output naming
        cleaned_files = clean_multiple_files(files, output_dir)
        print(f"\n✓ Successfully cleaned {len(cleaned_files)} files")

if __name__ == "__main__":
    main()
