WHITE = (255, 255, 255)


class Field:

    def __init__(self, i=0, j=0, x0=0, y0=0, field_size=70, n_l=0, n_r=0, n_u=0, n_d=0, n_lu=0, n_rd=0, n_ru=0, n_ld=0, color=WHITE):
        self.i = i
        self.j = j
        self.x_left = x0
        self.x_right = x0 + field_size
        self.y_up = y0
        self.y_down = y0 + field_size
        self.color = color
        self.field_size = field_size

        ''' Number of neighbours '''
        self.n_l = n_l
        self.n_r = n_r
        self.n_u = n_u
        self.n_d = n_d
        self.n_lu = n_lu
        self.n_rd = n_rd
        self.n_ru = n_ru
        self.n_ld = n_ld

    def print_cords(self):
        print("\nField on position ({0}, {1}):".format(self.i, self.j))
        print("   X0: {0} \t|  X1: {1}".format(self.x_left, self.x_right))
        print("   Y0: {0} \t|  Y1: {1}".format(self.y_up, self.y_down))

    def print_neighbours(self):
        print("   neighbours")
        print("   {0} | {1} | {2}".format(self.n_lu, self.n_u, self.n_ru))
        print("   {0} | x | {1}".format(self.n_l, self.n_r))
        print("   {0} | {1} | {2}".format(self.n_ld, self.n_d, self.n_rd))