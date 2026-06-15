with open(r"C:\Users\jyosh\Onedrive\Deskto\p2p_file_sharing\peer\myfile.txt", "rb") as f:
    data = f.read()
    print(len(data))  # This tells you how many bytes your file has