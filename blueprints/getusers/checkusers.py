


def checkuser(users):
    try : 
        remove_key = "password"
        processed_user_list = []

        for user in users : 
            user["_id"] = str(user["_id"])
            if remove_key in user : 
                del user[remove_key]
            
            processed_user_list.append(user) 

        return processed_user_list 

    except : 
        return []

