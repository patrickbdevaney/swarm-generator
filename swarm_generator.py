import os
import json
from dotenv import load_dotenv
from swarms import Agent, AgentRearrange, GraphWorkflow, Node, NodeType
from groq import Groq
import gradio as gr
from datetime import datetime

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Initialize Groq client
client = Groq(api_key=api_key)

# Define the Groq-based model
class GroqModel:
    def __init__(self, client):
        self.client = client

    def __call__(self, prompt):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a Python code expert."},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

# Initialize the model
model = GroqModel(client=client)

# Define agents with updated system prompts
organizational_designer = Agent(
    agent_name="Organizational Designer",
    system_prompt="""
    You are an expert in creating organizational structures. Choose one tuple from the following list of organizations, missions, agents, use cases, and create a new configuration with a novel organization, mission, agent, use case different from one of the following, and then choose an appropriate swarm architecture:

    - Organization: Customer Service
      Mission: Provide assistance through automated responses
      Agent: Chatbot Agent
      Use Case: Customer support
      Swarm Architecture: Hierarchical

    - Organization: AI Research
      Mission: Collect data for research purposes
      Agent: Data Collection Agent
      Use Case: Data gathering for AI
      Swarm Architecture: Parallel

    - Organization: E-commerce
      Mission: Manage and track inventory
      Agent: Inventory Management Agent
      Use Case: Inventory tracking
      Swarm Architecture: Sequential

    - Organization: Healthcare
      Mission: Track and manage patient information
      Agent: Patient Tracking Agent
      Use Case: Patient management
      Swarm Architecture: Hierarchical

    - Organization: Finance
      Mission: Assess financial risks for investments
      Agent: Risk Assessment Agent
      Use Case: Investment evaluation
      Swarm Architecture: Parallel

    - Organization: Marketing
      Mission: Manage ad campaigns and analyze results
      Agent: Ad Campaign Agent
      Use Case: Campaign analysis
      Swarm Architecture: Spreadsheet
    """,
    llm=model,
    max_loops=1,
)

