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
- **Deployment Platform:** Render
- **Live Deployment URL:** https://project01-ai-search-kh19.onrender.com
- **Video Presentation Link:** https://youtu.be/O1bRwwh3vZM

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    A* is the best choice for this problem. It found the shortest route, which was 83.08 km, and only checked 13 places. UCS also found the shortest route, but it checked 21 places. A* is faster because it uses the straight-line distance to guess which place is closer to the goal. The other algorithms found longer routes: 89.48 km for BFS, IDS, and Greedy, and 112.39 km for DFS.
- **Search Efficiency (Nodes expanded/time taken comparison):** 
    Greedy checked the fewest places (5) and DFS checked 7, but they did not find the shortest route. A* checked 13 places, while UCS checked 21, so A* did less work while still finding the shortest route. IDS checked the most places (61) because it repeats its search at each level.

    All six algorithms were very fast, taking less than 0.02 milliseconds. DFS and Greedy were the fastest, but the difference was very small. Since the graph only has 22 places, the number of places checked is a better way to compare the algorithms.    
- **Link the idea of search algorithm to today Generative AI.** 
    Generative AI also uses search when it creates text. For example, when AI writes a sentence, it chooses the next word from many possible words. Beam search keeps a few of the best choices instead of checking every possible choice. This is similar to how A* and Greedy focus on the options that look most promising.



