

# Stable Marriage Problem

Given *n* men and *n* women, where each person has ranked all members of the opposite sex in order of preference, marry the men and women together such that there are no two people of opposite sex who would both rather have each other than their current partners. When there are no such pairs of people, the set of marriages is deemed stable. The most counter-intutive thing is that there always exist a solution to this problem.

The solution to the problem is done by Gale–Shapley algorithm, which states, till all engagements are done, repeat this loop.
1. Each still not engaged woman sends a proposal to the best suitor of her preference list, to commmit an engagement.
2. Any man who receives a proposal, looks up into his preference list and accepts from the one with the most preference, and rejects all of them.

*Remember, engagements are temporary in nature, i.e., if a man gets a proposal from a better woman than what he is currently engaged to, he will happily call off the engagement.*

More about Stable Marriage Problem : [Original Paper](pages.cs.wisc.edu/~cs787-1/GaleShapley.pdf)

# Proof of Correctness:
**Everyone gets married** 
    At the end, there cannot be a man and a woman both unengaged, as he must have proposed to her at some point (since a man will eventually propose to everyone, if necessary) and, being proposed to, she would necessarily be engaged (to someone) thereafter.
**The marriages are stable** 
    Let Alice and Bob both be engaged, but not to each other. Upon completion of the algorithm, it is not possible for both Alice and Bob to prefer each other over their current partners. If Bob prefers Alice to his current partner, he must have proposed to Alice before he proposed to his current partner. If Alice accepted his proposal, yet is not married to him at the end, she must have dumped him for someone she likes more, and therefore doesn't like Bob more than her current partner. If Alice rejected his proposal, she was already with someone she liked more than Bob.

# About the Project
The project implements the basic Gale-Shapley algorithm presented in the paper in 1962. Two text files *mp.txt* and *fp.txt* refer to male and female preferences respectively.
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Clone the repo using 
```
git clone https://github.com/rj1997/StableMarriageProblem.git
```

### Prerequisites

Python3 will do.

## Running the tests

To run each simulation use the following command from terminal:

```
python3 stablemarriageproblem.py
```

## Contributing

The work is still in progress, I will add more functionalities to this algorithm in some time.
But you are free to make pull requests and start commiting.


## Authors

* **Rishabh Jain** - *LinkedIn* - [rj1997](https://www.linkedin.com/in/rj1997/)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* A wonderful video that got me started [Stable Marriage Problem - Numberphile](https://www.youtube.com/watch?v=Qcv1IqHWAzg)


