def csv_adapter(filename, data):
    with open(filename, 'w') as fp:
        fp.write("Word, Count\n")
        for word, count in data.items():
            fp.write(f"{word}, {count}\n")
