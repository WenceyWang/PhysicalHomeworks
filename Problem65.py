#
# Wencey's Physical Homework
# Copyright (C) 2016 Wencey Wang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from visual import *

dt = 1
t = 0
G = 6.7 * 10 ** -11

# Define spacecraft
SpaceCraft = sphere(pos = vector(6.4 * 10 ** 7,0,0),
					color = color.green,
					radius=900000,
					mass=15000,
					make_trail=True,
				    interval=60, 
					retain=1000000)

SpaceCraft_v = vector(0,2 * 10 ** 3,0)
SpaceCraft_p = SpaceCraft_v * SpaceCraft.mass

# Define arrow
MomentumArrow = arrow(color=color.green)
ForceArrow = arrow(color=color.red)

#Define earth
Earth = sphere(pos = vector(0,0,0),
			   color = color.blue,
			   radius = 6.4 * 10 ** 6,
			   mass = 6 * 10 ** 24)

while True:

	rate(4000) 	    

	# Measure the distance
	Distance = Earth.pos - SpaceCraft.pos

	F_net = G * SpaceCraft.mass * Earth.mass / (Distance.mag ** 2) * Distance.norm()

	# Calu spacecraft 
	SpaceCraft_p = SpaceCraft_p + F_net * dt
	SpaceCraft_v = (SpaceCraft_p / SpaceCraft.mass) 
	SpaceCraft.pos = SpaceCraft.pos + SpaceCraft_v * dt

	# Update Arrow
	MomentumArrow.pos = SpaceCraft.pos
	MomentumArrow.axis = SpaceCraft_p*0.5 # Make this arrow show better

	ForceArrow.pos = SpaceCraft.pos
	ForceArrow.axis = F_net*10**4 # Make this arrow show better

	# Time
	t = t + dt
