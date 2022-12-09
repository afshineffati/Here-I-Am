import iso6346

class ShippingContainer:

    next_serial = 1337

    # @staticmethod
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
        

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])


    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))


    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()



c1 = ShippingContainer("MM3", ["tools"])
print(c1.serial)
print(c1.next_serial)
print(ShippingContainer.next_serial)

c2 = ShippingContainer.create_empty("YMP")
print(c2.contents)

c3 = ShippingContainer.create_with_items("MAE", {"food", "textiles", "minerals"})
print(c3.contents)