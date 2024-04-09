import csv
import smtplib, ssl

def send_birthday_emails(sender_address, sender_password, birthdays_file):
    """Sends birthday emails to recipients in the specified CSV file.

    Args:
        sender_address (str): Email address of the sender.
        sender_password (str): Password for the sender's email account.
        birthdays_file (str): Path to the CSV file containing birthday data.
    """

    message_template = """Hi {fname},
I wish you a very Happy Birthday!
I hope you have a great day.

Best,
{your_name}
"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_address, sender_password)

        with open(birthdays_file, 'r') as birthdays:
            reader = csv.reader(birthdays)
            next(reader)  # Skip header row
            for fname, lname, email, dob in reader:
                message = message_template.format(fname=fname, your_name="Your Name")  # Customize signature
                server.sendmail(sender_address, email, message)
                print(f"Sent birthday email to {fname} ({email})")

def manage_birthday_list(birthdays_file):
    """Provides options to add or remove entries from the birthday CSV file.

    Args:
        birthdays_file (str): Path to the CSV file containing birthday data.
    """

    while True:
        choice = input("""
Do you wish to add or remove names from the birthday CSV file?
  - type 'add' to add names
  - type 'remove' to remove names
  - type 'exit' to quit
""")

        if choice.lower() == "add":
            new_data = input("Enter data as first name, last name, email, date of birth (comma-separated): ")
            new_data = new_data.split(",")
            with open(birthdays_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(new_data)
            print("New entry added successfully.")

        elif choice.lower() == "remove":
            removal_name = input("Enter the first name of the person to be removed: ")
            lines = []
            with open(birthdays_file, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0].lower() != removal_name.lower():  # Compare first names (case-insensitive)
                        lines.append(row)
            with open(birthdays_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(lines)
            print(f"Removed entry for {removal_name} (if found).")

        elif choice.lower() == "exit":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sender_address = "your_email@example.com"  # Replace with your actual email address
    sender_password = "your_email_password"  # Replace with your email password (consider app passwords)
    birthdays_file = "birthdays.csv"

    send_birthday_emails(sender_address, sender_password, birthdays_file)
    manage_birthday_list(birthdays_file)

    print("All tasks completed!")
