import GeneratorModul1 as mod

id_num = input("Please give me your id number: \n\t")
state = mod.id_checker(id_num)
while state == False:
    id_num = input("Please give me your id number: \n\t")
    state = mod.id_checker(id_num)

while True:

    prod_link = input("Please give me a link to the product you're interested in:\n")

    link_seg = mod.segmentation(prod_link)
    link_seg = mod.unnecessary_seg_del(link_seg)
    case = mod.site_recognision(link_seg)
    final_trans = mod.transformation(link_seg, case, id_num)

    result = '/'.join(final_trans)
    with open('createdlinks.txt', 'a+') as f:
        f.write(result)
        f.write("\n")

    print("\nCopy and use this link:\n", result)

    answer = mod.run_again()
    if answer == 'y':
        continue
    else:
        print('Goodbye!')
        break


