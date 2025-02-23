import csv
import os
from datetime import datetime

def log_action(file_name, action, message, status):
    log_file_path = 'C:/Users/Abdo/projects/templates/Filter/History/Actions/history.csv'
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file_name, action, message, status, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

def load_emails(file_path):
    emails = set()
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            emails.add(row[0].strip())
    return emails

def find_similar_emails(file_path1, file_path2, output_path):
    # Charger les emails des deux fichiers
    emails1 = load_emails(file_path1)
    emails2 = load_emails(file_path2)

    # Trouver les emails similaires
    similar_emails = emails1.intersection(emails2)

    # Enregistrer les emails similaires dans un fichier CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    file_exists = os.path.isfile(output_path)
    with open(output_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Email'])  # Header
        for email in similar_emails:
            writer.writerow([email])

    # Log action
    message = f"S=  : {len(similar_emails)}"
    log_action(f"{os.path.basename(file_path1)} & {os.path.basename(file_path2)}", 'FindSimilaire', message, os.path.basename(os.path.dirname(output_path)))

    return similar_emails

# Exemple d'utilisation
file_name1 = input("File 1 name ? : ")
file_path1 = f'C:/Users/Abdo/projects/templates/Filter/{file_name1}.csv'
file_name2 = input("Trash/ File 2 name ? : ")
file_path2 = f'C:/Users/Abdo/projects/templates/Filter/History/Trash/{file_name2}.csv'
output_path = f'C:/Users/Abdo/projects/templates/Filter/History/Duplicate/{file_name1}Du.csv'

similar_emails = find_similar_emails(file_path1, file_path2, output_path)

# Afficher les emails similaires
print("Emails similaires :")
for email in similar_emails:
    print(email)