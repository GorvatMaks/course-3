def print_info(**data):
    for key in data:
        print('Послуга –',key,', ціна –',data[key])
print_info(stories=100,management=1000)