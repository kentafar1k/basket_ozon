'''
яблоко = 50
банан = 40
апельсин = 20

скидки:
1 место - яблоко+банан = 70
2 место - яблоко+яблоко+яблоко = 130
3 место - яблоко+яблоко = 90
'''



import HelloWorld
from cart import total


def test_hello_world():
    assert 'Hello World!' == HelloWorld.hello_world()


def test_empty_cart_total_is_zero():
    assert total({}, {}) == 0
