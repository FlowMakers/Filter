import csv
from io import StringIO

def format_emails_to_csv(file_path):
    # Lire le contenu du fichier
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Process the lines
    emails = []
    for line in lines:
        line = line.strip()
        if line:
            # Extraire l'email de la ligne
            email = line.split(':')[0].strip()
            emails.append(email)
    
    # Remove duplicates while preserving order
    unique_emails = list(dict.fromkeys(emails))
    
    # Create a CSV string
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Email'])  # Header
    writer.writerows([[email] for email in unique_emails])
    
    return output.getvalue()

# Exemple d'utilisation
file_name = input(" File name ? : ")
file_path = f'C:/Users/Abdo/projects/templates/Filter/{file_name}.txt'
csv_output = format_emails_to_csv(file_path)
print(csv_output)

# Enregistrer le résultat dans un fichier CSV
output_csv_path = f'C:/Users/Abdo/projects/templates/Filter/{file_name}.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    csvfile.write(csv_output)