import this


class Tree:
    def create_tree(pid, list_data):
        data = []

        for x in list_data:
            if x['parentid'] == pid:
                next_pid = str(x['_id'])
                x['children'] = this.create_tree(next_pid, list_data)
                data.append(x)

        return data