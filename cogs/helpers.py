import json

ADMIN_ROLES = ['sys admins', 'Overlord']

def permission_check(self, ctx, username, permissions):
  user_roles = [role.name for role in username.roles]
  for role in permissions:
    if role in user_roles:
      return True
    else:
      continue
  return False
