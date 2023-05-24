import manageConnection as mc

class MenuManager:
    def get_by_name(self, name):
        query = f"""
        SELECT item_name FROM menu_items WHERE item_name = '{name}'
        """
        mc.cursor.execute(query)
        result = mc.cursor.fetchone()
        if result:
            return result
        else:
            return None
    # def all_items(self):
    #     pass
    #     # return from menut_item

item2 = MenuManager()
print(item2.get_by_name('tacos'))

