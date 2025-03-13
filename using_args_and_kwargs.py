def square(*args:list[int]):
    """ a function that computes the square root of numbers"""
    result =  []
    for data in args:
        result.append(data * data)
    return result


print(square(3, 4, 5))


def create_a_sentence(**kwargs: list[str]):
    """a sentence maker"""
    sentence = ''
    for data in kwargs.keys():
        sentence += kwargs[data]
        
    return sentence


print(create_a_sentence(name='Abel', space = ' ', action='flies'))