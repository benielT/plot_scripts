import pandas as pd

# Gradient interpolation function
def get_color(value, low_color, high_color, low_val=0, high_val=100, mid_color=None):
    """
    Calculates a color within a two or three-color gradient based on a value.

    This function performs linear interpolation. If a mid_color is provided,
    it creates a gradient from low_color -> mid_color -> high_color.

    Args:
        value (float | int): The input value to map to a color.
        low_color (tuple): The RGB tuple for the low end of the gradient.
        high_color (tuple): The RGB tuple for the high end of the gradient.
        low_val (float | int): The minimum value of the input range. Defaults to 0.
        high_val (float | int): The maximum value of the input range. Defaults to 100.
        mid_color (tuple, optional): The RGB tuple for the middle of the gradient.
                                     If None, a two-color gradient is used. Defaults to None.

    Returns:
        tuple: An RGB tuple as integers representing the interpolated color.
    """
    # Clamp value to the range [low_val, high_val] to handle extremes
    value = max(low_val, min(value, high_val))
    
    # Determine which segment of the gradient the value falls into
    if mid_color is not None:
        mid_val = (low_val + high_val) / 2
        if value < mid_val:
            # First half of the gradient: low_color -> mid_color
            high_color = mid_color
            high_val = mid_val
        else:
            # Second half of the gradient: mid_color -> high_color
            low_color = mid_color
            low_val = mid_val

    # Handle the case where the range is zero to prevent division by zero
    if high_val == low_val:
        return low_color

    # Calculate the fraction for the determined segment
    fraction = (value - low_val) / (high_val - low_val)

    # Linearly interpolate each color channel (r, g, b)
    color = tuple(
        int(low_color[i] + fraction * (high_color[i] - low_color[i]))
        for i in range(3)
    )

    return color

def preprocess_value(value: str) -> str:
    """Preprocess numeric string by removing % and converting to float."""
    if isinstance(value, str):
        value = value.replace('%', '').strip()
    try:
        return value
    except ValueError:
        return value  # return original if conversion fails
    
def round_mine(value: str, decimals=1) -> str:
    """Round a numeric string to specified decimal places."""
    try:
        num = float(value)
        if decimals < 0:
            decimals = 0
        if decimals == 0:
            return str(int(round(num)))
        
        return str(round(num, decimals))
    except ValueError:
        return value  # return original if conversion fails
    
# Highlight Colors (green → red)
# low_color = [0, 255, 0]   # green
# high_color = [255, 0, 0]  # red
# mid_color = [255, 255, 0] # yellow (optional)

# Pastol Colors (green → red)
# low_color = [180, 255, 200]   # pastel green
# high_color = [255, 180, 180]  # pastel red
# mid_color = [255, 255, 200]   # pastel yellow (optional)

# Slightly less vibrant pastel colors (green → red)
# low_color = [60, 220, 120]    # less vibrant green
# high_color = [220, 80, 80]    # less vibrant red
# mid_color = [240, 240, 120]   # less vibrant yellow (optional)

# Light to vibrant red (white → red)
low_color = [255, 255, 255]    # white
high_color = [220, 80, 80]    # less vibrant red
mid_color = None

# Colors (green → red), slightly darker
# low_color = [80, 180, 120]    # darker green
# high_color = [200, 80, 80]    # darker red
# mid_color = [220, 220, 120]   # darker yellow (optional)

# Color-blind aware heatmap (blue → yellow → red, ColorBrewer "YlOrRd" or "Viridis" inspired)
# Uncomment below for color-blind friendly option:
# low_color = [69, 117, 180]    # blue
# mid_color = [253, 231, 37]    # yellow
# high_color = [215, 48, 39]    # red
# Rounding options
enable_rounding = True
selective_rounding = True  # if True, only round specific columns
selective_rounding_cols = {
    "u280_cols" : {
        "Acv Frq": 0,
        "LUT": 1,
        "LUTRAM": 1,
        "FF": 1,
        "BRAM": 1,
        "URAM": 1,
        "DSP": 1,
        "IO": 1,
        "GT": 1,
        "BUFG": 0,
        "MMCM": 0,
        "PLL": 1,
        "PCIe": 1,
    },
    "vck_cols" : { #LUT,LUTRAM,FF,BRAM,URAM,DSP,IO,BUFG,MMCM,PLL
        "LUT": 1,
        "LUTRAM": 1,
        "FF": 1,
        "BRAM": 1,
        "URAM": 1,
        "DSP": 1,
        "IO": 1,
        "BUFG": 1,
        "MMCM": 1,
        "PLL": 1
    }
}
round_decimals = 1  # number of decimal places

