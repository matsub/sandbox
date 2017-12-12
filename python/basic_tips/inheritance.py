#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Parent:
    def __init__(self, x):
        self.x = x
        self._prop = x

    @property
    def prop(self):
        return self._prop

    @prop.setter
    def prop(self, v):
        self._prop = v


class Child(Parent):
    prop = property(Parent.prop.__get__)

    def __init__(self, x):
        super().__init__(x)
        print('i aaaaaaaaam a chiiiiiiiiiiiild')

    @prop.setter
    def prop(self, v):
        print(f'prop has set as {v}')
        self._prop = v


c = Child(10)
c.prop = 20
