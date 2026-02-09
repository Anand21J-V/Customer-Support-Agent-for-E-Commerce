from ecom_support_agent.app.graph.base_graph import build_graph

if __name__ == "__main__":
    graph = build_graph()

    result = graph.invoke({
        "query": "Say hello and confirm Groq is working"
    })

    print("\n--- FINAL RESPONSE ---")
    print(result["response"])
