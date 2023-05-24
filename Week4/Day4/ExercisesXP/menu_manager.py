import manageConnection as mc

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"""
        SELECT item_name FROM menu_items WHERE item_name = '{name}'
        """
        mc.cursor.execute(query)
        result = mc.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    @classmethod
    def all_items(cls):
        query = f"""
        SELECT item_name FROM menu_items
        """
        mc.cursor.execute(query)
        result = mc.cursor.fetchall()
        return result


item2 = MenuManager.get_by_name('pizza')
print(item2)
item3 = MenuManager.all_items()
for i in item3:
    print(i[0])
