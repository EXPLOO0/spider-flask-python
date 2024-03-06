import re

input_string = "https://img13.360buyimg.com/n5/s54x54_jfs/t1/185271/5/19964/128125/611cdf50Ee3cfe4ce/63d788eab3a382c0.jpg.avif"

pattern = r'^.*?(?=_jfs/t1)'

change_string = 'https://img30.360buyimg.com/shaidan/s616x405'

# Perform the replacement
output_string = re.sub(pattern, change_string, input_string)

# Output the result
print(output_string)
