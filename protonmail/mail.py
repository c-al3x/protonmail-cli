"""
A mail model, used for storing and printing loaded emails
"""
class Mail:
    def __init__(self, subject, time_received, mail, body):
        self.subject = subject
        self.time_received = time_received
        self.mail = mail
        self.body = body

    def __str__(self):
        """
        Mail string representation
        """
        res = "Date: %s\n" % self.time_received
        res += "From: %s\n" % self.mail
        res += "Subject: %s\n" % self.subject
        res += "Body: %s\n" % self.body
        return res
