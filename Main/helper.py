from Main.models import *

mcqs = [
    ("Which data structure is used to implement a LIFO (Last-In-First-Out) behavior?", "a) Queue", "b) Linked List", "c) Stack", "d) Tree", "c"),
    ("What is the key characteristic of a Binary Search Tree (BST)?", "a) All nodes have the same value", "b) It allows duplicate values", "c) The left child is always smaller than the parent, and the right child is always greater", "d) It has a linear structure", "c"),
    ("Which sorting algorithm works by repeatedly selecting the largest element and moving it to the end of the array?", "a) Bubble Sort", "b) Quick Sort", "c) Insertion Sort", "d) Merge Sort", "a"),
    ("What is the main advantage of using a Hash Table for data storage?", "a) It guarantees sorted order of elements", "b) It provides constant time insertion, deletion, and retrieval operations on average", "c) It is suitable for storing hierarchical data", "d) It supports efficient search operations for unsorted data", "b"),
    ("In the context of graph traversal, which algorithm uses a queue data structure?", "a) Depth-First Search (DFS)", "b) Breadth-First Search (BFS)", "c) Dijkstra's Algorithm", "d) Kruskal's Algorithm", "b"),
    ("What is the time complexity of finding the kth smallest element in a Min Heap?", "a) O(k)", "b) O(log k)", "c) O(n)", "d) O(n log n)", "b"),
    ("Which data structure is used to efficiently answer range queries (e.g., min/max/sum) on an array?", "a) Binary Search Tree (BST)", "b) Hash Table", "c) Segment Tree", "d) Heap", "c"),
    ("Which algorithmic paradigm involves solving subproblems only if needed and storing their solutions for later use?", "a) Greedy", "b) Dynamic Programming", "c) Divide and Conquer", "d) Backtracking", "b"),
    ("What is the purpose of the Floyd-War-shall algorithm?", "a) Finding the shortest path between two nodes in a graph", "b) Searching for a specific element in an array", "c) Sorting elements in a linked list", "d) Performing a topological sort on a graph", "a"),
    ("What is the primary advantage of using a self-balancing Binary Search Tree (BST) over a regular BST?", "a) Self-balancing BSTs have faster average case time complexity for search operations", "b) Self-balancing BSTs have a smaller memory footprint", "c) Self-balancing BSTs allow duplicate values", "d) Self-balancing BSTs are simpler to implement", "a"),
    ("What does the term 'DFS' stand for in the context of graph traversal algorithms?", "a) Depth-First Search", "b) Directed Function Set", "c) Data File System", "d) Double Frequency Search", "a"),
    ("Which sorting algorithm works by repeatedly selecting the smallest element and moving it to the beginning of the array?", "a) Bubble Sort", "b) Quick Sort", "c) Insertion Sort", "d) Merge Sort", "c"),
    ("In a priority queue, which element is dequeued first?", "a) The largest element", "b) The smallest element", "c) The element that was enqueued last", "d) The element that was enqueued first", "b"),
    ("What is the time complexity of finding the maximum element in a Max Heap?", "a) O(1)", "b) O(log n)", "c) O(n)", "d) O(n log n)", "a"),
    ("Which algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph?", "a) Dijkstra's Algorithm", "b) Prim's Algorithm", "c) Kruskal's Algorithm", "d) Floyd-Warshall Algorithm", "a"),
    ("What is the primary goal of an algorithm's space complexity analysis?", "a) To determine the physical size of memory used by the algorithm", "b) To measure the execution time of the algorithm", "c) To count the number of lines of code in the algorithm", "d) To estimate the amount of memory used by the algorithm", "d"),
    ("Which data structure allows efficient insertion and deletion of elements from both ends?", "a) Queue", "b) Stack", "c) Linked List", "d) Deque", "d"),
    ("What is the main advantage of using a Hash Table with open addressing for collision resolution?", "a) It ensures that all collisions are resolved perfectly", "b) It provides constant time insertion, deletion, and retrieval operations on average", "c) It reduces the memory consumption of the Hash Table", "d) It supports efficient search operations for unsorted data", "b"),
    ("In a Binary Search Tree (BST), which traversal visits the nodes in ascending order?", "a) Preorder", "b) Inorder", "c) Postorder", "d) Level order", "b"),
    ("What is the purpose of the Bellman-Ford algorithm?", "a) Finding the shortest path between two nodes in a graph", "b) Searching for a specific element in an array", "c) Detecting negative cycles in a graph", "d) Performing a topological sort on a graph", "c"),
    ("Which data structure allows efficient retrieval of the minimum and maximum element?", "a) Queue", "b) Stack", "c) Heap", "d) Linked List", "c"),
    ("What is the time complexity of finding an element in a Hash Table using linear probing?", "a) O(1)", "b) O(n)", "c) O(log n)", "d) O(n^2)", "b"),
    ("Which algorithmic paradigm involves solving a problem by making a series of locally optimal choices?", "a) Greedy", "b) Dynamic Programming", "c) Divide and Conquer", "d) Backtracking", "a"),
    ("In a Binary Search Tree (BST), what is the maximum number of nodes at level 'k'?", "a) 2^k", "b) k^2", "c) 2^(k+1) - 1", "d) 2^(k-1)", "a"),
    ("Which sorting algorithm works by dividing the input array into two parts and recursively sorting each part?", "a) Bubble Sort", "b) Quick Sort", "c) Merge Sort", "d) Insertion Sort", "c"),
    ("What is the process of combining two sorted arrays into a single sorted array called?", "a) Merging", "b) Sorting", "c) Partitioning", "d) Shuffling", "a"),
    ("Which sorting algorithm has the worst-case time complexity of O(n^2) but performs well on small datasets due to its adaptive nature?", "a) Merge Sort", "b) Bubble Sort", "c) Quick Sort", "d) Insertion Sort", "d"),
    ("In a binary search tree, what is the maximum number of nodes that a tree with height 'h' can have?", "a) 2^h", "b) 2^(h+1) - 1", "c) h^2", "d) h!", "b"),
    ("What is the primary difference between a breadth-first search (BFS) and a depth-first search (DFS) in graph traversal?", "a) BFS always finds the shortest path, while DFS does not guarantee it", "b) BFS can be implemented recursively, while DFS cannot", "c) DFS always finds the shortest path, while BFS does not guarantee it", "d) DFS is more memory-efficient than BFS", "a"),
    ("What is the main principle behind the Divide and Conquer algorithmic paradigm?", "a) Breaking down a problem into multiple subproblems and solving each subproblem independently", "b) Iteratively refining the solution until the desired outcome is achieved", "c) Solving a problem by transforming it into a different problem of the same type", "d) Merging two smaller problems into a larger problem to solve collectively", "a"),
    ("What is the time complexity of the brute-force approach to solve the Traveling Salesman Problem for 'n' cities?", "a) O(n)", "b) O(2^n)", "c) O(n^2)", "d) O(n!)", "d"),
    ("Which data structure is used to store a collection of key-value pairs with constant-time average-case lookup?", "a) Linked List", "b) Array", "c) Hash Table", "d) Tree", "c"),
    ("Which algorithmic paradigm involves making a series of locally optimal choices at each step to eventually reach a globally optimal solution?", "a) Greedy", "b) Dynamic Programming", "c) Backtracking", "d) Divide and Conquer", "a"),
    ("What is the main advantage of using a Red-Black Tree over a regular Binary Search Tree?", "a) Red-Black Trees have faster average-case insertion and deletion operations", "b) Red-Black Trees guarantee a balanced structure, ensuring logarithmic height", "c) Red-Black Trees use less memory compared to Binary Search Trees", "d) Red-Black Trees can store duplicate elements efficiently", "b"),
    ("In dynamic programming, what is the purpose of memoization?", "a) To optimize the space complexity of an algorithm", "b) To store intermediate results to avoid redundant calculations", "c) To divide the problem into smaller subproblems", "d) To ensure the algorithm is stable and does not crash", "b"),
    ("What is the concept of 'NP-completeness' in computational theory?", "a) The idea that some problems can be solved in non-polynomial time", "b) The concept of solving problems in parallel using multiple processors", "c) A class of decision problems for which a proposed solution can be verified quickly", "d) The notion of solving problems using neural networks and deep learning", "c"),
]

