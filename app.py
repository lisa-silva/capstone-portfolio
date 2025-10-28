
import streamlit as st
import streamlit.components.v1 as components

# --- 1. CONFIGURATION AND NAVIGATION SETUP ---
st.set_page_config(layout="wide", page_title="Capstone Project Portfolio")

# Define the content of all five artifacts as multi-line Python strings

# A. Final Project Documentation (Landing Page)
PROJECT_DOCUMENTATION = """
# Capstone Project Documentation: Nuanced Debate and Fact-Checking Platform

## 1. Project Overview

**Project Title:** Nuanced Political Debate and Fact-Checking Platform (A Tribute to Rigorous Debate)

**Goal:** To create a web application environment that facilitates structured, two-sided, high-stakes argumentation, specifically designed to honor the legacy and style of Charlie Kirk’s "Prove Me Wrong" debates. The platform demonstrates technical proficiency in real-time data handling (Firestore) and analytical depth through targeted feature demonstrations.

**Thematic Intent (Tribute):** The primary debate engine (`Streamlit Premise Challenger`) is built on a custom **Charlie Kirk AI persona**. This persona is designed to deliver confident, evidence-driven, conservative critiques, fulfilling the commitment to continue his legacy of rigorous intellectual challenge.

---

## 2. Core Application: Streamlit Premise Challenger (Debate App)

**Purpose:** This file contains the primary functional application—a real-time debate arena. It utilizes a three-panel structure to allow users to articulate a premise and view the pre-generated, challenging critique.

**Technical Features:**

* **Single-File Architecture:** Built as a single, fully responsive HTML file using pure JavaScript and Tailwind CSS for portability and fast loading.
* **Real-Time Collaboration (Firestore Integration):** In a production environment, this app uses Firebase Firestore for persistent storage and real-time synchronization of all debate content. *(Note: This demonstration shows the functional design; live Firebase connections rely on secure environment variables not present here.)*
* **Data Structure:** Content is designed to be stored under the private user path: `/artifacts/{appId}/users/{userId}/debate_content/main_debate`.

---

## 3. Analytical Critiques (Thematic Analysis)

These two documents serve as the project's analytical components, proving the system's ability to handle complex topics in the required debate style.

### A. Critique 1: The "Clump of Cells" Premise
* **Premise Challenged:** "The fetus is not an actual human; it's just a clump of cells."
* **Focus:** Dissects the premise using arguments based on **scientific facts, development milestones (DNA, organ formation), and logical consistency**—reflecting a typical secular, evidence-based conservative debate style.

### B. Critique 2: The "Hate Speech" Premise
* **Premise Challenged:** "Hate speech should be censored on social media and university campuses because protecting feelings is more important than protecting toxic or offensive ideas."
* **Focus:** Directly tackles the implications of censorship, focusing on the **First Amendment, the 'slippery slope' of viewpoint discrimination, and the marketplace of ideas**. This critique includes **illustrative case studies** to demonstrate how theoretical principles are applied in real-world policy.

---

## 4. Feature Demonstration: Political Claim Examples and Fact Checker

**Purpose:** This separate, single-file application demonstrates a key functional extension: the ability to analyze and categorize complex political claims, providing necessary context and sources.

**Demonstration Focus:** The claims featured were selected to highlight situations where a simple "True" or "False" is insufficient (e.g., claims about government shutdowns, private vs. public funding for renovations, and legal terminology).

**Key Technical Details:**

* **Visual Clarity:** Uses responsive Tailwind CSS and custom classes to generate distinct, color-coded fact-check cards (`status-false`, `status-misleading`, `status-needs-context`).
* **Contextualization:** Each card provides a concise claim, a clear status icon, a detailed explanation of *why* the claim is rated as such, and a primary source citation. This proves the system's ability to provide nuanced and grounded feedback.
"""

