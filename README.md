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

## How to Run

1. Place CSV or Excel files inside `Data/Source/`.

2. Install the required dependencies:

- pip install -r requirements.txt

3. Run the Python script:
- python excel_csv_merge.py

4. The merged file will be created in:
    Output/Merge_data.xlsx
5. Successfully processed files will be moved to:
    Data/Archive/

## Folder Structure
 ```
Excel-CSV-Merger/
│   │
│   └── Data/
│        ├── Source/
│        └── Archive/
│
├── Screenshots/
│           └── merging program.png
│
├── Output/
├── excel_csv_merge.py
├── LICENSE
│── requirements.txt
└── README.md
```

## Output

After execution, the project:

- Reads all CSV and Excel files
- Merges the datasets
- Removes duplicate records
- Creates a merged Excel file
- Moves processed files to the Archive folder


## Future Improvements

- Tkinter desktop interface
- File selection dialog
- Merge summary report

## License

This project is licensed under the MIT License.


## Author

**Akshay Gawand**