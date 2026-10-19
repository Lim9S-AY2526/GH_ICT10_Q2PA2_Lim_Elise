# Working with Sets: Student Club Members
from pyscript import display, document, HTML

# Predefined sets 
grade_7 = {'Boyet Buhok', 'Junjun Pancit', 'Totoy Tokwa', 'Kikay Kaboom'}
grade_8 = {'Mang Kurot', 'Neneng Noodles', 'Lito Lollipop', 'Bibo Banana'}
grade_9 = {'Tita Tickle', 'Dodong Donut', 'Pogi Pansit', 'Chika Chops'}
grade_10 = {'Nene Nachos', 'Kuya Ketchup', 'Biboy Bubble'}

def add_member(e):
    # Clearing output box before displaying new result
    document.getElementById('output-container').innerHTML = ''
    
    # Collecting inputs from text boxes
    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()
    
    # Concateneting inputs into full name
    full_name = f"{first_name} {last_name}".strip()
    
    # Storing new member inside the set
    new_member = {full_name}
    
    # Combining predefined grade sets and new member set
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member
    
    # Sorting set alphabetically
    sorted_members = sorted(master_set)
    members_list = "<br>".join(sorted_members)
    
    # Calculating total members 
    total_count = len(master_set)
    
    # Formatting result string 
    result_text = f"All members:<br>{members_list}<br>Total members: {total_count}"

    display(HTML(result_text), target='output-container')