# AI helpers - Chatbot and PDF helper
# MAIS Study Planner - Built by a 2nd Semester CIS Student

import random
import os


class AIChatBot:
    """
    Smart rule-based chatbot with detailed subject-wise answers.
    Covers 20-30 lines of knowledge per major subject.
    """

    def __init__(self):
        # Subject-wise detailed knowledge base (20-30 points each)
        self.subject_knowledge = {
            "math": [
                "📐 Mathematics Study Guide:\n"
                "1. Practice at least 5-10 problems daily — math improves with repetition.\n"
                "2. Start with easy questions before moving to hard ones.\n"
                "3. For algebra: isolate the variable step by step, don't skip steps.\n"
                "4. For calculus: understand derivatives as 'rate of change' — don't just memorize.\n"
                "5. Learn integration as the reverse of differentiation.\n"
                "6. Memorize key formulas but understand where they come from.\n"
                "7. Draw diagrams for geometry problems — visual help is huge.\n"
                "8. Use rough work paper — never solve in your head for complex problems.\n"
                "9. Revise multiplication tables and basic arithmetic — they save time in exams.\n"
                "10. For word problems: underline the key info, then set up the equation.\n"
                "11. Check your answer by substituting back into the original equation.\n"
                "12. Practice past papers — patterns repeat in exams.\n"
                "13. Don't skip steps in proofs — every line must logically follow the last.\n"
                "14. Group theory, sets, and logic: understand definitions first, examples second.\n"
                "15. Statistics: mean = sum/count. Median = middle value. Mode = most frequent.\n"
                "16. Probability: favorable outcomes / total outcomes.\n"
                "17. Matrix multiplication: rows × columns. Practice until it's automatic.\n"
                "18. Trigonometry: SOH-CAH-TOA — Sin=Opp/Hyp, Cos=Adj/Hyp, Tan=Opp/Adj.\n"
                "19. Unit circle is your best friend for trig identities.\n"
                "20. Keep a formula sheet and revise it before every exam.\n"
                "21. If stuck, skip and come back — don't waste time in one place.\n"
                "22. Use Khan Academy or YouTube for topics you don't understand.\n"
                "23. Time yourself while practicing — exam time management is key.\n"
                "24. Work in groups sometimes — explaining math to others solidifies your own understanding.\n"
                "25. Sleep well before math exam — a fresh brain calculates faster! 🧠"
            ],
            "physics": [
                "⚡ Physics Study Guide:\n"
                "1. Physics is all about understanding 'why' things happen, not just 'what'.\n"
                "2. Memorize the SI units for every quantity — marks are lost for wrong units.\n"
                "3. For mechanics: draw Free Body Diagrams (FBD) for every force problem.\n"
                "4. Newton's Laws: 1st=inertia, 2nd=F=ma, 3rd=action-reaction. Know them cold.\n"
                "5. For kinematics: list the 5 variables (u,v,a,s,t) and pick the right equation.\n"
                "6. Energy methods are often easier than force methods — try both approaches.\n"
                "7. Electricity: Ohm's Law V=IR is the foundation. Master it first.\n"
                "8. For circuits: series = same current, parallel = same voltage.\n"
                "9. Magnetism and electricity are linked — understand right-hand rule.\n"
                "10. Waves: frequency × wavelength = speed. This relation is essential.\n"
                "11. Understand interference, diffraction, and the Doppler effect with diagrams.\n"
                "12. Thermodynamics: 1st Law = energy conservation. 2nd Law = entropy increases.\n"
                "13. For optics: ray diagrams for mirrors and lenses — practice drawing them.\n"
                "14. Modern physics (quantum): photon energy E=hf. Photoelectric effect basics.\n"
                "15. Nuclear physics: understand fission, fusion, radioactive decay types.\n"
                "16. Always write formulas first, then substitute values with units.\n"
                "17. Significant figures matter — round answers appropriately.\n"
                "18. Don't just memorize problems — understand the concept behind each one.\n"
                "19. Physics requires math — if math is weak, improve it alongside physics.\n"
                "20. Solve MCQs by elimination when unsure — physics MCQs have patterns.\n"
                "21. For long questions: show all working even if the answer is wrong — partial marks!\n"
                "22. Use graphical methods — velocity-time graphs give displacement as area under curve.\n"
                "23. Dimensional analysis: check if both sides of an equation match in units.\n"
                "24. Online simulations (PhET) are great for visualizing physics concepts.\n"
                "25. Revise one full chapter daily and do 10 solved examples from it. ⚡"
            ],
            "chemistry": [
                "🧪 Chemistry Study Guide:\n"
                "1. Learn the periodic table — at least first 30 elements with symbols and atomic numbers.\n"
                "2. Understand periodic trends: atomic radius, ionization energy, electronegativity.\n"
                "3. Valence electrons determine bonding — this is the core of all of chemistry.\n"
                "4. Ionic bonding: metal + non-metal. Covalent: non-metal + non-metal.\n"
                "5. Lewis structures: draw them for every molecule — it shows bonding clearly.\n"
                "6. Balancing equations: atoms on left must equal atoms on right. Practice daily.\n"
                "7. Mole concept: 1 mole = 6.022×10²³ particles. Molar mass = grams per mole.\n"
                "8. Stoichiometry: ratio from balanced equation tells how much of each substance reacts.\n"
                "9. Acids: donate H⁺. Bases: accept H⁺. pH < 7 = acid, pH > 7 = base.\n"
                "10. Strong acids/bases fully dissociate. Weak ones partially — know examples of both.\n"
                "11. Redox reactions: oxidation = loss of electrons, reduction = gain (OIL RIG).\n"
                "12. Electrochemistry: anode = oxidation, cathode = reduction. (Red Cat, An Ox).\n"
                "13. Organic chemistry: learn functional groups first (alcohol -OH, aldehyde -CHO, etc.).\n"
                "14. IUPAC naming: longest chain = parent name. Substituents listed alphabetically.\n"
                "15. Isomers: same formula, different structure — draw them out.\n"
                "16. Thermochemistry: exothermic releases heat (ΔH negative), endothermic absorbs it.\n"
                "17. Hess's Law: enthalpy change is path-independent — use it for calculations.\n"
                "18. Equilibrium: Le Chatelier's Principle — system opposes changes to maintain balance.\n"
                "19. Reaction rates: increase with temperature, concentration, surface area, catalyst.\n"
                "20. Lab safety is exam content too — know safety symbols and equipment names.\n"
                "21. Use color-coding for organic mechanisms — arrows show electron movement.\n"
                "22. Memorize solubility rules for precipitation reactions.\n"
                "23. Electronegativity difference determines bond type — learn the cutoffs.\n"
                "24. Past papers in chemistry often repeat reaction types — recognize the pattern.\n"
                "25. Don't just read — write out reactions from memory. That's how you learn them. 🧪"
            ],
            "english": [
                "📝 English Study Guide:\n"
                "1. Read something in English every day — news, novels, anything. Reading builds all skills.\n"
                "2. For essays: introduction (hook + thesis), 3 body paragraphs, conclusion. Simple but effective.\n"
                "3. Topic sentence starts each paragraph. Supporting sentences explain it. Closing ties it up.\n"
                "4. Don't repeat words — use synonyms. A thesaurus is your friend.\n"
                "5. Active voice is stronger than passive. 'The dog bit the man' beats 'The man was bitten'.\n"
                "6. Grammar basics: subject-verb agreement — singular subject = singular verb.\n"
                "7. Tenses: simple present (I go), continuous (I am going), perfect (I have gone). Know all.\n"
                "8. Articles (a, an, the): 'a' before consonant sounds, 'an' before vowel sounds, 'the' for specific.\n"
                "9. Prepositions: at (time/place), in (inside), on (surface). Common but tricky.\n"
                "10. Punctuation: comma after introductory clause. Semicolons join related independent clauses.\n"
                "11. Vocabulary: learn 5 new words daily with their meaning, synonym, and usage in a sentence.\n"
                "12. For comprehension: read questions first, then the passage — saves time.\n"
                "13. Underline key information in reading passages before answering.\n"
                "14. Don't use informal language in formal writing (no 'gonna', 'wanna', 'kinda').\n"
                "15. Paragraph transitions: furthermore, however, in contrast, as a result, therefore.\n"
                "16. Paraphrasing skill: read a sentence, close the book, write what it means in your words.\n"
                "17. Speaking: record yourself and listen back — it's uncomfortable but very effective.\n"
                "18. Listening: watch English content with subtitles, then without. Build up gradually.\n"
                "19. For letters: formal letters have strict format — date, address, salutation, body, closing.\n"
                "20. Direct and indirect speech: 'He said he was tired' (indirect from 'I am tired').\n"
                "21. Simile vs metaphor: simile uses 'like/as', metaphor directly compares.\n"
                "22. Literature: understand themes, character development, symbolism — not just plot.\n"
                "23. Quote correctly in essays with author and page/line number when required.\n"
                "24. Proofread everything — common mistakes: their/there/they're, your/you're, its/it's.\n"
                "25. Practice writing under timed conditions — exam writing is a skill on its own. 📝"
            ],
            "oop": [
                "💻 Object-Oriented Programming (OOP) Study Guide:\n"
                "1. OOP = organizing code into objects that contain data and behavior together.\n"
                "2. Class = a blueprint. Object = actual instance created from that blueprint.\n"
                "3. Constructor (__init__ in Python) runs automatically when object is created.\n"
                "4. 'self' refers to the current object — always the first parameter in methods.\n"
                "5. Encapsulation: hide internal data with private attributes. Use getters/setters.\n"
                "6. Private in Python: __ (double underscore) makes it name-mangled and harder to access.\n"
                "7. Inheritance: child class gets all features of parent class. Use 'class Child(Parent)'.\n"
                "8. super() calls the parent class constructor — don't forget it in child __init__.\n"
                "9. Polymorphism: same method name, different behavior in different classes.\n"
                "10. Method Overriding: redefining a parent method in child class.\n"
                "11. Abstract classes (ABC module): define methods that MUST be implemented in child.\n"
                "12. Abstraction: hide complexity, show only what's needed. Interface = the visible part.\n"
                "13. Operator Overloading: __add__ for +, __str__ for print(), __len__ for len().\n"
                "14. __str__ makes your object printable — always override it for debugging.\n"
                "15. Class variables: shared by all objects. Instance variables: unique to each object.\n"
                "16. @staticmethod: doesn't need self or cls — utility function inside a class.\n"
                "17. @classmethod: takes cls instead of self — often used as alternative constructors.\n"
                "18. Composition: 'has-a' relationship. Inheritance: 'is-a' relationship.\n"
                "19. MRO (Method Resolution Order): Python looks for methods left to right in inheritance.\n"
                "20. List of objects: you can store objects in lists and loop through them normally.\n"
                "21. Exception handling: try-except inside classes makes them robust.\n"
                "22. Python doesn't have true method overloading — use default arguments instead.\n"
                "23. Practice: model real things (Bank Account, Student, Car) as classes.\n"
                "24. Exam tip: any question with 'design a class' — write constructor, attributes, and methods.\n"
                "25. UML diagrams: class name at top, attributes in middle, methods at bottom. Box format.\n"
                "26. Real use of OOP: Django, Flask, game development, data science libraries all use it.\n"
                "27. Debug OOP code: print(object.__dict__) shows all instance variables instantly.\n"
                "28. Dunder (magic) methods are what make Python OOP powerful — learn them! 💻"
            ],
            "programming": [
                "🖥️ Programming Study Guide:\n"
                "1. Programming = telling the computer exactly what to do, step by step.\n"
                "2. Start by understanding the problem fully before writing a single line of code.\n"
                "3. Variables store data. Names should be meaningful: 'student_marks' not 'x'.\n"
                "4. Data types: int, float, str, bool, list, dict, tuple, set — know when to use each.\n"
                "5. Control flow: if/elif/else — the backbone of decision making in code.\n"
                "6. Loops: for (known count), while (unknown count). Don't create infinite loops!\n"
                "7. Functions: reusable blocks of code. Avoid repeating the same logic twice.\n"
                "8. Parameters vs arguments: parameter is in function definition, argument is what you pass.\n"
                "9. Return values: functions should return results, not just print them (most of the time).\n"
                "10. List comprehensions: [x*2 for x in nums] — clean and Pythonic.\n"
                "11. Dictionaries: key-value pairs. Perfect for lookup tables and structured data.\n"
                "12. String methods: .split(), .strip(), .lower(), .upper(), .replace() — use them constantly.\n"
                "13. File handling: open(), read(), write(), close() — or better, use 'with open() as f'.\n"
                "14. Exception handling: try-except prevents crashes. Always handle exceptions in real code.\n"
                "15. Modules: import only what you need. 'from math import sqrt' not 'import math'.\n"
                "16. Recursion: function calls itself. Always have a base case or it runs forever.\n"
                "17. Algorithms: bubble sort, linear search, binary search — understand how they work.\n"
                "18. Time complexity: O(1) fastest, O(n) linear, O(n²) slow. Think about efficiency.\n"
                "19. Debugging: use print() to see variable values. Use try-except to catch errors.\n"
                "20. Comment your code: # this explains what the next line does. Future you will thank you.\n"
                "21. Indentation in Python is not optional — it defines code blocks. Be consistent.\n"
                "22. GitHub: version control is a professional skill. Start using it now.\n"
                "23. Practice: solve 2-3 coding problems on sites like HackerRank or LeetCode (easy level).\n"
                "24. Don't copy-paste code without understanding it — you'll fail when the exam asks why.\n"
                "25. Build small projects: calculator, quiz game, to-do list — real practice beats exercises. 🖥️"
            ],
            "dsa": [
                "🔢 Data Structures & Algorithms (DSA) Study Guide:\n"
                "1. DSA is the foundation of computer science — every tech company tests this.\n"
                "2. Array: fixed size, index-based access. O(1) access, O(n) search.\n"
                "3. Linked List: nodes connected by pointers. Insert/delete O(1) at head. No random access.\n"
                "4. Stack: LIFO (Last In, First Out). Push, pop, peek. Used in function calls, undo.\n"
                "5. Queue: FIFO (First In, First Out). Enqueue, dequeue. Used in scheduling.\n"
                "6. Binary Search Tree: left < root < right. Search O(log n) on balanced BST.\n"
                "7. Graph: nodes + edges. Directed (one way), undirected (both ways).\n"
                "8. BFS: level-by-level traversal using queue. DFS: depth-first using stack/recursion.\n"
                "9. Sorting: bubble O(n²), merge O(n log n), quick O(n log n) average.\n"
                "10. Binary Search: works only on sorted arrays. O(log n) — much faster than linear.\n"
                "11. Hash Table: key hashed to index. Average O(1) lookup. Collisions must be handled.\n"
                "12. Dynamic Programming: solve subproblems, store results (memoization/tabulation).\n"
                "13. Greedy algorithms: make the locally optimal choice at each step.\n"
                "14. Recursion tree: draw it out to understand how recursive calls branch.\n"
                "15. Time complexity analysis: count loops and nested loops — that's usually your Big-O.\n"
                "16. Space complexity: extra memory used. Recursion uses O(n) stack space.\n"
                "17. Heap (min/max): parent always smaller/larger than children. Used in priority queues.\n"
                "18. Trie: tree for string storage. Fast prefix search for autocomplete features.\n"
                "19. Always analyze edge cases: empty input, single element, all duplicates.\n"
                "20. Two-pointer technique: great for sorted array problems — reduces O(n²) to O(n).\n"
                "21. Sliding window: for subarray/substring problems with a condition on size.\n"
                "22. Exam tip: always state the time and space complexity of your solution.\n"
                "23. Visualize data structures — draw them on paper before coding.\n"
                "24. Implement each structure from scratch at least once to truly understand it.\n"
                "25. Practice on LeetCode, HackerRank, or GeeksForGeeks — start with Easy problems. 🔢"
            ],
            "statistics": [
                "📊 Statistics Study Guide:\n"
                "1. Statistics = collecting, organizing, analyzing, and interpreting data.\n"
                "2. Mean = sum of all values / number of values. Sensitive to outliers.\n"
                "3. Median = middle value when data is sorted. More robust to outliers than mean.\n"
                "4. Mode = the most frequently occurring value. A data set can have multiple modes.\n"
                "5. Range = max - min. Simple but ignores middle values.\n"
                "6. Variance = average of squared differences from the mean.\n"
                "7. Standard Deviation = square root of variance. Measures spread of data.\n"
                "8. Normal distribution: bell-shaped curve. Mean = Median = Mode at center.\n"
                "9. Empirical rule: 68% data within 1 SD, 95% within 2 SD, 99.7% within 3 SD.\n"
                "10. Z-score: how many standard deviations a value is from the mean. Z = (x - μ)/σ.\n"
                "11. Probability: P(event) = favorable outcomes / total outcomes. Range: 0 to 1.\n"
                "12. Complementary events: P(A') = 1 - P(A). Don't forget this shortcut.\n"
                "13. Conditional probability: P(A|B) = P(A∩B) / P(B). Read as 'A given B'.\n"
                "14. Independent events: P(A∩B) = P(A) × P(B). Occurrence of one doesn't affect other.\n"
                "15. Permutations: arrangement where order matters. nPr = n!/(n-r)!\n"
                "16. Combinations: selection where order doesn't matter. nCr = n!/(r!(n-r)!)\n"
                "17. Binomial distribution: n trials, each success/failure, fixed probability p.\n"
                "18. Hypothesis testing: null hypothesis H0, alternate H1. Reject H0 if p-value < 0.05.\n"
                "19. Type I error: rejecting true H0 (false positive). Type II: accepting false H0.\n"
                "20. Correlation: r = +1 (perfect positive), 0 (no relationship), -1 (perfect negative).\n"
                "21. Correlation ≠ causation. Two things can be correlated without causing each other.\n"
                "22. Regression: finding best-fit line y = mx + c to predict values.\n"
                "23. Always draw graphs: histogram, pie chart, box plot — they help understand data.\n"
                "24. Check your calculator settings: degrees vs radians, population vs sample formulas.\n"
                "25. In exams: show all steps. Even a wrong answer with correct method gets partial marks. 📊"
            ],
            "calculus": [
                "∫ Calculus Study Guide:\n"
                "1. Calculus has two main parts: Differential (derivatives) and Integral (integration).\n"
                "2. Limit: what value does f(x) approach as x approaches a number? Foundation of calculus.\n"
                "3. Derivative = rate of change. Slope of tangent line at any point on a curve.\n"
                "4. Basic derivative rules: power rule d/dx(xⁿ) = nxⁿ⁻¹. Learn it first.\n"
                "5. Product rule: d/dx(uv) = u'v + uv'. Quotient rule: d/dx(u/v) = (u'v - uv')/v².\n"
                "6. Chain rule: d/dx[f(g(x))] = f'(g(x)) · g'(x). The most used rule in practice.\n"
                "7. Derivatives of trig: d/dx(sin x) = cos x. d/dx(cos x) = -sin x. Memorize these.\n"
                "8. d/dx(eˣ) = eˣ. d/dx(ln x) = 1/x. These are elegant and important.\n"
                "9. Implicit differentiation: differentiate both sides, treat y as function of x.\n"
                "10. Critical points: set f'(x) = 0. Find where function increases, decreases, or turns.\n"
                "11. Second derivative test: f''(x) > 0 means minimum, f''(x) < 0 means maximum.\n"
                "12. Concavity: f''(x) > 0 means concave up (bowl shape), < 0 means concave down.\n"
                "13. Inflection point: where concavity changes sign.\n"
                "14. Integration is the reverse of differentiation (Fundamental Theorem of Calculus).\n"
                "15. ∫xⁿ dx = xⁿ⁺¹/(n+1) + C. Never forget the +C for indefinite integrals.\n"
                "16. Definite integral: gives actual area under curve between two limits.\n"
                "17. Substitution rule (u-sub): if integrand has a function and its derivative, use u-sub.\n"
                "18. Integration by parts: ∫u dv = uv - ∫v du. Use for products of functions.\n"
                "19. Partial fractions: break complex rational functions into simpler ones to integrate.\n"
                "20. Improper integrals: involve infinity. Check convergence using limits.\n"
                "21. Applications: area between curves, volumes of revolution, arc length.\n"
                "22. Differential equations: equations with dy/dx. Separable equations are the easiest type.\n"
                "23. Taylor/Maclaurin series: representing functions as infinite polynomial sums.\n"
                "24. Always verify your derivative by differentiating your integral answer.\n"
                "25. Draw graphs — calculus makes much more sense when you can visualize it visually. ∫"
            ],
            "economics": [
                "💹 Economics Study Guide:\n"
                "1. Economics = how individuals, firms, and governments allocate scarce resources.\n"
                "2. Microeconomics: individual decisions (firm, consumer). Macro: whole economy (GDP, inflation).\n"
                "3. Supply and demand: the most important model in economics. Master it completely.\n"
                "4. Law of demand: price up → quantity demanded down (inverse relationship).\n"
                "5. Law of supply: price up → quantity supplied up (direct relationship).\n"
                "6. Equilibrium: where supply curve meets demand curve. Market clears here.\n"
                "7. Elasticity: how responsive quantity is to price change. Elastic = very responsive.\n"
                "8. PED = % change in quantity demanded / % change in price. >1 elastic, <1 inelastic.\n"
                "9. Consumer surplus: difference between what consumer is willing to pay and actual price.\n"
                "10. Producer surplus: difference between price received and minimum seller would accept.\n"
                "11. Market structures: perfect competition, monopoly, oligopoly, monopolistic competition.\n"
                "12. Monopoly: single seller, price maker, high profits, inefficient (deadweight loss).\n"
                "13. Perfect competition: many sellers, price takers, normal profit in long run.\n"
                "14. GDP = C + I + G + (X - M). Consumption + Investment + Government + Net Exports.\n"
                "15. Inflation: general price rise over time. Measured by CPI (Consumer Price Index).\n"
                "16. Unemployment types: frictional (between jobs), structural (skills mismatch), cyclical.\n"
                "17. Phillips Curve: inverse relationship between inflation and unemployment (short-run).\n"
                "18. Fiscal policy: government spending and taxation. Expansionary = increase spending.\n"
                "19. Monetary policy: central bank controls money supply and interest rates.\n"
                "20. Interest rates down → borrowing up → spending up → economic growth.\n"
                "21. Trade: comparative advantage means countries specialize in what they produce cheapest.\n"
                "22. Exchange rates: affect imports, exports, and inflation.\n"
                "23. Market failure: externalities, public goods, information asymmetry, monopoly power.\n"
                "24. Government intervention: taxes, subsidies, price controls, regulations.\n"
                "25. Learn real-world examples — economics without context is just theory. 💹"
            ]
        }

        # General quick replies
        self.quick_replies = {
            "hi": "Hello! I'm your MAIS Study Assistant 📚 Ask me about any subject — Math, Physics, Chemistry, English, OOP, Programming, DSA, Statistics, Calculus, Economics — or ask for study tips!",
            "hello": "Hi there! 👋 Ready to study? Ask me about any subject and I'll give you a full guide!",
            "how are you": "I'm always ready to help you study! 💪 Ask me about Math, Physics, OOP, or any other subject.",
            "study tip": "🎯 Top Study Tips:\n1. Pomodoro: 25 mins study → 5 min break. After 4 rounds → 15 min break.\n2. Active recall: close the book and write what you remember.\n3. Spaced repetition: revise after 1 day, 3 days, 7 days, 21 days.\n4. Teach someone else — if you can explain it, you know it.\n5. Mix subjects — don't study one thing for too many hours straight.\n6. Turn off phone notifications during study sessions.\n7. Sleep 7-8 hours — memory consolidation happens during sleep!\n8. Drink water — a hydrated brain performs much better.",
            "exam": "📋 Exam Preparation Strategy:\n1. Start 2 weeks before — not 2 days!\n2. Make a subject-wise timetable.\n3. Do past papers under timed conditions.\n4. Focus on weak subjects first.\n5. Revise strong subjects briefly at the end.\n6. Sleep well the night before.\n7. Eat breakfast — your brain needs fuel.\n8. Read questions carefully before answering.",
            "motivation": "💪 You've got this! Remember:\n→ Every expert was once a beginner.\n→ Progress, not perfection.\n→ One hour of focus beats five hours of distraction.\n→ The pain of hard work is temporary. The pride of success lasts forever.\n→ You're a 2nd semester student doing amazing things — keep going! 🚀",
            "time management": "⏰ Time Management for Students:\n1. Plan your day the night before — 5 mins saves hours.\n2. Use time blocks: 2 hrs study, 30 min break, 2 hrs study.\n3. Hardest task first (eat the frog).\n4. Set realistic daily goals — 3-5 tasks maximum.\n5. Track where your time actually goes — you'll be surprised.\n6. Say no to unnecessary social media during study hours.\n7. Batch similar tasks together.",
            "stress": "🧘 Managing Study Stress:\n1. Take a 10-minute walk — physical movement reduces cortisol.\n2. Deep breathing: 4 sec in, hold 4 sec, out 4 sec.\n3. Break huge tasks into tiny steps — just start with 5 minutes.\n4. Talk to a friend or family member.\n5. Remind yourself: this exam is temporary, your effort is permanent.\n6. Sleep — stress doubles when you're tired.\n7. It's okay to not know everything — focus on what you CAN do. 💙",
            "sleep": "😴 Sleep is Study Tool #1:\n→ 7-8 hours minimum for a student.\n→ Sleep consolidates memory — you literally learn while sleeping.\n→ Staying up all night before exam HURTS your performance.\n→ Consistent sleep schedule beats irregular sleep patterns.\n→ No screens 30 mins before bed — blue light disrupts sleep.",
            "notes": "📓 Note-Taking That Actually Works:\n1. Don't copy — summarize in your own words.\n2. Use headings, bullet points, and diagrams.\n3. The Cornell method: main notes + summary + questions on the side.\n4. Review notes within 24 hours of writing them.\n5. Color code: blue for definitions, red for formulas, green for examples.\n6. Handwritten notes are remembered better than typed.",
            "memorize": "🧠 Memory Techniques:\n1. Spaced repetition — review at increasing intervals.\n2. Mnemonics — create a story or acronym.\n3. Chunking — group info into smaller pieces.\n4. Visualization — picture the concept in your mind.\n5. Teach it — explaining forces deep understanding.\n6. Use flashcards — Anki app is great for this.\n7. Exercise improves memory — even 20 mins of walking.",
            "thanks": "You're welcome! 😊 Good luck with your studies — you're going to do great! 🌟",
            "bye": "Bye! Keep studying smart, not just hard. You've got this! 🚀",
            "weak subject": "For a weak subject:\n1. Spend 2x more time on it than other subjects.\n2. Start from basics — find where your understanding broke.\n3. Do problems one by one, don't skip.\n4. Ask for help — teacher, YouTube, or a classmate.\n5. Practice past exam questions from that specific topic.\n6. Track improvement — seeing progress is motivating!",
            "strong subject": "For a strong subject:\n1. Revise once a week to keep it sharp.\n2. Do a few practice questions to stay confident.\n3. Use that time savings for weaker subjects.\n4. Don't get overconfident — exams can have tricky questions!",
        }

    def get_reply(self, msg):
        msg_lower = msg.lower().strip()

        # Check subject-specific detailed knowledge
        subject_keywords = {
            "math": ["math", "algebra", "geometry", "calculus", "trigonometry", "arithmetic"],
            "physics": ["physics", "force", "energy", "motion", "electricity", "waves", "thermodynamics"],
            "chemistry": ["chemistry", "chem", "organic", "inorganic", "periodic table", "reaction", "acid", "base", "mole"],
            "english": ["english", "grammar", "essay", "writing", "vocabulary", "comprehension", "literature"],
            "oop": ["oop", "object oriented", "class", "object", "inheritance", "polymorphism", "encapsulation", "abstraction", "constructor", "__init__", "self."],
            "programming": ["programming", "python", "coding", "code", "function", "loop", "variable", "debugging", "software"],
            "dsa": ["dsa", "data structure", "algorithm", "linked list", "stack", "queue", "tree", "graph", "sorting", "searching"],
            "statistics": ["statistics", "stats", "mean", "median", "mode", "probability", "distribution", "variance", "hypothesis"],
            "calculus": ["calculus", "derivative", "integral", "limit", "differentiation", "integration"],
            "economics": ["economics", "economy", "supply", "demand", "gdp", "inflation", "market", "micro", "macro"]
        }

        for subject, keywords in subject_keywords.items():
            if any(kw in msg_lower for kw in keywords):
                return random.choice(self.subject_knowledge[subject])

        # Check quick replies
        for key in self.quick_replies:
            if key in msg_lower:
                return self.quick_replies[key]

        # Smart default responses
        defaults = [
            "I can give you a detailed guide on these subjects:\n📐 Math | ⚡ Physics | 🧪 Chemistry | 📝 English | 💻 OOP | 🖥️ Programming | 🔢 DSA | 📊 Statistics | ∫ Calculus | 💹 Economics\n\nJust type the subject name and I'll help you!",
            "Try asking me: 'help with OOP', 'physics guide', 'how to study math', 'exam tips', 'motivation', or 'study tips'! 📚",
            "I'm your MAIS Study Assistant! Ask about any subject or say 'study tip', 'exam', or 'motivation' and I'll guide you. 🎯"
        ]
        return random.choice(defaults)


