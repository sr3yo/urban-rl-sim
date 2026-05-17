Training a virtual 2D block serving as a car to navigate on a race-car like track using reinforcement learning. (UPDATING AS I GO ALONG AFTER WHAT I CONSIDER A MILESTONE)

The first goal I had was making a simple environment; this includes the road, the block serving as a car, the grass and ray sensors through pygame. After this was done, using some of the pygame documentation (and Claude) I was able to add some simple wasd movement. 
Now focusing on the ray sensors, I wrote a small cast_ray function that casts 5 rays out of the car every frame at 60fps. We calculate the tip of the ray through the current distance, x and y position of the car and the desired angle I wish to cast the array. If the ray is out of bounds, we return the distance, and
if the tip of the array touches the green grass, we simply just return the distance  giving us the distance to the nearest wall boundary. That way, we know when we're close to the edge and can feed that to our neural network. 
