import streamlit_authenticator as stauth

passwords = ['veekstar2025']
hashed_passwords = stauth.Hasher(passwords).generate()
print(hashed_passwords)
