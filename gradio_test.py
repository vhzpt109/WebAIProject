import gradio as gr


def inference(name):
    return "Hello " + name + "!"


if __name__ == "__main__":
    demo = gr.Interface(fn=inference, inputs="text", outputs="text")
    demo.launch()