class Prototype:
    def clone(self):
        return Prototype()


class Creator:
    def create_copy(self, prototype: Prototype):
        return prototype.clone()


prototype = Prototype()
creator = Creator()

copy_object = creator.create_copy(prototype)

print(copy_object)

