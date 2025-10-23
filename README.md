![LangChain Academy](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/66e9eba1020525eea7873f96_LCA-big-green%20(2).svg)

## Introduction

Welcome to LangChain Academy! 
This is a growing set of modules focused on foundational concepts within the LangChain ecosystem. 
Module 0 is basic setup and Modules 1 - 4 focus on LangGraph, progressively adding more advanced themes. 
In each module folder, you'll see a set of notebooks. A LangChain Academy accompanies each notebook 
to guide you through the topic. Each module also has a `studio` subdirectory, with a set of relevant 
graphs that we will explore using the LangGraph API and Studio.

## Setup

### Python version

To get the most out of this course, please ensure you're using Python 3.11 or later. 
This version is required for optimal compatibility with LangGraph. If you're on an older version, 
upgrading will ensure everything runs smoothly.
```
python3 --version
```

### Clone repo
```
git clone https://github.com/langchain-ai/langchain-academy.git
$ cd langchain-academy
```

### Create an environment and install dependencies
#### Mac/Linux/WSL
```
$ python3 -m venv lc-academy-env
$ source lc-academy-env/bin/activate
$ pip install -r requirements.txt
```
#### Windows Powershell
```
PS> python3 -m venv lc-academy-env
PS> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS> lc-academy-env\scripts\activate
PS> pip install -r requirements.txt
```

### Running notebooks
If you don't have Jupyter set up, follow installation instructions [here](https://jupyter.org/install).
```
$ jupyter notebook
```

### Setting up env variables
Briefly going over how to set up environment variables. You can also 
use a `.env` file with `python-dotenv` library.
#### Mac/Linux/WSL
```
$ export API_ENV_VAR="your-api-key-here"
```
#### Windows Powershell
```
PS> $env:API_ENV_VAR = "your-api-key-here"
```

### Set OpenAI API key
* If you don't have an OpenAI API key, you can sign up [here](https://openai.com/index/openai-api/).
*  Set `OPENAI_API_KEY` in your environment 

