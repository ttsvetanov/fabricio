
def shell_escape(string):
    for char in ('"', '$', '`'):
        string = string.replace(char, '\%s' % char)
    return string
