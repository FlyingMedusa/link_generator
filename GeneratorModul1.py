

def id_checker(id_num):
    if len(id_num) != 5:
        print("Your id needs to have at least 5 digits.")
        return False
    elif id_num.isdigit() == False:
        print("Your id must contain only digits.")
        return False
    else:
        return True


def segmentation(link):
    segments = link.split("/")
    return segments


def unnecessary_seg_del(link_seg):
    while link_seg[-1] == " " or link_seg[-1] == "":
        link_seg.pop(-1)
    last_el = link_seg[-1]
    if last_el[-1] == " ":
        last_el = last_el[:-1]
    link_seg[-1] = last_el
    return link_seg


def site_recognision(link_seg):
    for seg in range(0, len(link_seg)):
        if link_seg[-1] == "helion.pl":
            case = 1
            return case
        elif link_seg[seg] == "helion.pl" and link_seg[seg+1] == "kategorie":
            case = 2
            return case
        elif link_seg[seg] == "helion.pl" and link_seg[seg+1] == "ksiazki":
            case = 3
            return case
        elif link_seg[seg] == "helion.pl" and link_seg[seg+1] == "zakupy":
            case = 4
            return case
    return "page not operated"


def transformation(link_seg,case, id_num):
    index = link_seg.index("helion.pl")
    if case == 1:
        link_seg.insert(index+1, "view")
        link_seg.insert(index + 2, id_num)
        return link_seg
    elif case == 2:
        link_seg.insert(index + 1, "page")
        link_seg.insert(index + 2, id_num)
        return link_seg
    elif case == 3:
        link_seg.pop(index + 1)
        link_seg.insert(index + 1, "view")
        link_seg.insert(index + 2, id_num)
        return link_seg
    elif case == 4:
        link_seg.pop(index + 1)
        link_seg.insert(index + 1, "add")
        link_seg.insert(index + 2, id_num)
        return link_seg


def run_again():
    while True:
        ans = input('\nDo you want to add another page? (y/n): ')
        if ans in ('y', 'n'):
            break
        print('Invalid input.')

    return ans
