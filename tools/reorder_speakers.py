import re

approved_order = [
    # 1. White Foreign Women & 2. Foreign Women
    "Marica Amadeo",
    
    # 3. Indian Women
    "Samiya Khan",
    
    # 4. Foreign Male
    "Keith Sherringham",
    "Giuseppe Ciaburro",
    "R.M. Chandima Ratnayake",
    "Yu-Chen Hu",
    "Dr. Ayodeji Olalekan Salau",
    "Muhammad Imran",
    "Dr Ganesh Kumar",
    # (USA-based Indians)
    "Biren (Brian) Prasad",
    "Rajesh Ranjan",
    "Dr. Arkadeep Mitra",
    "Vijayent Kohli",
    "Mohamed Hammad",
    
    # 5. Indian Male
    "SK Hafizul Islam",
    "Neil Harwani"
]

with open('speakers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The speakers list is inside `<div class="grid grid--3">`
# Let's find the container block.
start_marker = '<div class="grid grid--3">'
end_marker = '<!-- ======= Tracks Section ======= -->' # Just to be safe, find the end of speakers section

start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find start marker.")
    exit(1)

# Find the end of the grid div (not strictly necessary if we just split by `<article`)
# Let's use the same robust parsing as before
pre_blocks = content[:start_idx + len(start_marker)]
post_blocks = content[start_idx + len(start_marker):]

blocks = post_blocks.split('<article class="person')

pre_speakers = pre_blocks + blocks[0] # Anything before the first article

speaker_blocks = {}
remaining_blocks = []

for i in range(1, len(blocks)):
    block = '<article class="person' + blocks[i]
    
    # Extract the name to map it
    name_match = re.search(r'<p class="person__name">([^<]+)</p>', block)
    if name_match:
        name = name_match.group(1).strip()
        speaker_blocks[name] = block
    else:
        # If it doesn't have a name, keep it as is (shouldn't happen)
        remaining_blocks.append(block)

if len(speaker_blocks) != len(approved_order):
    print(f"Warning: Found {len(speaker_blocks)} speakers, but expected {len(approved_order)}")
    print("Found names:", list(speaker_blocks.keys()))

new_html = pre_speakers

# Add in sorted order
for name in approved_order:
    if name in speaker_blocks:
        new_html += speaker_blocks[name]
    else:
        print(f"Error: Could not find block for {name}")

# There is a closing div or other content after the last speaker?
# Actually, the last split block has the trailing HTML of the file!
# Wait! `blocks[-1]` contains the last speaker PLUS all the remaining HTML up to the end of the file.
# We need to separate the last speaker from the trailing HTML!
last_block_content = blocks[-1]
# The speaker block ends with `</article>`.
end_article_idx = last_block_content.find('</article>') + len('</article>')
last_speaker = '<article class="person' + last_block_content[:end_article_idx]
trailing_html = last_block_content[end_article_idx:]

# Let's fix the dictionary to only contain the speaker HTML
for name, block in speaker_blocks.items():
    end_idx = block.find('</article>') + len('</article>')
    speaker_blocks[name] = block[:end_idx]

# Re-build the sorted HTML
new_html = pre_speakers
for name in approved_order:
    if name in speaker_blocks:
        new_html += "\n      " + speaker_blocks[name].strip()
    else:
        print(f"Error: Could not find block for {name}")

new_html += trailing_html

with open('speakers.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Speakers rearranged successfully.")

