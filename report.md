# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** Harshit Aggarwal
- **UID (netID):** hagga@uic.edu
- **UIN:** 650453448

---

## Section 1: Selected City Region
- **Selected Region:** Chicago Metropolitan Area, Illinois, USA

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 22
- **Total Connection Edges:** 30
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** [Write your deployment platform here, e.g., Render]
- **Live Deployment URL:** [Provide your live deployment site URL here]
- **Video Presentation Link:** [Provide an accessible link to your 5–7 minute video presentation]

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    A* is the best. It found the shortest route (83.08 km), and it did it by checking only 13 places. UCS also found the shortest route, but it had to check 21 places. A* is faster because it uses a smart guess: the straight-line distance to the goal. That guess is never longer than the real road distance, so A* never picks a wrong "best" route. The other algorithms found longer routes: 89.48 km for BFS, IDS, and Greedy, and 112.39 km for DFS.
- **Search Efficiency (Nodes expanded/time taken comparison):** 
    Greedy checked the fewest places (5), then DFS (7). But both gave worse routes, so being quick did not make them better. Among the algorithms that found the shortest route, A* checked 13 places and UCS checked 21, so A* did less work. IDS checked the most places (61) because it starts over again and again each time it goes one level deeper. For time, all six algorithms were very fast, under 0.02 milliseconds. DFS and Greedy were the quickest, and UCS, A*, and IDS were a bit slower. The graph only has 22 places, so the time differences are tiny. The number of places checked is a better way to compare them.        
- **Link the idea of search algorithm to today Generative AI.** 
    Generative AI also uses search. When an AI writes a sentence, it is picking the next word out of thousands of choices, and it has to search for a good sequence of words. One method, called beam search, keeps only the few best options at each step, a bit like how A* and Greedy focus on the most promising places. Some AI models also try several lines of thinking and go back if one fails, which is like DFS and BFS. Game AIs like AlphaGo use a scoring guess to decide which moves to look at first, which is the same job the straight-line distance does in A*. In all of these, a better guess means less wasted work.

