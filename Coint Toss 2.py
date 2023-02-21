import CoinClass as c

def ShowCoinStatus(coin_obj):
    print('This side is up: ' + str(coin_obj.get_sideup()))
          
def flip(coin_obj):
    coin_obj.toss()

my_coin = c.Coin()

ShowCoinStatus(my_coin)
x=0
while x < 10:
    flip(my_coin)
    ShowCoinStatus(my_coin)
    x+=1