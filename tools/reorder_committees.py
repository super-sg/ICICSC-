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
    "Dr. Amrita",
    "Dr. Saroj Koul",
    "Dr. Kingsy Grace R",
    "Dr. Manvi Breja",
    "Dr. Renu Mishra",
    "Dr. Y. Sucharitha",
    "Dr. Jyoti Gautam",
    "Dr. Shelja Sharma",
    "Dr. K. Lakshmi",
    "Dr. Saptadeepa Kalita",
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
    "Prof. Dr. Ambuj Agarwal",
    "Dr. Velayudham",
    "Dr. Gouri Sankar",
    "Dr. Bal Krishna Saraswat",
    "Dr. Amit Seth",
    "Dr. Avinash Kumar Sharma",
    "Dr. Manmohan Yadav",
    "Dr. Gaurav Raj",
    "Dr. Mayank Goyal",
    "Dr. Rohit Sachan",
    "Dr. Abhishek Verma",
    "Dr. R. Manikandan",
    "Dr. Avijit Kumar Chaudhuri",
    "Dr. Nishant Doshi",
    "Dr. Amit Sharma",
    "Dr. Shivam Tiwari",
    "Dr. Sushant Jhingran",
    "Sannasi Chakravarthy S R",
    "Janmenjoy Nayak",
    "Mr. Ashish Kumar",
    "Mr. Ashish Jain",
]

with open('committee.html', 'r', encoding='utf-8') as f:
    content = f.read()

def process_section(start_regex, end_regex, approved_order):
    start_match = re.search(start_regex, content)
    if not start_match:
        print("Not found start.")
        return None, None
    
    start_idx = start_match.end()
    sub = content[start_idx:]
    
    end_match = re.search(end_regex, sub)
    if not end_match:
        print("Not found end.")
        return None, None
    
    end_idx = start_idx + end_match.start()
    
    section_content = content[start_idx:end_idx]
    
    blocks = section_content.split('<div class="person">')
    
    pre_speakers = blocks[0]
    
    speaker_blocks = {}
    remaining_blocks = []
    
    for i in range(1, len(blocks)):
        block = '<div class="person">' + blocks[i]
        
        name_match = re.search(r'<p class="person__name">([^<]+)</p>', block)
        if name_match:
            name = name_match.group(1).strip()
            # Handle duplicates if any by making a list
            if name not in speaker_blocks:
                speaker_blocks[name] = []
            speaker_blocks[name].append(block)
        else:
            remaining_blocks.append(block)
    
    new_html = pre_speakers
    
    processed_names = {}
    for name in approved_order:
        if name in speaker_blocks and len(speaker_blocks[name]) > 0:
            new_html += "\n                " + speaker_blocks[name].pop(0).strip()
        else:
            print(f"Error: Could not find block for {name}")

    # Append any remaining unmapped blocks just in case
    for name, blks in speaker_blocks.items():
        for b in blks:
            print(f"Warning: {name} was not in approved list.")
            new_html += "\n                " + b.strip()
            
    for b in remaining_blocks:
        new_html += "\n                " + b.strip()
        
    return start_idx, end_idx, new_html


# We must do this from back to front so indices don't shift!
# Technical Program Committee is later in the file
t_start, t_end, t_new = process_section(r'>Technical Program Committee members</h3>', r'</section>', tech_order)

if t_start:
    content = content[:t_start] + t_new + content[t_end:]

# International Advisory Committee is earlier
i_start, i_end, i_new = process_section(r'>International Advisory Committee</h3>', r'>National Advisory Committee</h3>', adv_order)

if i_start:
    content = content[:i_start] + i_new + content[i_end:]


with open('committee.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Committees rearranged successfully.")
