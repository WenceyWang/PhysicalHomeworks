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
from visual.graph import * 

# Define constant
t = 0
dt = 25
G = 6.7e-11

# Define spacecraft
SpaceCraft = sphere(pos = vector(6.4e7,0,0),
					color = color.green,
					radius=900000,
					mass=15000,
					make_trail=True,
					interval=60, 
					retain=1000000)

SpaceCraft.v = vector(0,2e3,0) # 2500 will make circular orbit
SpaceCraft.p = SpaceCraft.v * SpaceCraft.mass

# Define arrow
MomentumArrow = arrow(color=color.green)
ForceArrow = arrow(color=color.red)

# Define earth
Earth = sphere(pos = vector(0,0,0),
			   color = color.blue,
			   radius = 6.4e6,
			   mass = 6e24)

#Define graph
KGraph = gcurve(color=color.cyan) # Kinetic graph
UGraph = gcurve(color=color.red) # Gravitational potential graph
SumGraph = gcurve(color=color.yellow) # Sum graph

while True:

	# Limit frame
	rate(240) 	    

	# Measure the distance
	Distance = Earth.pos - SpaceCraft.pos

	FNet = G * SpaceCraft.mass * Earth.mass / (Distance.mag ** 2) * Distance.norm()

	# Calculate spacecraft
	SpaceCraft.p = SpaceCraft.p + FNet * dt
	SpaceCraft.v = (SpaceCraft.p / SpaceCraft.mass) 
	SpaceCraft.pos = SpaceCraft.pos + SpaceCraft.v * dt

	# Update Arrow
	MomentumArrow.pos = SpaceCraft.pos
	MomentumArrow.axis = SpaceCraft.p * 0.5 # Make this arrow show better

	ForceArrow.pos = SpaceCraft.pos
	ForceArrow.axis = FNet * 1e4 # Make this arrow show better

	# Update energy
	SpaceCraft.k = 0.5 * SpaceCraft.mass * (SpaceCraft.v.mag ** 2)
	SpaceCraft.u = -G * Earth.mass * SpaceCraft.mass / Distance.mag

	# Draw graph
	KGraph.plot(pos=(t,SpaceCraft.k))
	UGraph.plot(pos=(t,SpaceCraft.u))
	SumGraph.plot(pos=(t,SpaceCraft.k + SpaceCraft.u))

	# Add time
	t = t + dt
