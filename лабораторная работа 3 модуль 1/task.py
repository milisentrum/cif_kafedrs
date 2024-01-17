# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(participants_first_group,
                             participants_second_group, sprtr=','):
    prtcpnts_frst_grp_list = participants_first_group.split(sprtr)
    prtcpnts_scnd_grp_list = participants_second_group.split(sprtr)

    common_prtcpnt = set(prtcpnts_frst_grp_list).intersection(prtcpnts_scnd_grp_list)

    return sorted(list(common_prtcpnt))

print(find_common_participants(participants_first_group, participants_second_group, sprtr='|'))