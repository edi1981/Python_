def remove_empty_lines():
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open("D:/Users/pbutkowski/Desktop/Programowanie/Python/Python/Pliki_txt/words.txt", 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()
remove_empty_lines()