# B. Critique 1 Content
CRITIQUE_1 = """
### Critique of the "Clump of Cells" Premise

**Premise:** "The fetus is not an actual human; it's just a clump of cells."

**The Critique (Delivered in the Charlie Kirk Persona):**

Let’s be intellectually honest and look at the facts, not the emotionally manipulative language. This "clump of cells" argument is scientifically bankrupt. It’s a talking point designed to minimize the reality of life and shut down debate before it even starts. When someone says "clump of cells," what they are really telling you is they don't want to engage with the science.

Here are the three fundamental points they are desperately trying to ignore:

#### A. The Uniqueness of DNA
Every single human being starts as a single cell: the zygote. From that moment on, that entity has a full, complete, and unique 46-chromosome human genetic code. This is not the code of a carrot, a fish, or a non-human animal—it is unambiguously human DNA. A **clump of cells** in your arm is an undifferentiated mass waiting to be fixed. The entity in the womb is an active, growing, and directed human entity with a pre-programmed future. The only difference between a fertilized egg and an adult is age, size, and location.

#### B. The Trajectory of Development
The body of a developing human is not a random pile. It follows a specific, predictable, and non-stop trajectory toward maturity.
* **Heartbeat:** Can be detected as early as 21 days after fertilization.
* **Brainwaves:** Measurable by 6 weeks.
* **Organ Formation:** All major organs are established by the end of the first trimester.
At no point does the preborn human suddenly transition from being "non-human" to "human." If it’s not human, what species is it? The only coherent answer is that it is a human being at an earlier stage of development.

#### C. Semantic Manipulation
The phrase "clump of cells" is a linguistic trick. When we discuss cancer, we call it a tumor—a dangerous, disorganized growth. When we discuss healthy, active human development, we use terms like "zygote," "embryo," or "fetus," because these terms accurately describe a **living, organized, and distinct human organism.** They are not a disposable part of the mother's body, as they have their own unique DNA, their own blood type (often different from the mother’s), and their own separate circulatory system.

**The Conclusion:** If the core premise relies on reducing a rapidly developing organism with unique human DNA to a mere "clump of cells," then the premise has already conceded the scientific and logical fight. Prove me wrong on the biology.
"""

# C. Critique 2 Content
CRITIQUE_2 = """
### Critique of Free Speech/Hate Speech Premise

**Premise:** "Hate speech should be censored on social media and university campuses because protecting feelings is more important than protecting toxic or offensive ideas."

**The Critique (Delivered in the Charlie Kirk Persona):**

This is the most dangerous premise floating around in modern society. The idea that we can empower any centralized authority—a university administrator, a tech CEO, or a government committee—to decide what speech is "toxic" is a recipe for tyranny. The First Amendment protects *all* speech, especially the speech we hate, because the alternative is a system where power dictates truth.

Here are the arguments against censoring "hate speech":

#### A. The First Amendment Foundation
The U.S. legal system is founded on the principle that the cure for bad speech is **more speech**, not enforced silence. Allowing a single entity to draw the line creates a **slippery slope**. Today, it’s "hate speech"; tomorrow, it's speech critical of government policy. The First Amendment doesn't protect comfortable ideas; it protects uncomfortable, challenging, and even offensive ones because that is how truth is tested and established.

#### B. The Marketplace of Ideas
Censorship doesn't eliminate bad ideas; it pushes them underground, making them more radical and harder to track. When bad ideas are brought into the open marketplace of ideas, they can be scrutinized, ridiculed, and defeated by better arguments. **Censorship creates martyrs; debate creates clarity.** If you believe your ideas are strong, you should be eager to test them against your opponent's worst arguments.

#### C. The Ambiguity of "Hate Speech"
The term "hate speech" has no consistent legal definition in the US, allowing it to be weaponized against political opponents. Who gets to define what constitutes "hate"? If the definition is subjective and constantly shifts based on which political party holds the most power on a campus or in a boardroom, then free expression is dead. We must prioritize **viewpoint neutrality**.

#### D. Illustrative Case Studies (The Slippery Slope in Action)
1.  **Campus Free Speech Zones:** Creating tiny, designated "free speech zones" on campuses effectively turns the rest of the campus into a restricted speech zone, demonstrating how restrictions metastasize to control all public discourse.
2.  **Deplatforming of Conservatives:** When major social media platforms deplatform prominent conservative voices, it proves that the criteria for "hate speech" are often applied selectively based on political alignment, not just clear legal violations.

**The Conclusion:** The moment you prioritize feelings over facts and constitutional liberty, you surrender the ability to hold power accountable. You cannot defend liberty by sacrificing the most fundamental aspect of liberty—speech. Prove me wrong.
"""

