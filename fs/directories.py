import os
import glob

def there_is_a_subdirectory(dir):
    pattern = os.path.join(dir, '*')
    for candidate in glob.glob(pattern):
        if os.path.isdir(candidate):
            #print("{0} is a directory".format(candidate))
            return True
    return False

def there_is_a_flac(dir):
    pattern = os.path.join(dir, '*.flac')
    for candidate in glob.glob(pattern):
        if os.path.isfile(candidate):
            return True
    return False

def this_is_an_artist(dir):
    pattern = os.path.join(dir, '*')
    for candidate in glob.glob(pattern):
        if this_is_an_album(candidate):
            return True
    return False

def this_is_an_album(dir):
    if there_is_a_subdirectory(dir):
        return False
    elif there_is_a_flac(dir):
        return True
    else:
        return False

def get_album_list(dir):
    if this_is_an_artist(dir):
        album_list = []
        pattern = os.path.join(dir, '*')
        for candidate in glob.glob(pattern):
            if this_is_an_album(candidate):
                album_list.append(os.path.basename(candidate))
    return album_list