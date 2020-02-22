current_users = ['INNAG', 'eygeniup', 'nicolaeb', 'denisp','olgaa']
new_users = ['innag','INNAG','nicolaeb','johno','simonah','bradleyn','jamesb']
for new_user in new_users:
    if new_user in current_users:
        print(new_user + " user alredy exist")
    elif new_user.upper() in current_users:
        print(new_user + " user alredy exist")
    else:
        print(new_user + " user is available , you can create it")