# PART 2 : Value Iteration Algorithm

## TASK 1
## INTERPRETATIONS AND COMMENTS

1. #### CENTER
	When Indiana is at center and MM is in a dormant state we try to move to the east and hit it because of better accuracy at east or attack it but it has less probability of success.
	While MM is in ready state we would prefer to defend and move to safe positions, i.e, up or down or left.
	The output of policy matches with this, combination of center and dormant gave action as RIGHT and combination of center and ready gave action as UP or LEFT.

2.	#### NORTH
	When Indiana is in the North and MM is in a dormant state we try to move down to center, so that we can attack it.
	While MM is in a ready state we would prefer to defend, so we would either stay or craft if the material is available and arrows are not 3.
	The output of policy matches with this, combination of north and dormant gives action as DOWN and combination of center and ready gives action as STAY and CRAFT in cases where material is available, but STAY when arrows are max.

3. ##### EAST
	When Indiana is in East and MM is in dormant state we try to hit or shoot it.Hit has high damage but shoot has more success probability.Therefore we would want to shoot if there are arrows, exact action would still be negotiable.
	While MM is in ready state, we want to defend but moving to Center won't be helpful as would still get hit.Hence we would want to hit or shoot.
	The output of policy matches with this, combination of east and dormant gives action as HIT when arrows are 0 and shoot when arrows are available,but HIT when MM's health is 100. Combination of east and ready gives action as HIT and SHOOT same as in dormant state.

4.	#### WEST
	When MM is in dormant state we would want to attack it, so we would shoot or we would want to move to center, so that we can shoot as it has more success probability.
	When MM is ready we would rather stay here or shoot.
	so WEST,D was giving SHOOT or LEFT and WEST,R was giving SHOOT or STAY, as expected.
	
5.	#### SOUTH
	when MM is in dormant state we want to move UP so that we can attack it, or GATHER if material is 0.
	when MM is in ready state we would want to STAY or gather in material isn't maximum.
	so SOUTH,D gave GATHER or UP and SOUTH,R gave GATHER or STAY as expected above based on material and arrows available.



## ANALYSIS
    No.of iteration to converge = 118
We can see that our policy mostly match with our ideal expectations of risk averse person.When MM is in ready state Indiana is moving away to other safe position.This shows that Indiana is Risk-averse person.

Since the discount factor is high this justifies that Indiana
preparing to attack by moving to center or east from non-attackable states,when mm is in dormant state and prefers to play safe when mm is in ready state.I.e,considering long term benefits.
    
It took 118 iterations(including initial one ) to converge, understandable as delta value is as low as 0.001.


## SIMULATIONS
1. START : (W,0,0,D,0)  
* SIMULATION 1:(W, 0, 0, D, 100) 
* (W,0,0,D,100):RIGHT=[-221.23]
* (C,0,0,D,100):RIGHT=[-202.633]
* (E,0,0,R,100):HIT=[-231.155]
* (E,0,0,D,50):[Indiana Got hit by MM]
* (E,0,0,D,50):HIT=[-76.553]
* (E,0,0,R,0):NONE=[0]

2. START : (C,2,0,R,100) 
* (C,2,0,R,100):UP=[-237.628]
* (E,2,0,R,100):HIT=[-231.155]
* (E,2,0,D,50):[Indiana got hit by MM]
* (E,2,0,D,50):HIT=[-76.553]
* (E,2,0,R,0):NONE=[0]


## TASK 2
### CASE 1

    No.of iterations to converge = 120

Policy of other states where EAST wasn't the position of Indiana was almost same. So when indiana is at EAST and MM is ready to attack policy resulted in LEFT only for higher values of MM health.If health was<= 50, HIT or SHOOT were prefered.No.of iterations is almost nearly to older value(TASK 1). For states (E,X,3,R,75)/(E,X,3,R,100), the previous course of action was to attack. Now the policy says move to the west as it is defensive and mm cannot harm to IJ in West, bringing the strategy into line with rationality

### CASE 2

    No.of iterations to converge = 57

Almost all the states where we are not willing to attack resulted in STAY action. There are some states in NORTH and SOUTH, for both mm being ready and
dormant, according to policy IJ will stay, which means the game can get stuck, the game will also continue if IJ is teleported to the east position when trying to remain/move.

### CASE 3

    No.of iterations to converge = 8

Since the discount factor is reduced it leads to faster convergence. In comparison to the original case, a lower gamma value allows quicker convergence. This is because the previous utilities' effect is diminished (because gamma is decreased), and since the payout stays stable most of the time (except when the mm dies and the game ends, in which case IJ receives a loss from the monster), the convergence is faster.