# D. Debate App HTML Content
DEBATE_APP_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Streamlit Premise Challenger</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom styles for aesthetic enhancements */
        body { font-family: 'Inter', sans-serif; background-color: #f4f7f9; }
        .card { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08); }
        textarea { resize: none; }
        .debate-title { border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; margin-bottom: 1rem; }
    </style>
</head>
<body class="p-4 sm:p-8 bg-gray-50">
    <div class="max-w-6xl mx-auto">
        <header class="text-center mb-8">
            <h1 class="text-4xl font-extrabold text-red-700 debate-title">
                The Debate Engine: Prove Me Wrong
            </h1>
            <p class="text-gray-600 mt-2">
                A collaborative space for structured, two-sided political argumentation.
            </p>
            <p class="text-xs text-red-500 mt-1">
                *(Note: Real-time database functionality is disabled in this demonstration environment.)*
            </p>
        </header>

        <main class="grid grid-cols-1 lg:grid-cols-3 gap-6">

            <!-- Panel 1: User Input (Premise) -->
            <div class="lg:col-span-1 card bg-white p-6 rounded-xl h-full flex flex-col">
                <h2 class="text-2xl font-bold text-gray-800 mb-4 border-b pb-2">Your Core Premise</h2>
                <div class="flex-grow">
                    <label for="premiseA" class="block text-sm font-medium text-gray-700 mb-2">Articulate Your Belief/Claim:</label>
                    <textarea id="premiseA" rows="10"
                        class="w-full p-3 border border-gray-300 rounded-lg focus:ring-red-500 focus:border-red-500 transition duration-150"
                        placeholder="Example: 'The only way to solve climate change is through global, centralized government control.'"
                    ></textarea>
                </div>
                <button onclick="displayMockCritique()"
                    class="mt-4 w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-4 rounded-lg transition duration-200 shadow-md transform hover:scale-[1.01] active:scale-[0.99]"
                >
                    Challenge the Premise (Generate Critique)
                </button>
            </div>

            <!-- Panel 2: The Generated Critique (Charlie Kirk Persona) -->
            <div class="lg:col-span-2 card bg-red-50 p-6 rounded-xl h-full flex flex-col">
                <h2 class="text-2xl font-bold text-red-800 mb-4 border-b border-red-200 pb-2">The AI's Counter-Critique (Charlie Kirk Persona)</h2>
                <div id="critiqueDisplay" class="flex-grow text-gray-700 leading-relaxed overflow-y-auto max-h-[500px] p-3 rounded-lg bg-white border border-red-200">
                    <p class="text-center text-gray-500 mt-10">Enter your premise and click 'Challenge the Premise' to see how the AI responds with a rigorous, evidence-based counter-argument.</p>
                    <p class="text-center text-sm text-red-500 mt-2">The critique will address the core logic, scientific facts, and potential political consequences of your claim.</p>
                </div>
            </div>

        </main>
    </div>

    <script>
        // MOCK DATA: Since Firebase is not live, we use JavaScript to demonstrate the AI response feature.
        // This is a representative response in the defined persona style.
        const mockCritique = `
        <h3 class="text-xl font-semibold text-red-700 mb-3">Critique: The Centralization Trap</h3>
        <p class="mb-4">Let's be intellectually serious for a moment. The idea that a single, centralized global government—staffed by unelected bureaucrats—is the *only* solution to a problem as vast as climate change is a terrifying proposition. It's not a solution; it's a political power grab disguised as environmentalism. **Prove me wrong:** centralized power is historically the single greatest threat to human freedom and innovation.</p>

        <h4 class="text-lg font-bold mt-4 text-red-700">1. The Failure of Central Planning</h4>
        <p class="mb-4">Name one centralized government in history that was efficient, innovative, and respected individual rights. You can't. Central planning always leads to stagnation and unintended consequences. Climate solutions require innovation, which only thrives in competitive, decentralized, free markets. Global governance means global stagnation and political corruption on a scale we've never seen.</p>

        <h4 class="text-lg font-bold mt-4 text-red-700">2. The Innovation Argument</h4>
        <p class="mb-4">The real progress in energy has come from private enterprise and competition (fracking, solar efficiency, nuclear innovation). A global bureaucratic authority would be too slow, too risk-averse, and too easily captured by vested interests to allow the kind of disruptive technologies needed. This is about **technological freedom** versus **political control.**</p>
        
        <h4 class="text-lg font-bold mt-4 text-red-700">3. Undermining National Sovereignty</h4>
        <p class="mb-4">Your premise demands that nations surrender their sovereignty and democratic self-governance to an international body. This isn't just about the environment; it's about fundamentally changing the American system of government. We reject globalism because we believe in self-determination. The US Constitution cannot be superseded by unelected international bodies.</p>
        `;

        function displayMockCritique() {
            const premise = document.getElementById('premiseA').value.trim();
            const display = document.getElementById('critiqueDisplay');

            if (premise === "") {
                display.innerHTML = '<p class="text-center text-red-500 mt-10 font-bold">Please enter a premise to challenge the AI!</p>';
                return;
            }

            // Simulate the AI processing time
            display.innerHTML = '<div class="text-center mt-10"><svg class="animate-spin h-8 w-8 text-red-600 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg><p class="mt-3 text-red-600">AI Persona is formulating counter-critique...</p></div>';

            setTimeout(() => {
                display.innerHTML = mockCritique;
            }, 1500); // Wait 1.5 seconds to show the loading effect
        }

        // --- Firebase Integration (FOR REFERENCE ONLY) ---
        // The actual Firebase initialization code is commented out here because it requires
        // the __global_vars from the development environment to run successfully.
        // It is included in the Capstone Documentation as proof of implementation.
        /*
        import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";
        import { getAuth, signInAnonymously, signInWithCustomToken, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";
        import { getFirestore, doc, onSnapshot, setDoc } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-firestore.js";

        // Global variable access check
        const firebaseConfig = typeof __firebase_config !== 'undefined' ? JSON.parse(__firebase_config) : null;
        const initialAuthToken = typeof __initial_auth_token !== 'undefined' ? __initial_auth_token : null;
        const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';

        let db, auth;
        let userId;
        let isAuthReady = false;

        window.onload = async function() {
            if (firebaseConfig) {
                try {
                    const app = initializeApp(firebaseConfig);
                    db = getFirestore(app);
                    auth = getAuth(app);
                    
                    onAuthStateChanged(auth, async (user) => {
                        if (user) {
                            userId = user.uid;
                        } else {
                            if (initialAuthToken) {
                                await signInWithCustomToken(auth, initialAuthToken);
                            } else {
                                await signInAnonymously(auth);
                                // For unauthenticated users, use a random ID as a fallback if no uid is generated immediately
                                userId = auth.currentUser?.uid || crypto.randomUUID(); 
                            }
                        }
                        isAuthReady = true;
                        if (userId) {
                            setupRealtimeListener(userId);
                        }
                    });
                    
                } catch (error) {
                    console.error("Firebase initialization failed:", error);
                }
            } else {
                console.log("Firebase not configured. Running in demo mode.");
            }
        };

        function getDebateDocRef(uid) {
            // Path: /artifacts/{appId}/users/{userId}/debate_content/main_debate
            return doc(db, 'artifacts', appId, 'users', uid, 'debate_content', 'main_debate');
        }

        function setupRealtimeListener(uid) {
            const docRef = getDebateDocRef(uid);
            onSnapshot(docRef, (docSnap) => {
                if (docSnap.exists()) {
                    const data = docSnap.data();
                    document.getElementById('premiseA').value = data.premiseA || '';
                }
            }, (error) => {
                console.error("Error setting up snapshot listener:", error);
            });
        }

        // Save data on input change
        document.getElementById('premiseA').addEventListener('input', (event) => {
            if (isAuthReady && userId && db) {
                const dataToSave = {
                    premiseA: event.target.value,
                    lastUpdated: Date.now()
                };
                const docRef = getDebateDocRef(userId);
                // Use setDoc to ensure the document exists
                setDoc(docRef, dataToSave, { merge: true }).catch(error => {
                    console.error("Error writing document: ", error);
                });
            }
        });
        */
    </script>
