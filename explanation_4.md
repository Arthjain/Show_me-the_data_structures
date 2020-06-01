In this problem, we have implemented Recursion and called get_users and get_groups method.
    since, we need to check all the subgroups present in the group for a user, 
    recursion is the best choice to use.
First I have checked the name of the group whether it is same as the user I am looking for then I checked in the users list of that group.
Then I went for its child groups. If at any point I find the user. I returned True but aafter checking all the groups and users, if I don't find the user. Then I returned

Time complexity: O(depth x no. of users) Space complexity: O(depth x no. of users)
