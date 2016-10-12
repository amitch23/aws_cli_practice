# !/bin/bash
users=$( aws iam list-users | ./parse_users.py )

for user in $users; do
	echo $user
	echo $( aws iam list-groups-for-user --user-name $user)
done

