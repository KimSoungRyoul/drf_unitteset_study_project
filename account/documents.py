from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.inspectors import CoreAPICompatInspector, NotHandled


class DjangoFilterDescriptionInspector(CoreAPICompatInspector):
    def get_filter_parameters(self, filter_backend):
        if isinstance(filter_backend, DjangoFilterBackend):
            result = super(DjangoFilterDescriptionInspector, self).get_filter_parameters(filter_backend)
            print('---------', result)
            for param in result:
                print(param)
                if not param.get('description', ''):
                    param.description = "회원의 시리얼 넘버입니다 {field_name}".format(field_name=param.name)

            return result

        return NotHandled
