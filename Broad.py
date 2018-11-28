class Broad :
    def __init__(self,Rows=10,Cols=10) :
        Rows = Rows
        Cols = Cols
        Map = list()
        self.__initBroad()
    def __initBroad(self) :
        for x in range( Rows ) :
            for y in range (Cols ):
                Map[x][y] =0
    def setTic(self,x,y,player):
        """
        x,y is position using int
        player is int ( 1 or 2 )
        not return 
        """
        if (player not 1 or player 2):
            raise "player just 1 or 2"
        
        if !(0<x<10 or 0<y<10) :
            raise "position just in 0 to 9"
        
        self.Map[x][y] = player
    def getMap () :
        return self.Map
