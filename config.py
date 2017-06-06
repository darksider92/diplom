import json
VK_API_ENDPOINT = "https://api.vk.com/method"


with open("config.json", "w", encoding="utf-8") as f:
    json.dump(dict(access_token="d13e692be69592b09fd22c77a590dd34e186e6d696daa88d6d981e1b4e296b14acb377e82dcbc81dc0f22",
                   v="5.64"),
              f, ensure_ascii=False, indent=2)
