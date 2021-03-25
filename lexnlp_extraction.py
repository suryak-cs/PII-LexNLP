import lexnlp.extract.en.pii

def extract_pii(input_string):
    return list(lexnlp.extract.en.pii.get_pii(input_string))