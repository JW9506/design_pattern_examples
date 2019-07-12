from abc import ABCMeta, abstractmethod 

#Draw Circle

# Graph Editor

# Shape

# Rectangle

# Circle



class Shape(metaclass=ABCMeta):
    __m_type = None


    @property
    def m_type(self):
        return self.__m_type
    
    @m_type.setter
    def m_type(self, m_type):
        self.__m_type = m_type

    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.m_type = 1

    def draw(self):
        print(f'正在画出{self.__class__.__name__}')

class Circle(Shape):
    def __init__(self):
        self.m_type = 2

    def draw(self):
        print(f'正在画出{self.__class__.__name__}')

class Square(Shape):
    def __init__(self):
        self.m_type = 3

    def draw(self):
        print(f'正在画出{self.__class__.__name__}')


class GraphicEditor:
    def drawShape(self, shape):
        shape.draw()

if __name__ == '__main__':
    ge = GraphicEditor()
    ge.drawShape(Rectangle())
    ge.drawShape(Circle())
    ge.drawShape(Square())
