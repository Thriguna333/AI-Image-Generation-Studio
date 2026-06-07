import gradio as gr

def greet(prompt):
    return f"You entered: {prompt}"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="Enter Prompt"),
    outputs=gr.Textbox(label="Output"),
    title="AI Image Generation Studio"
)

demo.launch()