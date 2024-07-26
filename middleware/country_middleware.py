from models import *
from origin import *


class Country_processor:
    @classmethod
    def get_by_region(cls, region) -> List[Countries]:
        _countries = []
        for i in Countries.select().where(Countries.region == region):
            _countries.append(i)
        return _countries

    @classmethod
    def get_by_alpha2(cls, alpha2) -> Countries:
        _countries = []
        for i in Countries.select().where(Countries.alpha2 == alpha2):
            _countries.append(i)
        if len(_countries) == 0:
            raise ValueError
        else:
            return _countries[0]

    @classmethod
    def validate_coutry(cls, name):
        for i in Countries.select():
            if i.alpha2 == name:
                return name
            else:
                return 0