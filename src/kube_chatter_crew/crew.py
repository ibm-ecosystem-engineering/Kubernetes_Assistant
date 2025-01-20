import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class KubeChatterCrew():
    """KubeChatterCrew crew"""
    granite_llm = LLM(
        model=os.environ.get('GRANITE31_DENSE'),
       # model=os.environ.get('GRANITE3_MOE'),
        base_url=os.environ.get("OLLAMA_URL"),
    )

    # granite_llm = LLM(
    #     model=os.environ.get('GRANITE3_MOE'),
    #     base_url=os.environ.get("OLLAMA_URL"),
    # )

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def assistant(self) -> Agent:
        return Agent(
            config=self.agents_config['assistant'],
            verbose=True,
            llm=self.granite_llm,
        )
    #
    # @agent
    # def reviewer(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['reviewer'],
    #         verbose=True,
    #         llm=self.granite_llm,
    #     )

        # To learn more about structured task outputs,
        # task dependencies, and task callbacks, check out the documentation:
        # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def question_task(self) -> Task:
        return Task(
            config=self.tasks_config['question_task'],
            #    tools=[self.k8siodocs_search_tool]
        )

    # @task
    # def reviewer_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['reviewer_task'],
    #         # tools=[SerperDevTool()],
    #         context=[self.question_task()]
    #         # output_file='report.md'
    #     )

    @crew
    def crew(self) -> Crew:
        """Creates the KubeChatterCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
