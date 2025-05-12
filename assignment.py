import pandas as pd

# Step 1: Load the Excel file
df = pd.read_excel("HSN_SAC.xlsx")

# Step 2: Clean column names
df.columns = df.columns.str.strip()

# Step 3: Create a dictionary from the HSN code and description
hsn_dict = dict(zip(df["HSNCode"].astype(str), df["Description"]))

# Step 4: Function to validate a single HSN code
def validate_single_hsn(code):
    code = str(code).strip()
    
    # Format Validation
    if not code.isdigit():
        return f"{code}: Invalid format. HSN codes must be numeric."
    
    # Length Validation
    if len(code) not in [2, 4, 6, 8]:
        return f"{code}: Invalid length. HSN codes must be 2, 4, 6, or 8 digits long."
    
    # Existence Validation
    if code not in hsn_dict:
        return f"{code}: Code not found in the HSN master data."
    
    # Hierarchical Validation
    parents = [code[:i] for i in [2, 4, 6] if i < len(code)]
    missing_parents = [p for p in parents if p not in hsn_dict]
    if missing_parents:
        return f"{code}: Valid, but missing parent levels: {', '.join(missing_parents)}"
    
    return f"{code}: Valid HSN Code - {hsn_dict[code]}"

# Step 5: Main loop to handle multiple inputs
while True:
    user_input = input("Enter HSN code(s) (comma-separated, or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    
    codes = [code.strip() for code in user_input.split(",") if code.strip()]
    for code in codes:
        result = validate_single_hsn(code)
        print(result)
