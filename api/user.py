from flask_restx import Resource, reqparse

from api.users import users

# Resoure for a single user
# It has shared data coming from Users


class User(Resource):

    def get(self, id):
        for user in users:
            if id == user["id"]:
                return user

        return {"error": "user not found"}, 404

    def put(self, id):
        for user in users:
            if id == user["id"]:
                parser = reqparse.RequestParser()
                parser.add_argument("firstname", type=str, required=True)
                parser.add_argument("lastname", type=str, required=True)
                args = parser.parse_args()

                # avoid inserting duplicate user
                for userb in users:
                    if id == userb["id"]:
                        continue
                    if args["firstname"] != userb["firstname"] or args["lastname"] != userb["lastname"]:
                        continue
                    
                    return {"error": "user already exists!"}, 400
                
                # no changes made
                if user["firstname"] == args["firstname"] and user["lastname"] == args["lastname"]:
                    return {"msg": "no changes made"}, 200
                
                user["firstname"] = args["firstname"]
                user["lastname"] = args["lastname"]

                return {"msg": "user updated"}, 200
            
        return {"error": "user not found"}, 404


    def delete(self, id):
        for user in users:
            if id == user["id"]:
                users.remove(user)
                return {"msg": "user deleted"}, 200
            
        return {"error": "user not found"}, 404
    
