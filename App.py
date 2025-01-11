import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from random import randint, uniform

# Page Configuration
st.set_page_config(
    page_title="Enhanced AI Agent Metrics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Header
st.title("📊 Enhanced AI Agent Metrics Dashboard")
st.write("Monitor and analyze a detailed set of metrics for your AI agents with a vibrant, multi-container dashboard.")

# Demo Data
agents = [
    f"Agent {chr(i)}" for i in range(65, 91)  # Agents A to Z
]

metrics = [
    "Emails Sent", "Calls Answered", "Posts Created", "Search Queries",
    "Tasks Completed", "Response Time (ms)", "Customer Interactions",
    "Errors Logged", "Active Sessions", "Training Hours", "Feedback Ratings (%)",
    "Lead Conversions", "Social Media Mentions"
]

# Generate Random Demo Data
data = {agent: {metric: (randint(10, 500) if "Response Time" not in metric and "Ratings" not in metric 
                         else round(uniform(1, 100), 2)) for metric in metrics} for agent in agents}

# Dashboard Layout
st.subheader("🗄 Individual Agent Metrics")
cols_per_row = 4
rows = len(agents) // cols_per_row + 1
for i in range(rows):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        idx = i * cols_per_row + j
        if idx >= len(agents):
            break
        agent = agents[idx]
        with col:
            with stylable_container(
                key=f"container_{agent}",
                css_styles=f"""
                    {{
                        border: 2px solid #f0f2f6;
                        border-radius: 10px;
                        padding: 20px;
                        background-color: #ff0000;
                        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                    }}
                """
            ):
                st.subheader(agent)
                for metric, value in data[agent].items():
                    st.metric(label=metric, value=value)

# Overall Summary
with stylable_container(
    key="summary_section",
    css_styles="""
        {
            border: 2px solid #f0f2f6;
            border-radius: 10px;
            padding: 20px;
            background-color: #ff0000;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    """
):
    st.subheader("📊 Overall Metrics Summary")
    total_metrics = {metric: (sum(agent_data[metric] for agent_data in data.values()) if "Response Time" not in metric and "Ratings" not in metric 
                               else round(sum(agent_data[metric] for agent_data in data.values()) / len(data), 2)) for metric in metrics}
    cols = st.columns(3)  # Display summary metrics in columns
    for i, (metric, total) in enumerate(total_metrics.items()):
        with cols[i % 3]:
            st.metric(label=metric, value=total)

# Interactive Section
with stylable_container(
    key="interactive_section",
    css_styles="""
        {
            border: 2px solid #f0f2f6;
            border-radius: 10px;
            padding: 20px;
            background-color: #ff0000;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    """
):
    st.subheader("🔀 Compare Agent Metrics")
    agent_selected = st.selectbox("Select an Agent", agents)
    metric_selected = st.selectbox("Select a Metric", metrics)
    st.metric(label=f"{metric_selected} for {agent_selected}", value=data[agent_selected][metric_selected])

# Additional Container: Trending Metrics
with stylable_container(
    key="trending_metrics_section",
    css_styles="""
        {
            border: 2px solid #f0f2f6;
            border-radius: 10px;
            padding: 20px;
            background-color: #ff0000;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    """
):
    st.subheader("🔄 Trending Metrics")
    trending_metric = metrics[randint(0, len(metrics) - 1)]
    st.write(f"The trending metric today is: **{trending_metric}**")
    for agent in agents[:5]:  # Show top 5 agents for the trending metric
        st.metric(label=f"{agent} - {trending_metric}", value=data[agent][trending_metric])
