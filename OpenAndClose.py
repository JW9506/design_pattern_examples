from abc import ABCMeta, abstractmethod
from enum import Enum, unique, auto
# Draw Circle

# Graph Editor

# Shape

# Rectangle

# Circle

@unique
class ShapeType(Enum):
    Rectangle = auto()
    Circle = auto()
    Square = auto()


class Shape(metaclass=ABCMeta):
    __m_type = None


    @property
    def m_type(self):
        return self.__m_type
    
    @m_type.setter
    def m_type(self, m_type):
        if not isinstance(m_type, ShapeType):
            raise Exception('m_type must be a type of ShapeType')
        self.__m_type = m_type

    @abstractmethod
    def describe(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.m_type = ShapeType.Rectangle

    def describe(self):
        print(f'我是长方形, 我在{self.__class__.__name__}类里面被决定如何被画出')

class Circle(Shape):
    def __init__(self):
        self.m_type = ShapeType.Circle 

    def describe(self):
        print(f'我是圆形, 我在{self.__class__.__name__}类里面被决定如何被画出')

class Square(Shape):
    def __init__(self):
        self.m_type = ShapeType.Square

    def describe(self):
        print(f'我是正方形, 我在{self.__class__.__name__}类里面被决定如何被画出')


class GraphicEditor:
    def drawShape(self, shape):

        if shape.m_type == ShapeType.Rectangle:
            self.drawRectangle(shape)
        if shape.m_type == ShapeType.Circle:
            self.drawCircle(shape)
        if shape.m_type == ShapeType.Square:
            self.drawSquare(shape)

    def drawRectangle(self, shape):
        print(f'这里是图像管理器{self.__class__.__name__}, 正在绘制{shape.m_type.name}')
        shape.describe()

    def drawCircle(self, shape):
        print(f'这里是图像管理器{self.__class__.__name__}, 正在绘制{shape.m_type.name}')
        shape.describe()

    def drawSquare(self, shape):
        print(f'这里是图像管理器{self.__class__.__name__}, 正在绘制{shape.m_type.name}')
        shape.describe()


if __name__ == '__main__':
    ge = GraphicEditor()
    ge.drawShape(Rectangle())
    ge.drawShape(Circle())
    ge.drawShape(Square())