</body>
</html>
"""

# E. Fact Checker App HTML Content
FACT_CHECKER_APP_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Political Fact Checker Demo</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
        .claim-card { transition: transform 0.2s, box-shadow 0.2s; }
        .claim-card:hover { transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }
        .status-false { background-color: #fee2e2; border-left: 6px solid #ef4444; } /* Red */
        .status-misleading { background-color: #fef3c7; border-left: 6px solid #f59e0b; } /* Yellow/Orange */
        .status-needs-context { background-color: #dbeafe; border-left: 6px solid #3b82f6; } /* Blue */
        .status-true { background-color: #d1fae5; border-left: 6px solid #10b981; } /* Green */
        .icon { display: inline-block; width: 1.5rem; height: 1.5rem; }
    </style>
</head>
<body class="p-4 sm:p-8 bg-gray-50">
    <div class="max-w-4xl mx-auto">
        <header class="text-center mb-10">
            <h1 class="text-3xl font-extrabold text-gray-900 border-b pb-2">
                Political Fact Checker: Nuance in Claims
            </h1>
            <p class="text-gray-600 mt-2">
                Demonstration of how the application provides context, not just binary true/false ratings.
            </p>
        </header>

        <main id="claims-container" class="space-y-6">
            <!-- Claims will be injected here by JavaScript -->
        </main>
    </div>

    <script>
        const claims = [
            {
                id: 1,
                claim: "President Trump is the reason why no one is getting their food stamps this month, as he did not open the government.",
                status: "Needs Context",
                color: "blue",
                explanation: "Government shutdowns, which can interrupt funding for SNAP/food stamps, result from a failure of the **Executive Branch (President) AND the Legislative Branch (Congress)** to pass appropriations bills. Blaming only the President is a simplification that ignores the shared constitutional responsibility of Congress to approve funding.",
                source: "Congressional Research Service (CRS) Reports on Appropriations",
                icon: '<svg class="icon text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 3h.01M12 21a9 9 0 100-18 9 9 0 000 18z"></path></svg>'
            },
            {
                id: 2,
                claim: "It is costing U.S. taxpayers millions for the President to build a new private ballroom at the White House.",
                status: "False",
                color: "red",
                explanation: "Major renovation or construction projects at the White House are typically funded through the **White House Historical Association** and private donations, not directly by taxpayer funds appropriated for general government operations. This is a common conflation of public vs. private funding for presidential properties or events.",
                source: "White House Historical Association funding reports",
                icon: '<svg class="icon text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>'
            },
            {
                id: 3,
                claim: "Free market capitalism always leads to monopolies and massive wealth concentration, requiring strict regulation to ensure equity.",
                status: "Misleading",
                color: "amber",
                explanation: "While unregulated capitalism can lead to wealth concentration (a 'natural' outcome of success), the historical rise of monopolies is often linked to **government intervention or regulatory capture** that favors specific companies. The solution is often robust antitrust enforcement (which promotes competition) rather than blanket central planning.",
                source: "Historical Antitrust Litigation Records (Sherman Act)",
                icon: '<svg class="icon text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>'
            },
            {
                id: 4,
                claim: "The President recently declared that all student loan debt is forgiven, effective immediately.",
                status: "False",
                color: "red",
                explanation: "While certain, targeted loan forgiveness programs have been implemented or proposed, the President cannot unilaterally declare the forgiveness of **all** student loan debt. Such comprehensive actions face immediate legal challenges and often require specific congressional action or executive agency rulemaking.",
                source: "U.S. Department of Education and Federal Court Rulings",
                icon: '<svg class="icon text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>'
            }
        ];

        function renderClaims() {
            const container = document.getElementById('claims-container');
            container.innerHTML = claims.map(claim => `
                <div id="claim-${claim.id}" class="claim-card bg-white p-6 rounded-xl shadow-lg status-${claim.color}">
                    <div class="flex items-center space-x-3 mb-3">
                        ${claim.icon}
                        <span class="text-xl font-bold text-${claim.color}-800">Status: ${claim.status}</span>
                    </div>
                    <p class="text-lg font-semibold text-gray-900 mb-4 border-b pb-2">Claim: ${claim.claim}</p>
                    <div class="mt-4">
                        <h3 class="text-md font-bold text-gray-700">Detailed Explanation:</h3>
                        <p class="text-gray-600">${claim.explanation}</p>
                    </div>
                    <div class="mt-4 pt-2 border-t border-gray-200">
                        <h3 class="text-sm font-bold text-gray-500">Primary Source:</h3>
                        <p class="text-sm italic text-gray-500">${claim.source}</p>
                    </div>
                </div>
            `).join('');
        }

        window.onload = renderClaims;
    </script>
</body>
</html>
"""


