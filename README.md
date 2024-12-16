# Swarm Architecture Generator

## Overview

The **Swarm Architecture Generator** is a Python-based system designed to generate organizational structures and swarm AI agent architectures. It uses Groq’s API and a custom-defined agent-based architecture to automatically create Python code for different organizational use cases. The system is modular and supports various types of swarm architectures, such as **Hierarchical**, **Parallel**, **Sequential**, and **Spreadsheet-like** structures.

### How It Works

The architecture consists of two main components:

1. **Organizational Designer Agent**: 
   - This agent generates an organizational structure based on predefined templates and missions for various use cases (e.g., customer support, e-commerce, finance).
   
2. **Swarm Code Generator Agent**: 
   - After the organizational structure is generated, the Swarm Code Generator agent uses predefined templates to generate Python code for various swarm architectures. This code is used to build agent workflows, such as hierarchical team structures or parallel task processes.

### System Components

- **Groq Client**: Communicates with the Groq API to leverage LLM capabilities.
- **Agents**: Agents are Python objects responsible for specific tasks in the workflow (e.g., organizational design, swarm code generation).
- **Graph Workflow**: Defines how agents interact and pass data in the workflow.
- **Node Types**: Different types of nodes (agents, tasks) that can be included in a swarm architecture.
- **Swarm System**: A system composed of multiple agents working together, following a defined flow to accomplish a task.

### Swarm Architectures Supported

- **Hierarchical**: A tiered agent structure where supervisors manage teams, team leads assist with execution, and workers complete tasks.
- **Parallel**: Multiple agents working independently on different tasks simultaneously.
- **Sequential**: A linear agent structure where tasks are completed one after the other.
- **Spreadsheet-like**: Agents process data in parallel for each column, akin to a spreadsheet.

## How to Use

1. **Set Up**: 
   - Install required dependencies (e.g., `groq`, `swarms`, `gradio`, etc.).
   - Set your Groq API key in the environment variables.
   
2. **Run the Code**:
   - Once the environment is set up, run the `main_loop()` function to begin generating organizational structures and swarm code.

3. **Outputs**:
   - The system generates Python code for swarm architectures and writes it to a `.py` file.
   - The file is saved with a timestamp, and each time the loop runs, a new file is created.

4. **Customization**:
   - Modify the agent prompts and system configurations to define new organizational structures or swarm architectures.

## Example Output

The system will output Python code like the following for different swarm architectures:

```python
# Hierarchical structure template
supervisor = Agent(agent_name="Supervisor", system_prompt="Oversee the team", task="Manage team")
team_lead = Agent(agent_name="Team Lead", system_prompt="Assist with task execution", task="Lead team")
worker = Agent(agent_name="Worker", system_prompt="Perform assigned tasks", task="Execute tasks")
workflow = GraphWorkflow()
workflow.add_node(Node(id="supervisor", type=NodeType.AGENT, agent=supervisor))
workflow.add_node(Node(id="team_lead", type=NodeType.AGENT, agent=team_lead))
workflow.add_node(Node(id="worker", type=NodeType.AGENT, agent=worker))

```

To-Dos
While the system is functional, there are some improvements and features to be added in future versions:

1. Dynamic Prompt Injection of Variables
Current Limitation: The system generates static prompts based on predefined templates.
Goal: Implement dynamic prompt injection, where the organizational structure and agent tasks can be dynamically altered based on variables (e.g., project-specific data, real-time user input).
Approach: Pass variables such as department names, task priorities, and agent roles into the agent prompts at runtime, making the system more adaptable to diverse use cases.
2. Rate Limit Friendly Timing Measures
Current Limitation: The system executes agent tasks in a synchronous manner, which may result in high API request frequency and potential rate-limiting issues.
Goal: Implement rate-limit-friendly timing measures, such as introducing time delays between agent task executions, to avoid hitting API rate limits.
Approach: Use asynchronous calls or implement pauses between requests to ensure that the system doesn't overload the API or cause excessive delays.
3. Extend Agent Types
Current Limitation: The system currently supports basic agent types like Worker, Supervisor, and Team Lead.
Goal: Add more agent types and roles to cover a wider variety of organizational and task structures.
Approach: Create more specialized agents for different industries (e.g., marketing, healthcare, AI research) and workflows (e.g., DevOps, project management).
4. Improve Workflow Flexibility
Current Limitation: The workflow between agents is predefined, which limits flexibility.
Goal: Allow users to define custom agent flows and connections based on their needs.
Approach: Implement a more flexible workflow definition system that allows users to visually or programmatically define the connections and dependencies between agents.
5. User Interface for Configurations
Current Limitation: The system runs entirely from the command line without a graphical user interface.
Goal: Provide a simple user interface (UI) for users to select organizational structures, agent roles, and swarm architecture templates.
Approach: Use a framework like Gradio or Streamlit to create an easy-to-use UI for generating configurations.
Conclusion
This Swarm Architecture Generator is a powerful tool for automatically designing and generating code for various AI-driven swarm systems. With future improvements and dynamic capabilities, it can be expanded to handle a broader range of use cases and integrate seamlessly into real-world organizational workflows.

For contributions, bug fixes, or feature requests, please feel free to open an issue or submit a pull request.
