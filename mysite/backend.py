from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth.models import Permission, User
from django.contrib import admin


class PermissionBackend(OIDCAuthenticationBackend):
    def get_username(self, claims):
        return claims.get("sub")
    def create_user(self, claims):
        email = claims.get("email")
        username = self.get_username(claims)
        permClaim = (
            "urn:zitadel:iam:org:project:"
            + self.get_settings("ZITADEL_PROJECT")
            + ":roles"
        )

        if "admin" in claims[permClaim].keys():
            user = self.UserModel.objects.create_user(
                username, email=email, is_superuser=True, is_staff=True
            )
            user.first_name = claims.get("given_name")
            user.last_name = claims.get("family_name")
            user.save()
            return user
        elif "staff" in claims[permClaim].keys():
            user = self.UserModel.objects.create_user(
                username, email=email, is_staff=True
            )
            user.first_name = claims.get("given_name")
            user.last_name = claims.get("family_name")
            user.save()
            return user
        elif "user" in claims[permClaim].keys():
            user = self.UserModel.objects.create_user(username, email=email)
            user.first_name = claims.get("given_name")
            user.last_name = claims.get("family_name")
            user.save()
            return user
        else:
            return self.UserModel.objects.none()

    def update_user(self, user, claims):
        user.first_name = claims.get("given_name")
        user.last_name = claims.get("family_name")
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
        user.save()
        return user
