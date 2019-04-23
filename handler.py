import encoder

def handle_encode_single(input_num):
    return encoder.encode(input_num)

def handle_decode_single(input_num):
    return encoder.decode(input_num)

def handle_encode(request):
    file = request.files["encoder_input"]
    lines = file.read()
    nums = [int(l) for l in lines.split()]
    return [(n, encoder.encode(n)) for n in nums]

def handle_decode(request):
    file = request.files["decoder_input"]
    lines = file.read()
    return [(l.decode(), encoder.decode(l)) for l in lines.split()]
