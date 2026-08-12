# Building the Full Tree -- Recursive Splitting

last lecture = how to pick ONE split. this = doing that over and over to build the whole tree.

## the algorithm
1. all examples start at root
2. compute info gain for every feature, pick best
3. split into left/right branches
4. repeat steps 2-3 on left branch, then right branch
5. stop at a node when:
   - 100% one class
   - max depth would be exceeded
   - info gain below threshold
   - too few examples in node

that's really the whole thing. nothing new conceptually, just apply the rule at every node not just root.

## walking the cat example
root → info gain computed for all 3 features → ear shape wins → split pointy(5) / floppy(5)

**left branch (5 pointy):**
check stop criteria: mixed cats/dogs, not pure → keep going
recompute info gain but ONLY on these 5 examples, treat as fresh mini problem
- ear shape → info gain = 0 (obviously, all 5 already share this value, no new info)
- face shape vs whiskers → face shape wins
split round(4, all cats)/not round(1, dog) → both pure → leaf nodes: cat / not cat

**right branch (5 floppy):** -- same deal, own island
check stop : mixed → keep going
recompute info gain fresh on just these 5 → whiskers wins this time
split present(cat)/absent(dogs) → both pure → leaf nodes

note: whiskers won on the right, face shape won on the left. DIFFERENT winning feature depending on which subset you're in. makes sense since it's literally solving a smaller separate problem each time.

## why "recursive"
the whole insight of this lecture : building left branch = running the SAME algorithm again just on 5 examples instead of 10. right branch = same thing again, separately.

tree building = building smaller trees inside itself. function calls itself on subsets until stopping criteria hit.

→ don't need to fully get recursion as CS concept to use decision trees (libraries handle it), but if writing from scratch this is the structure: build_node() that calls build_node() twice (left subset, right subset) unless it's a leaf.

## max depth
bigger max depth = tree can be more complex = more overfit risk. same tradeoff as poly degree / bigger NN.

could cross-validate to pick max depth in theory. in practice libraries have decent defaults, rarely hand-tune this from scratch.

## next
so far only binary features (pointy/floppy etc). next lectures: features w/ >2 categories + continuous features.

*Source: Andrew Ng, Machine Learning Specialization*
