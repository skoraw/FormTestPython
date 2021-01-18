import string
import random


class TestData:
    name = "CloudServices Test"
    topic = "Rozliczenie"
    text = "automat test CloudServices"

    @staticmethod
    def makeEmail():
        extensions = ['com', 'net', 'org', 'gov']
        domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']

        winext = extensions[random.randint(0, len(extensions) - 1)]
        windom = domains[random.randint(0, len(domains) - 1)]

        acclen = random.randint(1, 20)

        winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

        generated_email = winacc + "@" + windom + "." + winext
        return generated_email