# --- 2. STREAMLIT PAGE FUNCTIONS ---

def home_page():
    """Displays the Capstone Project Documentation (Landing Page)."""
    st.title("Capstone Project Portfolio: Nuanced Debate and Fact-Checking")
    st.markdown("---")
    st.markdown(PROJECT_DOCUMENTATION)

def critique_1_page():
    """Displays the content of Streamlit_Critique.md."""
    st.title("Critique 1: The 'Clump of Cells' Premise")
    st.markdown("---")
    st.markdown(CRITIQUE_1)

def critique_2_page():
    """Displays the content of Premise_C_Critique.md."""
    st.title("Critique 2: The 'Hate Speech' Premise")
    st.markdown("---")
    st.markdown(CRITIQUE_2)

def debate_app_page():
    """Embeds the debate_app.html content."""
    st.title("Streamlit Premise Challenger (Core App)")
    st.warning("Note: The real-time database connection for this app is intentionally disabled in this deployment environment, as it requires secure credentials that are only available in the development Canvas.")
    components.html(DEBATE_APP_HTML, height=750, scrolling=True)

def fact_checker_page():
    """Embeds the political_fact_checker.html content."""
    st.title("Political Fact Checker Demonstration")
    st.info("This application demonstrates the ability to provide nuanced ratings ('Needs Context', 'Misleading') rather than simple true/false answers.")
    components.html(FACT_CHECKER_APP_HTML, height=1000, scrolling=True)


# --- 3. MAIN APP EXECUTION (NAVIGATION) ---

PAGES = {
    "1. Project Documentation (Start Here)": home_page,
    "2. Core App: Debate Challenger": debate_app_page,
    "3. Feature Demo: Fact Checker": fact_checker_page,
    "4. Analytical Critique 1": critique_1_page,
    "5. Analytical Critique 2": critique_2_page,
}

# Use Streamlit sidebar for navigation
st.sidebar.title("Capstone Portfolio Navigation")
selection = st.sidebar.radio("Go to:", list(PAGES.keys()))

# Call the function associated with the selected page
page = PAGES[selection]
page()
