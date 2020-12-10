from flask import Flask, json
from  flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
students = json.load(open('stud_list.json'))

class Student(Resource):
    def get(self, id):
        for student in students:
            if (id == student[students["id"]]):
                return student, 200
        return "student not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("surname")
        args = parser.parse_args()

        for student in students:
            if (id == student[students["id"]]):
                return "student with id {} already exists".format(id), 400

        student = {
            "id": id,
            "name": args["name"],
            "surname": args["surname"]
        }
        students.append(student)
       ''' with open('stud_list.json', 'r') as jfr:
            jf_file = json.load(jfr)
        with open('stud_list.json', 'w') as jf:
            jf_target = jf_file[0]
            jf_target.append(student)
            json.dump(jf_file, jf, indent=2)'''
        return student, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("surname")
        args = parser.parse_args()

        for student in students:
            if (id == student["id"]):
                student["name"] = args["name"]
                student["surname"] = args["surname"]
                return student, 200

        student = {
            "name": args["name"],
            "surname": args["surname"]
        }
        students.append(student)
        return student, 201

    def delete(self, id):
        global students
        students = [student for student in students if student["id"] != id]
        return "student with id {} is deleted.".format(id), 200


api.add_resource(Student, "/student/<string:id>")

app.run(debug=True)
