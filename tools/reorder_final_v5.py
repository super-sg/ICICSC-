import re

adv_order = [
    # 1. White Foreign Women
    "Dr. Rania Lampou",
    "Ivanna Dronyuk",
    "Pinar Demircioglu",
    
    # 2. Foreign Women
    "NUR AZALIAH ABU BAKAR",
    
    # 3. Indian Women
    
    # 4. Foreign Male
    "Rolando Herrero",
    "Sérgio Duarte Correia",
    "Vinícius Lima",
    "Muhannmad Ajmal Azad",
    "Fernando Ortiz-Rodríguez",
    "Faisal Nabi",
    "Muhamad Fazil Ahmad",
    "Oloruntoyin Sefiu Taiwo",
    "Noor Zaman Jhanjhi",
    "Inam Ullah",
    "Cun Ji",
    "Mohammed Edan AlKhazraje",
    "Gautam Srivastava",
    "Dr. Ismail Adaramola Abdul Azeez",
    "Muhammad Bilal",
    "Alaa Abdulhady Jaber",
    "Tariq Saeed Mian",
    "Mohd Anas Wajid",
    
    # 5. Indian Male
]

tech_order = [
    # 1. White Foreign Women
    
    # 2. Foreign Women
    "Ilham Laabab",
    
    # 3. Indian Women
    "Prof. Anuja Arora",
    "Dr. Saroj Koul",
    "Dr. Kingsy Grace R",
    "Dr. Manvi Breja",
    "Dr. Renu Mishra",
    "Dr. K. Lakshmi",
    "Ekta Maini",
    "Shriya Misra",
    
    # 4. Foreign Male
    "Kevin M. Rivera, Ph.D.",
    "Mehmet Recep Bozkurt",
    "HENRY CHIMA Chima UKWUOMA",
    "Prof Dr Arab Naz",
    "Qasem Abu Al-Haija",
    
    # 5. Indian Male
    "Prof. Sumit Gupta",
    "Dr. Velayudham",
    "Dr. Gouri Sankar",
    "Dr. Bal Krishna Saraswat",
    "Dr. Amit Seth",
    "Dr. R. Manikandan",
    "Dr. Avijit Kumar Chaudhuri",
    "Dr. Nishant Doshi",
    "Dr. Amit Sharma",
    "Sannasi Chakravarthy S R",
    "Janmenjoy Nayak",
    "Mr. Ashish Kumar",
]

with open('committee.html', 'r', encoding='utf-8') as f:
    content = f.read()

def process_section(start_regex, end_regex, approved_order):
    start_match = re.search(start_regex, content)
    if not start_match:
        print("Not found start.")
        return None, None, None
    
    start_idx = start_match.end()
    sub = content[start_idx:]
    
    end_match = re.search(end_regex, sub)
    if not end_match:
        print("Not found end.")
        return None, None, None
    
    end_idx = start_idx + end_match.start()
    
    section_content = content[start_idx:end_idx]
    
    blocks = section_content.split('<div class="person">')
    
    pre_speakers = blocks[0]
    
    person_htmls_by_name = {}
    trailing_htmls = []
    
    for i in range(1, len(blocks)):
        block = '<div class="person">' + blocks[i]
        
        # The first occurrence of </div>\s*</div> marks the end of the person block
        match = re.search(r'</div>\s*</div>', block)
        if match:
            split_idx = match.end()
            p_html = block[:split_idx]
            t_html = block[split_idx:]
        else:
            print("Warning: could not find end of person block")
            p_html = block
            t_html = ""
            
        trailing_htmls.append(t_html)
        
        name_match = re.search(r'<p class="person__name">([^<]+)</p>', p_html)
        if name_match:
            name = name_match.group(1).strip()
            if name not in person_htmls_by_name:
                person_htmls_by_name[name] = []
            person_htmls_by_name[name].append(p_html)
        else:
            print("Warning: could not find name in block")
            person_htmls_by_name["UNKNOWN_" + str(i)] = [p_html]

    # Reorder the person HTMLs
    ordered_p_htmls = []
    for name in approved_order:
        if name in person_htmls_by_name and len(person_htmls_by_name[name]) > 0:
            ordered_p_htmls.append(person_htmls_by_name[name].pop(0))
        else:
            print(f"Error: Could not find block for {name}")

    # Add any remaining unmapped blocks
    for name, blks in person_htmls_by_name.items():
        for b in blks:
            print(f"Warning: {name} was not in approved list.")
            ordered_p_htmls.append(b)
            
    # Combine the reordered person HTMLs with the original trailing HTMLs!
    new_html = pre_speakers
    for i in range(len(ordered_p_htmls)):
        new_html += ordered_p_htmls[i] + trailing_htmls[i]
        
    return start_idx, end_idx, new_html


# Technical Program Committee is later in the file
t_start, t_end, t_new = process_section(r'>Technical Program Committee members</h3>', r'<h3[^>]*>Publicity Chairs</h3>', tech_order)

if t_start:
    content = content[:t_start] + t_new + content[t_end:]

# International Advisory Committee is earlier
i_start, i_end, i_new = process_section(r'>International Advisory Committee</h3>', r'<h3[^>]*>National Advisory Committee</h3>', adv_order)

if i_start:
    content = content[:i_start] + i_new + content[i_end:]


with open('committee.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Committees rearranged successfully.")
