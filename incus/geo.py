from scipy.spatial import Delaunay
from numpy import ndarray, array, zeros, pi, linalg, math



class PointCloud(object):
    def __init__(self, points, layer=0, c=331.29, rho=1.225, time=None):
        
        if not isinstance(points, (list, tuple, ndarray)):
            raise TypeError("points must be a tuple, list or ndarray")
            
        if not isinstance(layer, int):
            raise TypeError("layer must be an int")
            
        if not isinstance(c, (float, int)):
            raise TypeError("c(speed of sound) must be a float or int")

        if not isinstance(rho, (float, int)):
            raise TypeError("rho(density) must be a float or int")
            
        if not isinstance(time, (list, tuple)) and not time is None:
            raise TypeError("time must be a list, tuple or None(for eternity)")
        
        
        if time is None:
            self.__eternity=True
        else:
            if time[0]>time[1]:
                raise ValueError(f"time flows past to future. Starting instance must be less than final instance:{time}")
            self.__eternity=False
            if len(time)!=2:
                raise ValueError(f"time must be time interval(both inclusive):{time}")
            if type(time[0])!=int:
                raise TypeError(f"Starting point must be an int: {time}")
        
        
        self.__c=c
        self.__rho=rho

        self.__time=time
        self.__delaunay=Delaunay(points)
        self.__num_points=len(points)
        self.__layer=layer
        self.__dim=len(points[0])
        self.__coverage=[]
        

 
            
        
        
        for d in range(self.__dim):
            __=[None,None]
            __[0]=int(min(self.__delaunay.points[:,d]))
            __[1]=int(max(self.__delaunay.points[:,d]))
            self.__coverage.append(__)
        
    def isIn(self, point):
        return self.__delaunay.find_simplex(point)>=0
        
    def ExistInInstance(self, time_step):
        if self.__eternity:
            return True
        else:
            return self.__time[0]<=time_step<=self.__time[1]
       
    @property
    def dimensionality(self):
        return self.__dim
    
    @property
    def info(self):
        return self.__dim, self.__layer, self.__delaunay, self.__c, self.__rho, self.__eternity, self.__time, self.__coverage

    @property
    def eternity(self):
        return self.__eternity
    
    @property
    def fielder(self):
        return self.__c, self.__rho
    
    @property
    def duration(self):
        return self.__time
    
    @property
    def coverage(self):
        return self.__coverage
    
    @property
    def layer(self):
        return self.__layer
    
    @property
    def anisotropy(self):
        return False
    
    def __repr__(self):
        return f"PointCloud-{self.__dim}D with {self.__num_points} points, c={self.__c}m*s^-1, rho={self.__rho}kg*m^-3"

        
class Rectangle(PointCloud):
    def __init__(self, A, B, layer=0, c=331.29, rho=1.225, time=None):
        
        if not isinstance(A, (tuple, list, ndarray)):
            raise TypeError("A must be a tuple or list")
        if not isinstance(B, (tuple, list, ndarray)):
            raise TypeError("B must be a tuple or list")
        
        if len(A)!=2:
            raise ValueError("A must be 2D")
            
        if len(B)!=2:
            raise ValueError("B must be 2D")
         
        for i in A:
            if not i>=0:
                raise ValueError("Coordinates of A must be greater than 0") 
        
        for i in B:
            if not i>=0:
                raise ValueError("Coordinates of B must be greater than 0")
                
        super().__init__((A, B,(A[0],B[1]),(B[0],A[1])),layer,c,rho,time)


class RectPrism(PointCloud):
   def __init__(self, A, B, layer=0, c=331.29, rho=1.225, time=None):
        if not isinstance(A, (tuple, list, ndarray)):
            raise TypeError("A must be a tuple, list or ndarray")
    
        if not isinstance(B, (tuple, list, ndarray)):
            raise TypeError("B must be a tuple, list or ndarray")
    
        if len(A)!=3:
            raise ValueError('A is defined in 3D')
    
        if len(B)!=3:
            raise ValueError('B is defined in 3D')
    
        for i in A:
            if i<0:
                raise ValueError("Each component of A must be >=0")
          
        for i in B:
            if i<0:
                raise ValueError("Each component of B must be >=0")
        
        hull=[]
        for i in A[0],B[0]:
            for j in A[1],B[1]:
                for k in A[2],B[2]:
                    hull.append((i,j,k))
         
        super().__init__(hull,layer,c,rho,time)


