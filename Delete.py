import csv
import os
import shutil
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

def remove_duplicate_emails(main_file_path, duplicates_file_path, output_file_path):
    # Charger les emails en double
    duplicate_emails = load_emails(duplicates_file_path)

    # Lire les emails de la liste principale et filtrer les doublons
    filtered_emails = []
    original_emails_count = 0
    with open(main_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            email = row[0].strip()
            original_emails_count += 1
            if email not in duplicate_emails:
                filtered_emails.append(email)

    # Enregistrer la liste filtrée dans un nouveau fichier CSV
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email'])  # Header
        for email in filtered_emails:
            writer.writerow([email])

    # Calculer le nombre d'emails supprimés
    removed_emails_count = original_emails_count - len(filtered_emails)

    # Log action
    message = f"D={removed_emails_count}"
    log_action(os.path.basename(main_file_path), 'DELETE', message, os.path.basename(os.path.dirname(output_file_path)))

    # Déplacer le fichier original vers le dossier Trash
    trash_path = f'C:/Users/Abdo/projects/templates/Filter/History/Trash/{os.path.basename(main_file_path)}'
    os.makedirs(os.path.dirname(trash_path), exist_ok=True)
    shutil.move(main_file_path, trash_path)

    return removed_emails_count

# If you want to delete similaire put filenameDu
main_file_name = input(" File of main List ? (if its for similaire : nameDu): ")
main_file_path = f'C:/Users/Abdo/projects/templates/Filter/{main_file_name}.csv'
duplicates_file_path = f'C:/Users/Abdo/projects/templates/Filter/History/Duplicate/{main_file_name}Du.csv'
output_file_path = f'C:/Users/Abdo/projects/templates/Filter/History/Filtred/{main_file_name}Fi.csv'

removed_emails_count = remove_duplicate_emails(main_file_path, duplicates_file_path, output_file_path)
print(f"Les emails en double ont été supprimés et la liste filtrée a été enregistrée dans {main_file_name}Fi . Nombre d'emails supprimés : {removed_emails_count}")