swarm_code_generator = Agent(
    agent_name="Swarm Code Generator",
    system_prompt="""
start wwith this boilerplate
import os
import json
from dotenv import load_dotenv
from swarms import Agent, AgentRearrange, GraphWorkflow, Node, NodeType
from groq import Groq
import gradio as gr
from datetime import datetime

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

# Initialize Groq client
client = Groq(api_key=api_key)

# Define the Groq-based model
class GroqModel:
    def __init__(self, client):
        self.client = client

    def __call__(self, prompt):
        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a Python code expert."},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

# Initialize the model
model = GroqModel(client=client)
then,


 generate Python code to implement the swarm ai agent architecture for the organization:

    Swarm Architecture Templates:

    - Hierarchical:
      # Hierarchical structure template
      supervisor = Agent(agent_name="Supervisor", system_prompt="Oversee the team", task="Manage team")
      team_lead = Agent(agent_name="Team Lead", system_prompt="Assist with task execution", task="Lead team")
      worker = Agent(agent_name="Worker", system_prompt="Perform assigned tasks", task="Execute tasks")
      workflow = GraphWorkflow()
      workflow.add_node(Node(id="supervisor", type=NodeType.AGENT, agent=supervisor))
      workflow.add_node(Node(id="team_lead", type=NodeType.AGENT, agent=team_lead))
      workflow.add_node(Node(id="worker", type=NodeType.AGENT, agent=worker))

    - Parallel:
      # Parallel structure template
      agent1 = Agent(agent_name="Agent 1", system_prompt="Process task 1", task="Process data")
      agent2 = Agent(agent_name="Agent 2", system_prompt="Process task 2", task="Process data")
      workflow = GraphWorkflow()
      workflow.add_node(Node(id="agent1", type=NodeType.AGENT, agent=agent1))
      workflow.add_node(Node(id="agent2", type=NodeType.AGENT, agent=agent2))

    - Sequential:
      # Sequential structure template
      agent1 = Agent(agent_name="Agent 1", system_prompt="Process task 1", task="Process data")
      agent2 = Agent(agent_name="Agent 2", system_prompt="Process task 2", task="Process data")
      workflow = GraphWorkflow()
      workflow.add_node(Node(id="agent1", type=NodeType.AGENT, agent=agent1))
      workflow.add_node(Node(id="agent2", type=NodeType.AGENT, agent=agent2))
      workflow.add_edge("agent1", "agent2")

    - Spreadsheet:
      # Spreadsheet-like structure template
      agent1 = Agent(agent_name="Agent 1", system_prompt="Process data for column 1", task="Process column")
      agent2 = Agent(agent_name="Agent 2", system_prompt="Process data for column 2", task="Process column")
      workflow = GraphWorkflow()
      workflow.add_node(Node(id="agent1", type=NodeType.AGENT, agent=agent1))
      workflow.add_node(Node(id="agent2", type=NodeType.AGENT, agent=agent2))

    - Default:
      # Default structure template
      agent1 = Agent(agent_name="Agent 1", system_prompt="General task processing", task="Handle task")
      workflow = GraphWorkflow()
      workflow.add_node(Node(id="agent1", type=NodeType.AGENT, agent=agent1))

      here is an example of defining swarm flow and making a swarm system:

      # Define flow and swarm system
agents = [first_draft_agent, compatibility_agent, qa_agent]
flow = f"{first_draft_agent.agent_name} -> {compatibility_agent.agent_name} -> {qa_agent.agent_name}"

code_refinement_system = AgentRearrange(
    name="PythonCodeRefinementSystem",
    description="Swarm system for generating, refining, and assessing Python programs",
    agents=agents,
    flow=flow,
    max_loops=1,
    output_type="all",
)

# Function to process user input through the agent system
def process_prompt(prompt):
    try:
        # First draft
        draft_code = first_draft_agent(prompt)
        
        # Compatibility review and framework suggestions
        refined_code = compatibility_agent(draft_code)
        
        # Final code after QA
        final_code = qa_agent(refined_code)
        
        return final_code
    except Exception as e:
        return f"Error: {e}"


      def chat_ui(user_input, chat_history):
    global conversation_history, is_first_launch

    # Process input through agent system
    ai_response = process_prompt(user_input)

    # Update conversation history
    chat_history.append(("User", user_input))
    chat_history.append(("AI", ai_response))
    conversation_history.append({"user": user_input, "ai": ai_response})

    # Only trigger sharing on the first launch
    share_flag = is_first_launch
    if is_first_launch:
        is_first_launch = False

    return chat_history, share_flag
      
    """,
    llm=model,
    max_loops=1,
)

# Define agent flow for the system
agents = [organizational_designer, swarm_code_generator]
flow = f"{organizational_designer.agent_name} -> {swarm_code_generator.agent_name}"

# Define the swarm system
swarm_system = AgentRearrange(
    name="SwarmCodeGenerationSystem",
    description="Swarm system for generating and refining Python programs for organizational structures and swarms",
    agents=agents,
    flow=flow,
    max_loops=1,
    output_type="all",
)

# Main loop to continuously run the system
# Main loop to continuously run the system
def main_loop():
    while True:
        try:
            # Step 1: Generate organizational structure using Agent 1
            org_structure = organizational_designer("Generate an organizational structure for a new project.")
            if "Error" in org_structure:
                print(f"Error generating organizational structure: {org_structure}")
              

            print(f"Generated Organizational Structure: {org_structure}")  # Debugging output

            # Step 2: Generate swarm code using Agent 2
            swarm_code = swarm_code_generator(org_structure)
            if "Error" in swarm_code:
                print(f"Error generating swarm code: {swarm_code}")
                

            print(f"Generated Swarm Code: {swarm_code}")  # Debugging output

            # Step 3: Write the generated code to a Python file
            file_name = f"generated_code_{datetime.now().strftime('%Y%m%d%H%M%S')}.py"
            print(f"About to save code to: {file_name}")  # Debugging output
            with open(file_name, "w") as f:
                f.write(swarm_code)
            print(f"Generated code saved to {file_name}")

            # If the code generation is successful, restart the loop
            print("Restarting the loop for a new iteration...")
            # Continue here might not be needed if you want to stop the loop once it writes to file
             # Use break to exit after writing the code once (if desired)

        except Exception as e:
            print(f"Error: {e}")
            continue  # If there's an error, restart the loop from the top

# Start the main loop
if __name__ == "__main__":
    main_loop()
