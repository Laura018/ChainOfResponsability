from decorator.ejemplo_decorator import *
from fachada.ejemplo_fachada import *
from proxy.ejemplo_proxy import *
from flyweight.ejemplo_flyweight import *
from interpreter.ejemplo_interpreter import *
from prototype.ejemplo_prototype import *
from singleton.ejemplo_singleton import *


class Handler:
    def __init__(self):
        self.__succesor__ = None

    def set_succesor(self, succesor):
        self.__succesor__ = succesor

    def handler_request(self, opt):
        pass


class HandlerOptionOne(Handler):

    def handler_request(self, opt):
        if opt == 1:
            decorator = EjemploDecorator()
            decorator.obtener_nombre()
            decorator.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionTwo(Handler):

    def handler_request(self, opt):
        if opt == 2:
            fachada = EjemploFachada()
            fachada.obtener_nombre()
            fachada.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionThree(Handler):

    def handler_request(self, opt):
        if opt == 3:
            proxy = EjemploProxy()
            proxy.obtener_nombre()
            proxy.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionFour(Handler):

    def handler_request(self, opt):
        if opt == 4:
            flyweight = EjemploFlyweight()
            flyweight.obtener_nombre()
            flyweight.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionFive(Handler):

    def handler_request(self, opt):
        if opt == 5:
            interpreter = EjemploInterpreter()
            interpreter.obtener_nombre()
            interpreter.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionSix(Handler):

    def handler_request(self, opt):
        if opt == 6:
            prototype = EjemploPrototype()
            prototype.obtener_nombre()
            prototype.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionSeven(Handler):

    def handler_request(self, opt):
        if opt == 7:
            singleton = EjemploSingleton()
            singleton.obtener_nombre()
            singleton.operacion()
        else:
            self.__succesor__.handler_request(opt)


class HandlerOptionDefault(Handler):

    def handler_request(self, opt):
        print("Opción no valida")