s = [
    ["Introduction & Components of Python",
        "Understanding Python",
        "Role of Python in AI and Data Science",
        "Installation and Working with Python",
        "The default graphical development environment for Python - IDLE",
        "Types and Operations",
            "Python Object Type : Number",
            "Python Object Type : Strings",
            "Python Object Type : Lists",
            "Python Object Type : Dictionaries",
            "Python Object Type :Tuples",
            "Python Object Type : Files",
            "User Defined Classes",
        "Understanding Python Blocks",
        "Python Program Flow Control",
        "Conditional Blocks using if, else, and elif",
        "Simple For Loops in Python",
        "For Loops using Ranges, Strings, Lists, and Dictionaries",
        "Using While Loops in Python",
        "Loop Manipulation using pass, continue, break, and else",
        "Programming using Python Conditional and Loops Block",
        "Extra Readings: Python installation with Windows, Linux, and MAC OS, creating a virtual environment, configuring Python on EC2 instance, understanding Python IDEs (VSCode, PyCharm, Spyder), Installing Anaconda, and setting up environment for Python"],
    
    ["Python Functions, Modules & Packages",
        "Function Basics",
            "Scope",
            "Nested Function",
            "Non-local Statements",
        "Built-in Functions",
        "Arguments Passing",
            "Anonymous Function: lambda",
        "Decorators and Generators",
        "Module Basics",
            "Namespaces",
            "Reloading Modules (math, random, datetime, etc.)",
        "Package Import Basics",
        "Python Namespace Packages",
        "User Defined Modules and Packages",
        "Extra Readings: GUI framework in Python"],
    
    ["Python Object Oriented Programming",
        "Concept of Class, Object, and Instances",
        "Constructor, Class Attributes, and Destructors",
        "Real-time Use of Class in Live Projects",
        "Inheritance, Superclass, and Overloading Operators",
        "Static and Class Methods",
        "Adding and Retrieving Dynamic Attributes of Classes",
        "Programming using OOPS",
        "Delegation and Container",
        "Extra Readings: Integrating GUI framework with OOP"],
    
    ["Python Regular Expression",
        "Powerful Pattern Matching and Searching",
        "Power of Pattern Searching using Regex in Python",
        "Real-time Parsing of Data using Regex",
        "Password, Email, URL Validation using Regular Expression",
        "Pattern Finding Programs using Regular Expression",
        "Extra Readings: Web scraping and pattern matching with regex"],
    
    ["Python Multithreading and Exception Handling",
        "Exception Handling",
            "Avoiding Code Break using Exception Handling",
            "Safeguarding File Operation using Exception Handling",
            "Handling and Helping Developer with Error Code",
        "Programming using Exception Handling",
        "Multithreading",
            "Understanding Threads",
            "Synchronizing the Threads",
        "Programming using Multithreading",
        "Extra Readings: Multiprocessing, deadlock, synchronization, monitors, and messaging queue"],
    
    ["Python File Operation",
        "Reading Config Files in Python",
        "Writing Log Files in Python",
        "Understanding Read Functions",
            "read()",
            "readline()",
            "readlines()",
        "Understanding Write Functions",
            "write()",
            "writelines()",
        "Manipulating File Pointer using Seek",
        "Programming using File Operations",
        "Extra Readings: Reading and writing the files on AWS S3 bucket"],
    
    ["Python Database Interaction",
        "Introduction to NoSQL Database",
        "Advantages of NoSQL Database",
        "SQL Vs NoSQL",
        "Introduction to MongoDB with Python",
        "Exploring Collections and Documents",
        "Performing Basic CRUD Operations with MongoDB and Python",
        "Extra Readings: Graph database like Neo4j with Python"],
    
    ["Python for Data Analysis",
        "NumPy Introduction",
        "Creating Arrays, Using Arrays and Scalars",
        "Indexing Arrays, Array Transposition",
        "Universal Array Function",
        "Array Input and Output",
        "Pandas Introduction",
        "Series in Pandas, Pandas DataFrames, Index Objects, ReIndex",
        "Drop Entry, Selecting Entries",
        "Data Alignment, Rank and Sort",
        "Summary Statistics, Missing Data, Index Hierarchy",
        "Matplotlib Introduction",
        "Visualization Tools",
        "Extra Readings: Text analytics with NLP and Python"]
]

