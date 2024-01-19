from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import Permission, User
from django.contrib import admin


class PermissionBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        email = claims.get("email")
        username = self.get_username(claims)
        permClaim = (
            "urn:zitadel:iam:org:project:"
            + self.get_settings("ZITADEL_PROJECT")
            + ":roles"
        )

        if "admin" in claims[permClaim].keys():
            return self.UserModel.objects.create_user(
                username, email=email, is_superuser=True, is_staff=True
            )
        elif "staff" in claims[permClaim].keys():
            return self.UserModel.objects.create_user(
                username, email=email, is_staff=True
            )
        elif "user" in claims[permClaim].keys():
            return self.UserModel.objects.create_user(username, email=email)
        else:
            return self.UserModel.objects.none()

    def update_user(self, user, claims):
        permClaim = (
            "urn:zitadel:iam:org:project:"
            + self.get_settings("ZITADEL_PROJECT")
            + ":roles"
        )
        
        if "admin" in claims[permClaim].keys():
            user.is_superuser = True
            user.is_staff = True
        elif "staff" in claims[permClaim].keys():
            user.is_superuser = False
            user.is_staff = True
        elif "user" in claims[permClaim].keys():
            user.is_superuser = False
            user.is_staff = False
        return user
