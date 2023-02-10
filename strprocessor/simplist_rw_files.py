with open("oldfile.txt", encoding="utf-8") as fr, open(
    "newfile", "w", encoding="utf8"
) as fw:
    # 1 read
    # read line by line?
    for ln in fr:
        # 2 filter logic, like eliminating empty lines
        if ln.strip():
            # 3 write
            fw.write(ln)
