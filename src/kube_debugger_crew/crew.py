import os

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from src.kube_debugger_crew.tools.custom_tool import KubeTool, PodOrMgrYaml
from crewai_tools import SerperDevTool


# Uncomment the following line to use an example of a custom tool
# from Kubernetes_Assistant_Agentic.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them


@CrewBase
class KubeDebuggerCrew:

    granite31_dense = LLM(
        model=os.environ.get('GRANITE31_DENSE'),
        base_url=os.environ.get("OLLAMA_URL"),
    )

    granite_moe = LLM(
        model=os.environ.get('GRANITE3_MOE'),
        base_url=os.environ.get("OLLAMA_URL"),
    )

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def sre(self) -> Agent:
        return Agent(
            config=self.agents_config['sre'],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
            llm=self.granite31_dense,
        )

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config['developer'],
            verbose=True,
            llm=self.granite_moe,
        )


    @task
    def debugger_task(self) -> Task:
        return Task(
            config=self.tasks_config['debugger_task'],
            tools=[KubeTool(), PodOrMgrYaml(), SerperDevTool()],

        )

    @task
    def fixer_task(self) -> Task:
        return Task(
            config=self.tasks_config['fixer_task'],
            #tools=[SerperDevTool()],
            context=[self.debugger_task()],
          #  output_file='report.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the KubeDebuggerCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator

            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
