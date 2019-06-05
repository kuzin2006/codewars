def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - h*3600) // 60
    s = seconds - h*3600 - m*60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)

print(make_readable(359999))