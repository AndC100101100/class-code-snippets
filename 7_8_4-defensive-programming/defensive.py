def no_negatives(number):
    assert isinstance(number, int), 'non-int value passed to no_negatives()'
    assert number >= 0, 'negative value passed to no_negatives()'
    print(number)

no_negatives(5)
#no_negatives("hello")
#no_negatives("-2")
