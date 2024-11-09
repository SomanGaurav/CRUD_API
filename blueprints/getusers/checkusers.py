


def checkuser(users):
    try : 
        processed_user_list = []

        for user in users : 
            user["_id"] = str(user["_id"])
            
            processed_user_list.append(user) 

        return processed_user_list 

    except : 
        return []