class PDFHelper:
    """Reads PDF file and gives real summary, mcqs, important points based on actual content."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self._read_pdf()

    def _read_pdf(self):
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(self.file_path)
            text = ""
            for page in reader.pages[:10]:  # read up to 10 pages
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            return text.strip()
        except Exception:
            return ""

    def _extract_sentences(self):
        """Split text into meaningful sentences."""
        import re
        if not self.text:
            return []
        sentences = re.split(r'(?<=[.!?])\s+', self.text)
        # Filter: keep sentences of reasonable length
        return [s.strip() for s in sentences if len(s.strip()) > 30]

    def make_summary(self):
        sentences = self._extract_sentences()
        if not sentences or len(self.text) < 50:
            return (
                "📄 PDF Summary:\n"
                "Could not extract readable text from this PDF (it may be image-based or scanned).\n"
                "Tip: For scanned PDFs, try an OCR tool first. For digital PDFs, the summary will appear here."
            )

        # Take first ~10 meaningful sentences as summary
        summary_sentences = sentences[:10]
        word_count = len(self.text.split())
        char_count = len(self.text)

        summary = f"📄 PDF Summary ({word_count} words extracted):\n\n"
        summary += " ".join(summary_sentences)
        if len(sentences) > 10:
            summary += f"\n\n[...and {len(sentences) - 10} more sentences in the document]"
        return summary

    def make_mcqs(self):
        sentences = self._extract_sentences()
        if not sentences or len(sentences) < 3:
            # Fallback generic MCQs
            return [
                {"q": "What is the best way to study a document?", "options": ["Read once", "Revise multiple times", "Skip it", "Just print it"], "ans": "Revise multiple times"},
                {"q": "What helps remember key points from reading material?", "options": ["Taking notes", "Reading fast", "Skipping summaries", "Ignoring examples"], "ans": "Taking notes"},
                {"q": "How should you approach difficult topics in a PDF?", "options": ["Skip them", "Read slowly and make notes", "Memorize word for word", "Only read headings"], "ans": "Read slowly and make notes"},
                {"q": "What is important in a study document?", "options": ["Definitions", "Examples", "Key concepts", "All of the above"], "ans": "All of the above"},
                {"q": "Best exam preparation from study material?", "options": ["Read once the night before", "Regular revision over days", "Copy everything", "Ignore it"], "ans": "Regular revision over days"},
            ]

        # Generate content-based MCQs from actual sentences
        import re
        mcqs = []

        # Try to create fill-in-blank style questions from sentences
        keywords_in_text = re.findall(r'\b[A-Z][a-z]{3,}\b', self.text)
        unique_keywords = list(dict.fromkeys(keywords_in_text))[:20]

        for i, sentence in enumerate(sentences[:8]):
            words = sentence.split()
            if len(words) < 6:
                continue
            # Pick a keyword to blank out
            # Find a meaningful word (noun/term) to make the question about
            key_word = None
            for w in words[2:]:
                clean = re.sub(r'[^a-zA-Z]', '', w)
                if len(clean) > 4 and clean[0].isupper():
                    key_word = clean
                    break
            if not key_word and unique_keywords:
                key_word = unique_keywords[i % len(unique_keywords)]

            if key_word:
                question = f"According to the document: {sentence[:80]}..."
                # Make wrong options from other keywords
                wrong_opts = [kw for kw in unique_keywords if kw != key_word][:3]
                while len(wrong_opts) < 3:
                    wrong_opts.append(f"Option {len(wrong_opts)+1}")
                import random as rnd
                options = [key_word] + wrong_opts[:3]
                rnd.shuffle(options)
                mcqs.append({"q": question, "options": options, "ans": key_word})

            if len(mcqs) >= 5:
                break

        # If we couldn't generate enough, add generic ones
        while len(mcqs) < 5:
            mcqs.append({
                "q": f"What is a key concept discussed in this document? (Q{len(mcqs)+1})",
                "options": ["Main Topic", "Background Info", "Examples Given", "All of the above"],
                "ans": "All of the above"
            })

        return mcqs[:5]

    def important_topics(self):
        sentences = self._extract_sentences()
        if not sentences:
            return [
                "⚠️ Could not extract text from this PDF (may be scanned/image-based).",
                "💡 Tip: Use a digital/text-based PDF for better analysis.",
                "📌 If this is a scanned document, try OCR tools like Adobe Acrobat or Google Drive.",
                "📝 Once text is extractable, this section will show real key topics from your document."
            ]

        import re
        # Find sentences with important signal words
        signal_words = ['important', 'key', 'note', 'remember', 'essential', 'must', 'critical',
                        'define', 'definition', 'example', 'therefore', 'conclusion', 'result', 'formula']

        important = []
        for s in sentences:
            if any(word in s.lower() for word in signal_words) and len(s) > 40:
                important.append(f"📌 {s.strip()}")
            if len(important) >= 5:
                break

        # If not enough signal sentences, take first meaningful ones
        if len(important) < 4:
            for s in sentences[:6]:
                tag = f"📌 {s.strip()}"
                if tag not in important:
                    important.append(tag)
                if len(important) >= 5:
                    break

        important.append("💡 Tip: Revise these points at least 3 times before your exam.")
        return important
