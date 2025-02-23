import csv
from io import StringIO

def format_emails_to_csv(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')
    
    # Process the lines
    emails = []
    for line in lines:
        line = line.strip()
        if line:
            # Remove quotation marks if present
            email = line.strip('"')
            emails.append(email)
    
    # Remove duplicates while preserving order
    unique_emails = list(dict.fromkeys(emails))
    
    # Create a CSV string
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Email'])  # Header
    writer.writerows([[email] for email in unique_emails])
    
    return output.getvalue()

# Example usage
input_text = '''
"test1@testsendblaster.com"
"test2@testsendblaster.com"
"mohameds.boufanzi@gmail.com"
"michelnersisyan@gmail.com"
"accompagnement.0524@gmail.com"
"archiprime01@gmail.com"
"youkamdigital@gmail.com"
"responsablerh5@gmail.com"
"bad4i5alid@gmail.com"
"milet1id@gmail.com"
"ali@syndic24.ma"
"rh.epcconline@gmail.com"
"nassimtriki01@gmail.com"
"rh@lgmc-mutandis.com"
"moxecccfd2022@gmail.com"
"erasmusplus@uae.ac.ma"
"imaginette22@gmail.com"
"josephineyolande.immo@gmail.com"
"recrutementurgent012019@gmail.com"
"hanaa@sendatrack.com"
"el.mehdi.sekkouri.alaoui@oracle.com"
"swiqat.ayoub@gmail.com"
"prod.images30@gmail.com"
"recrutement.nextacademy@gmail.com"
"fiscafisca2014@gmail.com"
"sce.recherche.cooperation@encgt.ma"
"kotorisan97@gmail.com"
"s.mamane@epc-projects-maroc.com"
"consultddss@gmail.com"
"contact.youzinsarl@gmail.com"
"corintosarl@gmail.com"
"cooperation@encgt.ma"
"tanger@masertech.ma"
"pharmatng80@gmail.com"
"gtec.info01@gmail.com"
"dalila.kamardine@efrei.net"
"escientifiques@gmail.com"
"torecandidature@gmail.com"
"garecrut@gmail.com"
"recrutement@continuum.ma"
"younesyassine5002@gmail.com"
"contact@atarec.com"
"jdaguerrej@gmail.com"
"jojoux0@gmail.com"
"economie.authentique@gmail.com"
"restoconcept73@gmail.com"
"asmaeelhaddouchi06@gmail.com"
'''

csv_output = format_emails_to_csv(input_text)
print(csv_output)