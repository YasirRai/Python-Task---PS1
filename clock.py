

h = 12               # Hour loop
while h <= 12:
    h_str = ("hour========================")
    print(h, h_str.upper())

    m = 1
    while m <= 60:          # Minutes loop
        print("=============", m, "Minutes ===========")
        m = m+1
    s = 1
    while s <= 60:              # Seconds loop
        print("=============Seconds ===========", s)
        s = s+1

    h = h+1
