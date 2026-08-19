import smtplib
import imaplib
import time
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass

# ============================================
# CONFIG
# ============================================

EMAIL = "your mail"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Enter securely in terminal
APP_PASSWORD = "XXXX XXXX XXXXX XXXX"

# Receiver
receiver_email = input("Enter receiver email: ")
receiver_name = input("Enter receiver name: ")
company_name = input("Enter company name: ")

# CC Recipients
cc_emails = []
while True:
    cc_input = input("Enter CC email (or space/- to skip): ").strip()
    if cc_input in ["-", "", " "]:
        break
    cc_emails.append(cc_input)

# Subject
SUBJECT = f"Application for Product Internship at {company_name} | Bhuvan Raj Guguloth, IIT Kharagpur"

# Resolve paths relative to the script's directory for maximum reliability
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("\n--- Select Mail Template ---")
print("[1] BlinkMoney (Terminal-themed)")
print("[2] Netflix (Cinematic-themed)")
print("[3] District by Zomato (Vibrant Event-themed)")
print("[4] PocketFM (Audio-themed)")
print("[5] Ownly by Rapido (Food-themed)")
print("[6] Cars24 (Automotive-themed)")
print("[7] Matiks (Brain Games-themed)")
print("[8] Lyzr (Enterprise AI-themed)")
print("[9] Scaler AI Labs (Monochrome-themed)")
print("[10] Convin (Sales Intelligence-themed)")
print("[11] Nosh (AI Robo Chef-themed)")
print("[12] Shapes Inc (Multiplayer AI-themed)")
print("[13] Spinny (Automotive-themed)")
print("[14] Clueso (AI Video/Docs-themed)")
print("[15] Clueso Terminal (Terminal-themed)")
print("[16] Plivo Terminal (Terminal-themed)")
print("[17] Cars24 Terminal (Terminal-themed)")
print("[18] Vapi Terminal (Terminal-themed)")
print("[19] Mem0 Terminal (Terminal-themed)")
print("[20] Mudrex Terminal (Terminal-themed)")
template_choice = input("Enter choice (1-20, default: 14): ").strip()

if template_choice == "1":
    HTML_FILE = os.path.join(SCRIPT_DIR, "blinkmoney.html")
    print("[INFO] Selected: BlinkMoney (Terminal)")
elif template_choice == "2":
    HTML_FILE = os.path.join(SCRIPT_DIR, "netflix.html")
    print("[INFO] Selected: Netflix (Cinematic)")
elif template_choice == "3":
    HTML_FILE = os.path.join(SCRIPT_DIR, "district.html")
    print("[INFO] Selected: District by Zomato (Vibrant)")
elif template_choice == "4":
    HTML_FILE = os.path.join(SCRIPT_DIR, "pocketfm.html")
    print("[INFO] Selected: PocketFM (Audio)")
elif template_choice == "5":
    HTML_FILE = os.path.join(SCRIPT_DIR, "ownly.html")
    print("[INFO] Selected: Ownly by Rapido (Food-themed)")
elif template_choice == "6":
    HTML_FILE = os.path.join(SCRIPT_DIR, "cars24.html")
    print("[INFO] Selected: Cars24 (Automotive-themed)")
elif template_choice == "7":
    HTML_FILE = os.path.join(SCRIPT_DIR, "matiks.html")
    print("[INFO] Selected: Matiks (Brain Games-themed)")
elif template_choice == "8":
    HTML_FILE = os.path.join(SCRIPT_DIR, "lyzr.html")
    print("[INFO] Selected: Lyzr (Enterprise AI-themed)")
elif template_choice == "9":
    HTML_FILE = os.path.join(SCRIPT_DIR, "scaler.html")
    print("[INFO] Selected: Scaler AI Labs (Monochrome-themed)")
elif template_choice == "10":
    HTML_FILE = os.path.join(SCRIPT_DIR, "convin.html")
    print("[INFO] Selected: Convin (Sales Intelligence-themed)")
elif template_choice == "11":
    HTML_FILE = os.path.join(SCRIPT_DIR, "nosh.html")
    print("[INFO] Selected: Nosh (AI Robo Chef-themed)")
elif template_choice == "12":
    HTML_FILE = os.path.join(SCRIPT_DIR, "shapes.html")
    print("[INFO] Selected: Shapes Inc (Multiplayer AI-themed)")
elif template_choice == "13":
    HTML_FILE = os.path.join(SCRIPT_DIR, "spinny.html")
    print("[INFO] Selected: Spinny (Automotive-themed)")
elif template_choice == "14":
    HTML_FILE = os.path.join(SCRIPT_DIR, "clueso.html")
    print("[INFO] Selected: Clueso (AI Video/Docs-themed)")
elif template_choice == "15":
    HTML_FILE = os.path.join(SCRIPT_DIR, "clueso-terminal.html")
    print("[INFO] Selected: Clueso Terminal (Terminal-themed)")
