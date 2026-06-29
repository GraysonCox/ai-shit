import os
import logging

import boto3
from langchain.agents import create_agent
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import HumanMessage

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))


def main():
    agent = create_agent(
        model=ChatBedrockConverse(
            client=boto3.client("bedrock-runtime", "us-east-2"),
            model="amazon.nova-micro-v1:0",
            # model="deepseek.v3-v1:0",
            # service_tier="flex",
            region_name="us-east-2",
        ),
        tools=[],
        system_prompt="You are a very mean chat bot that cares only about making other people suffer.",
    )

    messages = []
    while True:
        human_input = input("You: ")
        messages.append(HumanMessage(human_input))
        print("AI: ", end="")
        ai_output_chunks = []
        for step in agent.stream({"messages": messages}):
            for update in step.values():
                for message in update.get("messages", []):
                    message.pretty_print()
                    ai_output_chunks.append(message.content)


if __name__ == "__main__":
    main()
