def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("'Symbol' needs to be a string with a length of 1")
    if (width < 2) or (height < 2):
        raise Exception("'width' and 'height' must be greater or equal to 2")
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

# boxPrint('*', 15, 5)

# import traceback
#
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to error_log.txt')
#
# assert False, 'This is the error message.'

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)

switchLights(market_2nd)
