import re
import os

def update_readme():
    file_path = 'README.md'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. CALCULATE ACADEMIC AVERAGE ---
    # Look for the Academic Table rows. Pattern: | Name | Module | Grade% | Weight% | Status |
    # We look for lines containing numbers followed by % in the 3rd and 4th columns
    
    pattern = r"\|.*?\|.*?\|\s*(\d+)%\s*\|\s*(\d+)%\s*\|"
    matches = re.findall(pattern, content)
    
    total_weighted_score = 0
    total_weight = 0
    
    for grade, weight in matches:
        total_weighted_score += int(grade) * int(weight)
        total_weight += int(weight)
    
    if total_weight > 0:
        average = total_weighted_score / total_weight
        # Determine classification emoji
        if average >= 70:
            classification = "🌟 First Class"
        elif average >= 60:
            classification = "🥈 2:1"
        else:
            classification = "🥉 2:2"
            
        stats_line = f"**Current Weighted Average:** {average:.2f}% ({classification})"
    else:
        stats_line = "**Current Weighted Average:** N/A (No grades yet)"

    # Replace the old stats line or insert it if it doesn't exist
    # We look for the Academic Header and inject/replace the line below it
    header_pattern = r"(## 🎓 Academic Pillar \(The First Class Hub\)\n.*\n)"
    
    # Check if we already added a stats line previously to replace it
    if "**Current Weighted Average:**" in content:
        content = re.sub(r"\*\*Current Weighted Average:\*\*.*", stats_line, content)
    else:
        # Insert it for the first time
        content = re.sub(header_pattern, r"\1\n" + stats_line + "\n", content)

    # --- 2. WRITE CHANGES ---
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated README with Average: {stats_line}")

if __name__ == "__main__":
    update_readme()
