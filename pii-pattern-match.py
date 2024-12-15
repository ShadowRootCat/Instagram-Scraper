import os
import re
import sys
from datetime import datetime

# Output text file
OUTPUT_FILE = f'extracted_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'

# Enhanced Regex patterns for different data types
PATTERNS = {
    "Email Addresses": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',

    "Phone Numbers": r'(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{1,4}\)?[\s-]?)?\d{1,4}[\s-]?\d{1,4}[\s-]?\d{1,9}',

    "Addresses": r'\d+\s+[\w\s,.-]+(?:Street|St|Road|Rd|Avenue|Ave|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Plaza|Plz)[,\s]+[\w\s]+[,\s]+[A-Za-z]+[,\s]+\d{4,6}',

    "Postal Codes": {
        "US": r'\b\d{5}(?:-\d{4})?\b',
        "Canada": r'\b[A-Za-z]\d[A-Za-z]\s?\d[A-Za-z]\d\b',
        "UK": r'\b[A-Z]{1,2}\d{1,2}[A-Z]?\s?\d[A-Z]{2}\b',
        "Australia": r'\b\d{4}\b',
        "India": r'\b\d{6}\b',
        "Germany": r'\b\d{5}\b',
        "France": r'\b\d{5}\b'
    },

    "Dates of Birth": r'\b(?:\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2})\b',

    "Credit Card Numbers": r'\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b'
}

def extract_pattern(content, pattern):
    """
    Extract matches for a single regex pattern.
    Args:
        content (str): The text to search.
        pattern (str): The regex pattern to match.
    Returns:
        list: A list of matches found in the content.
    """
    return re.findall(pattern, content)

def extract_from_file(file_path):
    """
    Extract data from a single file by applying regex patterns.
    Args:
        file_path (str): Path to the file to process.
    Returns:
        dict: A dictionary of extracted data categorized by type.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    extracted_data = {}
    
    # Iterate over patterns to extract data
    for category, pattern in PATTERNS.items():
        if isinstance(pattern, dict):
            # Handle nested patterns (e.g., for postal codes by country)
            extracted_data[category] = {}
            for subcategory, subpattern in pattern.items():
                matches = extract_pattern(content, subpattern)
                if matches:
                    extracted_data[category][subcategory] = matches
        else:
            # Handle single patterns
            matches = extract_pattern(content, pattern)
            if matches:
                extracted_data[category] = matches
    
    return extracted_data

def save_to_txt(data, output_file):
    """
    Save extracted data to a text file in a readable format.
    Args:
        data (dict): The extracted data to save.
        output_file (str): Path to the output text file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for category, content in data.items():
            f.write(f"{category}:\n")
            if isinstance(content, dict):
                # Write nested categories
                for subcategory, matches in content.items():
                    f.write(f"  {subcategory}:\n")
                    for match in matches:
                        f.write(f"    {match}\n")
            else:
                # Write flat categories
                for match in content:
                    f.write(f"  {match}\n")
            f.write("\n")

def main():
    """
    Main function to process the file and save results.
    Reads a file path from command-line arguments, extracts data, and saves to a text file.
    """
    if len(sys.argv) < 2:
        print("\u274c Error: Please provide the file path as a command-line argument.")
        print("Usage: python script.py <file_path>")
        return

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"\u274c Error: File {file_path} does not exist.")
        return

    print(f"Processing {file_path}...")
    extracted_data = extract_from_file(file_path)

    # Save extracted data to a text file
    save_to_txt(extracted_data, OUTPUT_FILE)

    print(f"\u2705 Extraction completed. Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
