# assistants.py
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from api.ai.llms import get_openai_llm
from api.ai.tools import send_me_email, get_unread_emails

EMAIL_TOOLS = {
    "send_me_email": send_me_email,
    "get_unread_emails": get_unread_emails,
}

def email_assistant(query: str):
    llm = get_openai_llm().bind_tools(list(EMAIL_TOOLS.values()))

    messages = [
        SystemMessage(content="You are a helpful assistant for managing my email inbox."),
        HumanMessage(content=query),
    ]

    ai_msg = llm.invoke(messages)
    print(ai_msg)
    # Si no hay tool calls, devolver tal cual
    if not getattr(ai_msg, "tool_calls", None):
        return ai_msg

    # Añade el mensaje del asistente (con las tool calls) UNA sola vez
    messages.append(ai_msg)

    # Ejecuta cada tool y adjunta su observación correctamente
    for tc in ai_msg.tool_calls:
        name = tc["name"]
        print(name)
        args = tc.get("args", {}) or {}
        print(args)
        tool = EMAIL_TOOLS.get(name)
        print(tool)
        if not tool:
            continue
        result = tool.invoke(args)  # las @tool de LangChain exponen .invoke
        messages.append(ToolMessage(content=str(result), tool_call_id=tc["id"]))

    print(messages)
    # Segunda pasada ya con observaciones
    final = llm.invoke(messages)
    return final
