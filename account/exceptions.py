from rest_framework.exceptions import NotAuthenticated as DRFNotAuthenticated


class NotAuthentication(DRFNotAuthenticated):
    default_detail = '인증 되지 않은 사용자입니다.'
