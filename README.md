<div align="center">

# 🤖 Reinforcement Learning Assessment

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Reinforcement Learning](https://img.shields.io/badge/Reinforcement_Learning-FF4B4B?style=for-the-badge&logo=openai&logoColor=white)

*An assessment focused on the core mathematical and conceptual foundations of Reinforcement Learning, state tracking, reward functions, and agent-environment interaction loops applied to food delivery dispatch optimization.*

---

</div>

## 📑 Repository Structure

This repository is organized into four distinct sections to clearly demonstrate theoretical understanding and practical programming implementation.

### 📖 Section A: Concept Application
**File:** [Section_A_Concept_Application.ipynb](./Section_A_Concept_Application.ipynb)
- Detailed comparisons explaining why RL out-performs traditional supervised and unsupervised learning for dynamic, real-time problems.
- Identification of core RL components (Agent, Environment, Actions, Rewards) within a food delivery dispatch context.
- Parallels drawn between Game AI and autonomous delivery systems.

### 💻 Section B: Practical Coding Tasks
**File:** [Section_B_Practical_Coding_Tasks.ipynb](./Section_B_Practical_Coding_Tasks.ipynb)
- **Task 1:** Built a programmatic reward function that deducts points for late deliveries and calculates final agent reward.
- **Task 2:** Implemented an Agent State Tracker using Python dictionaries to maintain the agent's location, total rewards, and order count.
- **Task 3:** Built an Action-Reward logger to iterate through predefined sequences of actions and accumulate step-rewards.
- **Task 4:** Developed a complete Object-Oriented DeliveryEnvironment class featuring an internal step(action) method simulating environment state transitions.

### 🚀 Section C: Mini Capstone Project
**File:** [Section_C_Mini_Capstone.py](./Section_C_Mini_Capstone.py)
- A fully interactive, console-based **Food Delivery RL Concept Simulator**.
- Combines the state tracking, reward accumulation, and environment interaction concepts into a single working DeliverySimulator class.
- Run interactive episodes, view step-by-step logs of the agent's physical movement, and track cumulative statistical performance across multiple episodes.

### 🤖 Section D: AI-Augmented Learning
**File:** [Section_D_AI_Augmented_Learning.ipynb](./Section_D_AI_Augmented_Learning.ipynb)
- Showcases an AI-generated attempt at a Reinforcement Learning state tracker.
- Includes a debugging segment where I identified and manually fixed a logic flaw (the AI completely forgot to update the agent's positional location in the state dictionary during action transitions).

---

## ⚙️ How to Run the Capstone Simulator

The Mini Capstone Project (Section C) is an interactive console application. Run it directly from your terminal:

`ash
python Section_C_Mini_Capstone.py
`
