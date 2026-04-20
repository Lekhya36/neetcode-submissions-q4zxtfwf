class Solution:
    def numUniqueEmails(self, emails):
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            normalized = local + '@' + domain
            unique_emails.add(normalized)

        return len(unique_emails)