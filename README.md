# Excel & CSV File Merger

## Project Overview

This project automates the process of reading multiple CSV and Excel files, merging them into a single dataset, and exporting the final data as an Excel workbook.

## Features

- Read CSV and Excel files
- Merge multiple files
- Remove duplicate records
- Export merged Excel file
- Archive processed files

## Technologies

- Python
- Pandas
- OpenPyXL
- Shutil
- Glob
- OS

## Folder Structure

Excel-CSV-Merger/
│   │
│   └── Data/
│        ├── Source/
│        └── Archive/
│
├── Output/
├── excel_csv_merge.py
├── requirements.txt
└── README.md


## Output

After execution, the project:

- Reads all CSV and Excel files
- Merges the datasets
- Removes duplicate records
- Creates a merged Excel file
- Moves processed files to the Archive folder


## Future Improvements

- Tkinter desktop interface
- Progress bar
- File selection dialog
- Merge summary report

## License

This project is licensed under the MIT License.


## Author

**Akshay Gawand**