

class sinhvien:
    count = 0

    def __init__(self, id, name, date, gender, majors, course):
        self.id = id
        self.name = name
        self.date =  date
        self.gender = gender
        self.course = course
        self.majors = majors
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

    def set_gender(self,gender):
        self.gender = gender
    def get_gender(self):
        return self.gender

    def set_course(self,course):
        self.course = course
    def get_course(self):
        return self.course

    def set_majors(self,majors):
        self.major = majors
    def get_majors(self):
        return self.majors
        
    def show_info(self):
        print(f"\nMã sinh viên: {self.id}")
        print(f"Tên sinh viên: {self.name}")
        print(f"Ngày tháng năm sinh: {self.date}")
        print(f"Giới tính: {self.gender}")
        print(f"Nghành học: {self.majors}")
        print(f"Khóa: {self.course}\n")

