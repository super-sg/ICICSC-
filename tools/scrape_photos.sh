#!/bin/bash
# Script to download all missing committee member photos
DIR="/Users/supersg/Documents/Random Projects/ICNGCI Conference Site/assets/img/people"

download() {
  local url="$1"
  local name="$2"
  if [ -f "$DIR/$name" ]; then
    echo "SKIP (exists): $name"
    return
  fi
  echo "Downloading: $name"
  curl -L -o "$DIR/$name" "$url" --max-time 30 -s -f -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
  if [ $? -eq 0 ] && [ -s "$DIR/$name" ]; then
    echo "  OK: $name ($(wc -c < "$DIR/$name") bytes)"
  else
    echo "  FAIL: $name"
    rm -f "$DIR/$name"
  fi
}

echo "=== Downloading committee member photos ==="
echo ""

# 1. Dr. Narayan Debnath - from EIU profile (og:image)
download "https://eiu.edu.vn/wp-content/uploads/2025/05/Narayan-Chandra-Debnath.jpg" "narayan-debnath.jpg"

# 2. Prof. Bhuvanesh Unhelkar - from USF
download "https://www.usf.edu/business/images/about/headshots/unhelkar-bhuvanesh-100x100.jpg" "bhuvanesh-unhelkar.jpg"

# 3. Dr. Smrity Dwivedi - from IIT BHU
download "https://www.iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-04/1602865214764.jpg.webp?itok=n9oq9i67" "smrity-dwivedi.webp"

# 4. Dr. R. Mahanty - from IIT BHU  
download "https://www.iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-04/RM_sir-removebg-preview%20-%20Copy%20-%20Copy.png.webp?itok=pZ4Z7z-_" "r-mahanty.webp"

# 5. Dr. R. K. Saket - from IIT BHU
download "https://www.iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-04/DSC%205154%20SAA_0.jpg.webp?itok=yFwuLkyM" "r-k-saket.webp"

# 6. Prof. N. S. Rajput - from IIT BHU
download "https://iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-06/NSR%20-%20Profile%20Pic%202025%20-%20White%20Background%20-%20Compressed.png.webp?itok=GbLGCYP7" "n-s-rajput.webp"

# 7. Dr. Oppili Prasad L - from IIT BHU
download "https://www.iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-04/2.jpg.webp?itok=bKj_4Bc0" "oppili-prasad.webp"

# 8. Dr. Naveen Yalla - from IIT BHU
download "https://www.iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-04/Nav%20pic.jpeg.webp?itok=T0rnCcSS" "naveen-yalla.webp"

# 9. Prof. Kalpana Chaudhary - from IIT BHU
download "https://www.iitbhu.ac.in/sites/default/files/styles/large/public/pictures/2026-04/RAM_2249._0.jpg.webp?itok=_sznIuGq" "kalpana-chaudhary.webp"

# 10. Dr. D. P. Vidyarthi - from JNU
download "https://www.jnu.ac.in/sites/default/files/styles/medium/public/faculty_images/dpv.png?itok=O0TET7Jh" "d-p-vidyarthi.png"

# 11. Dr. Satish Chand - from JNU
download "https://www.jnu.ac.in/sites/default/files/styles/medium/public/styles/medium/public/schand_0.jpg?itok=Zzgw7rp2" "satish-chand.jpg"

# 12. Prof. (Dr.) Nanhay Singh - from NSUT
download "https://nsut.ac.in/sites/default/files/styles/node_image_/public/2021-07/Capture_4.png?itok=Yb2WJpHT" "nanhay-singh.png"

# 13. Prof. Sushama Nagpal - from NSUT
download "https://www.nsut.ac.in/sites/default/files/styles/node_image_/public/2021-07/sun_1.png?itok=Oq-sTwZd" "sushama-nagpal.png"

echo ""
echo "=== Done with direct downloads ==="
echo ""
echo "Files in people directory:"
ls -la "$DIR/" | tail -30
