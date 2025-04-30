from users.models import Support


def create_support_request(email, text):

    Support.objects.create(mail=email, text=text)