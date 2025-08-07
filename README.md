# CSV Cleaner Tool

A Python utility for cleaning CSV files by removing empty rows, trailing commas, and formatting issues while preserving UTF-8 encoding for international text (including Khmer script).

## 📋 Features

- **Remove empty rows** - Eliminates completely blank lines and rows with only commas
- **Trim trailing commas** - Removes extra commas at the end of rows that cause parsing issues
- **Preserve UTF-8 encoding** - Maintains international characters (Khmer, Chinese, Arabic, etc.)
- **Multiple encoding support** - Automatically detects and handles different file encodings
- **Column structure validation** - Ensures all rows have the same number of columns as the header
- **Batch processing** - Clean multiple files at once with glob patterns
- **Flexible output options** - Custom output paths or automatic naming with "_cleaned" suffix
- **Detailed reporting** - Shows processing statistics for each file

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No additional packages required (uses only standard library)

### Basic Usage

```bash
# Clean a single file (creates data_cleaned.csv)
python csv_cleaner.py data.csv

# Clean with custom output name
python csv_cleaner.py data.csv clean_data.csv

# Clean all CSV files in current directory
python csv_cleaner.py *.csv

# Clean multiple specific files
python csv_cleaner.py file1.csv file2.csv file3.csv
```

### Windows Batch File (Alternative)

For Windows users, use the included batch file:

```cmd
# Double-click clean_csv.bat for usage instructions
# Or use from command line:
clean_csv.bat data.csv
clean_csv.bat *.csv
```

## 📖 Detailed Usage

### Command Line Options

```bash
# Single file processing
python csv_cleaner.py input_file.csv [output_file.csv]

# Multiple file processing
python csv_cleaner.py file1.csv file2.csv file3.csv

# Glob pattern processing
python csv_cleaner.py "*.csv"

# Output to specific directory
python csv_cleaner.py input.csv --output-dir cleaned/
python csv_cleaner.py *.csv --output-dir cleaned/
```

### Examples

#### Example 1: Basic Cleaning
```bash
python csv_cleaner.py sample_data.csv
```
**Output:**
```
Cleaning file: sample_data.csv
✓ Cleaned file saved: sample_data_cleaned.csv
  Original rows: 156
  Cleaned rows: 154
  Rows removed: 2
```

#### Example 2: Batch Processing
```bash
python csv_cleaner.py *.csv --output-dir cleaned
```
**Output:**
```
Cleaning file: data1.csv
✓ Cleaned file saved: cleaned/data1_cleaned.csv
  Original rows: 156
  Cleaned rows: 154
  Rows removed: 2

Cleaning file: data2.csv
✓ Cleaned file saved: cleaned/data2_cleaned.csv
  Original rows: 180
  Cleaned rows: 178
  Rows removed: 2

✓ Successfully cleaned 2 files
```

## 🔧 What Gets Cleaned

### Before Cleaning
```csv
id,name,category,description,status,,,,,
,,,,,,,,
101,Product A,Electronics,High quality device,Active,,,,,
102,Product B,Clothing,Cotton material,Pending,,,,,
,,,,,,,,
```

### After Cleaning
```csv
id,name,category,description,status
101,Product A,Electronics,High quality device,Active
102,Product B,Clothing,Cotton material,Pending
```

### Issues Fixed
- ✅ Empty rows removed
- ✅ Trailing commas stripped
- ✅ Consistent column count
- ✅ UTF-8 encoding preserved
- ✅ Whitespace normalized

## 📁 File Structure

```
csv-cleaner/
├── csv_cleaner.py          # Main Python script
├── clean_csv.bat           # Windows batch file
├── README.md               # This documentation
└── examples/
    ├── input/
    │   ├── sample_data.csv     # Sample input file
    │   └── inventory.csv       # Sample input file
    └── output/
        ├── sample_data_cleaned.csv    # Cleaned output
        └── inventory_cleaned.csv      # Cleaned output
```

## 🛠️ Technical Details

### Encoding Support
The script automatically handles multiple text encodings:
1. **UTF-8** (primary) - For international text
2. **UTF-8-BOM** - For files with byte order mark
3. **CP1252** - For Windows Latin characters
4. **Latin1** - Fallback encoding

### Processing Logic
1. **Read file** with UTF-8 encoding (fallback to other encodings if needed)
2. **Strip whitespace** and trailing commas from each line
3. **Filter empty rows** and rows containing only commas
4. **Validate structure** ensuring consistent column count
5. **Write clean file** maintaining UTF-8 encoding

### Error Handling
- **File not found** - Clear error message with file path
- **Encoding errors** - Automatic fallback to alternative encodings
- **Permission errors** - Informative error messages
- **Invalid CSV structure** - Graceful handling with warnings

## ⚠️ Important Notes

### Data Safety
- **Original files are never modified** - Only cleaned copies are created
- **UTF-8 encoding preserved** - International characters remain intact
- **Data structure maintained** - Column relationships preserved

### Performance
- **Memory efficient** - Processes files line by line
- **Fast processing** - No external dependencies
- **Batch optimized** - Efficient handling of multiple files

### Limitations
- **CSV format only** - Does not process Excel files (.xlsx, .xls)
- **Memory usage** - Very large files (>100MB) may require more RAM
- **Column detection** - Assumes first non-empty row is the header

## 🚨 Troubleshooting

### Common Issues

#### Issue: "File not found" error
```bash
FileNotFoundError: Input file not found: myfile.csv
```
**Solution:** Check file path and ensure the file exists in the specified location.

#### Issue: Encoding problems with special characters
```bash
UnicodeDecodeError: Could not decode file with any common encoding
```
**Solution:** The script tries multiple encodings automatically. If this persists, the file may be corrupted or in an unsupported format.

#### Issue: No files processed with glob pattern
```bash
python csv_cleaner.py "*.csv"
# No output
```
**Solution:** Ensure CSV files exist in the current directory and use quotes around the glob pattern.

### Getting Help

1. **Check file permissions** - Ensure you can read input files and write to output directory
2. **Verify Python version** - Use Python 3.6 or higher
3. **Test with sample file** - Try with a simple CSV file first
4. **Check file encoding** - Open file in text editor to verify it's readable

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup
```bash
git clone <repository-url>
cd csv-cleaner
python csv_cleaner.py --help
```

## 📞 Support

For support or questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Verify your CSV file format and encoding

---

**Made with ❤️ for cleaning messy CSV files**