# Read CSVs
vck_df = pd.read_csv("./data/vck5000_apps_resource_usage_percentage.csv")
u280_df = pd.read_csv("./data/u280_apps_resource_usage_percentage.csv")

# Ensure both DataFrames have the same application order
assert all(vck_df['Application'] == u280_df['Application'])

# Columns for each platform
u280_cols = list(u280_df.columns[1:])  # skip Application
vck_cols = list(vck_df.columns[1:])

# Build LaTeX table
latex_lines = []
latex_lines.append("\\begin{table*}[h!]")
latex_lines.append("\\centering\\small")
latex_lines.append("\\caption{Resource Usage\\% Heatmap.}")
latex_lines.append("\\label{tbl:resource_usage}")
latex_lines.append("\\resizebox{\\textwidth}{!}{")
latex_lines.append("\\begin{tabular}{l" + "c"*len(u280_cols) + "c" + "c"*len(vck_cols) + "}")
latex_lines.append("\\toprule")

# Header
latex_lines.append("& \\multicolumn{" + str(len(u280_cols)) + "}{c}{\\textbf{U280}} & & \\multicolumn{" + str(len(vck_cols)) + "}{c}{\\textbf{VCK5000}} \\\\")
latex_lines.append("\\cmidrule{2-" + str(len(u280_cols)+1) + "} \\cmidrule{" + str(len(u280_cols)+3) + "-" + str(len(u280_cols)+2+len(vck_cols)) + "}")

# Column names
header = ["\\textbf{Application}"]
header += [f"\\begin{{sideways}}\\textbf{{{c}}}\\end{{sideways}}" for c in u280_cols]
header.append("empty_col")  # Placeholder for the empty column
header += [f"\\begin{{sideways}}\\textbf{{{c}}}\\end{{sideways}}" for c in vck_cols]
header_line = " & ".join(header) + " \\\\"
header_line = header_line.replace("empty_col", "")  # Remove placeholder text
latex_lines.append(header_line)
latex_lines.append("\\cmidrule{2-" + str(len(u280_cols)+1) + "} \\cmidrule{" + str(len(u280_cols)+3) + "-" + str(len(u280_cols)+2+len(vck_cols)) + "}")

# Data rows
for i in range(len(u280_df)):
    row = []
    app = u280_df.loc[i, 'Application']
    row.append(app)
    # U280 values
    for c in u280_cols:
        val = preprocess_value(u280_df.loc[i, c])
        if enable_rounding:
            if selective_rounding and c in selective_rounding_cols['u280_cols']:
                val = round_mine(val, selective_rounding_cols['u280_cols'][c])
            elif not selective_rounding:
                val = round_mine(val, round_decimals)
        if c == "Acv Frq":
            color = get_color(float(val), high_color, low_color, low_val=250, high_val=300, mid_color=mid_color)
        else:
            color = get_color(float(val), low_color, high_color, low_val=0, high_val=100, mid_color=mid_color)
        row.append(f"\\cellcolor[RGB]{{{color[0]},{color[1]},{color[2]}}}{val}")
    row.append("empty_col")  # Placeholder for the empty column
    # VCK values
    for c in vck_cols:
        val = preprocess_value(vck_df.loc[i, c])
        if enable_rounding:
            if selective_rounding and c in selective_rounding_cols['vck_cols']:
                val = round_mine(val, selective_rounding_cols['vck_cols'][c])
            elif not selective_rounding:
                val = round_mine(val, round_decimals)
        if c == "Acv Frq":
            color = get_color(float(val), high_color, low_color, low_val=250, high_val=300, mid_color=mid_color)
        else:
            color = get_color(float(val), low_color, high_color, low_val=0, high_val=100, mid_color=mid_color)
        row.append(f"\\cellcolor[RGB]{{{color[0]},{color[1]},{color[2]}}}{val}")
    # Remove placeholder text
    line = " & ".join(row).replace("empty_col", "") + " \\\\"
    latex_lines.append(line)

latex_lines.append("\\bottomrule")
latex_lines.append("\\end{tabular}")
latex_lines.append("}")
latex_lines.append("\\end{table*}")

# Write to file
with open("./output/resource_usage_heatmap.tex", "w") as f:
    f.write("\n".join(latex_lines))

print("LaTeX table written to ./output/resource_usage_heatmap.tex")
