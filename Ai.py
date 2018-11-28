class AI (object) :
    def __init__(self, broad, state, depth) :
        self.__broad = broad
        self.__state = state
        self.__X = -1
        self.__Y = -1
    def setBroad(self, x, y ,state) :
        self.__broad.setTic(x,y,state)