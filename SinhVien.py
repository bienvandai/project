

class sinhvien:
    count = 0

    def __init__(self, id, name, date, sex, major, course):
        self.id = id
        self.name = name
        self.date =  date
        self.sex = sex
        self.course = course
        self.major = major
        sinhvien.count +=1


    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def set_date(self, date):
        self.date = date
    def get_date(self):
        return self.date

    def set_sex(self,sex):
        self.sex = sex
    def get_sex(self):
        return self.sex

    def set_course(self,course):
        self.course = course
    def get_course(self):
        return self.course

    def set_major(self,major):
        self.major = major
    def get_major(self):
        return self.major
        
    def show_info(self):
        print(f"\nMã sinh viên: {self.id}")
        print(f"Tên sinh viên: {self.name}")
        print(f"Ngày tháng năm sinh: {self.date}")
        print(f"Giới tính: {self.sex}")
        print(f"Nghành học: {self.major}")
        print(f"Khóa: {self.course}\n")

