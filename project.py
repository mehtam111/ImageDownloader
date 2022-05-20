def image(keyword):
    with open("keyword.txt", "w") as f:
        f.write(keyword)


keyword = "coffee"
image(keyword)
