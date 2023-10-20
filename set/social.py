all_users=["mamootty","mohanlal","prithvi","dq","fahad","asif","nivin"]
nivin_friends=["asif","dq","fahad"]
dq_friends=["mamootty","fahad","dq"]
#nivin_suugest=

all_users_st=set(all_users)
nivin_friends_st=set(nivin_friends)
suggestion=all_users_st.difference(nivin_friends_st)
suggestion.discard("nivin")
print(suggestion)

nivindqmutual=nivin_friends_st.intersection(dq_friends)
print(nivindqmutual)

