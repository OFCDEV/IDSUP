users = [{"id":0, "name":"Hero"},
         {"id":1, "name":"Dunn"},
         {"id":2, "name":"Sue"},
         {"id":3, "name":"Chi"},
         {"id":4, "name":"Thor"},
         {"id":5, "name":"Clive"},
         {"id":6, "name":"Hero"},
         {"id":7, "name":"Hicks"},
         {"id":8, "name":"Devun"},
         {"id":9, "name":"Klein"}]
friendship_pairs = [{0,1},{0,2},{1,2},{1,3},{2,3},{3,4},
                    {4,5},{5,6},{5,7},{6,8},{7,8},{8,9}]
friendships = {user["id"]:[] for user in users}
for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
print(friendships)
def num_of_friend(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)
print(num_of_friend({"id":0,"name":"Hero"}))
total_connections = sum(num_of_friend(user) for user in users)
print(total_connections)
num_users = len(users)
avg_connection = total_connections / num_users
print(avg_connection)
num_friends_by_id =[(user["id"],num_of_friend(user)) for user in users]
print(num_friends_by_id)
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],reverse=True
)

