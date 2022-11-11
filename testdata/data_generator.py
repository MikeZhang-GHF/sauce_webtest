#! /usr/bin/python3
# -*-coding:utf-8-*-
# @Time: 2022-11-11 10:55 a.m.
# Author: Ding
from faker import Faker


class DataGenerator:
    fake = Faker()

    @classmethod
    def firstname(cls, *args, **kwargs):
        return cls.fake.first_name(*args, **kwargs)

    @classmethod
    def lastname(cls, *args, **kwargs):
        return cls.fake.last_name(*args, **kwargs)

    @classmethod
    def postalcode(cls, *args, **kwargs):
        return cls.fake.postalcode(*args, **kwargs)


if __name__ == '__main__':
    print(DataGenerator.firstname())
    print(DataGenerator.lastname())
    print(DataGenerator.postalcode())