s = [
    ["Linear Project Management Framework",
        "Overview of Project Management",
        "Project Management Life Cycle-IEEE Life Cycle",
        "Project Management Process",
        "Role of Project Manager",
        "Quality Metrics",
        "Risk Management Process (Case Study Based)",
        "Risk Identification",
        "Risk Analysis",
        "Risk Mitigation",
        "RMMM",
        "Hands-on MS Project Tool– Resource Allocation, Scheduling, Gantt chart",
        "Extra Reading: Different software project management, Types of Risk, Risk Information sheet (RIS), CPM and PERT"],
    
    ["Linear Software Project Estimation",
        "Different methods of Cost Estimation",
        "COCOMO-I & II model (Problem Statement)",
        "Delphi Cost Estimation",
        "Function Point Analysis (Problem Statement)",
        "The SEI Capability Maturity Model CMM",
        "Software Configuration Management",
        "Note: Case studies/Numerical Problems based on COCOMO-I and FPA",
        "Extra Reading: KLOC, Rayleigh Curve, Change Management, Configuration management tool - SVN Tool or Redmine"],
    
    ["Agile Project Management Framework",
        "Introduction and Definition Agile, Agile Project Life Cycle",
        "Agile Manifesto: History of Agile and Agile Principles",
        "Key Agile Concepts:",
        "User Stories, Story Points",
        "Product Backlog",
        "Sprint Backlog",
        "Sprint Velocity",
        "Swim Lanes",
        "Minimum Viable Product (MVP)",
        "Version and Release",
        "Agile Project Management v/s Traditional Project Management",
        "Note: Case studies based on Agile vs. Traditional Project",
        "Extra Reading: Study Scrum Agile Framework, Agile project management delivery & methodology framework, Software project team management and different team structures"],
    
    ["Agile Teams, Size and Schedule",
        "Dynamic System Development Method",
        "Value-Driven Development",
        "Team and Roles of an Agile Team",
        "Scrum Master",
        "Product Owner",
        "Development Team",
        "Product Vision and Product Roadmap",
        "Project Objective and Key Metrics",
        "Introduction to User Stories",
        "Estimate the Product Backlog",
        "Techniques for Estimating Story Points",
        "Plan Product Releases",
        "Product Prioritization",
        "Note: Case studies based on Estimation of Product backlog & Story points, design your team and Add screenshots with the caption, Design User stories, log efforts and task in detail",
        "Extra Reading: Personnel Management, Release & Iteration Planning, eXtreme Programming (XP), Values and Principles, Team Dynamics and Collaboration"],
    
    ["Tracking Agile Project and Reports",
        "Introduction",
        "Plan and Execute Iteration",
        "Facilitate Retrospective, Making Team Decisions and Closing out Retrospective",
        "Agile Reports",
        "Daily Reports",
        "Sprint Burn Down Chart and Reports",
        "Benefits of Agile Project Management",
        "Note: Case studies based on No. of iterations and Project Report, Sprint Chart",
        "Extra Reading: Use of MS Project to track agile project, Agile project management tools, Feature-Driven Development, Agile Metrics"],
    
    ["Implementation with Agile Tools",
        "Introduction of Agile Tools",
        "Hands-on GitHub",
        "Create Project using Kanban",
        "Project Repositories",
        "Continuous Integration",
        "Project Backlog",
        "Team Management",
        "Progress Tracking",
        "Releases",
        "Implementation of Problem Statement with Agile Tools- GitHub",
        "Designing Product Vision, Product Backlog",
        "Sprint Backlog, Estimate Story Points",
        "Iteration Release",
        "Note: Case study on design of product vision & backlog with features and user stories, Estimation of story points, Design Iteration Plan, Iteration progress and close iteration in detail",
        "Extra Reading: Agile modeling, Explore various Agile Tools"]
]







