def get_kv(row: str) -> tuple[str]:
    kv = row.split(':')
    return kv[0].replace('"', '').strip(), kv[1].replace('"', '').replace(',', '').strip()


with open('./users.log', encoding="utf-8") as f:
    rows = [i for i in f]
    users = {}
    limit = 5
    page = 1
    while True:
        offset = (page-1) * limit
        page += 1
        try:
            key = get_kv(rows[offset])[1]
        except IndexError:
            break
        if exs := users.get(key):
            continue

        new_u = {}
        for i in rows[offset:offset + limit]:
            k, v = get_kv(i)
            new_u.update({k: v})
        users[key] = new_u

    print('\n')
    for val in users.values():
        pprint.pprint(val)
        print('')
