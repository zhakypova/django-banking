import datetime
import random
from banking.models import Client, Account, Credit

client1 = Client(name='Berdiev N.D.', birth_year=1994, work_place='Codify')
# client1.save()
client2 = Client(name='Zhakypova Z.Zh.', birth_year=1998, work_place='-')
# client2.save()


account_1 = Account.objects.create(number=random.randrange(10 ** 15, 10 ** 16), client=client1)
account_2 = Account.objects.create(number=random.randrange(10 ** 15, 10 ** 16), client=client1)
account_3 = Account.objects.create(number=random.randrange(10 ** 15, 10 ** 16), client=client2)
account_4 = Account.objects.create(number=random.randrange(10 ** 15, 10 ** 16), client=client2)
# account_1.save()
# account_2.save()
# account_3.save()
# account_4.save()


credit_1 = Credit.objects.create(sum=1000000, account=account_1)
credit_2 = Credit.objects.create(sum=200000, account=account_3)
# credit_1.save()
# credit_2.save()