elif template_choice == "16":
    HTML_FILE = os.path.join(SCRIPT_DIR, "plivo-terminal.html")
    print("[INFO] Selected: Plivo Terminal (Terminal-themed)")
elif template_choice == "17":
    HTML_FILE = os.path.join(SCRIPT_DIR, "cars24-terminal.html")
    print("[INFO] Selected: Cars24 Terminal (Terminal-themed)")
elif template_choice == "18":
    HTML_FILE = os.path.join(SCRIPT_DIR, "vapi-terminal.html")
    print("[INFO] Selected: Vapi Terminal (Terminal-themed)")
elif template_choice == "19":
    HTML_FILE = os.path.join(SCRIPT_DIR, "mem0-terminal.html")
    print("[INFO] Selected: Mem0 Terminal (Terminal-themed)")
elif template_choice == "20":
    HTML_FILE = os.path.join(SCRIPT_DIR, "mudrex-terminal.html")
    print("[INFO] Selected: Mudrex Terminal (Terminal-themed)")
else:
    HTML_FILE = os.path.join(SCRIPT_DIR, "clueso.html")
    print("[INFO] Selected: Clueso (AI Video/Docs-themed)")

CV_FILE = os.path.join(SCRIPT_DIR, "Bhuvan_Raj_Guguloth_IITKharagpur.pdf")

# ============================================
# LOAD HTML
# ============================================

with open(HTML_FILE, "r", encoding="utf-8") as file:
    html_content = file.read()

# ============================================
# TRACKING CONFIG
# ============================================
# TRACKING & PERSONALIZATION
import urllib.parse

# Replace this with your NEW Deployed Google Apps Script Web App URL
TRACKING_BASE_URL = "" #custom tracking script
 
# URL Encode all parameters for reliability
params = {
    "email": receiver_email,
    "subject": SUBJECT,
    "company": company_name,
    "cc": ", ".join(cc_emails) if cc_emails else "none"
}
tracking_url = f"{TRACKING_BASE_URL}?{urllib.parse.urlencode(params)}"
pixel_tag = f'<img src="{tracking_url}" width="1" height="1" style="display:none; opacity:0; visibility:hidden;" alt="">'

# Inject into HTML
html_content = html_content.replace("{{tracking_pixel}}", pixel_tag)
html_content = html_content.replace("[Name]", receiver_name)

# ============================================
# CREATE EMAIL
# ============================================

# Prompt to attach CV
attach_cv_input = input("Attach CV (Bhuvan_Raj_Guguloth_IITKharagpur.pdf)? (y/n, default: y): ").strip().lower()
attach_cv = attach_cv_input in ["y", "yes", ""]

# Create the outer mixed container
msg = MIMEMultipart("mixed")

msg["Subject"] = SUBJECT
msg["From"] = EMAIL
msg["To"] = receiver_email
if cc_emails:
    msg["Cc"] = ", ".join(cc_emails)

# Create inner alternative container for body content
msg_body = MIMEMultipart("alternative")

# Plain text fallback
plain_text = f"""
Hey {receiver_name},

Thought sending a normal resume would be boring.
So I built this instead.

- Bhuvan Raj Guguloth
"""

# Attach plain text and HTML to body container
msg_body.attach(MIMEText(plain_text, "plain"))
msg_body.attach(MIMEText(html_content, "html"))

# Attach body to the outer message
msg.attach(msg_body)

# Attach CV file if selected
if attach_cv:
    if os.path.exists(CV_FILE):
        filename = os.path.basename(CV_FILE)
        print(f"[INFO] Attaching CV: {filename}...")
        try:
            with open(CV_FILE, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={filename}",
            )
            msg.attach(part)
            print("[SUCCESS] CV attached successfully.")
        except Exception as attr_error:
            print(f"[ERROR] Failed to attach CV: {attr_error}")
    else:
        print(f"[WARNING] CV file not found at: {CV_FILE}")

# ============================================
# SEND OR SAVE DRAFT
# ============================================

action = input("\nSend email or Save as Draft? (s/d): ").strip().lower()

try:
    if action == 'd':
        print("\n[INFO] Connecting to Gmail IMAP...\n")
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(EMAIL, APP_PASSWORD)
        
        # Save to Drafts
        imap.append("[Gmail]/Drafts", '', imaplib.Time2Internaldate(time.time()), msg.as_bytes())
        imap.logout()
        
        print("[SUCCESS] Email saved to Drafts!")
    else:
        print("\n[INFO] Connecting to Gmail SMTP...\n")

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        server.login(EMAIL, APP_PASSWORD)

        print("[INFO] Logged in successfully.")

        all_recipients = [receiver_email] + cc_emails
        server.sendmail(
            EMAIL,
            all_recipients,
            msg.as_string()
        )

        server.quit()

        print("\n[SUCCESS] HTML email sent successfully!")

except Exception as e:
    print("\n[ERROR] Failed to process email")
    print(e)
