import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

path = "registration.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the table inside .table-scroll
table_html = """<div class="table-scroll">
      <table class="data">
        <caption>Registration fees — Indian delegates (INR) and foreign delegates (USD)</caption>
        <thead>
          <tr>
            <th rowspan="2" scope="col">Category</th>
            <th colspan="2" scope="colgroup">India — INR</th>
            <th colspan="2" scope="colgroup">Foreign — USD</th>
            <th rowspan="2" scope="col">Presents a paper</th>
          </tr>
          <tr>
            <th scope="col">Early bird<br><span class="small">until 25 Apr 2027</span></th>
            <th scope="col">Standard<br><span class="small">until 15 May 2027</span></th>
            <th scope="col">Early bird<br><span class="small">until 25 Apr 2027</span></th>
            <th scope="col">Standard<br><span class="small">until 15 May 2027</span></th>
          </tr>
        </thead>
        <tbody>
          <tr><td><strong>Attendee / listener</strong><br><span class="small muted">No paper presentation</span></td><td class="num">₹3,125</td><td class="num">₹3,125</td><td class="num">US$65</td><td class="num">US$65</td><td>No</td></tr>
          <tr><td><strong>Research scholar / student</strong><br><span class="small muted">Valid institutional ID required</span></td><td class="num">₹7,500</td><td class="num">₹8,125</td><td class="num">US$100</td><td class="num">US$125</td><td>Yes</td></tr>
          <tr><td><strong>Academician / faculty</strong></td><td class="num">₹8,750</td><td class="num">₹9,375</td><td class="num">US$125</td><td class="num">US$155</td><td>Yes</td></tr>
          <tr><td><strong>Industry / corporate</strong></td><td class="num">₹9,375</td><td class="num">₹10,000</td><td class="num">US$125</td><td class="num">US$155</td><td>Yes</td></tr>
        </tbody>
        <tfoot><tr><td colspan="6">Fees reflect the revised structure and are subject to confirmation by the organising committee. GST and other applicable taxes are extra where levied on Indian payments. Delegates from SAARC and low-income economies may request concessional consideration by writing to the organising secretariat with proof of affiliation.</td></tr></tfoot>
      </table>
    </div>"""

content = re.sub(r'<div class="table-scroll">.*?</div>\s*</div>\s*</section>', table_html + '\n  </div>\n</section>', content, flags=re.DOTALL)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("registration.html updated successfully.")
