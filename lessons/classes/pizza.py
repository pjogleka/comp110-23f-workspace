class Pizza:

    #attributes
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size:str, inp_toppings, inp_gf):
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf