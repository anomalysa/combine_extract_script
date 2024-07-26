# combine_extract_script

This script combines the contents of two text files (`Backside_results.txt` and `Flatness.txt`) into one file and extracts specific parameters.

## How to Use

1. Place `Backside_results.txt` and `Flatness.txt` in the same directory as the script.
2. Run the script:
   ```sh
   python combine_extract_script.py or python3 combine_extract_script.py

3. The combined and filtered results will be saved to Filtered_results.txt.
   
4. Parameters Extracted:
    Component ID, 
    Component Material, 
    Component Thickness (in mm), 
    Flatness, 
    Component Passed (boolean value: true/false)
