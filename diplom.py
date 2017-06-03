import requests
import json
import config

config.get_params()


def print_process():
    """Показ процесса работы"""
    print('.', end='', flush=True)


def make_request(method, params):
    """Отправка запроса"""
    url = "{}/{}".format(config.VK_API_ENDPOINT, method)
    print_process()
    while True:
        try:
            response = requests.get(url, params)
            response_list = response.json()
            response_list['response']
            break
        except KeyError:
            pass
    return response_list


def get_users_is_members(params, friends_list):
    """Является ли пользователь из списка друзей подписчиком группы"""
    final_list = []
    for i in range(0, len(friends_list), 250):
        params['user_ids'] = ", ".join([str(i) for i in friends_list[i:i+250]])
        members = make_request('groups.isMember', params)
        [final_list.append(member) for member in members['response']]
    return final_list


def get_group_without_user_friends(params, groups_list, friends_list):
    """Является ли пользователь из списка друзей подписчиком группы"""
    user_is_along = []
    for group in groups_list['response']['items']:
        params['group_id'] = group['id']
        params['user_ids'] = ", ".join([str(i) for i in friends_list])
        members_group = get_users_is_members(params, friends_list)
        flag = False
        for member in members_group:
            if member['member'] == 1:
                flag = True
                break
        if not flag:
            params['group_id'] = group['id']
            str_dict = {'name': group['name'], 'gid': group['id'],
                        'members_count': make_request('groups.getMembers',
                                                      params)['response']['count']}
            user_is_along.append(str_dict)
    return user_is_along


def save_json(data):
    """Сохранение файла в json"""
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print("The size of the saved file: {}".format(len(data)))


def main():
    params = config.get_params()
    params['user_id'] = int(input("Enter id user: "))
    friends_list = make_request('friends.get', params)["response"]["items"]
    params['extended'] = 1
    groups_list = make_request('groups.get', params)
    data = get_group_without_user_friends(params, groups_list, friends_list)
    save_json(data)


if __name__ == '__main__':
    main()