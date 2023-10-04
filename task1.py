
def is_unique_algorythm(string:str) -> bool:

    if len(string)>128:
        return False

    char_map = [False]*128

    for char in string:
        val = ord(char)
        if char_map[val]:
            return False
        char_map[val] = True

    return True

is_unique_algorythm("ab")
is_unique_algorythm("aa")
