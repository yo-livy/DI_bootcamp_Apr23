import manageConnection as mc

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def save(self):
        save_item = f"""
        INSERT INTO menu_items 
        (item_name, item_price)
        VALUES ('{self.name}', {self.price})
        """
        mc.cursor.execute(save_item)
        mc.connection.commit()
    def delete(self):
        delete_item = f"""
        DELETE FROM menu_items
        WHERE item_name = '{self.name}2'
        """
        mc.cursor.execute(delete_item)
        mc.connection.commit()
    def update(self, new_name, new_price):
        update_item= f"""
        UPDATE menu_items
        SET item_price = {new_price}, item_name = '{new_name}' WHERE item_name = '{self.name}'
        """
        mc.cursor.execute(update_item)
        mc.connection.commit()

# item_pizza = MenuItem('pizza', 30)
# item_tacos = MenuItem('tacos', 15)
# item_sandwich = MenuItem('sandwich', 10)

# item_pizza.save()
# item_tacos.save()
# item_sandwich.save()



