# Excel File Merger

This program is a Python script that reads in two Excel files and merges them on the 'Reference' column. The resulting merged DataFrame is saved as a new Excel file with the current date and time added to the filename.

## Installation

To run this program, you must have Python and the pandas library installed. You can install pandas using pip:

```sh
pip install -r requirements.txt
```

## Usage

To use this program, call the script with two command line arguments: the filenames of the two Excel documents you wish to merge. For example:

```sh
python excel_merger.py ./example/1.xlsx ./example/2.xlsx
```

The resulting merged DataFrame will be printed to the console, and a new Excel file with the merged data will be created in the same directory as the script with a filename in the format of `merged_doc_<date>-<time>.xlsx`, where `<date>-<time>` is the current date and time.

## Example

Suppose we have two Excel files, `sales.xlsx` and `inventory.xlsx`, that we want to merge. We can run the script as follows:

```sh
python excel_merger.py sales.xlsx inventory.xlsx
```

The resulting merged DataFrame will be printed to the console, and a new Excel file named `merged_doc_<date>-<time>.xlsx` will be created in the same directory as the script with the merged data.