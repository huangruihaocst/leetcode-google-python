class Solution:
    
    @staticmethod
    def formalize(email):
        local, domain = email.split('@')
        local = local.split('+')[0]
        local = local.replace('.', '')
        return local + '@' + domain
    
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            s.add(self.formalize(email))
        return len(s)
