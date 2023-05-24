import manageConnection as mc

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"""
        SELECT item_name, item_price FROM menu_items WHERE item_name = '{name}'
        """
        mc.cursor.execute(query)
        result = mc.cursor.fetchone()
        if result:
            return f"{result[0]} {result[1]}"
        else:
            return None

    @classmethod
    def all_items(cls):
        query = f"""
        SELECT item_name, item_price FROM menu_items
        """
        mc.cursor.execute(query)
        result = mc.cursor.fetchall()
        for i in result:
            print(i[0], i[1])


# item2 = MenuManager.get_by_name('pizza')
# print(item2)
# item3 = MenuManager.all_items()


