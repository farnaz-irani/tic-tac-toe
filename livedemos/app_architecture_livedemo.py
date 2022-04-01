task_list = []


def part_of_day(part_of_day_dict):
    # access a global variable
    global task_list

    for key, values in part_of_day_dict.items():
        info = key
        tasks = values
        
    var_morning = input(info + ' - Use "yes" or "no" to answer.')
    if var_morning == 'yes':
        task = '- ' + tasks[0]
    else:
        task = '- ' + tasks[1]
    task_list.append(task)
    
def to_do_complex3(morning_dict, midday_dict, evening_dict):
    part_of_day(morning_dict)
    part_of_day(midday_dict)
    part_of_day(evening_dict)
    print('*'*60)
    print(*task_list, sep='\n')
    print('*'*60)


if __name__ == "__main__":
    morning_dict = {'Good morning. Is it a working day?': ['Go to work', 'Get a newspaper']}
    midday_dict = {'Good day. Are you really hungry?': ['Prepare a meal', 'Get some yoghurt']}
    evening_dict = {'Good evening. Are you going to work tomorrow?': ['Choose a good night book', 'Invite friends for a party']}

    to_do_complex3(morning_dict, midday_dict, evening_dict)