### Sign up and Set LangSmith API
* Sign up for LangSmith [here](https://smith.langchain.com/), find out more about LangSmith
* and how to use it within your workflow [here](https://www.langchain.com/langsmith), and relevant library [docs](https://docs.smith.langchain.com/)!
*  Set `LANGSMITH_API_KEY`, `LANGSMITH_TRACING_V2=true` `LANGSMITH_PROJECT="langchain-academy"`in your environment 

### Set up Tavily API for web search

* Tavily Search API is a search engine optimized for LLMs and RAG, aimed at efficient, 
quick, and persistent search results. 
* You can sign up for an API key [here](https://tavily.com/). 
It's easy to sign up and offers a very generous free tier. Some lessons (in Module 4) will use Tavily. 

* Set `TAVILY_API_KEY` in your environment.

### Set up LangGraph Studio

* LangGraph Studio is a custom IDE for viewing and testing agents.
* Studio can be run locally and opened in your browser on Mac, Windows, and Linux.
* See documentation [here](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/#local-development-server) on the local Studio development server and [here](https://langchain-ai.github.io/langgraph/cloud/how-tos/studio/quick_start/#local-development-server). 
* Graphs for LangGraph Studio are in the `module-x/studio/` folders.
* To start the local development server, run the following command in your terminal in the `/studio` directory each module:

```
langgraph dev
```

You should see the following output:
```
- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs
```

Open your browser and navigate to the Studio UI: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`.

* To use Studio, you will need to create a .env file with the relevant API keys
* Run this from the command line to create these files for module 1 to 5, as an example:
```
for i in {1..5}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```
>MODULE 1 
   > Video 1
    >When I explored LangGraph, I realized it’s basically a smarter way to build AI systems that think and act more like humans. Instead of making AIs follow a rigid path, LangGraph lets me create workflows where the AI can make its own choices, loop back, and even ask for help if needed like an intelligent teammate rather than just a tool.
    >At the same time, it keeps a good balance by letting developers set important rules and structure, ensuring the system stays reliable but still flexible enough to respond to unexpected situations. It also supports memory and collaboration between multiple AI agents, plus human oversight when necessary, which makes it practical and trustworthy for serious applications
    > I made a new node of my own and and redefined the function 

  >Video 2-
   > I learnt how a LangGraph is built using connected nodes and edges, where data (the state) moves from one step to the next.
   >I saw how to add a conditional edge so the graph can take different paths depending on a rule — like choosing between two nodes.
   >Finally, I ran the graph to see how it updates the state at each step, giving different results each time based on the path it takes.
   > I tried to do different promts to see what output i got and observed them.

  >Video 3-
  > I got a quick intro on how to use langsmith studio. 
  > It helps with the visualisation of what i just created 

 > Video 4-
  > I learned how to use LangChain components like chat models, messages, tools, and function calls to build a conversational chain.

  >I explored how to structure conversations using message sequences and connect them through nodes and conditional edges in a graph.

  >I practiced integrating chat models with external tools and executing tool calls to make interactions more dynamic and functional. 

>Video 5-
  > Learned how a router enables dynamic control flow in LangGraph by letting the chat model decide between natural language responses and tool invocations.
  
  >Understood how to build conditional logic using nodes and edges to route execution based on model decisions.

  >Gained practical knowledge of tool integration with LangChain, using llm.bind_tools() to let the model call tools like multiply(a, b) during interaction.
  > Tried some different operations of my own 

>Video 6-

  >Saw a dynamic router architecture where the chat model decides whether to respond in natural language or call a tool based on user input, enabling flexible control flow in LangGraph.

  >Saw the implementation conditional edges and nodes to manage execution flow, routing between assistant and tool nodes, forming a loop that allows the model to call multiple tools sequentially or respond directly.

  >Learnt the Integratation multiple simple math tools (add, multiply, divide) with LangChain through llm.bind_tools(), enabling the model to invoke tools in sequence and reason about their outputs using a ReAct-like agent architecture.

  > I made some edits in the operations to see how the agent route backs to form a loop

>Video 7-   

  >I learnt how to build an AI agent with memory that can remember past interactions and use that memory to improve future responses and decision-making.

  >I learnt that an agent works through a continuous cycle of acting, observing, and reasoning — where it calls tools, analyzes results, and decides what to do next — and that adding memory makes this process more intelligent and context-aware.

  > I did some operations of my own and saw how it remembers the past interactions

>Module 2- 
  
  >Video 1-
    
    >State schema is a representation of structures and type of data our graph will use.
    >Typedict- It is the most basic tool amongst all 3 other tools I learnt about. It defines the keys and types of a dictionary but it doesn't check values at runtime. 
    >Dataclass- It automatically creates a class with an easy constructor and printing features which helps in organising data neatly.
    >Pydantic- It Builds data models that validate and convert data at runtime and ensures that everything is the right type and format.
    >I changed my code to have its own variables and tested the features of all the tools on my changed variables

  >Video 2-

    >State Updates: LangGraph nodes share and modify a common state that stores data across the workflow.
    >Reducers: They are the Functions that control how multiple updates to the same state key are merged instead of overwritten.
    >Custom Reducers: User-defined rules  for safely combining parallel updates. eg: sum,merge,etc. 
    >Message State: A special state type that stores conversation history, enabling context-aware AI interactions.
    >I changed the inputs and outputs to my desired inputs and outputs and say the working of reducers in messages. 

  >Video 3- 

    > Private State:It is the Temporary internal data used between nodes but excluded from final outputs.
    >Input Schema:It Defines the required information to start the graph execution.
    >Output Schema:It Specifies what final data is returned from the graph.
    >Multiple Schemas:It Enable modular, secure, and cleaner data flow across complex AI pipelines.
    > I modified the input & ouput schema and the notes. 

  Video 4-    

    >Messages as State: Use message objects (HumanMessage, AIMessage) to maintain chat history between nodes.
    >Filtering & Trimming: Remove or shorten old messages to manage context length and model token limits.
    >Model Integration: Connect LangGraph with OpenAI models (ChatOpenAI) to process conversational states.
    > I asked different questions and invoked the llm and tested the use of these tools myself.

  Video 5-

    >Message Summarization:It converts older messages into compact summaries, preserving context without exceeding token limits.

    >State Enhancement:It extends MessagesState by adding a summary field to manage both raw messages and condensed history.

    >Efficient Context Management: It ensures the chatbot remains aware of prior discussions even after trimming message history.

    >LangSmith Integration:It provides real-time tracing, debugging, and performance visualization for each chatbot interaction.    

    > I changed some inputs in the code. 

  Video 6- 
    
    >External Database Memory: It stores conversation history and summaries in SQLite for long-term, persistent chatbot memory.

    >Checkpointing with SqliteSaver: It automatically saves and retrieves the graph’s state to resume chats across sessions.

    >Persistent Context Management: It ensures the chatbot remembers prior interactions even after being closed or rebooted.

    > i changed some inputs and saww that it still conversed with me by reflecting its external memory in the chat.




   