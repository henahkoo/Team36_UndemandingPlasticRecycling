def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print("Number of lines in text_not detected file: ",file_len('text_not_detected.txt'))
print("Number of lines in text_detected file: ",file_len('text_detected.txt'))
