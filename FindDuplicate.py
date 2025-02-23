import csv
import os
from datetime import datetime

def log_action(file_name, action, message, status):
    log_file_path = 'C:/Users/Abdo/projects/templates/Filter/History/Actions/history.csv'
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([file_name, action, message, status, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])

def find_duplicate_emails(file_path, output_path):
    email_count = {}
    duplicates = {}

    # Lire le fichier CSV
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email = row[0].strip()
            if email in email_count:
                email_count[email] += 1
            else:
                email_count[email] = 1

    # Trouver les emails en double
    for email, count in email_count.items():
        if count > 1:
            duplicates[email] = count

    # Enregistrer les emails en double dans un fichier CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email', 'TD={total_repetitions}'])  # Header
        for email, count in duplicates.items():
            writer.writerow([email, count])

    # Calculer la somme des répétitions
    total_repetitions = sum(duplicates.values())
    print("Total des répétitions :", total_repetitions)

    # Log action
    message = f"DU={len(duplicates)} / TD={total_repetitions}"
    log_action(os.path.basename(file_path), 'FindDuplicate', message, os.path.basename(os.path.dirname(output_path)))

    return duplicates

# Exemple d'utilisation
file_name = input(" File name ? : ")
file_path = f'C:/Users/Abdo/projects/templates/Filter/{file_name}.csv'
output_path = f'C:/Users/Abdo/projects/templates/Filter/History/Duplicate/{file_name}Du.csv'

duplicates = find_duplicate_emails(file_path, output_path)

# Afficher les emails en double et leurs comptes
print("Emails en double :")
for email, count in duplicates.items():
    print(f"{email} : {count}")