class Broad :
    def __init__(self,Rows=10,Cols=10) :
        Rows = Rows
        Cols = Cols
        Map = list()
        __initBroad()
    def __initBroad(self) :
        for x in range( Rows ) :
            for y in range (Cols ):
                Map[x][y] =0
    def setTic(x,y,player):
        """
        x,y is position using int
        player is int ( 1 or 2 )
        not return 
        """
        if (player != 1 or 2):
            raise "player just 1 or 2"
        
        if !(0<x<10 or 0<y<10) :
            raise "position just in 0 to 9"
        
        self.Map[x][y] = player
    def getMap () :
        return self.Map
    def checkPoint(x,y,player):
        if ()


    
def rules (player) :
    if player ==1 :
        point1 = [[0,0,0,0],[1,0,0,3],[1,1,0,0],[1,1,1,0],[1,1,1,1]]
    if player == 2:
        point2 = [[0,0,0,0],[2,0,0,3],[2,2,0,0],[2,2,2,0],[2,2,2,2]]
    return point1,point2

    

