class School(object):
    studentList = {}
    def __init__(self, name):
        self.schoolName = name
        self.studentList = {}


    def add(self, student, grade):
        self.studentList[student] = grade

    def grade(self, gradeNumber):
        count = 0
        students = []
        for key, value in self.studentList.iteritems():
            if (value == gradeNumber):
                students.append(key)
        return students

    def sort(self):
        newStudentList = {}
        gradeList = []
        for index in range(12):
            for key, value in sorted(self.studentList.iteritems()):
                if (value == index):
                    gradeList.append(key)
            if gradeList:
                newStudentList[index] = tuple(gradeList)
            gradeList = []
        return newStudentList