s= [
    ["Introduction to Data Communication and Computer Networks",
        "Internet basics and network components. [Transmission Media-Guided, Unguided, Network Devices]",
        "Various types of Networks (only overview)",
        "Connection Oriented N/Ws Vs Connectionless N/Ws",
        "Ethernet- Ethernet standards ZigBee, WiFi, Access Technique -CSMA-CD, Negotiation technique Overview",
        "Wireless Network",
        "Unified Communication –VOIP",
        "Extra Reading: Switching Techniques, CSMA/CA, CSMA/CD, Unified Communication"],

    ["Principle of Layering concept",
        "Need for layering",
        "ISO-OSI 7 Layer Model",
        "TCP/IP model",
        "OSI Model vs TCP/IP mode",
        "Extra Reading: Data Encapsulation, PDU Formation, network devices"],

    ["Link Layer Communication",
        "Error detection and correction techniques",
        "Framing and its types",
        "Flow and error control",
        "HDLC protocol",
        "P2P Protocol",
        "Note: Examples based on 3.1 to be covered",
        "Extra Readings: DLL protocol examples, IEEE 802.2 MAC protocol"],

    ["IP Addressing",
        "Internet Protocol and IPv4 Packet format",
        "Addressing, Physical Addresses, Logical Addresses",
        "Port Addresses, Specific Addresses",
        "IP Address- Network Part and Host Part",
        "Network Masks, Network Addresses and Broadcast Addresses, Loop Back Address",
        "Address Classes",
        "TCP and UDP Connections",
        "TCP Performance in wireless network",
        "Overview of IPv6",
        "IP Routing - Types of routing protocol, Border Gateway Protocol (BGP), Routing Information Protocol (RIP), Open Shortest Path First (OSPF), Routing Table concept",
        "Notes: Examples based on IP addressing and subnetting to be covered",
        "Extra Reading: Network Monitoring Tools –Open NMS, Putty, Wireshark, Nagios core, Cacti"],

    ["Application Layer Protocols",
        "DHCP – DHCP Client, DHCP server, DHCP scope",
        "DNS – Resolution process, Resource Records, DNS protocol structure",
        "HTTP – WWW architecture, HTTP: Request and Response Message",
        "Email protocols – SMTP, POP3, IMAP4 & MIME",
        "FTP, Telnet",
        "Extra Reading: Practical on FTP, Telnet, DNS, Putty"],

    ["Network Security",
        "Active and Passive attacks",
        "Cryptography (Symmetric and Asymmetric)",
        "Firewall",
        "Extra Reading: Examples on symmetric and asymmetric algorithms"],

    ["Socket Programming",
        "Introduction",
        "Berkeley Sockets",
        "Specifying A Protocol Interface",
        "The Socket Abstraction",
        "System Data Structures for Sockets",
        "Specifying an Endpoint Address",
        "A Generic Address Structure",
        "Major System Calls Used with Sockets",
        "Utility Routines for Integer Conversion",
        "Using Socket Calls in A Program",
        "Extra Reading: Client-Server Architecture and its implementation using Socket programming"]
]










test=Test.objects.get(id=44)
for question, op1, op2, op3, op4, correct_op in mcqs:    
    q = Question.objects.create(test=test,question=question)
    choice1 = Choice.objects.create(question=q, choice=op1, is_correct=(correct_op == 'a'))
    choice2 = Choice.objects.create(question=q, choice=op2, is_correct=(correct_op == 'b'))
    choice3 = Choice.objects.create(question=q, choice=op3, is_correct=(correct_op == 'c'))
    choice4 = Choice.objects.create(question=q, choice=op4, is_correct=(correct_op == 'd'))
    
    

sub=Subject.objects.get(id=7)
for i in s:
    s=Topic.objects.create(subject=sub,name=i[0])
    s.save()
    for x in i[1:]:
        k = SubTopic.objects.create(topic=s,name=x)
        k.save()
