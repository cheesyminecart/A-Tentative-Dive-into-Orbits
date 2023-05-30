from manim import *
# proxima centauri system (just b, orbits testing)
class ProximaCentauri(Scene): 
    def construct(self): 
        proxima = Circle(color=RED, fill_opacity=0.5).scale(0.4)
        orbit = Ellipse(width = 5, height = 4.9)
        planetB = Dot()
        planetB.move_to(orbit.point_from_proportion(0))
        self.offset = 0
        
        def planet_orbit(mob,dt): 
            rate = 1.2 / (1 + np.linalg.norm(mob.get_center() - proxima.get_center()) ** 2)
            mob.move_to(orbit.point_from_proportion(((self.offset + rate))%1))
            self.offset += (rate * dt)
            
        self.add(proxima, orbit, planetB)
        planetB.add_updater(planet_orbit)
        self.update_self(0)
        self.wait(10)


