from oops_project import chatbook

# user1 = chatbook()
# user1.send_message()

user1=chatbook()
print(user1.id)

user2 = chatbook()
print(user2.id)

chatbook.set_id(10)
user2=chatbook()
print(user2.id)