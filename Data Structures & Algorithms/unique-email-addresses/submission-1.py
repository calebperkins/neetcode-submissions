class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.replace(".", "")
            split = name.split("+")
            if len(split) >= 2:
                name = split[0]
            unique.add(f"{name}@{domain}")
        return len(unique)
