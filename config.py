VK_API_ENDPOINT = "https://api.vk.com/method"


def get_params():
    """Необходимые параметры для запроса."""
    VERSION = '5.64'
    access_token = "d13e692be69592b09fd22c77a590dd34e186e6d696daa88d6d981e1b4e296b14acb377e82dcbc81dc0f22"
    params = {'access_token': access_token,
              'v': VERSION,
              }
    return params