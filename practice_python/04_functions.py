sample_text = "Today the S&P 500 had its best performance in ten years"
blacklist = ["had", 'ten years']
replacement = "__"

def word_conv(sample_text):

    out_text = [sample_text.split()]

    for word in out_text:
        if word in blacklist:
            out_text.replace(word,"__")
        else:
            print(sample_text)
    
    return([' '.join(word) for word in out_text])

