from ecom_support_agent.app.graph.base_graph import build_graph

def test_graph_runs():
    graph = build_graph()

    result = graph.invoke({
        "query": "Test message"
    })

    assert "response" in result
    assert isinstance(result["response"], str)
    assert len(result["response"]) > 0
