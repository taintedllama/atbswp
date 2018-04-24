import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 3 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

print(phoneRegex.findall(r'''Hi you have reached Tom and my mobile number is (612) 618-1843,
    and my work number is 612-977-6426.'''))