class Circle(object):
    def __init__(self, A, r, layer=0, c=331.29, rho=1.225, time=None):
        if not isinstance(A, (tuple, list)):
            raise TypeError("A(center) must be a tuple or list")
            
        if len(A)!=2:
            raise ValueError("A(center) must be 2D")
            
        for i in A:
            if not i>=0:
                raise ValueError("Coordinates of A must be greater than 0") 
        
        if not isinstance(r, (int, float)):
            raise TypeError("r(radius) must be an int")
        
        if not r>=0:
            raise ValueError("r(radius) must be more than 0")
            
            
        if not isinstance(layer, int):
            raise TypeError("layer must be an int")
            
        if not isinstance(c, (float, int)):
            raise TypeError("c(speed of sound) must be a float or int")

        if not isinstance(rho, (float, int)):
            raise TypeError("rho(density) must be a float or int")
            
    
        if not isinstance(time, (list, tuple)) and not time is None:
            raise TypeError("time must be a list, tuple or None(for eternity)")
        
        
        if time is None:
            self.__eternity=True
        else:
            if time[0]>time[1]:
                raise ValueError(f"time flows past to future. Starting instance must be less than final instance:{time}")
            self.__eternity=False
            if len(time)!=2:
                raise ValueError(f"time must be time interval(both inclusive):{time}")
            if type(time[0])!=int:
                raise TypeError(f"Starting point must be an int: {time}")
        
        
        self.__c=c
        self.__rho=rho
        self.__A=array(A)
        self.__r=r
        self.__layer=layer
        self.__time=time
        self.__coverage=[[self.__A[i]-r,self.__A[i]+r] for i in range(2)]
        self.__dim=2
        
        
    def isIn(self, point):
        return linalg.norm(self.__A-point)<=self.__r
        
    def ExistInInstance(self, time_step):
        if self.__eternity:
            return True
        else:
            return self.__time[0]<=time_step<=self.__time[1]
       
    @property
    def dimensionality(self):
        return self.__dim
    
    @property
    def info(self):
        return self.__dim, self.__layer, ("CIRCLE",self.__A, self.__r), self.__c, self.__rho, self.__eternity, self.__time, self.__coverage

    @property
    def eternity(self):
        return self.__eternity
    
    @property
    def fielder(self):
        return self.__c, self.__rho
    
    @property
    def duration(self):
        return self.__time
    
    @property
    def coverage(self):
        return self.__coverage
    
    @property
    def layer(self):
        return self.__layer
    
    @property
    def anisotropy(self):
        return False
    
    def __repr__(self):
        return f"Circle with A={self.__A} , r={self.__r}, c={self.__c}m*s^-1, rho={self.__rho}kg*m^-3"
    
    
class Sphere(object):
    def __init__(self, A, r,layer=0, c=331.29, rho=1.225, time=None):
        if not isinstance(A, (tuple, list)):
            raise TypeError("A(center) must be a tuple or list")
            
        if len(A)!=3:
            raise ValueError("A(center) must be 3D")
            
        for i in A:
            if not i>=0:
                raise ValueError("Coordinates of A must be greater than 0") 
        
        if not isinstance(r, (int, float)):
            raise TypeError("r(radius) must be an int")
        
        if not r>=0:
            raise ValueError("r(radius) must be more than 0")
            
            
        if not isinstance(layer, int):
            raise TypeError("layer must be an int")
            
        if not isinstance(c, (float, int)):
            raise TypeError("c(speed of sound) must be a float or int")

        if not isinstance(rho, (float, int)):
            raise TypeError("rho(density) must be a float or int")
            
        if not isinstance(time, (list, tuple)) and not time is None:
            raise TypeError("time must be a list, tuple or None(for eternity)")
        
        
        if time is None:
            self.__eternity=True
        else:
            if time[0]>time[1]:
                raise ValueError(f"time flows past to future. Starting instance must be less than final instance:{time}")
            self.__eternity=False
            if len(time)!=2:
                raise ValueError(f"time must be time interval(both inclusive):{time}")
            if type(time[0])!=int:
                raise TypeError(f"Starting point must be an int: {time}")
        
        
        self.__c=c
        self.__rho=rho
        self.__A=array(A)
        self.__r=r
        self.__layer=layer
        self.__time=time
        self.__coverage=[[self.__A[i]-r,self.__A[i]+r] for i in range(3)]
        self.__dim=3

        
    def isIn(self, point):
        return linalg.norm(self.__A-point)<=self.__r
        
    def ExistInInstance(self, time_step):
        if self.__eternity:
            return True
        else:
            return self.__time[0]<=time_step<=self.__time[1]
       
    @property
    def dimensionality(self):
        return self.__dim
    
    @property
    def info(self):
        return self.__dim, self.__layer, ("SPHERE",self.__A, self.__r), self.__c, self.__rho, self.__eternity, self.__time, self.__coverage
    @property
    def eternity(self):
        return self.__eternity
    
    @property
    def fielder(self):
        return self.__c, self.__rho
    
    @property
    def duration(self):
        return self.__time
    
    @property
    def coverage(self):
        return self.__coverage
    
    @property
    def layer(self):
        return self.__layer
    
    @property
    def anisotropy(self):
        return False
    
    def __repr__(self):
        return f"Sphere with A={self.__A}, r={self.__r}, c={self.__c}m*s^-1, rho={self.__rho}kg*m^-3"


