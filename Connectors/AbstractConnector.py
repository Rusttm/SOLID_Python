from abc import ABCMeta, abstractmethod, abstractproperty


class Connector(object):
    """ Материнский класс для коннектора"""
    __metaclass__ = ABCMeta

    class ConnectorName(property):
        pass
