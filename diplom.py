import requests
import json
import time
import config

config.get_params()  # Конфигурация парраметров

<<<<<<< HEAD

def print_process():
    """Показ процесса работы"""
    print('.')


def make_request(method, params):
    """Отправка запроса"""
    url = "{}/{}".format(config.VK_API_ENDPOINT, method)
=======
def get_params():
    """Необходимые параметры для запроса."""
    VERSION = '5.64'
    access_token = "d13e692be69592b09fd22c77a590dd34e186e6d696daa88d6d981e1b4e296b14acb377e82dcbc81dc0f22"
    params = {'access_token': access_token,
              'v': VERSION,
              }
    return params


def print_process():
    """Показ процесса работы"""
    print('.')


def make_request(url, params):
    """Отправка запроса"""
>>>>>>> c16104b0de34223ff764f0a74a3171bfe299d087
    print_process()
    while True:
        try:
            response = requests.get(url, params)
            response_list = response.json()
            response_list['response']
            break
        except:
            time.sleep(1)  # при возврате неверного ответа на запрос: ожидание 1с и отравка повторного запроса
            # print('Except, a new try.')
    return response_list


def get_users_is_members(params, friends_list):
    """Является ли пользователь из списка друзей подписчиком группы"""
    final_list = []
    x = 0
    y = 250
    all_params = params['user_ids'].split(', ')
    while all_params[x:y]:
        params['user_ids'] = str(friends_list['response']['items'][x:y])[1:-1]
        x = y
        y += 250
<<<<<<< HEAD
        members = make_request('groups.isMember', params)
=======
        members = make_request('https://api.vk.com/method/groups.isMember', params)
>>>>>>> c16104b0de34223ff764f0a74a3171bfe299d087
        for member in members['response']:
            final_list.append(member)
    return final_list


def get_group_without_user_friends(params, groups_list, friends_list):
    """Является ли пользователь из списка друзей подписчиком группы"""
    user_is_along = []
    for group in groups_list['response']['items']:
        params['group_id'] = group['id']
        params['user_ids'] = str(friends_list['response']['items'])[1:-1]
        members_group = get_users_is_members(params, friends_list)
        flag = False
        for member in members_group:
            if member['member'] == 1:
                flag = True
                break
        if not flag:
            params['group_id'] = group['id']
            str_dict = {'name': group['name'], 'gid': group['id'],
<<<<<<< HEAD
                        'members_count': make_request('groups.getMembers',
=======
                        'members_count': make_request('https://api.vk.com/method/groups.getMembers',
>>>>>>> c16104b0de34223ff764f0a74a3171bfe299d087
                                                      params)['response']['count']}
            user_is_along.append(str_dict)
    return user_is_along


def save_json(data):
    """Сохранение файла в json"""
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
<<<<<<< HEAD
        print("Размер сохраненного файла: {}".format(len(data)))


def main():
    params = config.get_params()
    params['user_id'] = int(input("Enter id user: "))
    friends_list = make_request('friends.get', params)
    params['extended'] = 1
    groups_list = make_request('groups.get', params)
=======
        print(len(data))


def main():
    params = get_params()
    params['user_id'] = 5030613
    friends_list = make_request('https://api.vk.com/method/friends.get', params)
    params['extended'] = 1
    groups_list = make_request('https://api.vk.com/method/groups.get', params)
>>>>>>> c16104b0de34223ff764f0a74a3171bfe299d087
    data = get_group_without_user_friends(params, groups_list, friends_list)
    save_json(data)


if __name__ == '__main__':
    main()
