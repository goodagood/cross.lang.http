

def main(json_data = {}):
    if 'ask4' not in json_data:
        json_data['error'] = 'what is "ask4"? what is "ask for" from input?'
        return json_data

    output = dict(
            answer = 4,
            reason = '2x2=4',
            byTheWay = 'I am using Python to answer, ok?'
            )
    return output
