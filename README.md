
## Steps to Run the Script

1. **Ensure that the following files are in the same directory**:
   - `assignment.py`
   - `HSN_SAC.xlsx`

2. **Open Terminal or PowerShell**:
   Navigate to the directory where `assignment.py` and `HSN_SAC.xlsx` are located.

3. **Run the Script**:
   In the terminal, run the following command:

   ```bash
   python assignment.py
Sample Input and Output
Sample Input:

text
Copy
Edit
Enter HSN code(s) (comma-separated, or 'exit' to quit): 0101, 9999
Sample Output:

text
Copy
Edit
0101: Valid HSN Code - Live horses, asses, mules and hinnies
9999: Code not found in the HSN master data.
Troubleshooting
If you encounter any issues such as errors related to pandas, try the following:

Make sure the pandas library is properly installed by running:

bash
Copy
Edit
pip install pandas
