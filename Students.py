class student:

    def __init__(self, student_id, student_name, email, grades=None, courses=None):
      self.id_name = student_id, student_name
      self.email = email
      self.grades = grades if grades is not None else {}
      self.grades = set(courses) if courses is not None else set()
      
    #def _str_(self)
    
class student_records:
      
    def __init__(self)
