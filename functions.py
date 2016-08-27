#functions for signup pages
import cgi

#email
def valid_email(text):
    answer= ""
    if "@" in text and ".com" in text:
            answer = text
    return answer

#username
def valid_user(text):
    answer=""
    if " " not in text and text != answer:
        answer = text
    return answer

#password
def valid_password(text):
    answer=""
    if text != answer:
        answer = text
    return answer

#strings
def sub(text):
    f = "Welcome, %s!"
    return f % text
#escaping html
def escape(text):
    return cgi.escape(text, quote=True)
