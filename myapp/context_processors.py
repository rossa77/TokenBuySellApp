from .models import Account
import requests
def balance(request):
    balance = 0
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)
        balance = user.balance
    return {'balance': balance}

def token(request):
    token = 0
    if request.user.is_authenticated:
        user = Account.objects.get(email=request.user.email)
        address = user. wallet_address
        url = 'https://api-sepolia.etherscan.io/api'
        params = {
            'module': 'account',
            'action': 'tokenbalance',
            'contractaddress': '0xa7d1Ca330Df16a5D3f898014Ff3910448FC94660', 
            'address': address,
            'tag':'latest',
            'apikey': 'Y78GHU6BV8C738419TXXDIJB7E7BX7P327', 
           }
        response = requests.get(url, params=params)
        data = response.json()
        token=data['result']
    return {'token': token}