class Cylinder(object):
    def __init__(self, A, r, h, layer=0, c=331.29, rho=1.225, time=None):
        if not isinstance(A, (tuple, list)):
            raise TypeError("A(center) must be a tuple or list")
            
        if len(A)!=3:
            raise ValueError("A(center) must be 3D")
            
        for i in A:
            if not i>=0:
                raise ValueError("Coordinates of A must be greater than 0") 
        
        if not isinstance(r, (int, float)):
            raise TypeError("r(radius) must be an int")
        
        if not r>=0:
            raise ValueError("r(radius) must be more than 0")
                
        if not isinstance(h, (int, float)):
            raise TypeError("h(height) must be an int")
        
        if not r>=0:
            raise ValueError("h(height) must be more than 0")

            
        if not isinstance(layer, int):
            raise TypeError("layer must be an int")
            
        if not isinstance(c, (float, int)):
            raise TypeError("c(speed of sound) must be a float or int")

        if not isinstance(rho, (float, int)):
            raise TypeError("rho(density) must be a float or int")
        
        
        if not isinstance(time, (list, tuple)) and not time is None:
            raise TypeError("time must be a list, tuple or None(for eternity)")
        
        
        if time is None:
            self.__eternity=True
        else:
            if time[0]>time[1]:
                raise ValueError(f"time flows past to future. Starting instance must be less than final instance:{time}")
            self.__eternity=False
            if len(time)!=2:
                raise ValueError(f"time must be time interval(both inclusive):{time}")
            if type(time[0])!=int:
                raise TypeError(f"Starting point must be an int: {time}")
        
        
        self.__c=c
        self.__rho=rho
        self.__A=A
        self.__r=r
        self.__r_2=r**2
        self.__h=h
        self.__layer=layer
        self.__time=time
        self.__coverage=[[self.__A[i]-r,self.__A[i]+r] for i in range(3)]
        self.__dim=3
        self.__coverage=[[A[0]-r,A[0]+r],[A[1]-r,A[1]+r],[A[2],A[2]+h]]
        
    def isIn(self, point):
        return (point[0]-self.__A[0])**2+(point[1]-self.__A[1])**2<=self.__r_2 and 0<=point[2]-self.__A[2]<=self.__h
        
    def ExistInInstance(self, time_step):
        if self.__eternity:
            return True
        else:
            return self.__time[0]<=time_step<=self.__time[1]
       
    @property
    def dimensionality(self):
        return self.__dim
    
    @property
    def info(self):
        return self.__dim, self.__layer, ("CYLINDER",self.__A, self.__r, self.__h), self.__c, self.__rho, self.__eternity, self.__time, self.__coverage
    @property
    def eternity(self):
        return self.__eternity
    
    @property
    def fielder(self):
        return self.__c, self.__rho
    
    @property
    def duration(self):
        return self.__time
    
    @property
    def coverage(self):
        return self.__coverage
    
    @property
    def anisotropy(self):
        return False
    
    @property
    def layer(self):
        return self.__layer
    
    def __repr__(self):
        return f"Cylinder with A={self.__A}, r={self.__r}, h={self.__h}, c={self.__c}m*s^-1, rho={self.__rho}kg*m^-3"
                 
